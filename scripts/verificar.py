#!/usr/bin/env python3
"""Verificación local y sencilla sin dependencias. NO certifica privacidad ni permisos."""
from html.parser import HTMLParser
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class Scan(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.links=[]; self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if tag=='img' and 'src' in a:self.images.append(a['src'])
scan=Scan();scan.feed((ROOT/'index.html').read_text(encoding='utf-8'))
errors=[]
for identifier in ('inicio','recuerdos','galeria','dedicatoria'):
    if identifier not in scan.ids:errors.append('Falta ancla '+identifier)
for link in scan.links:
    if link.startswith('#') and link[1:] not in scan.ids: errors.append('Enlace interno roto '+link)
for path in scan.images:
    if not path.startswith(('data:','https:','http:')) and not (ROOT/path).is_file():errors.append('No existe imagen '+path)
for file in ('style.css','script.js','AGENTS.md','materiales-aula/presentacion-clase-1.html','materiales-aula/referencias-para-votar.html','materiales-aula/fichas-para-imprimir.pdf'):
    if not (ROOT/file).is_file(): errors.append('Archivo faltante: '+file)
if errors:
    print('ERROR:',*errors,sep='\n- ');raise SystemExit(1)
print('OK: 4 secciones, enlaces y archivos base presentes.')
print(f'Galería: {len(scan.images)} imágenes. Documento clase 1 y fichas presentes.')
print('ADVERTENCIA: este chequeo NO reemplaza la revisión institucional de fotos y datos personales.')
