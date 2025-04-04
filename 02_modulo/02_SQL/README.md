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

### ¿Qué es una Base de Datos Relacional?
Una base de datos relacional es una colección de datos organizados en **tablas**, que permiten almacenar, acceder y gestionar información de manera estructurada. Las tablas son como hojas de cálculo donde cada fila representa un **registro** y cada columna representa un **atributo**.

**Conceptos básicos:**
- **Tabla:** Una estructura que organiza los datos en filas y columnas.
- **Fila (Registro):** Cada fila es una entrada única que contiene información completa sobre un elemento.
- **Columna:** Define un atributo o propiedad de los datos.

Por ejemplo, una tabla de clientes podría verse así:
| cliente_id | nombre      | correo            |
|------------|-------------|-------------------|
| 1          | Juan Pérez | juan@gmail.com    |
| 2          | Ana López  | ana@gmail.com     |

### Claves Primarias y Foráneas
- **Clave primaria:** Un identificador único para cada registro de una tabla. Es como el número de identificación de una persona.
- **Clave foránea:** Una columna que conecta una tabla con otra mediante la clave primaria.

Ejemplo práctico:
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
En este caso, `cliente_id` es una clave primaria en la tabla `clientes` y una clave foránea en la tabla `pedidos`.

estos son algunos datos de ejemplo para estas tablas:

```sql
INSERT INTO clientes (cliente_id, nombre, correo) VALUES
(4, "Callie Morris", "ut.pharetra.sed@outlook.net"),
(7, "Kevyn Nguyen", "vehicula.et.rutrum@protonmail.edu"),
(3, "Daquan Savage", "molestie.in.tempus@outlook.net"),
(1, "Victor Mcneil", "vitae.aliquam@protonmail.edu"),
(9, "Tamekah Gilbert", "eu@yahoo.org");



INSERT INTO pedidos (pedido_id, cliente_id, monto) VALUES
(1, 4, 150.75),
(2, 7, 200.50),
(3, 3, 300.00),
(4, 1, 450.25),
(5, 9, 120.00),
(6, 7, 95.80),
(7, 3, 180.60),
(8, 4, 220.15),
(9, 1, 310.00),
(10, 9, 75.40);

```

### Ventajas de las Bases de Datos Relacionales
- **Organización clara:** Los datos están organizados en estructuras lógicas.
- **Consistencia:** Las claves primarias y foráneas aseguran la integridad de los datos.
- **Flexibilidad:** Fácil de modificar y actualizar según sea necesario.

---

## 2. Introducción al Lenguaje SQL

SQL (Structured Query Language) es el lenguaje estándar para interactuar con bases de datos relacionales. Permite realizar tareas como:
- **Consultar datos:** Buscar información específica en una tabla.
- **Modificar datos:** Agregar, actualizar o eliminar registros.
- **Administrar estructuras:** Crear y modificar tablas y bases de datos.

### Sintaxis Básica de SQL
La estructura de una consulta básica es:
```sql
SELECT columnas
FROM tabla
WHERE condiciones;
```

Ejemplo:
```sql
SELECT nombre, correo FROM clientes;
```
Esto muestra los nombres y correos de todos los clientes.

### Uso de Filtros
Los filtros permiten seleccionar registros específicos:
- **WHERE:** Filtra filas según condiciones.
- **Operadores:** `=`, `>`, `<`, `!=`, `IN`, `BETWEEN`.

Ejemplo:
```sql
SELECT * FROM pedidos WHERE monto > 100;
```
Esto selecciona todos los pedidos con un monto mayor a 100.

### Funciones Agregadas
Las funciones agregadas calculan valores sobre varias filas:
- `COUNT`: Cuenta filas.
- `SUM`: Suma valores.
- `AVG`: Calcula el promedio.
- `MIN` y `MAX`: Encuentran el mínimo y máximo.

Ejemplo:
```sql
SELECT cliente_id, SUM(monto) AS total_gastado 
FROM pedidos
GROUP BY cliente_id
ORDER BY total_gastado DESC;
```
Esto muestra cuánto gastó cada cliente, ordenado de mayor a menor.

---

## 3. Relaciones y Joins

Cuando los datos están distribuidos en varias tablas, los **joins** permiten combinarlos.

### Tipos de Joins
- **INNER JOIN:** Combina filas que tienen coincidencias en ambas tablas.
- **LEFT JOIN:** Muestra todas las filas de la tabla izquierda, aunque no haya coincidencias en la derecha.
- **RIGHT JOIN:** Similar al LEFT JOIN pero con las filas de la tabla derecha.
- **FULL JOIN:** Combina todas las filas de ambas tablas.

