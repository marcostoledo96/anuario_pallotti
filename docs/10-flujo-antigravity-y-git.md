# Flujo docente: dos Antigravity, un único repositorio y PCs que pueden resetearse

## Regla base

**Los alumnos no hacen Git.** El docente inicia y supervisa Antigravity, y siempre guarda todo al terminar. La carpeta del colegio es para **originales privados y fichas de clase**; GitHub para código y documentación **sin datos personales**.

## Carpeta de cada agente

- PC con equipo Portada: `prototipos/portada/`
- PC con equipo Recuerdos: `prototipos/recuerdos/`
- PC con equipo Galería: `prototipos/galeria/`
- PC con equipo Dedicatoria: `prototipos/dedicatoria/`

Las dos PCs tienen **copias separadas** del repo. Ningún agente edita archivos fuera de su carpeta. El docente copia o integra los resultados en el repo maestro después de cada clase. Si ambos equipos usan la misma rama local en PCs distintas, **no empujar cambios simultáneamente**: copiar los archivos validados a la copia maestra y hacer un único commit por tanda.

## Si los alumnos trabajan con PCs que borran al reiniciar

Al cierre: 1) guardar prompt y ficha en carpeta institucional, 2) copiar archivos de prototipo/capturas a la copia docente, 3) verificar que se pueden volver a abrir, 4) recién entonces apagar. Para fotos de menores usar únicamente almacenamiento institucional restringido.

## Repositorio ya creado y copia local del docente

Repositorio real: `marcostoledo96/anuario_pallotti`, rama `main`. Al crear este kit figuraba **público**. Se recomienda cambiarlo a privado desde GitHub → Settings → General → Danger Zone si corresponde. En cualquier caso, nunca subir fotografías de menores, autorizaciones ni textos identificables sin aprobación institucional.

En tu ordenador, clonar la copia maestra:

```bash
git clone https://github.com/marcostoledo96/anuario_pallotti.git
cd anuario_pallotti
python3 scripts/verificar.py
```

La identidad pública del anuario (título y estética) es independiente del nombre técnico de GitHub. El docente debe revisar cada `git add`, commit y push; durante el aula, los alumnos no ejecutan Git.

## Trabajo de los agentes por equipo

1. Entrar en `prototipos/<equipo>/` con Antigravity.
2. Pegar el prompt de `prompts/01-pedido-por-equipo.md` editado por el grupo.
3. Repetir reglas `AGENTS.md`: no tocar raíz ni otros prototipos, usar solo demo y HTML/CSS/JS.
4. Docente revisa diff local y preview; copia únicamente archivos aprobados a la copia maestra.
5. Guardar mensajes del grupo y resumen de QA, commit controlado del docente.

## Integración posterior

El docente solicita a un agente aparte: reunir las secciones dentro de `index.html`, fusionar estilos en `style.css`, mantener `script.js`, conservar cuatro IDs, usar sistema visual votado y conservar ampliación de galería. No entregar a agentes permisos de deploy sin revisión.

## Vercel

No conectar producción hasta aprobar fotos/textos y política de publicación. Si se usa Vercel con este repositorio: importar repo → Framework preset `Other` → root `./` → sin build command; revisar dominio/preview con contenido ficticio únicamente. No considerar una URL de preview como privada.
