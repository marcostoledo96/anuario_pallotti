# AGENTS.md — Reglas obligatorias de Antigravity y demás agentes

**Aviso 2026:** este repositorio se creó con visibilidad pública. No incluir datos ni fotografías de estudiantes, permisos, prompts con información personal o referencias a carpetas privadas. Cambiar la visibilidad es una gestión del docente en GitHub.

## Naturaleza del proyecto

Anuario escolar de 7.º grado con **vibe coding**. El objetivo es que los alumnos diseñen y aprendan a dirigir una IA, **no enseñar programación ni sintaxis**. Dos agentes podrían trabajar en paralelo con supervisión docente, un agente por equipo. No hay autorización para publicar nada automáticamente.

## Antes de hacer cambios

1. Leer `README.md`, `docs/00-brief-y-alcance.md`, `docs/08-decisiones-y-configuracion.md`, `docs/10-flujo-antigravity-y-git.md` y el `README.md` de la carpeta de tu equipo.
2. Revisar la lista de **skills disponibles**. Usar solo las que sumen a HTML/CSS/JS, UI, accesibilidad o QA; no agregar dependencias, descargar skills ni pedir cuentas nuevas.
3. Confirmar con el docente: sección, estética votada, recursos realmente aprobados y dos elementos visuales de referencias humanas. Si falta la votación, limitarse a pruebas **reversibles** con recursos DEMO.

## Límites innegociables

- SOLO HTML, CSS y JS nativos. No React, Vue, Angular, Tailwind, npm, build tools, frameworks, CDN, backend, almacenamiento externo ni cookies.
- Una sola página pública final con cuatro anclas `#inicio`, `#recuerdos`, `#galeria`, `#dedicatoria`. No crear páginas nuevas para el producto final.
- En modo equipo, escribir **solo en `prototipos/<equipo>/`**. No editar la raíz, los archivos de otro grupo, `docs/`, `assets/publicables/` ni configuraciones. El docente hace la integración luego.
- No cambiar la estructura entera por una solicitud pequeña. Hacer cambios localizados, mantenibles y fáciles de mostrar en 40 minutos.
- No copiar HTML, CSS, textos, logos, ilustraciones o fotografías de las webs de referencia. Extraer ideas de disposición, tono, tipografía, color, composición, pero crear recursos originales.
- Solo texto `DEMO` y gráficos neutros hasta que el docente aporte expresamente contenido aprobado. No inventar recuerdos, dichos, fechas, nombres, pronombres ni perfiles de alumnos como si fueran reales.
- No subir fotografías, imágenes identificables ni datos de menores a IA externa; ni incluirlos en prompts, commits, logs o capturas. No procesar archivos de la carpeta privada del colegio.
- No publicar, desplegar, ejecutar `git push`, crear cuentas o instalar herramientas sin aprobación explícita del docente.
- Responsive desde 360 px; HTML semántico; foco visible; navegación por teclado; `alt` útil; contrastes; respetar `prefers-reduced-motion`.
- Si trabajás la galería: **ampliación de imagen con botón y `dialog`**, cierre con tecla Escape y botón, sin bibliotecas de terceros.
- No reutilizar marcas de franquicias (por ejemplo, Netflix) literalmente: una referencia a carteles de cine es inspiración conceptual, no permiso para usar logos ajenos.

## Dinámica con alumnos

1. Preguntar qué quieren lograr y qué vieron en las webs reales.
2. Repetir en palabras sencillas qué vas a hacer. Máximo dos opciones viables.
3. Generar una pequeña prueba en su carpeta.
4. Mostrarla funcionando, dejar que los alumnos hagan QA.
5. Pedir feedback concreto según la regla 2–2–1: dos aciertos, dos cambios y una prueba.
6. Hacer una sola iteración importante por turno, explicando lo que cambió sin enseñar sintaxis.

## Entrega de cada sesión

Informar en lenguaje claro:
- Archivos creados o cambiados, **dentro de la carpeta asignada**.
- Instrucción original y cambios pedidos por los alumnos.
- Qué funciona y qué queda pendiente.
- 3 comprobaciones visuales/manuales (PC, celular, teclado si corresponde).
- Cómo guardar el resultado en el almacenamiento controlado del docente; nunca asumir persistencia de las PCs del colegio.

## Integración

Solo el docente puede solicitar explícitamente consolidar los prototipos en la raíz. Mantener como máximo `index.html`, `style.css`, `script.js` y recursos estáticos. Evitar sobreingeniería. El sitio neutral inicial no fija estética definitiva. Antes de publicar, revisar `docs/06-qa-y-publicacion.md`.
