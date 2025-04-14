1. UNIQUE

Descripción: La función np.unique en Numpy se utiliza para encontrar elementos únicos en un arreglo. También puede devolver el conteo de ocurrencias de cada elemento único si se especifica el parámetro return_counts=True. Esto es útil para análisis de datos, como contar frecuencias de elementos.

Ejemplos:

Código: 

survey_responses = np.array(["bueno", "excelente", "malo",

                              "bueno", "malo", "excelente",

                              "bueno", "bueno", "malo",

                              "excelente", "excelente", "excelente"])

print(np.unique(survey_responses))

 Resultado: ['bueno' 'excelente' 'malo'] Explicación: La función np.unique extrae las respuestas distintas en el arreglo survey_responses.
Código: unique_elements, counts = np.unique(survey_responses, return_counts=True)

print(unique_elements)

print(counts)

 Resultado: unique_elements: ['bueno' 'excelente' 'malo']

counts: [4 5 3]

 Explicación: Además de los elementos únicos, se devuelven los conteos de cada valor único. Por ejemplo, "bueno" aparece 4 veces, "excelente" aparece 5 veces y "malo" aparece 3 veces.
2. COPIAS / VISTAS
Descripción: Los arreglos en Numpy pueden crear copias o vistas:

Vistas: Son subconjuntos de los datos originales. Cualquier cambio en una vista afecta el arreglo original.
Copias: Son duplicados independientes de los datos. Modificar una copia no afecta el arreglo original.
Ejemplos:

**EJEMPLO DE VISTA:**array_x = np.arange(10)

view_y = array_x[1:3]

print(array_x)

print(view_y)

array_x[1:3] = [10, 11]

print(array_x)

print(view_y)

 **Resultado:**array_x: [0 1 2 3 4 5 6 7 8 9]

view_y: [1 2]

array_x (después de modificación): [ 0 10 11  3  4  5  6  7  8  9]

view_y (después de modificación): [10 11]

 Explicación: view_y es una vista de array_x. Cuando los elementos en el segmento [1:3] se modifican en array_x, los cambios se reflejan en view_y.
EJEMPLO DE COPIA: array_x = np.arange(10)

copy_x = array_x[[1, 2]]

print(array_x)

print(copy_x)

array_x[1:3] = [10, 11]

print(array_x)

print(copy_x)

 Resultado: array_x: [0 1 2 3 4 5 6 7 8 9]

copy_x: [1 2]

array_x (después de modificación): [ 0 10 11  3  4  5  6  7  8  9]

copy_x (sin cambios): [1 2]

 Explicación: copy_x es una copia de array_x. Los cambios en el segmento [1:3] en array_x no afectan a copy_x, ya que opera de manera independiente.