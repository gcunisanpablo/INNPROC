document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById('myModal')
    var btnInsertar = document.getElementById('insertar_indicadores')
    var span = document.getElementById('closeModal')

    // Función para obtener el valor de una cookie
    function getCookie(name) {
        let cookieArr = document.cookie.split(';')
        for (let i = 0; i < cookieArr.length; i++) {
            let cookiePair = cookieArr[i].split('=')
            if (name === cookiePair[0].trim()) {
                return decodeURIComponent(cookiePair[1])
            }
        }
        return null
    }

    // Función para cargar el formulario desde la API
    function loadForm(url) {
        fetch(url)
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Error al cargar el formulario')
                }
                return response.text()
            })
            .then((data) => {
                document.getElementById('modalContent').innerHTML = data
                modal.style.display = 'block'

                const form = document.querySelector('#modalContent form')
                if (form) {
                    form.action = url

                    form.onsubmit = function (event) {
                        event.preventDefault()
                        const formData = new FormData(form)
                        const csrfToken = getCookie('csrftoken')

                        fetch(form.action, {
                            method: form.method,
                            body: formData,
                            headers: {
                                'X-CSRFToken': csrfToken
                            }
                        })
                            .then((response) => {
                                if (!response.ok) {
                                    throw new Error('Error en la respuesta del servidor')
                                }
                                return response.json()
                            })
                            .then((data) => {
                                if (data.success) {
                                    Swal.fire('Éxito', 'Datos enviados correctamente', 'success')
                                    modal.style.display = 'none'
                                    cargarIndicadores()
                                } else {
                                    const errorMessages = Object.entries(data.errors)
                                        .map(([field, messages]) => `${field}: ${messages.join(', ')}`)
                                        .join('<br>')

                                    Swal.fire('Error', errorMessages, 'error')
                                }
                            })
                            .catch((error) => {
                                console.error('Error:', error)
                                Swal.fire('Error', 'Hubo un problema al enviar los datos', 'error')
                            })
                    }
                }

                // Actualiza el nombre de la caracterización
                const nombreCaracterizacionElement = document.getElementById('editable5')
                if (nombreCaracterizacionElement) {
                    const nombreCaracterizacion = nombreCaracterizacionElement.innerText
                    const caracterizacionField = document.getElementById('caracterizacion')
                    if (caracterizacionField) {
                        caracterizacionField.value = nombreCaracterizacion
                    }
                }
            })
            .catch((error) => console.error('Error:', error))
    }

    // Abrir el modal al hacer clic en el botón de insertar
    btnInsertar.onclick = function () {
        const modelName = document.getElementById('indicadores').innerText // Obtener el nombre del modelo
        const documentId = 'nuevo' // Define un valor para documentId
        const url = `/crear-documento/${modelName}/${modelName}/` // Construir la URL
        loadForm(url)
    }

    // Manejar clics en botones de eliminar
    document.addEventListener('click', function (event) {
        if (event.target.matches('[id^="eliminar_indicadores_"]')) {
            event.preventDefault()
            const documentId = event.target.id.split('_')[2]
            const fileName = event.target.getAttribute('data-nombre')
            const modelName = document.getElementById('indicadores').innerText

            Swal.fire({
                title: '¿Estás seguro?',
                html: `¡Vas a eliminar!<br><strong style="color: red;">"${fileName}"</strong><br>No podrás revertir esto.`,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sí, eliminarlo'
            }).then((result) => {
                if (result.isConfirmed) {
                    const url = `/eliminar-documento/${modelName}/${documentId}/`

                    fetch(url, {
                        method: 'DELETE',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken')
                        }
                    })
                        .then((response) => {
                            if (response.ok) {
                                Swal.fire('Eliminado', `El documento "${fileName}" ha sido eliminado`, 'success')
                                cargarIndicadores()
                            } else {
                                Swal.fire('Error', 'Hubo un problema al eliminar el documento', 'error')
                            }
                        })
                        .catch((error) => {
                            console.error('Error:', error)
                            Swal.fire('Error', 'Hubo un problema al enviar la solicitud', 'error')
                        })
                }
            })
        }
    })

    function cargarIndicadores() {
        const modelName = document.getElementById('indicadores').innerText // Obtener el nombre del modelo
        console.log('Cargando indicadores para:', modelName)
        fetch(`/buscar-indicadores-especificos/${modelName}/`)
            .then((response) => {
                console.log('Respuesta del servidor:', response)
                if (!response.ok) {
                    throw new Error('Error al cargar la lista de indicadores')
                }
                return response.text()
            })
            .then((data) => {
                document.getElementById('contenido-principal-indicadores').innerHTML = data
                asignarUrls(); // Llama a la función para asignar las URLs después de inyectar el HTML
            })
            .catch((error) => {
                console.error('Error en cargarIndicadores:', error)
            })
    }
    function asignarUrls() {

        document.querySelectorAll('a[id^="mi-enlace-indicadores_"]').forEach((link) => {
            const documentId = link.getAttribute('data-id');
            if (documentId) {
                const url = `/ver-pdf-solo/${documentId}/`; // Construye la URL
                link.href = url; // Asigna la URL al enlace
            }
        });
    }
    cargarIndicadores()
    document.getElementById('insertar_indicadores').addEventListener('click', function () {
        // Obtener los datos a guardar

        const modelo = document.getElementById('modelo-formato-documentos').innerText
        const editable5 = document.getElementById('editable5').innerText

        // Guardar los datos en Local Storage

        localStorage.setItem('modelo', modelo)
        localStorage.setItem('editable5', editable5)
    })
    // Cerrar el modal
    span.onclick = function () {
        modal.style.display = 'none'
    }

    // Cerrar el modal al hacer clic fuera de él
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = 'none'
        }
    }
})
