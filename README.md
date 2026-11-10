# Proyecto Anuario 7.º · Promoción 2026

**Proyecto de vibe coding para 7.º grado.** Cuatro equipos diseñan una web **single page**. El docente ejecuta los agentes, gestiona GitHub y se ocupa de integrar, animar y publicar.

> **Estado:** KIT LISTO PARA CLASE 1 / SIN IDENTIDAD FINAL NI NOMBRE PÚBLICO.
> El aspecto y nombre los decidirán los alumnos después de ver referencias reales. Toda foto, frase y fecha del sitio inicial está marcada **DEMO**.

## Decisiones confirmadas

- **4 equipos:** Portada y navegación, Recuerdos, Galería, Dedicatoria y créditos.
- **4 encuentros de ~40 minutos por equipo**, en tandas de dos equipos. Dos PCs con Antigravity (docente presente) y otras con Internet, Canva, búsqueda y pruebas.
- **No enseñar código:** investigar diseños, describir pedidos a la IA, revisar y corregir.
- **Todos usan la misma identidad visual:** cada equipo propone UNA referencia y entre las cuatro propuestas se acuerda una estética final.
- **Materiales:** colegio + familias, en almacenamiento privado de la escuela, nunca en este repositorio mientras estén pendientes de autorización.
- **Interacción elegida:** la galería permite ampliar las fotos. Demo funcional con gráficos abstractos que no representan a menores.
- **Producto final:** sitio web público solo cuando el colegio valide contenido y derechos.

## Empezar por aquí

1. **Docente:** abrir [`materiales-aula/presentacion-clase-1.html`](materiales-aula/presentacion-clase-1.html) a pantalla completa. Se pasa con flechas o botones.
2. **Equipos:** recorrer [`materiales-aula/referencias-para-votar.html`](materiales-aula/referencias-para-votar.html). Cada tarjeta lleva a una web o pieza de autor; su miniatura de estilo es solo orientativa.
3. **Imprimir:** [`materiales-aula/fichas-para-imprimir.pdf`](materiales-aula/fichas-para-imprimir.pdf) (una ficha por equipo + acta, si hacen falta más copias imprimir la hoja del grupo).
4. **Docente:** seguir [`docs/09-guion-clase-1.md`](docs/09-guion-clase-1.md) y anotar la propuesta de cada equipo en [`docs/02-votacion-diseno.md`](docs/02-votacion-diseno.md).
5. Cuando se cierre la votación, llenar [`docs/08-decisiones-y-configuracion.md`](docs/08-decisiones-y-configuracion.md) y usar [`prompts/01-pedido-por-equipo.md`](prompts/01-pedido-por-equipo.md).

## Página web neutral

- `index.html` + `style.css` + `script.js`: **maqueta provisional**, nunca el diseño definitivo. Tiene cuatro anclas y una galería DEMO con lightbox accesible.
- `assets/demo/`: ilustraciones abstractas de prueba, sin fotos reales.
- `assets/publicables/`: vacío y **excluido de Git por seguridad** hasta que, tras las autorizaciones, el docente habilite expresamente solo las piezas aprobadas.
- `prototipos/<equipo>/`: zona independiente del agente de cada equipo.
- `AGENTS.md`: reglas del agente; leer antes de ejecutar Antigravity.

## Documentación principal

| Archivo | Uso |
|---|---|
| `docs/00-brief-y-alcance.md` | Alcance y qué queda fuera |
| `docs/01-cronograma.md` | Cuatro clases por equipo |
| `docs/02-votacion-diseno.md` | Propuesta de cada grupo y método para resolver estética única |
| `docs/03-equipos-y-roles.md` | Roles rotativos (sin programar) |
| `docs/04-materiales-y-privacidad.md` | Recolección, autorización y custodia |
| `docs/05-tablero-de-tareas.md` | Backlog sencillo y checklists |
| `docs/06-qa-y-publicacion.md` | Pruebas y gate de publicación |
| `docs/07-referencias-visuales.md` | Referencias verificadas por URL y qué observar |
| `docs/08-decisiones-y-configuracion.md` | Lo definido y pendientes reales |
| `docs/09-guion-clase-1.md` | Guión minuto a minuto para el aula |
| `docs/10-flujo-antigravity-y-git.md` | Cómo evitar conflictos entre dos agentes y guardar el avance |
| `docs/11-solicitud-a-colegio.md` | Borrador para solicitar contenidos y autorizaciones |

## Abrir y probar

Doble clic en `index.html` para un vistazo. Para un servidor local, ejecutar en la carpeta del proyecto:

```bash
python3 -m http.server 8000
# Abrir http://localhost:8000
```

No hay npm, instalación ni build. Para un chequeo local de estructura: `python3 scripts/verificar.py`.

## Repo GitHub (a cargo del docente)

**Repositorio real:** [`marcostoledo96/anuario_pallotti`](https://github.com/marcostoledo96/anuario_pallotti). **Visibilidad verificada al iniciar: público.** Cambiar a **privado** en GitHub → Settings → General → Danger Zone, si la institución lo requiere. No subir imágenes, nombres ni materiales de menores aunque se vuelva privado. Ver [`docs/10-flujo-antigravity-y-git.md`](docs/10-flujo-antigravity-y-git.md). **No conectar Vercel ni publicar el sitio con material real hasta la revisión institucional.**
