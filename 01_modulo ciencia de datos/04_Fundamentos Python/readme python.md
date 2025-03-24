# El Zen de Python: Una Guía Filosófica para Iniciarte en la Ciencia de Datos

Bienvenido a este espacio donde la filosofía se fusiona con el análisis de datos. Si estás dando tus primeros pasos en Python y te interesa la ciencia de datos, esta guía es para ti. Aquí descubrirás cómo los principios del **Zen de Python** pueden inspirarte a escribir código claro, sencillo y poderoso, permitiéndote enfrentar problemas complejos de manera ordenada y eficaz.

---

## ¿Qué es el Zen de Python?

El Zen de Python es un poema escrito por Tim Peters, un desarrollador de Python, que encapsula los valores fundamentales del lenguaje. Cada línea contiene sabiduría práctica para escribir programas que sean no solo funcionales, sino también elegantes y comprensibles. Para acceder a él, simplemente abre tu terminal o consola de Python y escribe:


<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
import this
```

</div>
<br>

Al ejecutarlo, verás algo similar a lo siguiente:

> The Zen of Python, by Tim Peters
  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts.
  Special cases aren't special enough to break the rules.
  Although practicality beats purity.
  Errors should never pass silently.
  Unless explicitly silenced.
  In the face of ambiguity, refuse the temptation to guess.
  There should be one-- and preferably only one --obvious way to do it.
  Although that way may not be obvious at first unless you're Dutch.
  Now is better than never.
  Although never is often better than *right* now.
  If the implementation is hard to explain, it's a bad idea.
  If the implementation is easy to explain, it may be a good idea.
  Namespaces are one honking great idea -- let's do more of those!


A primera vista, estos aforismos pueden parecer abstractos, pero cada uno ofrece una valiosa lección sobre cómo abordar la programación y, en particular, la ciencia de datos.  

---

## ¿Por Qué es Importante el Zen de Python en la Ciencia de Datos?

La ciencia de datos se basa en transformar grandes volúmenes de información en conocimiento práctico. En este proceso, un código limpio y bien estructurado es esencial. A continuación, se explican algunos aspectos clave que destacan la relevancia del Zen de Python:

- **Claridad y Sencillez:**  
  En lugar de complicar las soluciones, siempre es recomendable buscar la opción más directa y comprensible. Esto facilita la detección de errores y permite realizar mejoras futuras sin dificultad.

- **Legibilidad:**  
  Un código fácil de leer es fundamental cuando se trabaja en equipo. Utilizar nombres descriptivos para variables y funciones asegura que tanto tú como tus compañeros comprendan el proceso de análisis sin confusiones.

- **Mantenimiento:**  
  Al estructurar el código en pequeñas partes bien definidas, será posible actualizar o modificar proyectos de forma rápida y segura. Esta modularidad es clave en proyectos de ciencia de datos que evolucionan constantemente.

- **Colaboración:**  
  Seguir prácticas reconocidas (como el uso de bibliotecas estándar tipo Pandas, NumPy y Scikit-learn) permite que otros entiendan y colaboren en los proyectos, potenciando la creatividad y la eficiencia.

---

## Aplicación Práctica de los Principios del Zen de Python

Cuando comienzas a trabajar con Python, es natural enfocarse en conceptos simples que ayuden a construir una base sólida. Aquí hay algunos principios clave del Zen de Python que pueden guiarte en tus primeros pasos:

1. **"Lo bello es mejor que lo feo":**  
   Un código organizado y armonioso facilita la comprensión y el mantenimiento, permitiendo que el flujo de ideas sea claro.

2. **"Lo simple es mejor que lo complejo":**  
   Comienza con soluciones sencillas. A medida que vayas entendiendo tus datos y el problema a resolver, podrás introducir mejoras graduales sin abrumarte con técnicas demasiado avanzadas.

3. **"La legibilidad cuenta":**  
   Utiliza nombres descriptivos y estructura tu proyecto en pequeñas funciones o módulos. Esto hará que tu código sea fácil de seguir, tanto para ti como para quienes te acompañen en tu aprendizaje.

4. **"Los errores nunca deben pasar desapercibidos":**  
   Presta atención a cada detalle y no ignores los pequeños fallos. Detectar y solucionar problemas desde el inicio te ayudará a obtener resultados más confiables en tus análisis.

5. **"Debería haber una —y preferiblemente solo una— manera obvia de hacerlo":**  
   Sigue las convenciones y utiliza herramientas y librerías de confianza. Esto te permite enfocarte en el análisis de datos en lugar de reinventar soluciones ya existentes.

---


El Zen de Python es más que un conjunto de reglas: es una filosofía que te invita a buscar la claridad, la simplicidad y la elegancia en cada línea de código. Al adoptar estos principios desde el inicio de tu aventura en Python, no solo mejorarás la calidad de tu programación, sino que también te equiparás para enfrentar desafíos complejos en la ciencia de datos de manera organizada y efectiva.

Recuerda: cada línea de código es una oportunidad para aprender y crecer. ¡Que el Zen de Python ilumine tu camino en este emocionante viaje hacia el análisis de datos!


¿Listo para comenzar? Deja que la sencillez y la belleza guíen cada uno de tus proyectos. ¡Bienvenido al fascinante mundo de Python y la ciencia de datos!

---

# Conjuntos en Python

La teoría de conjuntos es una rama de las matemáticas y de la lógica que estudia objetos llamados *conjuntos*, formados por elementos que, al agruparse, adquieren propiedades propias. Su finalidad es analizar las características de estos conjuntos y las operaciones que se pueden realizar entre ellos.

## ¿Qué es un Conjunto?

Un conjunto es una colección de elementos considerada en sí misma como un objeto. Por ejemplo:

- **Conjunto de las vocales:**  
  V = {a, e, i, o, u}
- **Conjunto de los días de la semana:**  
  D = {domingo, lunes, martes, miércoles, jueves, viernes, sábado}

## Operaciones con Conjuntos

La teoría de conjuntos nos permite llevar a cabo diversas operaciones que nos ayudan a comparar y combinar colecciones de elementos. A continuación, se presentan algunas de las operaciones más importantes:

### Unión de Conjuntos

La unión de conjuntos consiste en identificar todos los elementos que pertenecen a uno o a varios conjuntos. Se define como:

  A ∪ B = {x | x ∈ A ∨ x ∈ B}

![union de conjuntos](https://static.platzi.com/media/articlases/Images/Uni%C3%B3n%20de%20conjuntos.png)

Es decir, reúne todos los elementos de A y B, sin repetir aquellos que se encuentren en ambos.

### Intersección de Conjuntos

La intersección es la operación que obtiene un conjunto formado únicamente por los elementos comunes a ambos conjuntos. Se expresa como:

  A ∩ B = {x | x ∈ A ∧ x ∈ B}

![intersección de conjuntos](https://static.platzi.com/media/articlases/Images/Intersecci%C3%B3n%20de%20conjuntos.png)

### Diferencia de Conjuntos

La diferencia entre dos conjuntos genera un nuevo conjunto con los elementos del primero que no se encuentran en el segundo:

  A - B = {x | x ∈ A ∧ x ∉ B}

![Diferencia de conjuntos](https://static.platzi.com/media/articlases/Images/image%28237%29.png)

Es importante destacar que A - B no es lo mismo que B - A.

### Diferencia Simétrica

La diferencia simétrica se compone de los elementos que están en A pero no en B, junto con aquellos que están en B pero no en A. Se define de la siguiente manera:



$A \triangle B = {x | x \in A-B \lor x \in B-A} = (A-B) \cup (B-A)$


![Diferencia simétrica de conjuntos](https://static.platzi.com/media/articlases/Images/Diferencia%20sim%C3%A9trica%20de%20conjuntos.png)

Por ejemplo, si tenemos:

  P = {a, e, i, o, u}  
  Q = {a, b, c, d, e}

Entonces,  
  P Δ Q = {i, o, u, b, c, d}

### Complemento de Conjuntos

El complemento de un conjunto A se refiere a los elementos que pertenecen al conjunto universal U, pero no a A:

  Aᶜ = {x | x ∉ A ∧ x ∈ U}

![Complemento de conjuntos](https://static.platzi.com/media/articlases/Images/Complemento%20de%20conjuntos.png)

Considera el siguiente ejemplo:

- U = {1, 2, 3, 4, 5, 6, 7, 8, 9}
- A = {5, 6, 7, 8, 9}
- B = {1, 6, 7, 8}

Entonces:

- Aᶜ = {1, 2, 3, 4}
- Bᶜ = {2, 3, 4, 5, 9}
- A - B = {5, 9}
- B - A = {1}
- A Δ B = {1, 5, 9}

## Conjuntos en Python

Python incorpora la estructura de datos `set` para trabajar con conjuntos de manera sencilla y eficiente. Algunas características importantes son:

- **Colección desordenada:** Los elementos no tienen un orden fijo.
- **No admite duplicados:** Al crear un conjunto, los elementos repetidos se eliminan automáticamente.
- **Operaciones matemáticas:** Permite realizar operaciones como unión, intersección, diferencia y diferencia simétrica.

Aquí algunos ejemplos prácticos:



<div style="background: #1E1E1E; padding: 10px; border-radius: 8px border: 4px solid; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
<hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# Creación de un conjunto de países
set_countries = {'col', 'mex', 'bol'}
print(set_countries)  # Ejemplo de salida: {'bol', 'col', 'mex'}
print(type(set_countries))  # Salida: <class 'set'>

# Creación de un conjunto con números (los duplicados se eliminan)
set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)  # Ejemplo de salida: {1, 2, 443, 23}

# Conjunto con elementos de diferentes tipos
set_types = {1, 'hola', False, 12.12}
print(set_types)

# Convertir una cadena en un conjunto (cada carácter único)
set_from_string = set('hoola')
print(set_from_string)

# Convertir una tupla en un conjunto
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

# Convertir una lista en un conjunto para obtener elementos únicos
numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
```

