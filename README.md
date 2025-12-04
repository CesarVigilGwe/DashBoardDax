# DashBoardDax

Guía interactiva de DAX (Data Analytics Expressions) enfocada en el sector energético. Incluye un dashboard en HTML con secciones navegables, ejemplos de fórmulas y referencias rápidas para acelerar la creación de modelos en Power BI.

## Contenido
- **`dax-energy-cheatsheet.html`**: Dashboard principal con modo oscuro, buscador global y tarjetas temáticas.
- **`verification/`**: Scripts y capturas generadas con Playwright para verificar la búsqueda y el estado visual.

## Cómo usar
1. Abre `dax-energy-cheatsheet.html` directamente en tu navegador favorito (no requiere servidor).
2. Utiliza el buscador superior para filtrar secciones y tarjetas por palabras clave.
3. Explora la tabla de **Referencia Rápida** con el nuevo diseño compacto y chips por tipo de función.

## Verificación local
Si deseas recrear las capturas de verificación:
```bash
python verification/verify_final.py
```
Esto generará imágenes dentro de la carpeta `verification/`.

## Tecnologías destacadas
- HTML + CSS + JavaScript sin dependencias de build.
- Fuentes de Google (Inter) y iconografía de Font Awesome.
- Highlight.js para resaltar sintaxis de código.

## Créditos
Creado como hoja de referencia rápida para analistas y modeladores DAX en energía.
