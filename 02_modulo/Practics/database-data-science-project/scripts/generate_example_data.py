import sqlite3
from faker import Faker
import random
import pandas as pd
import os

# Inicializar Faker
fake = Faker()

# Conectar a la base de datos
conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

# Crear datos de ejemplo
def generate_example_data(num_clients=100, num_products=50, num_sales=200):
    # Generar datos de clientes
    clients = []
    for _ in range(num_clients):
        clients.append((fake.name(), fake.email()))

    # Insertar datos de clientes
    cursor.executemany('INSERT INTO clientes (nombre, correo) VALUES (?, ?)', clients)

    # Generar datos de productos
    products = []
    for _ in range(num_products):
        products.append((fake.word(), round(random.uniform(10, 100), 2)))

    # Insertar datos de productos
    cursor.executemany('INSERT INTO productos (nombre, precio) VALUES (?, ?)', products)

    # Generar datos de ventas
    sales = []
    for _ in range(num_sales):
        product_id = random.randint(1, num_products)
        client_id = random.randint(1, num_clients)
        quantity = random.randint(1, 5)
        price = round(random.uniform(10, 100), 2)
        date = fake.date_this_decade().isoformat()  # Generar una fecha aleatoria
        sales.append((product_id, client_id, quantity, price, date))

    # Insertar datos de ventas
    cursor.executemany('INSERT INTO ventas (producto_id, cliente_id, cantidad, precio, fecha) VALUES (?, ?, ?, ?, ?)', sales)

    # Crear la carpeta "data/" si no existe
    data_dir = os.path.join(os.path.dirname(__file__), "../data")
    os.makedirs(data_dir, exist_ok=True)

    # Exportar datos a CSV
    clients_df = pd.DataFrame(clients, columns=['nombre', 'correo'])
    clients_df.to_csv(os.path.join(data_dir, "clients.csv"), index=False)

    products_df = pd.DataFrame(products, columns=['nombre', 'precio'])
    products_df.to_csv(os.path.join(data_dir, "products.csv"), index=False)

    sales_df = pd.DataFrame(sales, columns=['producto_id', 'cliente_id', 'cantidad', 'precio', 'fecha'])
    sales_df.to_csv(os.path.join(data_dir, "sales.csv"), index=False)


# Llamar a la función para generar datos
generate_example_data()

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()