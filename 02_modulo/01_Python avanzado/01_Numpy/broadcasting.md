📝 Ejemplos de broadcasting con numpy

Ejemplo #1:

Tenemos un conjunto de datos que representa la medición de temperatura de 7 días en 3 ciudades diferentes (array de 3 x 7). Sin embargo las mediciones tienen un margen de error, y se nos da un array unidimensional con los valores de corrección para cada día de la semana (array de 1 x 7). Para acer la corrección en la medición de temperatura, en lugar de duplicar el array de corrección para cada ciudad (fila), aplicamos broadcasting:

```python
import numpy as np

# Temperaturas (3 ciudades, 7 días)
temperaturas = np.array([
    [30, 32, 31, 29, 28, 27, 26],
    [25, 24, 22, 23, 26, 27, 28],
    [20, 21, 19, 18, 17, 16, 15]
])

# Corrección (1 valor por día)
correccion = np.array([1, -1, 0.5, -0.5, 0, 1, -1])

# Aplicar la corrección usando broadcasting
temperaturas_corregidas = temperaturas + correccion

print("Temperaturas originales:\n", temperaturas)
print("\nCorrección aplicada:\n", correccion)
print("\nTemperaturas corregidas:\n", temperaturas_corregidas)
```

Resultado:

```bash
[[30 32 31 29 28 27 26]
 [25 24 22 23 26 27 28]
 [20 21 19 18 17 16 15]]
```

Corrección aplicada:
```bash
 [ 1.  -1.   0.5 -0.5  0.   1.  -1. ]
``` 

Temperaturas corregidas:
```bash
 [[31.  31.  31.5 28.5 28.  28.  25. ]
 [26.  23.  22.5 22.5 26.  28.  27. ]
 [21.  20.  19.5 17.5 17.  17.  14. ]]
```

Internamente numpy expande verticalmente el array de correcciones para que tenga la misma forma (3 x 7) que el array con los datos de las temperaturas por ciudad, visualmente sería algo así:


![ejemplo1](https://res.cloudinary.com/dmwsbri4c/image/upload/v1723849647/Numpy_broadcasting_qi8zzw.jpg)





Ejemplo #2:

Tenemos una matriz 3x3 que representa los valores de ventas de tres productos en tres diferentes tiendas, y un vector 3x1 que contiene un bono de ventas que se aplica por tienda. El broadcasting permite sumar este bono de manera eficiente a cada fila de la matriz.

```python
import numpy as np

# Ventas de productos en diferentes tiendas
ventas = np.array([
  [100, 200, 300],
  [400, 500, 600],
  [700, 800, 900]
])

# Bono de ventas por tienda
bono = np.array([
  [10],
  [20],
  [30]
])

ventas_actualizadas = ventas + bono

print("Ventas actualizadas:\n", ventas_actualizadas)
```


Resultado:

```bash
Ventas actualizadas:
 [[110 210 310]
 [420 520 620]
 [730 830 930]]
```
En este ejemplo, numpy expande el array de forma horizontal (agregando las columnas "faltantes"), visualmente lo que ocurre es lo siguiente:

![ejemplo2](https://res.cloudinary.com/dmwsbri4c/image/upload/v1723849647/Numpy_broadcasting_2_eabw1w.jpg)

