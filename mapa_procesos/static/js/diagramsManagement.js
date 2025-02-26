document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('myModal');
    const btnInsertar = document.getElementById('insertar_diagramas');
    const span = document.getElementById('closeModal');

    // Función para obtener el valor de una cookie
    function getCookie(name) {
        const cookieArr = document.cookie.split(';');
        const cookie = cookieArr.find(cookie => cookie.trim().startsWith(name + '='));
        const value = cookie ? decodeURIComponent(cookie.split('=')[1]) : null;
        return value;
    }

    // Función para mostrar alertas
    function showAlert(title, text, icon) {
        Swal.fire({
            title,
            text,
            icon,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
        });
    }

    // Función para cargar el formulario desde la API
    async function loadForm(url) {
        try {
            const response = await fetch(url);
            if (!response.ok) throw new Error('Error al cargar el formulario');
            const data = await response.text();
            document.getElementById('modalContent').innerHTML = data;
            modal.style.display = 'block';

            const form = document.querySelector('#modalContent form');
            if (form) {
                form.action = url;
                form.onsubmit = async function (event) {
                    event.preventDefault();
                    const formData = new FormData(form);
                    const csrfToken = getCookie('csrftoken');  // Obtener el CSRF Token
                    if (!csrfToken) {  // Verificar que el CSRF Token no sea null
                        console.error('El CSRF Token es null. La solicitud no se enviará correctamente.');
                        showAlert('Error', 'El CSRF Token no está disponible', 'error');
                        return;
                    }
                    try {
                        const formResponse = await fetch(form.action, {
                            method: form.method,
                            body: formData,
                            headers: { 'X-CSRFToken': csrfToken }
                        });
                        if (!formResponse.ok) throw new Error('Error en la respuesta del servidor');
                        showAlert('Éxito', 'Imagen subida correctamente', 'success');
                        modal.style.display = 'none';
                        cargarDiagramas();
                    } catch (error) {
                        console.error('Error:', error);
                        showAlert('Error', 'Hubo un problema al enviar los datos', 'error');
                    }
                };
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }

    // Abrir el modal al hacer clic en el botón de insertar
    btnInsertar.onclick = function () {
        const modelName = document.getElementById('DiPr').innerText;
        const url = `/subir-diagrama-procedimientos/${modelName}/${modelName}_form/`; // URL para cargar el formulario
        loadForm(url);
    };

    // Manejar clics en botones de eliminar
    document.addEventListener('click', function (event) {
        if (event.target.matches('[id^="eliminar_diagramas_"]')) {
            event.preventDefault();
            const documentId = event.target.id.split('_')[2]; // Obtener el ID
            const fileName = event.target.getAttribute('data-nombre');
            const modelName = document.getElementById('DiPr').innerText;

            if (documentId && fileName) {
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
                        const url = `/eliminar-diagrama-procedimientos/${modelName}/${documentId}/`; // URL de eliminación con el ID

                        // Verificar CSRF Token antes de hacer la solicitud DELETE
                        const csrfToken = getCookie('csrftoken');
                        if (!csrfToken) {
                            console.error('CSRF Token no disponible. No se puede realizar la solicitud.');
                            showAlert('Error', 'El CSRF Token no está disponible', 'error');
                            return;
                        }

                        fetch(url, {
                            method: 'DELETE',
                            headers: {
                                'X-CSRFToken': csrfToken,  // Incluir el token CSRF en los encabezados
                                'Content-Type': 'application/json',
                            }
                        })
                            .then(response => response.text())  // Cambiar a `response.text()` para ver la respuesta como texto
                            .then(data => {
                                console.log('Respuesta del servidor para diagramas de procedimientos: \n(como texto):', data);

                                // Verifica si la respuesta es JSON o HTML
                                try {
                                    const jsonResponse = JSON.parse(data);  // Intentar convertir la respuesta a JSON
                                    if (jsonResponse.success) {
                                        showAlert('Eliminado', `La imagen "${fileName}" ha sido eliminada`, 'success');
                                        cargarDiagramas();
                                    } else {
                                        showAlert('Error', `No se pudo eliminar la imagen: ${jsonResponse.error}`, 'error');
                                    }
                                } catch (error) {
                                    console.error('Error al procesar la respuesta como JSON:', error);
                                    showAlert('Error', 'Hubo un problema al procesar la respuesta del servidor', 'error');
                                }
                            })
                            .catch((error) => {
                                console.error('Error al eliminar:', error);
                                showAlert('Error', 'Hubo un problema al eliminar la imagen', 'error');
                            });

                        console.log('url: ', url);
                    }
                });
            }
        }
    });

    function asignarUrls() {
        // Obtén el valor 
        const modelName = document.getElementById('DiPr').innerText;
        document.querySelectorAll('a[id^="mi-enlace-diagramas_"]').forEach((link) => {
            const documentId = link.getAttribute('data-id');
            if (documentId && modeloBase) {
                const url = `/ver-diagrama-procedimientos/${modelName}/${documentId}/`; // Construye la URL
                link.href = url; // Asigna la URL al enlace
            }
        });
    }

    // Cargar los diagramas iniciales
    async function cargarDiagramas() {
        const modelName = document.getElementById('DiPr').innerText;
        console.log('Cargando diagramas para:', modelName)
        try {
            const response = await fetch(`/lista-diagramas-procedimientos/${modelName}/`);
            console.log('Respuesta del servidor:', response)
            if (!response.ok) throw new Error('Error al cargar la lista de imágenes');
            const data = await response.text();
            document.getElementById('contenido-principal-diagramas').innerHTML = data;
            asignarUrls();
        } catch (error) {
            console.error('Error en cargarDiagramas:', error);
        }
    }

    // Cerrar el modal
    span.onclick = function () {
        modal.style.display = 'none';
    };

    // Cerrar el modal al hacer clic fuera de él
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    cargarDiagramas(); // Cargar al inicio
    asignarUrls();
});
