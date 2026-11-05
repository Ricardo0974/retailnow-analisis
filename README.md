# RetailNow · Análisis con NumPy y Pandas

Proyecto académico para analizar ventas, inventario y satisfacción de clientes. Incluye una aplicación web para cargar y procesar archivos CSV en el navegador, más el análisis reproducible de Python con Pandas y NumPy.

## Contenido

- `index.html`: aplicación web adaptable a PC, tableta y móvil. Permite cargar CSV, ejecutar el análisis y descargar tablas, gráficos PNG e informes Word/PDF.
- `MANUAL_USUARIO.md`: instrucciones paso a paso para cargar archivos, ejecutar el análisis y guardar resultados.
- `MANUAL_TECNICO.md`: estructura interna, columnas reconocidas y pautas de mantenimiento.
- `analisis_red_tiendas.ipynb`: análisis explicado con Pandas y NumPy para Jupyter en VS Code.
- `main.py`: versión de consola en Python.
- `sales.csv`, `inventories.csv`, `satisfaction.csv`: archivos de ejemplo.
- `requirements.txt`: dependencias de Python.

## Abrir la aplicación web

Abre `index.html` en un navegador, o visita la página publicada con GitHub Pages. Pulsa **Cargar archivos**, selecciona CSV de ventas y, si están disponibles, los CSV de inventario y satisfacción. Luego pulsa **Ejecutar análisis**. La aplicación procesa los archivos en el navegador; no los envía a un servidor.

Consulta el [Manual de usuario](MANUAL_USUARIO.md) para los pasos completos y el [Manual técnico](MANUAL_TECNICO.md) para los detalles de las columnas y cálculos.

## Ejecutar con Python en VS Code

Necesitas Python 3.10 o superior, Visual Studio Code y las extensiones Python y Jupyter.

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Para el notebook, ábrelo en VS Code, selecciona el intérprete `.venv` como kernel y ejecuta las celdas en orden.

## Publicación

`index.html` está en la raíz y se publica mediante GitHub Pages desde la rama `main`, carpeta `/ (root)`. El sitio es estático: las funciones web se ejecutan en el navegador. El análisis del script y notebook se ejecuta localmente en Python.
