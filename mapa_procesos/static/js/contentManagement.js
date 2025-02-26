// Función para cargar contenido desde la base de datos
async function loadContent() {
  const modelName = document.getElementById('model-name').value;
  const loadingModal = document.getElementById('loading-modal');
  loadingModal.style.display = 'flex';  // Mostrar el modal de carga

  // Hacer que todos los elementos editable sean invisibles mientras cargan
  const loadingElements = Array.from({ length: 40 }, (_, i) => document.getElementById(`editable${i + 1}`));
  loadingElements.forEach(element => {
    if (element) {
      element.classList.remove('loaded');
      element.innerText = 'Cargando...';
      element.style.color = 'gray';  // Establecer color gris para indicar que está cargando
    }
  });

  try {
    // Esperamos 2 segundos para que se vea la animación de carga
    await new Promise(resolve => setTimeout(resolve, 2000));
    const response = await fetch(`/obtener-contenido/${modelName}/`);
    if (!response.ok) {
      throw new Error('Error al obtener contenido');
    }

    const data = await response.json();
    updateContent(data);  // Actualizar el contenido en el DOM

  } catch (error) {
    console.error('Error al cargar el contenido:', error);
  } finally {
    loadingModal.style.display = 'none'; // Ocultar el modal de carga
  }
}

// Función para actualizar el contenido en el DOM
function updateContent(data) {
  const loadingElements = Array.from({ length: 40 }, (_, i) => document.getElementById(`editable${i + 1}`));
  loadingElements.forEach((element, i) => {
    const key = `editable${i + 1}`;
    if (element && data[key]) {
      element.innerText = data[key];
      element.style.color = 'black';
      element.classList.add('loaded');
    }
  });
}

// Función para guardar contenido
const saveButton = document.getElementById('saveButton');

if (saveButton) {
  saveButton.addEventListener('click', async function () {
    const modelName = document.getElementById('model-name').value;
    const folderName = document.getElementById('folder-name').innerText;
    const htmlFileName = document.getElementById('html-file-name').innerText;
    const keys = Array.from({ length: 40 }, (_, i) => `editable${i + 1}`);

    const sendingModal = document.getElementById('sending-modal');
    sendingModal.style.display = 'flex'; // Mostrar el modal de "Enviando datos..."

    // Preparar los datos a enviar en un solo objeto
    const formData = keys.map(key => ({
      id: key,
      content: document.getElementById(key).innerText.trim() || '...'  // Si está vacío, se usa '...'
    }));

    try {
      // Esperamos 1 segundo para que se vea la animación de envío
      await new Promise(resolve => setTimeout(resolve, 1000));
      // Enviar todos los datos de una vez en una sola solicitud POST
      const response = await fetch(`/guardar-contenido/${modelName}/${folderName}/${htmlFileName}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ data: formData })  // Enviamos todos los datos en una sola solicitud
      });

      // Verificar si la respuesta no es exitosa
      if (!response.ok) {
        // Si la respuesta no es OK (404, 500, etc.), lanzar un error con el contenido de la respuesta
        const errorData = await response.json();
        throw new Error(`Error: ${JSON.stringify(errorData)}`);
      }

      // Si no hubo error, ocultamos el modal de "Enviando datos"
      sendingModal.style.display = 'none';

      // Mostrar SweetAlert de éxito
      await Swal.fire({
        title: '¡Enviado correctamente!',
        text: 'La información ha sido guardada.',
        icon: 'success',
        confirmButtonText: 'Aceptar'
      });

      // Recargar el contenido desde la base de datos después de guardar los datos
      loadContent();  // Cargar el contenido actualizado desde la base de datos

    } catch (error) {
      // Si ocurrió un error durante el proceso, mostrar el error en consola y en la interfaz
      console.error('Error al guardar los datos:', error);

      // Asegurarnos de ocultar el modal de "Enviando datos" incluso si hay un error
      sendingModal.style.display = 'none';

      // Mostrar el mensaje de error usando SweetAlert
      await Swal.fire({
        title: '¡Error!',
        text: 'Hubo un problema al enviar los datos. Intenta nuevamente.',
        icon: 'error',
        confirmButtonText: 'Aceptar'
      });
    }
  });
}

// Función para obtener el CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Cargar contenido al cargar la página
document.addEventListener('DOMContentLoaded', function () {
  loadContent();
});
