document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById('myModal')
    var btnInsertar = document.getElementById('insertar_requilegalnorma')
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
                                    cargarDocumentos()
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


                const caracterizacionField = document.getElementById('caracterizacion')
                if (caracterizacionField) {
                    caracterizacionField.value = "GLOBAL"
                }

            })
            .catch((error) => console.error('Error:', error))
    }

    // Abrir el modal al hacer clic en el botón de insertar
    btnInsertar.onclick = function () {
        const url = `/crear-documento/RequisitosLegalesNormativos_globales/RequisitosLegalesNormativos_globales/` // Construir la URL
        loadForm(url)
    }

    // Manejar clics en botones de eliminar
    document.addEventListener('click', function (event) {
        if (event.target.matches('[id^="eliminar_requilegalnorma_"]')) {
            event.preventDefault()
            const documentId = event.target.id.split('_')[2]
            const fileName = event.target.getAttribute('data-nombre')

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
                    const url = `/eliminar-documento/RequisitosLegalesNormativos_globales/${documentId}/`

                    fetch(url, {
                        method: 'DELETE',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken')
                        }
                    })
                        .then((response) => {
                            if (response.ok) {
                                Swal.fire('Eliminado', `El documento "${fileName}" ha sido eliminado`, 'success')
                                cargarDocumentos()
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

    function cargarDocumentos() {
        console.log('Cargando requisitos legales normativos para:', "RequisitosLegalesNormativos_globales")
        fetch(`/buscar-requisitos-legales-normativos-epecificos/RequisitosLegalesNormativos_globales/`)
            .then((response) => {
                console.log('Respuesta del servidor:', response)
                if (!response.ok) {
                    throw new Error('Error al cargar la lista de documentos')
                }
                return response.text()
            })
            .then((data) => {
                document.getElementById('contenido-principal-requilegalnorma').innerHTML = data
            })
            .catch((error) => {
                console.error('Error en cargarDocumentos:', error)
            })
    }
    cargarDocumentos()
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
