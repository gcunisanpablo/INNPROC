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
                        {
                            pathId: 'path50',
                            textId: 'text18',
                            hover: true,
                            click: true,
                            link: "planeacion-estrategica"
                        },
                        {
                            pathId: 'path49',
                            textId: 'text13',
                            hover: true,
                            click: true,
                            link: "relaciones-internacionales"
                        },
                        {
                            pathId: 'path48',
                            textId: 'text14',
                            hover: true,
                            click: true,
                            link: "calidad-integral"
                        },
                        {
                            pathId: 'path47',
                            textId: 'text15',
                            hover: true,
                            click: true,
                            link: "talento-humano-bienestar"
                        }
                    ]

                    specificElements.forEach(({ pathId, textId, hover, click, link }) => {
                        const pathElement = svgDoc.getElementById(pathId)
                        const textElement = svgDoc.getElementById(textId)

                        if (pathElement && textElement) {
                            // Hover
                            if (hover) {
                                // Hover sobre el path
                                pathElement.addEventListener('mouseover', function () {
                                    this.style.cursor = 'pointer'
                                    this.style.fill = ' #de9107'
                                    this.style.stroke = 'black'
                                    this.style.strokeWidth = '2'
                                    if (this.id == 'path49') {
                                        this.style.opacity = '1'
                                        this.style.fillOpacity = '1'
                                    }
                                    if (this.id == 'path48') {
                                        this.style.opacity = '1'
                                        this.style.fillOpacity = '1'
                                    }
                                    textElement.style.cursor = 'pointer'
                                    textElement.style.fill = 'red'
                                })

                                pathElement.addEventListener('mouseout', function () {
                                    this.style.fill = ' #eeb500'
                                    this.style.stroke = 'none'
                                    this.style.strokeWidth = '0'
                                    if (this.id == 'path49') {
                                        this.style.opacity = '0'
                                        this.style.fillOpacity = '0'
                                    }
                                    if (this.id == 'path48') {
                                        this.style.opacity = '0'
                                        this.style.fillOpacity = '0'
                                    }
                                    textElement.style.fill = 'black'
                                })

                                // Hover sobre el texto
                                textElement.addEventListener('mouseover', function () {
                                    pathElement.style.stroke = 'black'
                                    pathElement.style.strokeWidth = '2'
                                    if (this.id == 'text13') {
                                        pathElement.style.opacity = '1'
                                        pathElement.style.fillOpacity = '1'
                                    }
                                    if (this.id == 'text14') {
                                        pathElement.style.opacity = '1'
                                        pathElement.style.fillOpacity = '1'
                                    }
                                    this.style.cursor = 'pointer'
                                    this.style.fill = 'red'
                                    pathElement.style.fill = ' #de9107'
                                })

                                textElement.addEventListener('mouseout', function () {
                                    this.style.fill = 'black'
                                    pathElement.style.stroke = 'none'
                                    pathElement.style.strokeWidth = '0'
                                    if (this.id == 'text13') {
                                        pathElement.style.opacity = '0'
                                        pathElement.style.fillOpacity = '0'
                                    }
                                    if (this.id == 'text14') {
                                        pathElement.style.opacity = '0'
                                        pathElement.style.fillOpacity = '0'
                                    }
                                    pathElement.style.fill = ' #eeb500'
                                })
                            }

                            // Clic
                            if (click) {
                                pathElement.addEventListener('click', function () {
                                    console.log(`Elemento ${pathId} clickeado`)

                                    pathElement.style.fill = 'rgb(255, 0, 0)'
                                    textElement.style.fill = 'black'

                                    window.location.href = link
                                })

                                textElement.addEventListener('click', function () {
                                    console.log(`Elemento ${textId} clickeado`)

                                    pathElement.style.fill = 'rgb(255, 0, 0)'
                                    textElement.style.fill = 'black'

                                    window.location.href = link
                                })
                            }
                        } else {
                            console.warn(`Elementos no encontrados: path: ${pathId}, text: ${textId}`)
                        }
                    })
                } catch (error) {
                    console.error('Error interactuando con elementos del SVG:', error)
                }
            }
            // PROCESOS DE APOYO
            if (svgDoc) {
                try {
                    // Definir los elementos específicos
                    const specificElements = [
                        {
                            pathId: 'path46',
                            textId: 'text7',
                            hover: true,
                            click: true,
                            link: "gestion-juridica-contractual"
                        },
                        {
                            pathId: 'path45',
                            textId: 'text9',
                            hover: true,
                            click: true,
                            link: "gestion-mercadeo-admisiones"
                        },
                        {
                            pathId: 'path44',
                            textId: 'text10',
                            hover: true,
                            click: true,
                            link: "gestion-administrativa-financiera"
                        },
                        {
                            pathId: 'path43',
                            textId: 'text11',
                            hover: true,
                            click: true,
                            link: "gestion-infraestructura-fisica-tecnologica"
                        }
                    ]

                    specificElements.forEach(({ pathId, textId, hover, click, link }) => {
                        const pathElement = svgDoc.getElementById(pathId)
                        const textElement = svgDoc.getElementById(textId)

                        if (pathElement && textElement) {
                            // Hover
                            if (hover) {
                                // Hover sobre el path
                                pathElement.addEventListener('mouseover', function () {
                                    this.style.cursor = 'pointer'
                                    this.style.fill = ' #f6a017'
                                    this.style.stroke = 'black'
                                    this.style.strokeWidth = '2'
                                    if (this.id == 'path44') {
                                        this.style.opacity = '1'
                                        this.style.fillOpacity = '1'
                                    }
                                    if (this.id == 'path45') {
                                        this.style.opacity = '1'
                                        this.style.fillOpacity = '1'
                                    }
                                    textElement.style.cursor = 'pointer'
                                    textElement.style.fill = 'red'
                                })

                                pathElement.addEventListener('mouseout', function () {
                                    this.style.fill = ' #ed7d31'
                                    this.style.stroke = 'none'
                                    this.style.strokeWidth = '0'
                                    if (this.id == 'path44') {
                                        this.style.opacity = '0'
                                        this.style.fillOpacity = '0'
                                    }
                                    if (this.id == 'path45') {
                                        this.style.opacity = '0'
                                        this.style.fillOpacity = '0'
                                    }
                                    textElement.style.fill = 'black'
                                })

                                // Hover sobre el texto
                                textElement.addEventListener('mouseover', function () {
                                    this.style.cursor = 'pointer'
                                    this.style.fill = 'red'
                                    pathElement.style.stroke = 'black'
                                    pathElement.style.strokeWidth = '2'
                                    if (this.id == 'text10') {
                                        pathElement.style.opacity = '1'
                                        pathElement.style.fillOpacity = '1'
                                    }
                                    if (this.id == 'text9') {
                                        pathElement.style.opacity = '1'
                                        pathElement.style.fillOpacity = '1'
                                    }
                                    pathElement.style.stroke = 'black'
                                    pathElement.style.strokeWidth = '2'

                                    pathElement.style.fill = ' #f6a017'
                                })

                                textElement.addEventListener('mouseout', function () {
                                    this.style.fill = 'black'
                                    pathElement.style.stroke = 'none'
                                    pathElement.style.strokeWidth = '0'
                                    if (this.id == 'text10') {
                                        pathElement.style.opacity = '0'
                                        pathElement.style.fillOpacity = '0'
                                    }
                                    if (this.id == 'text9') {
                                        pathElement.style.opacity = '0'
                                        pathElement.style.fillOpacity = '0'
                                    }
                                    pathElement.style.fill = ' #ed7d31'
                                })
                            }

                            // Clic
                            if (click) {
                                pathElement.addEventListener('click', function () {
                                    console.log(`Elemento ${pathId} clickeado`)

                                    pathElement.style.fill = 'rgb(255, 0, 0)'
                                    textElement.style.fill = 'black'

                                    window.location.href = link
                                })

                                textElement.addEventListener('click', function () {
                                    console.log(`Elemento ${textId} clickeado`)

                                    pathElement.style.fill = 'rgb(255, 0, 0)'
                                    textElement.style.fill = 'black'

                                    window.location.href = link
                                })
                            }
                        } else {
                            console.warn(`Elementos no encontrados: path: ${pathId}, text: ${textId}`)
                        }
                    })
                } catch (error) {
                    console.error('Error interactuando con elementos del SVG:', error)
                }
            }

            // PROCESOS MISIONALES
            if (svgDoc) {
                try {
                    // Definir los elementos específicos
                    const specificElements = [
                        {
                            pathId: 'path42',
                            textId: 'text12',
                            hover: true,
                            click: true,
                            link: "proyeccion-social-impacto"
                        },
                        {
                            pathId: 'path41',
                            textId: 'text16',
                            hover: true,
                            click: true,
                            link: "investigacion-pertinente"
                        },
                        {
                            pathId: 'path40',
                            textId: 'text17',
                            hover: true,
                            click: true,
                            link: "docencia-calidad"
                        }
                    ]

                    specificElements.forEach(({ pathId, textId, hover, click, link }) => {
                        const pathElement = svgDoc.getElementById(pathId)
                        const textElement = svgDoc.getElementById(textId)

                        if (pathElement && textElement) {
                            // Hover
                            if (hover) {
                                // Hover sobre el path
                                pathElement.addEventListener('mouseover', function () {
                                    this.style.cursor = 'pointer'
                                    this.style.fill = ' #ffc000'
                                    this.style.stroke = 'black'
                                    this.style.strokeWidth = '2'
                                    if (this.id == 'path41') {
                                        this.style.opacity = '1'
                                        this.style.fillOpacity = '1'
                                    }
                                    textElement.style.cursor = 'pointer'
                                    textElement.style.fill = 'red'
                                })

                                pathElement.addEventListener('mouseout', function () {
                                    this.style.fill = ' #ffd966'
                                    textElement.style.fill = 'black'
                                    if (this.id == 'path41') {
                                        this.style.opacity = '0'
                                        this.style.fillOpacity = '0'
                                    }
                                    this.style.stroke = 'none'
                                    this.style.strokeWidth = '0'
                                })

                                // Hover sobre el texto
                                textElement.addEventListener('mouseover', function () {
                                    this.style.cursor = 'pointer'
                                    this.style.fill = 'red'
                                    pathElement.style.stroke = 'black'
                                    pathElement.style.strokeWidth = '2'
                                    if (this.id == 'text16') {
                                        pathElement.style.opacity = '1'
                                        pathElement.style.fillOpacity = '1'
                                    }
                                    pathElement.style.fill = ' #ffc000'
                                })

                                textElement.addEventListener('mouseout', function () {
                                    this.style.fill = 'black'
                                    pathElement.style.fill = ' #ffd966'
                                    if (this.id == 'text16') {
                                        pathElement.style.opacity = '0'
                                        pathElement.style.fillOpacity = '0'
                                    }
                                    pathElement.style.stroke = 'none'
                                    pathElement.style.strokeWidth = '0'
                                })
                            }

                            // Clic
                            if (click) {
                                pathElement.addEventListener('click', function () {
                                    console.log(`Elemento ${pathId} clickeado`)

                                    pathElement.style.fill = 'rgb(255, 0, 0)'
                                    textElement.style.fill = 'black'

                                    window.location.href = link
                                })

                                textElement.addEventListener('click', function () {
                                    console.log(`Elemento ${textId} clickeado`)

                                    pathElement.style.fill = 'rgb(255, 0, 0)'
                                    textElement.style.fill = 'black'

                                    window.location.href = link
                                })
                            }
                        } else {
                            console.warn(`Elementos no encontrados: path: ${pathId}, text: ${textId}`)
                        }
                    })
                } catch (error) {
                    console.error('Error interactuando con elementos del SVG:', error)
                }
            }
        })
    }
})
