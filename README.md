# RetailNow · Análisis con NumPy y Pandas

Panel web del proyecto: abre [`index.html`](index.html) en un navegador para ver la portada visual. El notebook y el script contienen el análisis reproducible con Pandas y NumPy.

## Contenido

- `index.html`: portada web responsiva con indicadores, gráficos y enlaces a los recursos.
- `analisis_red_tiendas.ipynb`: análisis explicado paso a paso para Jupyter en Visual Studio Code.
- `main.py`: versión ejecutable desde la terminal.
- `sales.csv`, `inventories.csv`, `satisfaction.csv`: datos de entrada.
- `requirements.txt`: dependencias de Python.

## Requisitos

Python 3.10 o superior, Visual Studio Code y las extensiones Python y Jupyter.

## Ejecutar el análisis

```bash
python -m venv .venv
```

En Windows PowerShell, activa el entorno e instala las dependencias:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Para el notebook, ábrelo en VS Code, selecciona el intérprete de `.venv` como kernel y ejecuta las celdas en orden. El análisis busca primero los archivos CSV en `/workspace` y después junto al proyecto.

## Publicar la portada

El archivo `index.html` está en la raíz para publicarlo con GitHub Pages. En GitHub, abre **Settings → Pages**, elige **Deploy from a branch**, selecciona `main` y `/ (root)`, y guarda.

La página presenta un resumen estático de los datos; los cálculos reproducibles están en el notebook y en `main.py`.
