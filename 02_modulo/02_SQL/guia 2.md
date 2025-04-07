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
2. Instala las librerías necesarias:
   ```bash
   pip install pandas sqlalchemy
   ```

