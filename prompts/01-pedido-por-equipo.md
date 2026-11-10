# Prompts de inicio para copiar en Antigravity (docente)

**Antes:** pegar `AGENTS.md` como contexto, confirmar carpeta asignada, reemplazar campos entre `[ ]` con decisiones reales. Los alumnos aportan dos recursos de la referencia; las instrucciones técnicas las mantiene el docente.

## 1. Portada y navegación

> Somos el equipo de Portada de un anuario escolar single page. Vamos a trabajar en `prototipos/portada/` y en ningún otro lugar. El estilo común votado es `[ESTILO]`, inspirado en `[URL]`; nos gustan `[RECURSO 1]` y `[RECURSO 2]`. Crear una portada con título PROVISIONAL `Anuario de 7.º - DEMO`, una composición visual con gráficos neutros y navegación a cuatro secciones. No usar fotos ni nombres reales. Solo HTML/CSS/JS puro, responsive. No hagas deploy ni toques raíz. Al final, abrir vista y explicar dos decisiones visuales.

## 2. Recuerdos

> Somos el equipo Recuerdos. Trabajá únicamente en `prototipos/recuerdos/`. Nuestra identidad común es `[ESTILO]` y la referencia visual es `[URL]`; queremos adaptar `[DOS DETALLES]`. Proponer una pequeña línea de tiempo de 3 hitos y 4 frases **DEMO** claramente ficticias, sin hacer pasar inventos por verdaderos. Mostrar una disposición interesante y legible para celular. HTML/CSS/JS puro, sin librerías y sin tocar otros archivos. Dejá fácil reemplazar textos luego.

## 3. Galería

> Somos el equipo Galería. Solo `prototipos/galeria/`. Estilo `[ESTILO]`, referencia `[URL]`, detalles `[DOS DETALLES]`. Diseñar una grilla visual que empiece con 6 imágenes abstractas de demostración y que permita ampliar una al seleccionarla. Usar `<dialog>`, abrir con botón, cerrar con botón y Escape, recuperar foco al cerrar y soportar móvil. No usar fotos reales ni herramientas externas. HTML/CSS/JS puro, sin modificar raíz ni otras carpetas. Hacer una prueba con teclado.

## 4. Dedicatoria y créditos

> Somos el equipo Dedicatoria. Trabajá solo en `prototipos/dedicatoria/`. Estilo común `[ESTILO]` e inspiración `[URL]`; adaptar `[DOS DETALLES]` sin copiar. Crear un cierre claro y emotivo con un mensaje **DEMO**, espacio para una dedicatoria auténtica que escribiremos después y créditos por los cuatro equipos (sin nombres reales). Evitar frases típicas de IA, confeti, clichés y fondos genéricos. HTML/CSS/JS puro, responsive. No tocar otros equipos.

## Primer pedido para integrar (solo el docente, DESPUÉS de recibir 4 prototipos)

> Leé README, AGENTS, brief, votación y los cuatro `prototipos/*`. No escribas en carpetas de prototipos. Integrá los diseños elegidos en UNA página usando `index.html`, `style.css` y `script.js`, con IDs `inicio`, `recuerdos`, `galeria`, `dedicatoria`. Conservá la identidad votada y el lightbox de galería. Mantener todo con texto/fotos DEMO hasta contar con autorizaciones. No agregues frameworks, build, plugins externos ni despliegue. Señalá conflictos y registrá qué decisiones técnicas tomaste para integrar sin borrar ideas de los chicos.
