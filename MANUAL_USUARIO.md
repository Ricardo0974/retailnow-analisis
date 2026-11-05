# Manual de usuario · RetailNow

## 1. Abrir la aplicación

Puedes abrir `index.html` directamente en Chrome, Edge u otro navegador actual. También puedes abrir la página de GitHub Pages. No hace falta instalar Python para analizar los archivos desde la aplicación web.

## 2. Preparar los archivos

Guarda los datos como archivos `.csv`. La aplicación acepta archivos separados por coma, punto y coma, tabulador o barra vertical, con encabezados en español o inglés. Para combinar varias partes de un mismo conjunto de datos, selecciona todos esos CSV en el mismo selector.

Ejemplos de columnas reconocidas:

- Ventas: tienda (`ID_Tienda`, `tienda`, `store`, `sucursal`), producto (opcional), unidades (`Cantidad_Vendida`, `quantity`, `unidades`) y precio (`Precio_Unitario`, `unit_price`). Si el CSV ya tiene ingresos, puede usar `Total_Ventas`, `ingresos` o `revenue`.
- Inventario: tienda, producto y stock (`Stock_Disponible`, `stock`, `inventario`). Es opcional.
- Satisfacción: tienda y calificación (`Satisfacción_Promedio`, `satisfaction`, `rating`). Es opcional.

Cada archivo debe tener una fila de encabezados. Las filas sin valores útiles o con importes/unidades no numéricos pueden omitirse.

## 3. Cargar y ejecutar

1. En **Cargar tus archivos**, selecciona el botón de archivos de ventas y elige uno o varios CSV.
2. Si los tienes, agrega archivos de inventarios y satisfacción en sus respectivos cuadros.
3. Verifica los nombres que aparecen debajo de cada selector.
4. Pulsa **Ejecutar análisis** y espera el mensaje **Análisis finalizado**.
5. Revisa los indicadores, el gráfico de ingresos, la tabla por tienda y los hallazgos.
6. Para comenzar con los datos incluidos en el proyecto, pulsa **Cargar ejemplo RetailNow** y después **Ejecutar análisis**.
7. Para analizar otros datos, selecciona los archivos nuevos y vuelve a pulsar **Ejecutar análisis**. La nueva ejecución reemplaza el resumen anterior de la pantalla.

## 4. Descargar resultados

- **Descargar tabla CSV**: ingresos, unidades, stock, rotación y satisfacción por tienda.
- **Descargar hallazgos CSV**: productos con menos del 10% vendido y tiendas con satisfacción inferior al 60%.
- **Descargar gráfica PNG**: imagen del gráfico de ingresos por tienda.
- **Informe Word**: descarga un archivo `.doc` que se abre en Microsoft Word y contiene los indicadores y la tabla del análisis.
- **Imprimir / PDF**: abre el diálogo de impresión del navegador. Selecciona **Guardar como PDF** para crear el archivo PDF.

## 5. Interpretar los porcentajes

- **Venta / stock** = unidades vendidas del producto divididas por su stock disponible, multiplicado por 100. Menos del 10% aparece como inventario crítico.
- **Satisfacción**: los valores inferiores al 60% se marcan para revisar la experiencia de compra. Si el origen usa escala de 0 a 1, se convierte automáticamente a porcentaje.
- Si falta el CSV opcional de inventario o satisfacción, la aplicación lo indica y omite esa parte del análisis.

## 6. Privacidad y ayuda

La aplicación web lee y analiza los archivos dentro del navegador. No transmite el contenido de los CSV a GitHub ni a un servicio externo. El sitio publicado contiene únicamente el código de la aplicación y los archivos de ejemplo del proyecto.

Si una columna no se reconoce, revisa que tenga un encabezado en la primera fila y consulta el [Manual técnico](MANUAL_TECNICO.md), que explica cómo agregar nuevos alias.
