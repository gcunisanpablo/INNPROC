// Funcion enfocar el mapa de procesos al ingresar a la pagina principal
window.onload = function () {
    setTimeout(function () {
        var svgContainer = document.getElementById('svgContainer')
        svgContainer.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }, 1500) // Retraso 
}

document.addEventListener('DOMContentLoaded', function () {
    // Mostrar mensaje de bienvenida con nombre de usuario
    // Verifica si el modal ya se ha mostrado previamente
    if (!localStorage.getItem('modalShown')) {
        Swal.fire({
            icon: 'info',
            title: `¡Bienvenido, ${window.USER_NAME}!`,
            html: `
            <p>Te damos la bienvenida al Repositorio UNISANPABLO, un espacio diseñado para almacenar y gestionar los procesos clave que sustentan nuestra institución.</p>
            <p>Te invitamos a explorar nuestro Mapa de Procesos, donde podrás entender cómo interactúan los distintos procesos misionales, de apoyo y estratégicas, y cómo cada una contribuye al éxito y crecimiento de UNISANPABLO.</p>
            <p>¡Bienvenido a un entorno de eficiencia y excelencia!</p>
        `,
            confirmButtonText: 'Continuar',
            customClass: {
                confirmButton: 'btn btn-primary'
            },
            width: '60%', // Ajuste del tamaño del modal para una mejor visualización
            backdrop: true, // Agrega un fondo desdibujado para enfocar la atención en el modal
            showCloseButton: true, // Añade un botón de cerrar para mayor flexibilidad
        });

        // Marca el modal como mostrado para evitar que se repita
        localStorage.setItem('modalShown', 'true');
    }

    // Mostar modal de video apartado tutoriales
    const tutorialItems = document.querySelectorAll('.tutorial-item a')
    const videoModal = document.querySelector('.modal-video-overlay') // Seleccionamos la capa del modal
    const videoFrame = document.querySelector('.modal-video-wrapper iframe') // Seleccionamos el iframe
    const closeModalBtn = document.querySelector('.modal-video-close')

    tutorialItems.forEach((item) => {
        item.addEventListener('click', function (e) {
            e.preventDefault()
            const videoUrl = this.getAttribute('data-video-url')

            // Asegurarnos de que el video URL existe
            if (videoUrl) {
                videoFrame.src = videoUrl
                videoModal.style.display = 'flex' // Muestra el modal

                // Obtener la posición del enlace clickeado y desplazar el modal
                const rect = item.getBoundingClientRect() // Obtenemos la posición del enlace
                const modalHeight = videoModal.offsetHeight

                // Usamos scrollIntoView para desplazar el modal hacia la posición adecuada
                videoModal.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center' // Centra el modal verticalmente
                })

                document.body.style.overflow = 'hidden' // Bloquea el scroll del body mientras el modal está abierto
            }
        })
    })

    // Cerrar el modal cuando se haga clic en el botón de cerrar
    closeModalBtn.addEventListener('click', function () {
        videoModal.style.display = 'none'
        videoFrame.src = '' // Resetear la fuente del video
        document.body.style.overflow = '' // Restaurar el scroll del body
    })

    // Cerrar el modal si se hace clic fuera del contenedor del video
    videoModal.addEventListener('click', function (e) {
        if (e.target === videoModal) {
            videoModal.style.display = 'none'
            videoFrame.src = '' // Resetear la fuente del video
            document.body.style.overflow = '' // Restaurar el scroll del body
        }
    })
})
