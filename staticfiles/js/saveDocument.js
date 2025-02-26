document.getElementById('saveButton').addEventListener('click', function () {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF('p', 'mm', 'letter');
    const contenido = document.getElementById('contenido');
    const documentoTitulo = document.getElementById('editable5').innerText.trim();

    // Función para obtener el valor de una cookie
    function getCookie(name) {
        const cookieArr = document.cookie.split(';');
        const cookie = cookieArr.find(cookie => cookie.trim().startsWith(name + '='));
        const value = cookie ? decodeURIComponent(cookie.split('=')[1]) : null;
        return value;
    }

    // Márgenes personalizados (en milímetros)
    const marginTop = 2;
    const marginBottom = 2;
    const marginLeft = 20;
    const marginRight = 20;

    // Función para ocultar todos los botones
    function ocultarBotones() {
        const botones = document.querySelectorAll('button');
        botones.forEach(function (boton) {
            boton.style.display = 'none';
        });
    }

    // Función para mostrar todos los botones
    function mostrarBotones() {
        const botones = document.querySelectorAll('button');
        botones.forEach(function (boton) {
            boton.style.display = 'inline-block';
        });
    }

    // Función para aplicar el estilo temporal al fondo blanco de los elementos contenteditable
    function aplicarEstilosTemporales() {
        const estilos = `
            <style>
                th[contenteditable='true'],
                p[contenteditable='true'],
                td[contenteditable='true'] {
                    background-color: white !important;
                }
            </style>
        `;
        document.head.insertAdjacentHTML('beforeend', estilos);
    }

    // Función para eliminar los estilos temporales después de la captura
    function eliminarEstilosTemporales() {
        const estilos = `
            <style>
                th[contenteditable='true'],
                p[contenteditable='true'],
                td[contenteditable='true'] {
                    background-color: #f0f0f0 !important;
                    /* color de fondo gris claro para visibilidad */
                }
            </style>         
        `;
        document.head.insertAdjacentHTML('beforeend', estilos);
    }

    // Función para capturar el contenido con html2canvas
    function capturarConHtml2Canvas(elemento) {
        return new Promise(function (resolve, reject) {
            html2canvas(elemento, {
                scale: 1,
                useCORS: true,
                ignoreElements: (div) => {
                    return div.id === 'sending-modal' || div.id === 'loading-modal';
                }
            }).then(resolve).catch(reject);
        });
    }

    // Información adicional para el envío
    const caracterizacion = document.getElementById('editable3').innerText;
    const codigoCompleto = document.getElementById('editable2').innerText;
    const codigo = codigoCompleto.replace('Código: ', '');

    // Ocultar los botones antes de capturar
    ocultarBotones();

    // Aplicar el estilo temporal antes de la captura
    aplicarEstilosTemporales();

    capturarConHtml2Canvas(contenido)
        .then(function (canvas) {
            const imgData = canvas.toDataURL('image/jpeg', 0.5); // Segundo parámetro es la calidad (0-1)

            // Dimensiones de página
            const pageWidth = 215.9;
            const pageHeight = 279.4;

            // Calcular área útil
            const usableWidth = pageWidth - (marginLeft + marginRight);
            const usableHeight = pageHeight - (marginTop + marginBottom);

            // Escalar al ancho máximo horizontal
            const scaleFactor = usableWidth / canvas.width;
            const finalWidth = usableWidth;
            const finalHeight = canvas.height * scaleFactor;

            // Agregar imagen con márgenes personalizados
            doc.addImage(
                imgData,
                'PNG',
                marginLeft,
                marginTop,
                finalWidth,
                finalHeight,
                undefined,
                'FAST'
            );

            // Generar PDF como ArrayBuffer
            const pdfData = doc.output('arraybuffer');

            // Crear FormData para enviar al servidor
            const formData = new FormData();
            formData.append('file', new Blob([pdfData]), `${documentoTitulo}.pdf`);
            formData.append('codigo', codigo);
            formData.append('titulo', documentoTitulo);
            formData.append('caracterizacion', caracterizacion);

            // Obtener token CSRF
            const csrfToken = getCookie('csrftoken');

            // Enviar al servidor
            fetch('/guardar-caracterizacion/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                body: formData
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Error en la respuesta del servidor');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Documento guardado exitosamente', data);
                    // Puedes agregar una notificación de éxito aquí si lo deseas
                })
                .catch(error => {
                    console.error('Error al guardar el documento:', error);
                    alert('Hubo un error al guardar el documento. Por favor, intente nuevamente.');
                });

            // Mostrar los botones nuevamente después de generar el PDF
            mostrarBotones();

            // Eliminar los estilos temporales después de la captura
            eliminarEstilosTemporales();
        })
        .catch(function (error) {
            console.error('Error al capturar el contenido:', error);
            // Aseguramos que los botones se muestren nuevamente si ocurre un error
            mostrarBotones();

            // Eliminar los estilos temporales en caso de error
            eliminarEstilosTemporales();

            // Mostrar mensaje de error al usuario
            alert('Hubo un problema al generar el PDF. Por favor, intente nuevamente.');
        });
});