# Manual técnico · RetailNow

## Arquitectura

- `index.html` es una aplicación estática de página única que integra estructura HTML, estilos CSS y lógica JavaScript.
- GitHub Pages entrega el archivo sin servidor de aplicación. La carga CSV se realiza con la API `File` del navegador. El contenido de los archivos permanece en el equipo del usuario durante la sesión.
- El panel no necesita dependencias JavaScript externas. El gráfico usa Canvas nativo; CSV y el informe Word se generan con `Blob`; el PDF usa la función de impresión del navegador.
- Para el análisis académico con las librerías solicitadas, el repositorio conserva `main.py` y `analisis_red_tiendas.ipynb`, que utilizan Pandas y NumPy en un entorno Python.

## Flujo de datos

1. Los tres selectores HTML aceptan múltiples archivos `.csv` para ventas, inventario y satisfacción.
2. `readGroup()` lee cada archivo con `File.text()` y combina los registros del grupo seleccionado.
3. `parseCSV()` detecta coma, punto y coma, tabulador o barra vertical; respeta comillas dobles y campos que incluyen separadores.
4. `normalize()` elimina tildes y normaliza mayúsculas, espacios y signos para buscar los encabezados.
5. `findColumn()` asigna las columnas mediante listas de alias en el objeto `aliases`.
6. `analyze()` calcula métricas, agrega resultados por tienda y relaciona ventas, inventarios y satisfacción.
7. `render()` actualiza tarjetas, tablas, alertas, gráfico Canvas y cuerpo del informe imprimible.
8. Las funciones `downloadTable()`, `downloadChart` y `downloadWord` exportan los resultados. `downloadPdf` activa el diálogo de impresión del navegador.

## Columnas reconocidas

Los alias actuales se configuran en `aliases` dentro de `index.html`.

- Tienda: `ID_Tienda`, `tienda`, `store_id`, `store`, `sucursal`, `branch`, `local`.
- Producto: `producto`, `product`, `articulo`, `item`, `sku`.
- Unidades: `cantidad_vendida`, `unidades_vendidas`, `cantidad`, `quantity`, `units_sold`, `unidades`, `vendido`.
- Precio unitario: `precio_unitario`, `unit_price`, `precio`, `price`.
- Ingresos: `total_ventas`, `ingresos`, `revenue`, `sales_total`, `importe`, `total`.
- Stock: `stock_disponible`, `stock`, `inventario`, `available_stock`, `existencias`.
- Satisfacción: `satisfaccion_promedio`, `satisfaccion`, `satisfaction`, `calificacion`, `rating`, `score`.

Para agregar un encabezado nuevo, añade su versión normalizada al arreglo correcto dentro de `aliases`. Por ejemplo, si llega `cant_vta`, agrega `"cant_vta"` a `aliases.quantity`. `normalize()` ya convierte encabezados acentuados, así que no hace falta añadir variantes solo por mayúsculas o tildes.

## Cálculos

- Los ingresos por fila son el valor existente en una columna de ingresos reconocida o, en su defecto, unidades × precio unitario.
- El resumen agrega ingresos y unidades por tienda. La mediana se calcula ordenando los totales y tomando el valor central; la desviación estándar es poblacional.
- El porcentaje de rotación mostrado es unidades vendidas / stock disponible × 100. El aviso crítico aplica estrictamente cuando es inferior al 10%.
- La satisfacción se promedia por tienda si existen varias filas. Valores entre 0 y 1 se convierten a escala porcentual; se marcan los promedios inferiores al 60%.
- Cuando faltan columnas necesarias para inventario o satisfacción, la aplicación muestra el problema o indica que la sección fue omitida.

## Mantener y publicar cambios

1. Edita `index.html` y los manuales en el repositorio local.
2. Revisa que las rutas de descargas apunten a nombres existentes en la raíz del repositorio.
3. Sube los archivos actualizados a la rama `main`.
4. GitHub Pages volverá a publicar la versión estática tras el commit.
5. Para un nuevo informe o métrica, actualiza el cálculo en `analyze()`, el renderizado en `render()` y los formatos descargables en `createPrintReport()` y las funciones de descarga.

## Limitaciones conocidas

- El análisis web se ejecuta en el dispositivo y depende de la memoria disponible del navegador; archivos CSV extremadamente grandes pueden resultar lentos.
- Las columnas deben coincidir con los alias reconocidos o añadirse al mapa `aliases`.
- El documento de Word se ofrece en formato `.doc` HTML compatible para mantener la aplicación sin librerías externas. Para PDF, el usuario elige **Guardar como PDF** desde el diálogo del navegador.
- La web no ejecuta Python en el servidor. `main.py` y el notebook se ejecutan localmente en VS Code, fuera del navegador.
