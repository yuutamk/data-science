Ejercicio: Análisis de Ventas Mensuales con NumPy
El objetivo de este ejercicio es trabajar con arrays de NumPy para analizar y manipular datos de ventas de tres productos a lo largo de un año. A través de diversas operaciones, explorarás cómo usar NumPy para obtener estadísticas, realizar manipulaciones avanzadas y aplicar técnicas de indexación para extraer información clave.

Instrucciones:

Paso 1: Crear Arrays con Datos de Ventas

Usa la librería numpy para crear los siguientes arrays:
meses: un array con los nombres de los meses del año.
ventas_A, ventas_B, ventas_C: arrays que representan las ventas mensuales de tres productos diferentes.
Paso 2: Estadísticas Básicas

Calcula la media y la suma de ventas para los productos A, B y C usando las funciones de NumPy.
Imprime estos valores en el formato siguiente:
Media de ventas Producto A: <valor>
Suma de ventas Producto A: <valor>
Repite para los productos B y C.
Paso 3: Manipulación y Análisis de Datos

Total de ventas por mes: Suma las ventas de los tres productos para cada mes.
Promedio de ventas por producto: Calcula el promedio de ventas por producto.
Mes con mayor y menor ventas: Identifica qué mes tuvo el total de ventas más alto y cuál el más bajo usando las funciones np.argmax y np.argmin.
Paso 4: Operaciones Avanzadas con NumPy

Reshape y Transposición:

Crea una matriz 2D con las ventas de los tres productos y transforma su forma (reshape) a un array tridimensional con dimensiones (3, 4, 3).
Transpone la matriz de ventas para que las filas se conviertan en columnas.
Invertir arrays: Invierte las ventas de cada producto en orden de meses.
Aplanar la matriz: Convierte la matriz de ventas a un array unidimensional.
Paso 5: Análisis de Elementos Únicos

Utiliza np.unique para encontrar los elementos únicos en los datos de ventas y cuenta cuántas veces aparece cada uno.
Paso 6: Indexación y Slicing

Ventas del primer trimestre: Extrae las ventas de los tres primeros meses del año.
Indexación booleana: Selecciona los meses donde el total de ventas de los tres productos supere los 800.
Selección avanzada: Usa una lista de índices para seleccionar las ventas de los meses pares (o selecciona los meses a tu elección) y muestra esas ventas en una nueva matriz.