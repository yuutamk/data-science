import sqlite3

# Conexión a la base de datos (se creará si no existe)
conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

# Crear tabla de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INTEGER PRIMARY KEY,
    nombre TEXT,
    correo TEXT
);
''')

# Crear tabla de productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    producto_id INTEGER PRIMARY KEY,
    nombre TEXT,
    precio REAL
);
''')

# Crear tabla de ventas
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    venta_id INTEGER PRIMARY KEY,
    producto_id INTEGER,
    cantidad INTEGER,
    precio REAL,
    cliente_id INTEGER,
    fecha TEXT DEFAULT (DATE('now')),  -- Agregamos la columna fecha con un valor por defecto
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

''')

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()