Ejemplo de INNER JOIN:
```sql
SELECT clientes.nombre, pedidos.monto
FROM clientes
INNER JOIN pedidos ON clientes.cliente_id = pedidos.cliente_id;
```
Esto muestra los nombres de los clientes y los montos de sus pedidos.

---

## 4. Creación y Gestión de Tablas

### Creación de Tablas
Las tablas se crean usando `CREATE TABLE`. Debes especificar el nombre y las columnas:
```sql
CREATE TABLE productos (
    producto_id INTEGER PRIMARY KEY,
    nombre TEXT,
    precio REAL
);
```

### Modificación de Tablas
Usa `ALTER TABLE` para agregar columnas:
```sql
ALTER TABLE productos ADD COLUMN stock INTEGER;
```

---

## 5. Integración de SQL con Python

Python permite automatizar tareas y analizar datos de bases de datos. Usaremos librerías como:
- `sqlite3`: Para trabajar con bases de datos SQLite.
- `pandas`: Para análisis de datos.
- `SQLAlchemy`: Para una integración más avanzada.

### Configuración del Entorno
1. Descarga e instala Python desde [python.org](https://www.python.org/).

**Nota:** no olvides crear tu entorno virtual para evitar choque de dependencias   
```bash

```
2. Instala las librerías necesarias:
   ```bash
   pip install pandas sqlalchemy
   ```

### Uso de `sqlite3`
`sqlite3` es una librería estándar en Python para trabajar con bases de datos SQLite. Es ideal para aprender porque no requiere instalación adicional.

Ejemplo básico:
```python
import sqlite3

# Crear o conectar a una base de datos
conexion = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INTEGER PRIMARY KEY,
    nombre TEXT,
    correo TEXT
)
''')

# Insertar datos
cursor.execute("INSERT INTO clientes (nombre, correo) VALUES (?, ?)", ("Juan Pérez", "juan@gmail.com"))

# Guardar cambios y cerrar la conexión
conexion.commit()
conexion.close()
```

### Uso de `pandas` para Análisis de Datos
`pandas` permite cargar datos desde bases de datos directamente en un DataFrame para análisis.

Ejemplo:
```python
import pandas as pd
import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('mi_base_de_datos.db')

# Leer datos en un DataFrame
df = pd.read_sql_query("SELECT * FROM clientes", conexion)

print(df)
```

### Uso de `SQLAlchemy` para Gestión Avanzada
`SQLAlchemy` simplifica la interacción con bases de datos y permite trabajar con varios motores (SQLite, MySQL, PostgreSQL).

Ejemplo:
```python
from sqlalchemy import create_engine
import pandas as pd

# Crear motor de base de datos
engine = create_engine('sqlite:///mi_base_de_datos.db')

# Leer datos usando pandas
df = pd.read_sql("SELECT * FROM clientes", engine)
print(df)
```
---



## 6. Aplicaciones Prácticas en Ciencia de Datos

### Importación y Exportación de Datos
En el contexto de la ciencia de datos, la importación y exportación de datos son operaciones fundamentales para mover información entre diferentes sistemas o herramientas. Por ejemplo:

- **Importación:** Los datos suelen estar almacenados en formatos como CSV, Excel, JSON o en bases de datos. SQL permite importar esta información directamente a tablas para su posterior análisis.
  ```sql
  -- Importar datos desde un archivo CSV usando SQLite
  .mode csv
  .import ruta_del_archivo.csv nombre_tabla
  ```

- **Exportación:** Una vez que se ha procesado y analizado la información, los resultados se pueden exportar para ser utilizados en otras aplicaciones.
  ```sql
  -- Exportar resultados a un archivo CSV
  .mode csv
  .output resultados.csv
  SELECT * FROM tabla;
  .output stdout
  ```

### Análisis Exploratorio Inicial con SQL
El análisis exploratorio es el primer paso para comprender los datos. SQL facilita tareas como:
- **Resumir datos:**
  ```sql
  SELECT AVG(edad) AS promedio_edad, MAX(salario) AS salario_maximo
  FROM empleados;
  ```
- **Detectar valores faltantes:**
  ```sql
  SELECT * FROM clientes WHERE correo IS NULL;
  ```
- **Obtener distribuciones:**
  ```sql
  SELECT departamento, COUNT(*) AS empleados_por_departamento
  FROM empleados
  GROUP BY departamento;
  ```

### Combinación de SQL y Python para Visualización y Análisis Avanzado
SQL es potente para la consulta de datos, pero Python complementa con librerías como Matplotlib, Seaborn o Plotly para visualización.

Ejemplo de análisis avanzado:
```python
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos
conexion = sqlite3.connect('ventas.db')

# Consulta SQL
query = """
SELECT categoria, SUM(ventas) AS total_ventas
FROM productos
GROUP BY categoria
ORDER BY total_ventas DESC;
"""

data = pd.read_sql_query(query, conexion)

# Crear un gráfico de barras
plt.bar(data['categoria'], data['total_ventas'])
plt.xlabel('Categorías')
plt.ylabel('Total Ventas')
plt.title('Ventas por Categoría')
plt.show()
```
Esta combinación permite realizar visualizaciones y modelado avanzado.

---

## 7. Ejercicios Prácticos y Ejemplos

### Análisis de Datos de Ventas
#### Ejercicio 1: Identificar los productos más vendidos
Escribe una consulta para encontrar los 5 productos con mayor volumen de ventas:
```sql
SELECT producto_id, nombre, SUM(cantidad_vendida) AS total_vendido
FROM ventas
GROUP BY producto_id, nombre
ORDER BY total_vendido DESC
LIMIT 5;
```

#### Ejercicio 2: Evaluar el rendimiento de las tiendas
Calcula el total de ingresos por tienda:
```sql
SELECT tienda_id, SUM(total_ventas) AS ingresos_totales
FROM ventas
GROUP BY tienda_id
ORDER BY ingresos_totales DESC;
```

### Segmentación de Clientes
#### Ejercicio 3: Identificar clientes frecuentes
Crea una consulta para encontrar clientes con más de 10 compras:
```sql
SELECT cliente_id, COUNT(*) AS total_compras
FROM ventas
GROUP BY cliente_id
HAVING total_compras > 10;
```

#### Ejercicio 4: Clasificar clientes según su gasto total
Agrupa clientes en niveles de gasto:
```sql
SELECT cliente_id,
       SUM(monto) AS gasto_total,
       CASE
           WHEN SUM(monto) < 500 THEN 'Bajo'
           WHEN SUM(monto) BETWEEN 500 AND 2000 THEN 'Medio'
           ELSE 'Alto'
       END AS nivel_gasto
FROM ventas
GROUP BY cliente_id;
```

### Evaluación de Patrones de Transacciones
#### Ejercicio 5: Analizar compras por fecha
Encuentra el día con mayor cantidad de ventas:
```sql
SELECT fecha, COUNT(*) AS transacciones
FROM ventas
GROUP BY fecha
ORDER BY transacciones DESC
LIMIT 1;
```

#### Ejercicio 6: Evaluar recurrencia de compras
Determina cuánto tiempo promedio transcurre entre compras:
```sql
SELECT cliente_id, AVG(julianday(fecha_actual) - julianday(fecha_anterior)) AS intervalo_promedio
FROM (
    SELECT cliente_id,
           fecha AS fecha_actual,
           LAG(fecha) OVER (PARTITION BY cliente_id ORDER BY fecha) AS fecha_anterior
    FROM ventas
) subquery
WHERE fecha_anterior IS NOT NULL
GROUP BY cliente_id;
```

---

## 8. Recursos Adicionales

### Documentación Oficial de SQLite y SQLAlchemy
- **SQLite:** [https://sqlite.org/docs.html](https://sqlite.org/docs.html)
- **SQLAlchemy:** [https://docs.sqlalchemy.org/](https://docs.sqlalchemy.org/)

Estas documentaciones ofrecen guías completas y ejemplos prácticos para trabajar con bases de datos.

### Libros Recomendados
1. **"SQL in 10 Minutes, Sams Teach Yourself"** de Ben Forta
   - Ideal para principiantes que buscan aprender rápidamente.
2. **"Learning SQL"** de Alan Beaulieu
   - Un recurso más profundo para consolidar conocimientos.
3. **"Python for Data Analysis"** de Wes McKinney
   - Recomendado para aprender cómo combinar Python con SQL para ciencia de datos.

### Cursos en Línea
- **"The Complete SQL Bootcamp"** (Udemy): Un curso completo con proyectos prácticos.
- **"Data Science with Python and SQL"** (Coursera): Enseña cómo combinar SQL con Python.
- **"Advanced SQL for Data Scientists"** (DataCamp): Focado en temas avanzados como optimización de consultas.

Estos recursos son ideales para profundizar en los temas tratados y ampliar tus habilidades en SQL y ciencia de datos.



