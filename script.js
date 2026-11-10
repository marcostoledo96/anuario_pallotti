// Sitio DEMO: la única interacción es ampliar/cerrar imágenes de prueba.
const dialog = document.getElementById('visor');
const enlarged = document.getElementById('visor-image');
const caption = document.getElementById('visor-caption');
const close = document.getElementById('cerrar-visor');
let lastOpener = null;

document.querySelectorAll('.photo-button').forEach(button => {
  button.addEventListener('click', () => {
    lastOpener = button;
    enlarged.src = button.dataset.image;
    enlarged.alt = button.dataset.description || 'Imagen abstracta de demostración ampliada';
    caption.textContent = button.dataset.description || 'Imagen de prueba';
    dialog.showModal();
    close.focus();
  });
});
close.addEventListener('click', () => dialog.close());
dialog.addEventListener('close', () => { enlarged.removeAttribute('src'); lastOpener?.focus(); });
dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
