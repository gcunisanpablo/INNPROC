
window.onload = function () {
    setTimeout(function () {
        var svgContainer = document.getElementById('svgContainer')
        svgContainer.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }, 1500) // Retraso de 5 segundos (5000 milisegundos)
}

document.addEventListener('DOMContentLoaded', function () {
    // Verifica si el modal ya se ha mostrado
    if (!localStorage.getItem('modalShown')) {
        Swal.fire({
            icon: 'info',
            title: `¡Bienvenido ${window.USER_NAME} al Repositorio UNISANPABLO!`,
            html: '<p>En este espacio dedicado, almacenamos y gestionamos los procesos fundamentales que dan vida a nuestra institución. Explora nuestro Mapa de Procesos para comprender la sinergia de las áreas misionales, de apoyo y estratégicas para entender cómo trabajamos y cómo cada componente se entrelaza para construir el éxito de nuestra institución.</p> <br> <p>¡Descubre la esencia de UNISANPABLO! Bienvenido a nuestro viaje de eficiencia y excelencia.</p>',
            confirmButtonText: 'Continuar',
            customClass: {
                confirmButton: 'btn btn-primary'
            }
        })

        // Marca el modal como mostrado
        localStorage.setItem('modalShown', 'true')
    }
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
