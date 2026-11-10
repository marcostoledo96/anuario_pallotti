# QA de alumnos y checklist de publicación

## QA: preguntas simples (no programación)

- [ ] ¿La web tiene carácter propio, o parece una plantilla automática?
- [ ] ¿Desde el menú se llega a Portada, Recuerdos, Galería y Dedicatoria?
- [ ] ¿Se lee en una pantalla de celular sin cortar el texto?
- [ ] ¿Los colores y las letras coinciden con lo elegido por la clase?
- [ ] ¿Las frases o fechas dicen `DEMO` o son material verdadero revisado? ¿La IA inventó algo?
- [ ] ¿Las fotos se abren más grandes al tocarlas? ¿Se pueden cerrar?
- [ ] ¿No hay fotos repetidas, cortadas de forma rara o fuera de lugar?
- [ ] ¿Hay partes que resultan demasiado largas, ruidosas o confusas?

## QA técnico del docente

- [ ] `index.html` único, 4 IDs, enlaces sin error, JS sin errores en consola.
- [ ] Teclado: Tab, Enter/Espacio en fotos, Escape para cerrar, foco recuperado.
- [ ] Responsive 360/768/1280; imágenes contenidas, no scroll lateral.
- [ ] Sin recursos de terceros inyectados; sin cuenta, cookie, analytics ni backend.
- [ ] `prefers-reduced-motion` y alt text funcionales; alto contraste y foco visible.
- [ ] Fotografías comprimidas, sin EXIF; nombres de archivo neutros y descripción segura.
- [ ] `assets/demo/` no se confunde con material real.

## Gate ANTES de cualquier web pública identificable

- [ ] Dirección escolar aprueba el proyecto y el contenido final.
- [ ] Autorización verificada por pieza/identificación y terceros que aparezcan.
- [ ] Ninguna foto sin permiso en código, historial Git, carpetas o previews.
- [ ] Tras el gate: revisar `.gitignore` y versionar **solo** los archivos aprobados en `assets/publicables/` (si se opta por deploy Git).
- [ ] Se revisaron derechos de material externo y voluntariedad de participación.
- [ ] Se definió responsable de corrección y retiro del contenido.

**Nunca desplegar material de menores como «preview» sin autorización: los previews pueden ser accesibles por URL.** Un repo privado no implica web privada.

## Vercel (opcional, luego del gate)

Tras revisar el contenido y la visibilidad del repositorio, se puede importar en Vercel usando `Other`/sitio estático y directorio raíz. No hay comando de build ni frameworks. Publicar únicamente cuando el docente apruebe los contenidos; las direcciones `*.vercel.app` son públicas salvo protección configurada y validada.
