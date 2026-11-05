from pathlib import Path
import numpy as np
import pandas as pd

# Cambia la semilla si quieres generar otra simulación reproducible.
SEMILLA = 42


def cargar_csv(nombre: str) -> pd.DataFrame:
    """Carga un CSV desde la carpeta del proyecto."""
    rutas = [Path("/workspace") / nombre, Path(__file__).resolve().parent / nombre]
    for ruta in rutas:
        if ruta.exists():
            return pd.read_csv(ruta).dropna().copy()
    raise FileNotFoundError(f"No se encontró {nombre} en /workspace ni junto a main.py.")


def main() -> None:
    np.random.seed(SEMILLA)
    ventas = cargar_csv("sales.csv")
    inventarios = cargar_csv("inventories.csv")
    satisfaccion = cargar_csv("satisfaction.csv")

    # Normalizar las columnas numéricas y retirar registros que no se puedan analizar.
    for df, columnas in [
        (ventas, ["ID_Tienda", "Cantidad_Vendida", "Precio_Unitario"]),
        (inventarios, ["ID_Tienda", "Stock_Disponible"]),
        (satisfaccion, ["ID_Tienda", "Satisfacción_Promedio"]),
    ]:
        for columna in columnas:
            df[columna] = pd.to_numeric(df[columna], errors="coerce")
    ventas = ventas.dropna(subset=["ID_Tienda", "Cantidad_Vendida", "Precio_Unitario"])
    inventarios = inventarios.dropna(subset=["ID_Tienda", "Stock_Disponible"])
    satisfaccion = satisfaccion.dropna(subset=["ID_Tienda", "Satisfacción_Promedio"])

    ventas["Total_Ventas"] = ventas["Cantidad_Vendida"] * ventas["Precio_Unitario"]
    por_tienda = ventas.groupby("ID_Tienda", as_index=False).agg(
        Unidades_Vendidas=("Cantidad_Vendida", "sum"),
        Total_Ventas=("Total_Ventas", "sum"),
    )
    por_producto = ventas.groupby("Producto", as_index=False).agg(
        Unidades_Vendidas=("Cantidad_Vendida", "sum"),
        Ingresos=("Total_Ventas", "sum"),
    )

    ventas_producto = ventas.groupby(["ID_Tienda", "Producto"], as_index=False).agg(
        Unidades_Vendidas=("Cantidad_Vendida", "sum")
    )
    detalle_inventario = inventarios.merge(ventas_producto, on=["ID_Tienda", "Producto"], how="left")
    detalle_inventario["Unidades_Vendidas"] = detalle_inventario["Unidades_Vendidas"].fillna(0)
    detalle_inventario["Rotacion_Inventario"] = (
        detalle_inventario["Unidades_Vendidas"] /
        detalle_inventario["Stock_Disponible"].replace(0, np.nan)
    )
    detalle_inventario["Porcentaje_Vendido"] = 100 * detalle_inventario["Rotacion_Inventario"]
    critico = detalle_inventario[detalle_inventario["Porcentaje_Vendido"] < 10]

    rendimiento = por_tienda.merge(
        satisfaccion[["ID_Tienda", "Satisfacción_Promedio"]], on="ID_Tienda", how="left"
    )
    baja_satisfaccion = rendimiento[rendimiento["Satisfacción_Promedio"] < 60]

    total_array = por_tienda["Total_Ventas"].to_numpy(dtype=float)
    print("\n=== Ventas por tienda ===")
    print(por_tienda.to_string(index=False))
    print("\n=== Ventas por producto ===")
    print(por_producto.to_string(index=False))
    print("\n=== Estadísticas de ventas ===")
    print(ventas[["Cantidad_Vendida", "Total_Ventas"]].describe())
    print(f"\nMediana de ingresos por tienda: {np.median(total_array):.2f}")
    print(f"Desviación estándar poblacional: {np.std(total_array, ddof=0):.2f}")
    print("\n=== Productos con inventario crítico (<10% vendido) ===")
    print(critico.to_string(index=False) if not critico.empty else "No se encontraron casos.")
    print("\n=== Tiendas con satisfacción <60% ===")
    print(baja_satisfaccion.to_string(index=False) if not baja_satisfaccion.empty else "No se encontraron casos.")

    # Proyección ilustrativa de 1,000 escenarios por tienda, con variación del 10%.
    rng = np.random.default_rng(SEMILLA)
    base = por_tienda["Total_Ventas"].to_numpy(dtype=float)
    simulacion = np.maximum(
        rng.normal(loc=base[:, None], scale=np.maximum(base[:, None] * 0.10, 1), size=(len(base), 1000)),
        0,
    )
    proyecciones = pd.DataFrame({
        "ID_Tienda": por_tienda["ID_Tienda"].to_numpy(),
        "Proyeccion_Media": simulacion.mean(axis=1),
        "P10": np.percentile(simulacion, 10, axis=1),
        "P90": np.percentile(simulacion, 90, axis=1),
    })
    print("\n=== Proyección simulada por tienda ===")
    print(proyecciones.to_string(index=False))
    print(f"\nMedia global simulada: {simulacion.mean():.2f}")
    print(f"Desviación estándar simulada: {simulacion.std():.2f}")

    if not baja_satisfaccion.empty:
        print("\nRecomendación: revisar comentarios de clientes, reforzar la atención y comprobar disponibilidad y reposición; luego medir de nuevo satisfacción y ventas.")


if __name__ == "__main__":
    main()