</div>
<br>



---


## Modificando Conjuntos en Python

En Python, los conjuntos son colecciones desordenadas que almacenan elementos únicos, lo que significa que no permiten duplicados. Esta característica los hace ideales para manejar datos sin repeticiones y para realizar operaciones rápidas de verificación y comparación. A continuación, exploramos cómo modificar conjuntos de manera efectiva utilizando algunos de sus métodos clave.

---

### Agregar Elementos

Para añadir un solo elemento a un conjunto, el método **add()** es la opción perfecta. Este método garantiza que el elemento se agregue solo si no está ya presente, preservando la propiedad de unicidad del conjunto.

**Ejemplo:**

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">


```python
set_countries = {'Colombia', 'Mexico', 'Chile'}
set_countries.add('Perú')
print(set_countries)  # Salida: {'Colombia', 'Mexico', 'Chile', 'Perú'}
```

</div>
<br>



Incluso si intentas agregar 'Perú' nuevamente, el conjunto no lo duplicará.

---

### Actualizar Conjuntos con Múltiples Elementos

Si necesitas añadir varios elementos a la vez, **update()** es tu aliado. Este método permite agregar todos los elementos de otro conjunto (u otra colección) de forma simultánea sin crear duplicados.

**Ejemplo:**


<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
set_countries = {'Colombia', 'Mexico', 'Chile', 'Perú'}
nuevos_paises = {'Argentina', 'Ecuador', 'Perú'}
set_countries.update(nuevos_paises)
print(set_countries)  
# Salida: {'Colombia', 'Mexico', 'Chile', 'Perú', 'Argentina', 'Ecuador'}
```

</div>
<br>



Observa cómo 'Perú' no se repite, incluso al intentar agregarlo a través del método update().

---

### Eliminando Elementos: remove() vs. discard()

Eliminar elementos de un conjunto es sencillo, pero es importante elegir el método adecuado según el comportamiento que desees:

- **remove():**  
  Elimina un elemento específico del conjunto. Sin embargo, si el elemento no existe, Python lanzará un error.
  
  **Ejemplo:**

  <div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">


  ```python
  set_countries = {'Colombia', 'Mexico', 'Chile', 'Perú'}
  set_countries.remove('Colombia')
  print(set_countries)  # Salida: {'Mexico', 'Chile', 'Perú'}
  ```

</div>
<br>
  

  
- **discard():**  
  También elimina un elemento, pero si éste no se encuentra en el conjunto, no se genera ningún error. Este método es ideal para un manejo más robusto y seguro.
  
  **Ejemplo:**

  <div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">


  ```python
  set_countries.discard('ARG')  # No pasa nada, 'ARG' no existe
  ```

</div>
<br>
  


---

### Vaciar un Conjunto: Reiniciando Tu Colección

Para eliminar todos los elementos de un conjunto y dejarlo completamente vacío, utiliza el método **clear()**. Esto es útil cuando necesitas reiniciar la colección y comenzar de nuevo.

**Ejemplo:**

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">


```python
set_countries.clear()
print(set_countries)  # Salida: set()
```

</div>
<br>



---

### Más Allá de la Modificación

Python ofrece muchas funcionalidades avanzadas para trabajar con conjuntos. Puedes explorar operaciones como uniones, intersecciones, diferencias y diferencias simétricas para manipular y comparar colecciones de datos de forma eficiente.



[Python Set Methods](https://www.w3schools.com/python/python_ref_set.asp)


¡Sigue explorando y perfeccionando tus habilidades en Python para descubrir aún más formas de trabajar con datos y optimizar tus programas!

---

# Funciones

## 🔮 Creando una Función en Python  

Para invocar una función, usamos la palabra clave `def`, seguida de un nombre creativo y parámetros (si los necesitas). ¡Veamos un ejemplo!  

```python  
def duplicar_mensaje(mensaje):  
    print(mensaje * 2)  
