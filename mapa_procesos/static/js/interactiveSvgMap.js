document.addEventListener('DOMContentLoaded', function () {
    const svgObject = document.querySelector('object[type="image/svg+xml"]')

    if (svgObject) {
        svgObject.addEventListener('load', function () {
            const svgDoc = this.contentDocument

            // DIRECCIONAMIENTO ESTRATEGICO
            if (svgDoc) {
                try {
                    // Definir los elementos específicos
                    const specificElements = [
                        { pathId: 'path50', textId: 'text18', link: "planeacion-estrategica" },
                        { pathId: 'path49', textId: 'text13', link: "relaciones-internacionales" },
                        { pathId: 'path48', textId: 'text14', link: "calidad-integral" },
                        { pathId: 'path47', textId: 'text15', link: "talento-humano-bienestar" }
                    ];

                    specificElements.forEach(({ pathId, textId, link }) => {
                        const pathElement = svgDoc.getElementById(pathId);
                        const textElement = svgDoc.getElementById(textId);

                        if (pathElement && textElement) {
                            // Hover
                            const hoverIn = () => {
                                pathElement.style.cursor = 'pointer';
                                pathElement.style.fill = '#de9107';
                                pathElement.style.stroke = 'black';
                                pathElement.style.strokeWidth = '2';
                                textElement.style.cursor = 'pointer';
                                textElement.style.fill = 'red';

                                if (pathId === 'path49' || pathId === 'path48') {
                                    pathElement.style.opacity = '1';
                                    pathElement.style.fillOpacity = '1';
                                }
                            };

                            const hoverOut = () => {
                                pathElement.style.fill = '#eeb500';
                                pathElement.style.stroke = 'none';
                                pathElement.style.strokeWidth = '0';
                                textElement.style.fill = 'black';

                                if (pathId === 'path49' || pathId === 'path48') {
                                    pathElement.style.opacity = '0';
                                    pathElement.style.fillOpacity = '0';
                                }
                            };

                            pathElement.addEventListener('mouseover', hoverIn);
                            pathElement.addEventListener('mouseout', hoverOut);
                            textElement.addEventListener('mouseover', hoverIn);
                            textElement.addEventListener('mouseout', hoverOut);

                            // Clic
                            const handleClick = () => {
                                console.log(`Elemento ${pathId} clickeado`);
                                pathElement.style.fill = 'rgb(255, 0, 0)';
                                textElement.style.fill = 'black';
                                window.location.href = link;
                            };

                            pathElement.addEventListener('click', handleClick);
                            textElement.addEventListener('click', handleClick);
                        } else {
                            console.warn(`Elementos no encontrados: path: ${pathId}, text: ${textId}`);
                        }
                    });
                } catch (error) {
                    console.error('Error interactuando con elementos del SVG:', error);
                }
            }
            // PROCESOS DE APOYO
            if (svgDoc) {
                try {
                    // Definir los elementos específicos
                    const specificElements = [
                        { pathId: 'path46', textId: 'text7', link: "gestion-juridica-contractual" },
                        { pathId: 'path45', textId: 'text9', link: "gestion-mercadeo-admisiones" },
                        { pathId: 'path44', textId: 'text10', link: "gestion-administrativa-financiera" },
                        { pathId: 'path43', textId: 'text11', link: "gestion-infraestructura-fisica-tecnologica" }
                    ];

                    specificElements.forEach(({ pathId, textId, link }) => {
                        const pathElement = svgDoc.getElementById(pathId);
                        const textElement = svgDoc.getElementById(textId);

                        if (pathElement && textElement) {
                            // Hover
                            const hoverIn = () => {
                                pathElement.style.cursor = 'pointer';
                                pathElement.style.fill = '#f6a017';
                                pathElement.style.stroke = 'black';
                                pathElement.style.strokeWidth = '2';
                                textElement.style.cursor = 'pointer';
                                textElement.style.fill = 'red';

                                if (pathId === 'path44' || pathId === 'path45') {
                                    pathElement.style.opacity = '1';
                                    pathElement.style.fillOpacity = '1';
                                }
                            };

                            const hoverOut = () => {
                                pathElement.style.fill = '#ed7d31';
                                pathElement.style.stroke = 'none';
                                pathElement.style.strokeWidth = '0';
                                textElement.style.fill = 'black';

                                if (pathId === 'path44' || pathId === 'path45') {
                                    pathElement.style.opacity = '0';
                                    pathElement.style.fillOpacity = '0';
                                }
                            };

                            pathElement.addEventListener('mouseover', hoverIn);
                            pathElement.addEventListener('mouseout', hoverOut);
                            textElement.addEventListener('mouseover', hoverIn);
                            textElement.addEventListener('mouseout', hoverOut);

                            // Clic
                            const handleClick = () => {
                                console.log(`Elemento ${pathId} clickeado`);
                                pathElement.style.fill = 'rgb(255, 0, 0)';
                                textElement.style.fill = 'black';
                                window.location.href = link;
                            };

                            pathElement.addEventListener('click', handleClick);
                            textElement.addEventListener('click', handleClick);
                        } else {
                            console.warn(`Elementos no encontrados: path: ${pathId}, text: ${textId}`);
                        }
                    });
                } catch (error) {
                    console.error('Error interactuando con elementos del SVG:', error);
                }
            }

            // PROCESOS MISIONALES
            if (svgDoc) {
                try {
                    // Definir los elementos específicos
                    const specificElements = [
                        { pathId: 'path42', textId: 'text12', link: "proyeccion-social-impacto" },
                        { pathId: 'path41', textId: 'text16', link: "investigacion-pertinente" },
                        { pathId: 'path40', textId: 'text17', link: "docencia-calidad" }
                    ];

                    specificElements.forEach(({ pathId, textId, link }) => {
                        const pathElement = svgDoc.getElementById(pathId);
                        const textElement = svgDoc.getElementById(textId);

                        if (pathElement && textElement) {
                            // Hover
                            const hoverIn = () => {
                                pathElement.style.cursor = 'pointer';
                                pathElement.style.fill = '#ffc000';
                                pathElement.style.stroke = 'black';
                                pathElement.style.strokeWidth = '2';
                                textElement.style.cursor = 'pointer';
                                textElement.style.fill = 'red';

                                if (pathId === 'path41') {
                                    pathElement.style.opacity = '1';
                                    pathElement.style.fillOpacity = '1';
                                }
                            };

                            const hoverOut = () => {
                                pathElement.style.fill = '#ffd966';
                                textElement.style.fill = 'black';

                                if (pathId === 'path41') {
                                    pathElement.style.opacity = '0';
                                    pathElement.style.fillOpacity = '0';
                                }

                                pathElement.style.stroke = 'none';
                                pathElement.style.strokeWidth = '0';
                            };

                            pathElement.addEventListener('mouseover', hoverIn);
                            pathElement.addEventListener('mouseout', hoverOut);
                            textElement.addEventListener('mouseover', hoverIn);
                            textElement.addEventListener('mouseout', hoverOut);

                            // Clic
                            const handleClick = () => {
                                console.log(`Elemento ${pathId} clickeado`);
                                pathElement.style.fill = 'rgb(255, 0, 0)';
                                textElement.style.fill = 'black';
                                window.location.href = link;
                            };

                            pathElement.addEventListener('click', handleClick);
                            textElement.addEventListener('click', handleClick);
                        } else {
                            console.warn(`Elementos no encontrados: path: ${pathId}, text: ${textId}`);
                        }
                    });
                } catch (error) {
                    console.error('Error interactuando con elementos del SVG:', error);
                }
            }
        })
    }
})
