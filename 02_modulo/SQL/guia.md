# Guía Práctica para Introducción a Bases de Datos (SQL) enfocada en Ciencia de Datos

## Índice

1. **Introducción a las Bases de Datos Relacionales**
   - Conceptos clave: tablas, registros, claves primarias y foráneas.
   - Ventajas de las bases de datos relacionales en Ciencia de Datos.

2. **Introducción al Lenguaje SQL**
   - Sintaxis básica de SQL.
   - Consultas SELECT.
   - Operadores y filtros: WHERE, AND, OR, IN, BETWEEN.
   - Funciones agregadas: COUNT, SUM, AVG, MIN, MAX.
   - Agrupación y orden: GROUP BY y ORDER BY.

3. **Relaciones y Joins**
   - Tipos de JOINS: INNER, LEFT, RIGHT, FULL.
   - Subconsultas y expresiones comunes (CTEs).

4. **Creación y Gestión de Tablas**
   - Creación de tablas (CREATE TABLE).
   - Modificación de tablas (ALTER TABLE).
   - Claves primarias y foráneas.

5. **Integración de SQL con Python**
   - Configuración del entorno: instalación de Python y librerías necesarias.
   - Uso de `sqlite3` para interactuar con bases de datos SQLite.
   - Introducción a `pandas` y `SQLAlchemy` para análisis de datos.

6. **Aplicaciones Prácticas en Ciencia de Datos**
   - Importación y exportación de datos.
   - Análisis exploratorio inicial con SQL.
   - Combinación de SQL y Python para visualización y análisis avanzado.

7. **Ejercicios Prácticos y Ejemplos**
   - Análisis de datos de ventas.
   - Segmentación de clientes.
   - Evaluación de patrones de transacciones.

8. **Recursos Adicionales**
   - Documentación oficial de SQLite y SQLAlchemy.
   - Libros recomendados.
   - Cursos en línea.

---

## 1. Introducción a las Bases de Datos Relacionales

Las bases de datos relacionales organizan los datos en **tablas** que están compuestas por:
- **Filas (registros):** representan una instancia específica de los datos.
- **Columnas:** atributos o propiedades de los datos.

### Claves Principales y Foráneas
- **Clave primaria:** identifica únicamente cada registro en una tabla.
- **Clave foránea:** establece relaciones entre tablas vinculando claves primarias de otras tablas.

Ejemplo:
```sql
CREATE TABLE clientes (
    cliente_id INTEGER PRIMARY KEY,
    nombre TEXT,
    correo TEXT
);

CREATE TABLE pedidos (
    pedido_id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    monto REAL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);
```

---

## 2. Introducción al Lenguaje SQL

### Consultas Básicas
Ejemplo de consulta SELECT:
```sql
SELECT nombre, correo FROM clientes;
```

### Uso de Filtros
```sql
SELECT * FROM pedidos WHERE monto > 100;
```

### Funciones Agregadas y Agrupación
```sql
SELECT cliente_id, SUM(monto) AS total_gastado
FROM pedidos
GROUP BY cliente_id
ORDER BY total_gastado DESC;
```

---

## 3. Relaciones y Joins

### Tipos de Joins
Ejemplo de INNER JOIN:
```sql
SELECT clientes.nombre, pedidos.monto
FROM clientes
INNER JOIN pedidos ON clientes.cliente_id = pedidos.cliente_id;
```

---

## 4. Creación y Gestión de Tablas

### Creación de Tablas
```sql
CREATE TABLE productos (
    producto_id INTEGER PRIMARY KEY,
    nombre TEXT,
    precio REAL
);
```

### Modificación de Tablas
```sql
ALTER TABLE productos ADD COLUMN stock INTEGER;
```

---

## 5. Integración de SQL con Python

### Configuración del Entorno
1. Instalar Python desde [python.org](https://www.python.org/).
2. Instalar las librerías necesarias:
   ```bash
   pip install pandas sqlalchemy seaborn Faker
   ```

### Uso de `sqlite3` con Python
Ejemplo básico:
```python
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    venta_id INTEGER PRIMARY KEY,
    producto_id INTEGER,
    cantidad INTEGER,
    precio REAL,
    cliente_id INTEGER,
    fecha TEXT DEFAULT (DATE('now')),
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);
''')

# Insertar datos
cursor.execute('''
INSERT INTO ventas (producto_id, cantidad, precio, cliente_id)
VALUES (1, 1, 800.0, 1);
''')

conn.commit()
conn.close()
```

### Uso de `pandas` y `SQLAlchemy`
```python
import pandas as pd
from sqlalchemy import create_engine

# Crear motor de base de datos
engine = create_engine('sqlite:///tienda.db')

# Leer datos desde SQL
df = pd.read_sql('SELECT * FROM ventas', engine)
print(df)
```

---

## 6. Aplicaciones Prácticas en Ciencia de Datos

### Importación de Datos
```python
df.to_sql('ventas', engine, if_exists='replace', index=False)
```

### Análisis Exploratorio
Usar SQL para calcular estadísticas iniciales:
```sql
SELECT AVG(precio), MAX(precio), MIN(precio) FROM ventas;
```

### Combinación con Python
Visualizar datos usando `matplotlib` o `seaborn`:
```python
import seaborn as sns
sns.barplot(data=df, x='producto_id', y='precio')
```

---

## 7. Ejercicios Prácticos y Ejemplos

1. **Consulta de Ventas:**
   - Obtener el producto más vendido y su total de ingresos.

2. **Análisis de Clientes:**
   - Encontrar los clientes que gastaron más de $500.

3. **Patrones de Transacciones:**
   - Calcular el promedio de ventas por día.

---

## 8. Recursos Adicionales

- **Documentación:**
  - [SQLite](https://www.sqlite.org/docs.html)
  - [SQLAlchemy](https://docs.sqlalchemy.org/)

- **Libros:**
  - [*SQL in 10 Minutes, Sams Teach Yourself* de Ben Forta](https://dokumen.pub/sql-in-10-minutes-a-day-sams-teach-yourself-5thnbsped-0135182794-9780135182796-o-2809157.html).

- **Cursos en Línea:**
  - [Real python: Introduction to python-sqlite-sqlalchemy](https://realpython.com/python-sqlite-sqlalchemy/).
  - [Tutorials: sqlite python](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

---

