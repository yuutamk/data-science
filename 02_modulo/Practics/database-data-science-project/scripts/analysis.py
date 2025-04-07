import pandas as pd
import seaborn as sns
import sqlite3
import matplotlib.pyplot as plt
import os

# Conexión a la base de datos
conn = sqlite3.connect('tienda.db')

# Análisis exploratorio de datos

# 1. Obtener estadísticas básicas de ventas
ventas_stats = pd.read_sql('SELECT AVG(precio) AS promedio_precio, MAX(precio) AS max_precio, MIN(precio) AS min_precio FROM ventas', conn)
print("Estadísticas de Ventas:")
print(ventas_stats)

# 2. Producto más vendido
producto_mas_vendido = pd.read_sql('SELECT producto_id, SUM(cantidad) AS total_vendido FROM ventas GROUP BY producto_id ORDER BY total_vendido DESC LIMIT 1', conn)
print("\nProducto más vendido:")
print(producto_mas_vendido)

# 3. Clientes que gastaron más de $500
clientes_alto_gasto = pd.read_sql('SELECT cliente_id, SUM(precio * cantidad) AS total_gastado FROM ventas GROUP BY cliente_id HAVING total_gastado > 500', conn)
print("\nClientes que gastaron más de $500:")
print(clientes_alto_gasto)

# 4. Promedio de ventas por día
promedio_ventas_por_dia = pd.read_sql('SELECT DATE(fecha) AS fecha, AVG(precio * cantidad) AS promedio_ventas FROM ventas GROUP BY fecha', conn)
print("\nPromedio de ventas por día:")
print(promedio_ventas_por_dia)


# Crear la carpeta "data/" si no existe
data_dir = os.path.join(os.path.dirname(__file__), "../data")
os.makedirs(data_dir, exist_ok=True)

# Exportar resultados del análisis a CSV
ventas_stats.to_csv(os.path.join(data_dir, "ventas_stats.csv"), index=False)
producto_mas_vendido.to_csv(os.path.join(data_dir, "producto_mas_vendido.csv"), index=False)
clientes_alto_gasto.to_csv(os.path.join(data_dir, "clientes_alto_gasto.csv"), index=False)
promedio_ventas_por_dia.to_csv(os.path.join(data_dir, "promedio_ventas_por_dia.csv"), index=False)

# Visualización de datos
# Gráfico de ventas por producto
sns.barplot(data=promedio_ventas_por_dia, x='fecha', y='promedio_ventas')
plt.title('Promedio de Ventas por Día')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Cerrar la conexión
conn.close()