```  

Esta función, `duplicar_mensaje`, toma un texto y lo imprime dos veces. Por ejemplo, si lanzas `duplicar_mensaje("Hola")`, el resultado será `HolaHola`. ¡Abracadabra!  

---

## 🎩 ¿Cómo Usar Tus Funciones?  

Una vez definida tu función, puedes llamarla cuantas veces quieras:  

```python  
duplicar_mensaje("¡A programar! ")  # Salida: ¡A programar! ¡A programar!  
duplicar_mensaje("Python ")         # Salida: Python Python  
```  

¡Sin repetir código! Cada llamada ejecuta el bloque mágico que creaste.  

---

## 🔢 Funciones con Múltiples Parámetros  

¿Y si necesitas que tu hechizo maneje más de un ingrediente? Las funciones pueden recibir **tantos parámetros como necesites**. Por ejemplo, una función para sumar números:  

```python  
def sumar_numeros(num1, num2):  
    print(num1 + num2)  
```  

Al llamar `sumar_numeros(3, 5)`, ¡obtendrás `8` en tu consola!  

---

## 🌀 Funciones que Usan Otras Funciones  

La verdadera magia surge cuando mezclas funciones. Imagina que quieres duplicar el resultado de una suma:  

```python  
def duplicar_mensaje(mensaje):  
    print(mensaje * 2)  

