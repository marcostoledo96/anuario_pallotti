# Materiales, autorizaciones y custodia (lectura docente)

**Destino previsto: web abierta en Internet.** **El repositorio actual es público**, y aunque se haga privado tampoco vuelve privado al sitio desplegado; toda URL pública puede copiarse o difundirse. **Estado de permisos: PENDIENTE DE GESTIONAR CON EL COLEGIO.**

## Carpeta institucional, NO repositorio

Sugerir estructura en el almacenamiento privado de la escuela (configurar según sus reglas):

```
ANUARIO_7_2026_PRIVADO/
  00_autorizaciones/           ← acceso restringido: solo institución/docente autorizado
  01_originales_colegio/       ← fotos sin publicar
  02_aportes_familias/         ← fotos sin publicar
  03_textos_para_revision/     ← frases y anécdotas sin publicar
  04_preparados_aprobados/     ← únicamente material validado para web pública
  05_registro_autorizaciones/  ← ID de recurso + autorización + revisión
```

No poner nombres de alumnos ni consentimientos dentro de GitHub, prompts o material imprimible.

## Protocolo en 7 pasos

1. Dirección valida proyecto, responsable, canal institucional para recibir materiales, período de publicación, retiros y acceso.
2. Obtener autorizaciones adecuadas al **uso concreto: publicación de fotos, nombres o frases en sitio público**, respetando la decisión de cada familia/alumno. Aclarar posibilidad de no participar.
3. Mantener originales en almacenamiento institucional restringido; **nunca subir imágenes de menores a servicios de IA** sin evaluación y permiso expreso específico (por defecto: NO).
4. Contenidos revisa dignidad y contexto; no anécdotas humillantes, apodos ofensivos, teléfonos, direcciones, datos de salud, fechas de nacimiento, horarios o ubicaciones que expongan menores.
5. Registrar cada pieza con ID (`F001`, `T005`) y estado en planilla privada. No hacer públicas las planillas de autorización.
6. Solo imágenes y textos aprobados pasan a `assets/publicables/`, con nombres neutros, tamaño comprimido, metadatos EXIF eliminados y alternativas textuales adecuadas. **La carpeta está excluida por `.gitignore` por defecto:** luego del gate, el docente debe autorizar expresamente cada archivo, ajustar esa regla e incorporar solo esos archivos a Git para que Vercel los publique. **Verificar que un tercero que salga en la foto también tenga permiso.**
7. Antes del despliegue público el docente revisa **código, carpetas, historial Git, URLs de preview y publicación**. Mantener un canal de baja/rectificación posterior.

## Recursos de demostración

`assets/demo/` contiene gráficos abstractos originales y textos marcados `DEMO`. Son suficientes para las cuatro clases si los permisos llegan más tarde.

## Marco general (confirmar con dirección)

- Ley argentina 26.061, art. 22 (propia imagen, dignidad y privacidad): https://www.argentina.gob.ar/normativa/nacional/ley-26061-110778/actualizacion
- AAIP, niños y privacidad en entornos digitales: https://www.argentina.gob.ar/node/436471
- Defensoría de CABA, fotos escolares y autorización (material orientativo; la aplicación local puede variar): https://navegador.defensoria.org.ar/preguntas-y-temas/puede-la-escuela-difundir-fotos-de-mi-hijo-en-redes-sociales-y-que-debe/

**Este documento es un protocolo didáctico, no reemplaza las directivas o asesoramiento legal de la institución.**
