# Proyecto de Ciencia de Datos con Bases de Datos

Este proyecto tiene como objetivo proporcionar un entorno práctico para aprender sobre bases de datos relacionales y su integración con Python para el análisis de datos. A través de este proyecto, se crearán y gestionarán datos de ejemplo que se utilizarán para realizar diversas prácticas de análisis.

## Estructura del Proyecto

```
database-data-science-project
├── data
│   ├── clients.csv               # Datos de clientes en formato CSV
│   ├── products.csv              # Datos de productos en formato CSV
│   ├── sales.csv                 # Datos de ventas en formato CSV
│   ├── ventas_stats.csv          # Resultados del análisis de estadísticas de ventas
│   ├── producto_mas_vendido.csv  # Resultados del análisis del producto más vendido
│   ├── clientes_alto_gasto.csv   # Resultados del análisis de clientes con alto gasto
│   ├── promedio_ventas_por_dia.csv # Resultados del análisis del promedio de ventas por día
├── scripts
│   ├── create_database.py        # Script para crear la base de datos y tablas
│   ├── generate_example_data.py  # Script para generar datos de ejemplo
│   ├── analysis.py               # Script para análisis exploratorio
├── docs
│   ├── guia-sqlite3.md           # Guía de instalación de SQLite3
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Documentación del proyecto
```

## Instrucciones

### Configuración del Entorno

1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Instala las dependencias necesarias ejecutando:
   ```sh
   pip install -r requirements.txt
   ```
4. Instala dependencias faltantes `sqlite3` siguiendo la [Guía de instalación de SQLite3](./docs/guia-sqlite3.md).

### Creación de la Base de Datos

Para crear la base de datos y las tablas necesarias, ejecuta el siguiente script:

```sh
python scripts/create_database.py
```

### Generación de Datos de Ejemplo

Para generar y poblar la base de datos con datos de ejemplo, ejecuta:

```sh
python scripts/generate_example_data.py
```

### Análisis de Datos

Para realizar análisis exploratorios sobre los datos, ejecuta:

```sh
python scripts/analysis.py
```

## Contenido de los Archivos

- **data/clients.csv**: Contiene datos de ejemplo de clientes.
- **data/products.csv**: Contiene datos de ejemplo de productos.
- **data/sales.csv**: Contiene datos de ejemplo de ventas.
- **data/ventas_stats.csv**: Contiene los resultados del análisis de estadísticas de ventas.
- **data/producto_mas_vendido.csv**: Contiene los resultados del análisis del producto más vendido.
- **data/clientes_alto_gasto.csv**: Contiene los resultados del análisis de clientes con alto gasto.
- **data/promedio_ventas_por_dia.csv**: Contiene los resultados del análisis del promedio de ventas por día.
- **scripts/create_database.py**: Script que crea la base de datos SQLite 'tienda.db' y las tablas necesarias.
- **scripts/generate_example_data.py**: Script que genera datos ficticios utilizando la biblioteca Faker.
- **scripts/analysis.py**: Script que realiza análisis exploratorios y visualizaciones de los datos.
- **docs/guia-sqlite3.md**: Guía de instalación de SQLite3 en diferentes sistemas operativos.

## Recursos Adicionales

Consulta la guía práctica para obtener más información sobre el uso de bases de datos y análisis de datos en Python.