def sumar_y_duplicar(a, b):  
    resultado_suma = a + b  
    duplicar_mensaje(resultado_suma)  
```  

Si ejecutas `sumar_y_duplicar(2, 4)`, la suma (6) se duplicará, mostrando `12`. ¡Cooperación entre funciones!  

---

## 🌟 Los Tesoros que Ofrecen las Funciones  

### 🧰 **Código Reutilizable**  
Olvídate de copiar y pegar. ¡Una función bien hecha es como una herramienta que usas para siempre!  

### 🛠️ **Mantenimiento Sin Dolor**  
¿Necesitas corregir un error? Modifica la función una vez, y todos los lugares donde se usa se actualizarán.  

### 📖 **Código Legible**  
Un nombre descriptivo (como `calcular_promedio`) explica lo que hace el código sin necesidad de comentarios.  

### 🎭 **Flexibilidad Creativa**  
Usa parámetros variables, combina funciones, ¡y adapta tu código a cualquier desafío!  


```python  
# ¿Listo para crear tu propio hechizo?  
def crear_magia():  
    print("✨ ¡Tu código ahora es mágico! ✨")  

crear_magia()  
```  

¡Atrévete a experimentar y verás cómo tu código cobra vida! 🐍💫


Aquí tienes la versión ajustada:

---

# Funciones que retornan valores en Python
## ¿Qué son y por qué son útiles?  
Las funciones que devuelven valores son herramientas esenciales para organizar y optimizar tu código. Permiten encapsular operaciones específicas, ejecutarlas cuando sea necesario, y obtener resultados que pueden usarse en otras partes del programa.  

---

## Creando una función para sumar rangos numéricos  
Este ejemplo demuestra cómo crear una función flexible para sumar números dentro de un rango personalizado:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
def suma_con_rango(minimo, maximo):
    suma = 0
    for x in range(minimo, maximo + 1):
        suma += x
    return suma
```
</div>
<br>  

---

## Cómo utilizar la función en diferentes escenarios  
Una vez definida, puedes reutilizar la función con distintos parámetros:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
resultado1 = suma_con_rango(1, 10)
print(f"Suma del 1 al 10: {resultado1}")  # Resultado: 55

resultado2 = suma_con_rango(20, 30)
print(f"Suma del 20 al 30: {resultado2}")  # Resultado: 275
```
</div>
<br>  

---

## 4 Beneficios clave de estas funciones  
1. **Reutilización inteligente**: Ejecuta la misma lógica con diferentes datos  
2. **Código modular**: Divide problemas complejos en partes manejables  
3. **Actualizaciones sencillas**: Modifica la función una vez para afectar todos sus usos  
4. **Mayor claridad**: Nombres descriptivos hacen el código más comprensible  

---

## Cómo almacenar y usar los resultados  
El verdadero potencial está en guardar los valores devueltos para usarlos posteriormente:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
total = suma_con_rango(5, 15)
porcentaje = total * 0.20
print(f"20% del total: {porcentaje}")
```
</div>
<br>  

---

## Combinando funciones para operaciones complejas  
Los resultados pueden convertirse en entradas para nuevas operaciones:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">
  
```python
primera_suma = suma_con_rango(1, 5)
segunda_suma = suma_con_rango(primera_suma, primera_suma + 3)
print(f"Resultado final: {segunda_suma}")  # Usa el 15 (resultado de 1-5) como nuevo mínimo
```
</div>
<br>  

---

**Consejo final**: Empieza con funciones simples y ve conectándolas gradualmente. Verás cómo tu código gana en eficiencia y organización sin esfuerzo. ¡El poder está en la práctica constante!