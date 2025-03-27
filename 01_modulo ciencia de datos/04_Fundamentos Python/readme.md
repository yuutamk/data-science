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

---

# Funciones que retornan valores en Python: Desde lo básico hasta múltiples retornos  

## ¿Qué son y cómo definirlas?  
Las funciones que devuelven valores nos permiten encapsular operaciones y obtener resultados específicos. Aquí un ejemplo para calcular el volumen de un objeto:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
def volumen(length, width, depth):
    return length * width * depth
```
</div>
<br>  

**Uso básico:**  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
result = volumen(10, 20, 3)
print(result)  # Output: 600
```
</div>
<br>  

---

## Parámetros con valores predeterminados  
Python permite definir valores por defecto para mayor flexibilidad:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
def volumen(length=1, width=1, depth=1):
    return length * width * depth

# Usando solo un parámetro personalizado
result = volumen(width=10)
print(result)  # Output: 10 (1*10*1)
```
</div>
<br>  

---

## Retornando múltiples valores  
Python permite devolver varios resultados usando tuplas:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
def volumen(length, width, depth):
    calculated_volume = length * width * depth
    return calculated_volume, width, "hola"

# Obteniendo y usando la tupla completa
result = volumen(10, 20, 3)
print(result)  # Output: (600, 20, 'hola')
```
</div>
<br>  

---

## Descomponiendo los resultados  
Podemos extraer valores individuales de la tupla retornada:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
volume, width, greeting = volumen(10, 20, 3)
print(f"Volumen: {volume}, Ancho: {width}, Saludo: {greeting}")
# Output: Volumen: 600, Ancho: 20, Saludo: hola
```
</div>
<br>  

---

### 3 Ventajas Clave:  
1. **Personalización**: Parámetros con valores por defecto adaptan la función a distintos casos  
2. **Versatilidad**: Retornar múltiples valores simplifica el flujo de datos  
3. **Organización**: La descomposición de tuplas hace el código más legible  

**Consejo práctico**: Combina parámetros predeterminados con retornos múltiples para crear funciones flexibles y poderosas. ¡Experimenta con diferentes combinaciones!

---

# Scope en Python: Alcance de Variables  

## ¿Qué es y por qué es importante?  
El scope (alcance) determina dónde y cómo pueden usarse las variables o funciones en un programa. Es clave para evitar conflictos entre datos y mantener el código organizado.  

---

## Tipos de Scope  
1. **Local**: Variables declaradas dentro de una función. Solo existen ahí.  
2. **Enclosing**: Variables en funciones anidadas (exteriores a una función interna).  
3. **Global**: Accesibles en todo el programa.  
4. **Built-in**: Palabras reservadas y funciones integradas del lenguaje.  

---

## Ejemplo Práctico: Global vs Local  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
precio_global = 100  # Variable global

def calcular_aumento():
    precio_local = 200  # Variable local
    return precio_local + 10

print(precio_global)        # Output: 100
print(calcular_aumento())   # Output: 210
```
</div>
<br>  

---

## Errores Frecuentes  

### 1. Acceder a variables locales fuera de su contexto  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
def funcion_problematica():
    variable_local = 50

print(variable_local)
```
</div>
<br>  

---
#  👉**Playground Refactor Game**👈


Refactoriza el juego de piedra papel o tijera ahora con funciones:

[piedra papel o tijera.py](./Class/05_funciones/04_refactor/01_origin-piedra-papel-tijera.py)

# 👉**Tienda de Tecnología**👈

Playgraund [Tienda de Tecnología](./Playgraunds/Tienda-de-Tecnologia/readme.md)

---


# Funciones Lambda en Python: Simplificando tu Código  

## ¿Para qué sirven y cómo se usan?  
Las funciones lambda son herramientas para crear operaciones simples en una sola línea. Ideales cuando necesitas funciones rápidas sin la formalidad de `def`.  

---

## Transformando una función tradicional a lambda  
### Versión con `def`  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
def increment(x):
    return x + 1
```
</div>
<br>  

### Versión lambda equivalente  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
increment_v2 = lambda x: x + 1
```
</div>
<br>  

**Uso práctico:**  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
print(increment_v2(10))  # Resultado: 11
```
</div>
<br>  

---

## Trabajando con múltiples parámetros  
Ejemplo para formatear nombres completos:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
formatear_nombre = lambda nombre, apellido: f"{nombre.capitalize()} {apellido.capitalize()}"
print(formatear_nombre('juan', 'pérez'))  # Output: Juan Pérez
```
</div>
<br>  

---

## Asignación y reutilización  
Las lambdas pueden guardarse en variables para usarlas repetidamente:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
multiplicar = lambda a, b: a * b
print(multiplicar(5, 3))  # Output: 15
```
</div>
<br>  

---

### 3 Beneficios Clave:  
1. **Sintaxis concisa**: Ideales para operaciones de una línea  
2. **Sin nombres permanentes**: Útiles para funciones temporales  
3. **Integración con otras funciones**: Perfectas para `map()`, `filter()`, etc.  

**Consejo**: Usa lambdas para tareas simples. Si la lógica crece, prefiere funciones tradicionales con `def`.  

![Lambda](./Assets/img/lambda.gif)
---

## Ejemplo Final: Combinación con Funciones  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# Filtrar números pares usando lambda
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Output: [2, 4]
```
</div>
<br>  

**¡Domina las lambdas y lleva tu código al siguiente nivel!** 🚀


---

# Funciones de Orden Superior

## ¿Qué son y cómo funcionan?  
Las funciones de orden superior (HOF) son aquellas que pueden recibir otras funciones como parámetros o devolverlas como resultado. Esto permite crear soluciones flexibles y modulares.  

---

## Ejemplo Básico  
### Función clásica + HOF  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
def incrementar(x):
    return x + 1

def hof(x, funcion):
    return x + funcion(x)

resultado = hof(2, incrementar)
print(resultado)  # Output: 5 (2 + incrementar(2)=3 → 2+3=5)
```
</div>
<br>  

---

## Integrando Funciones Lambda  
Las lambdas simplifican el uso de HOF al evitar definir funciones completas:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# Versión con lambda
hof_lambda = lambda x, func: x + func(x)
resultado = hof_lambda(2, lambda x: x + 1)
print(resultado)  # Output: 5
```
</div>
<br>  

---

### 3 Ventajas de Usar Lambdas con HOF  
1. **Código compacto**: Define la lógica directamente donde se usa  
2. **Menos variables**: Evita declarar funciones con `def` para operaciones simples  
3. **Dinamismo**: Cambia el comportamiento de la HOF al vuelo  

---

## Casos de Uso Ideales  
- **Transformar datos**: Aplicar operaciones a listas (ej: multiplicar todos los elementos por 2)  
- **Filtrar información**: Seleccionar elementos que cumplan cierta condición  
- **Personalizar comportamientos**: Modificar cómo funciona una función según el contexto  

---

## Ejemplo Avanzado: Uso Directo de Lambda  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
resultado = hof_lambda(2, lambda x: x * 3)
print(resultado)  # Output: 8 (2 + (2*3)=6 → 2+6=8)
```
</div>
<br>  

---

## ¿Qué Aprender Después?  
Las HOF son la base para funciones integradas como `map()`, `filter()`, y `reduce()`. Por ejemplo:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
numeros = [1, 2, 3]
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)  # Output: [2, 4, 6]
```
</div>
<br>  

**Consejo**: Practica creando tus propias HOF y combinándolas con lambdas para dominar estos conceptos. 🚀

---

# Función Map en Python: Transformación Eficiente de Listas  

## ¿Qué hace y cómo funciona?  
La función `map` aplica una operación a cada elemento de una lista, generando una nueva lista con los resultados. Mantiene la misma cantidad de elementos pero transformados.  

---

## Uso Básico: Multiplicar Elementos  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
numeros = [1, 2, 3, 4]

# Duplicar cada elemento con map + lambda
resultado = list(map(lambda x: x * 2, numeros))

print(resultado)  # Output: [2, 4, 6, 8]
```
</div>
<br>  

---

## Operando Entre Dos Listas  
Combina elementos de dos listas posición por posición:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 7]

suma = list(map(lambda a, b: a + b, lista_a, lista_b))
print(suma)  # Output: [5, 7, 9] (Se detiene en el índice 2)
```
</div>
<br>  

---

## Consideraciones Clave  
1. **Longitud de listas**: `map` procesa hasta el final de la lista más corta.  
2. **Tipos de datos**: Funciona con cualquier iterable (tuplas, conjuntos, etc.).  
3. **Eficiencia**: Es más rápido que un bucle `for` tradicional para operaciones simples.  

---

## Ejemplo Práctico: Transformar Textos  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
palabras = ["vaca", "pollo", "maíz"]
transformadas = list(map(lambda x: x.capitalize(), palabras))

print(transformadas)  # Output: ['Vaca', 'Pollo', 'Maíz']
```
</div>
<br>  

---

### ¿Cuándo Usar Map?  
- **Transformaciones en masa**: Cambiar formatos, cálculos matemáticos, etc.  
- **Integración con otras funciones**: Perfecto para combinar con `filter` o `reduce`.  
- **Código limpio**: Evita bucles explícitos cuando la lógica es simple.  

**Consejo**: Combina `map` con funciones lambda para operaciones rápidas, pero usa funciones definidas (`def`) si la lógica es compleja.  

---

**¡Experimenta con `map` y descubre cómo simplifica tu manipulación de datos!** 🚀

---

# Método Filter en Python: Filtra Datos con Precisión  

## ¿Cómo funciona y para qué sirve?  
El método `filter` permite seleccionar elementos de una lista que cumplen una condición específica, creando una nueva lista con ellos. Ideal para extraer información relevante sin modificar los datos originales.  

---

## Filtrado Básico: Números Pares  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Output: [2, 4, 6]
```
</div>
<br>  

---

## Filtrado en Estructuras Complejas: Diccionarios  
Ejemplo para seleccionar partidos ganados por equipos locales:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
partidos = [
    {"equipo_local": "Bolivia", "resultado": "victoria"},
    {"equipo_local": "Argentina", "resultado": "empate"},
    {"equipo_local": "Perú", "resultado": "victoria"}
]

victorias = list(filter(lambda p: p['resultado'] == 'victoria', partidos))
print(victorias)  # Muestra solo los diccionarios con 'victoria'
```
</div>
<br>  

---

## Consideraciones Importantes  
1. **Lista original intacta**: Siempre genera una nueva lista  
2. **Resultado iterable**: Necesitas convertir a lista con `list()`  
3. **Cantidad variable**: La nueva lista puede tener menos elementos o ninguno  
4. **Condiciones claras**: Asegúrate que la lógica del filtro sea precisa  

---

### Casos de Uso Comunes  
- **Datos numéricos**: Filtrar rangos, múltiplos, o valores atípicos  
- **Textos**: Seleccionar palabras con ciertas características  
- **Datos estructurados**: Filtrar registros en listas de diccionarios  

---

## Ejemplo Avanzado: Filtros Anidados  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# Filtrar números pares mayores a 4
numeros = [2, 5, 8, 3, 10]
filtrados = list(filter(lambda x: x % 2 == 0 and x > 4, numeros))
print(filtrados)  # Output: [8, 10]
```
</div>
<br>  

**Consejo**: Combina `filter` con `map` para transformar y filtrar datos en un solo flujo.  

---

**¡Domina el filtrado de datos y lleva tu manipulación de listas al siguiente nivel!** 🔍🐍

---

# Función Reduce en Python: Acumulación de Datos Simplificada  

## ¿Qué es y para qué sirve?  
La función `reduce` procesa una lista para generar un único resultado acumulativo. Ideal para sumatorias, productos máximos, o cualquier operación que combine elementos secuencialmente.  

---

## Implementación Paso a Paso  
### Requisito: Importar `functools`  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
import functools

numeros = [1, 2, 3, 4]

# Sumar todos los elementos
resultado = functools.reduce(lambda acumulado, item: acumulado + item, numeros)
print(resultado)  # Output: 10
```
</div>
<br>  

---

## Desglose de Iteraciones  
### Visualizando el proceso interno  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
def acumulador(acumulado, item):
    print(f"Acumulado: {acumulado} | Item actual: {item}")
    return acumulado + item

resultado = functools.reduce(acumulador, numeros)
# Output paso a paso:
# Acumulado: 1 | Item actual: 2 → 3
# Acumulado: 3 | Item actual: 3 → 6
# Acumulado: 6 | Item actual: 4 → 10
```
</div>
<br>  

---

## 3 Ventajas Clave de Reduce  
1. **Código conciso**: Reemplaza bucles `for` con una sola línea  
2. **Flexibilidad**: Funciona con cualquier operación acumulativa (suma, multiplicación, concatenación)  
3. **Legibilidad**: Claridad al expresar la intención del código  

---

## Ejemplo Avanzado: Encontrar el Máximo  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
valores = [15, 8, 22, 3, 9]
maximo = functools.reduce(lambda a, b: a if a > b else b, valores)
print(maximo)  # Output: 22
```
</div>
<br>  

---

### ¿Cuándo Evitar Reduce?  
- **Listas vacías**: Genera error si no se provee un valor inicial (`initializer`).  
- **Lógica compleja**: Si la operación requiere múltiples pasos, mejor usar bucles.  

---

**Consejo Final**: Combina `reduce` con `map` y `filter` para flujos de datos potentes. Por ejemplo, filtrar números negativos y luego sumarlos:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
datos = [5, -3, 10, -8, 2]
suma_positivos = functools.reduce(
    lambda a, b: a + b,
    filter(lambda x: x > 0, datos),
    0  # Valor inicial para evitar errores
)
print(suma_positivos)  # Output: 17 (5 + 10 + 2)
```
</div>
<br>  

**¡Domina `reduce` y lleva tu manipulación de datos a otro nivel!** 🔄🐍

# Módulos en Python: Organiza y Potencia tu Código  

## ¿Qué son y cómo funcionan?  
Los módulos son archivos `.py` que contienen funciones, variables o clases reutilizables. Permiten dividir proyectos complejos en partes manejables y aprovechar funcionalidades predefinidas.  

---

## Módulos Integrados Más Usados  
Python incluye módulos listos para usar. Algunos esenciales:  
- **`random`**: Generación de números aleatorios.  
- **`sys`**: Acceso a variables del sistema.  
- **`re`**: Trabajo con expresiones regulares.  
- **`time`**: Manejo de fechas y horas.  
- **`collections`**: Estructuras de datos avanzadas.  

---

## Cómo Importar y Usar Módulos  
### Ejemplo con `random`:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
import random

numero = random.randint(1, 10)
print(numero)  # Ejemplo: 7
```
</div>
<br>  

---

## Manipulación de Rutas con `sys`  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
import sys

print(sys.path)  # Muestra rutas de búsqueda de módulos
```
</div>
<br>  

---

## Expresiones Regulares con `re`  
Extracción de números de un texto:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
import re

texto = "Teléfono: 311-1234567"
numeros = re.findall(r'\d+', texto)
print(numeros)  # Output: ['311', '1234567']
```
</div>
<br>  

---

## Manejo de Tiempo con `time`  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
import time

print(time.time())          # Tiempo en segundos desde 1970
print(time.asctime())       # Fecha legible: 'Mon Oct 2 12:00:00 2023'
```
</div>
<br>  

---

## Conteo de Elementos con `collections`  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
from collections import Counter

datos = ['manzana', 'pera', 'manzana', 'uva']
conteo = Counter(datos)
print(conteo)  # Output: {'manzana': 2, 'pera': 1, 'uva': 1}
```
</div>
<br>  

---

### 4 Beneficios de Usar Módulos  
1. **Reutilización**: Evita reinventar la rueda con funcionalidades ya existentes.  
2. **Organización**: Separa lógica en archivos independientes.  
3. **Mantenibilidad**: Facilita actualizaciones y corrección de errores.  
4. **Eficiencia**: Aprovecha código optimizado por la comunidad.  

---

## Próximos Pasos  
Una vez dominados los módulos integrados, el siguiente nivel es crear **módulos personalizados**. Por ejemplo:  
- Agrupar funciones de cálculo matemático en `calculos.py`.  
- Organizar utilidades de formato en `herramientas.py`.  

**Consejo clave**: Usa nombres descriptivos y documenta tus módulos para que otros (o tu yo futuro) entiendan su propósito.  
 

**Explora, practica y verás cómo tu código se vuelve más profesional y escalable.** 🚀

---


# Cómo Crear Módulos Personalizados en Python

## ¿Por Qué y Cómo Organizar tu Código en Módulos?  
Dividir tu código en módulos mejora la mantenibilidad y reutilización. Un módulo es simplemente un archivo `.py` con funciones, clases o variables relacionadas. Te mostramos cómo implementarlo:

---

## Creación Básica de un Módulo  
### 1. Estructura de archivos  
Crea una carpeta para tu proyecto (ej: `app`) y dentro dos archivos:  
- `mod.py`: Tu módulo personalizado  
- `main.py`: Programa principal  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# mod.py
def get_population():
    countries = ['Colombia', 'Bolivia']
    populations = [300, 400]
    return countries, populations
```
</div>
<br>  

### 2. Uso del Módulo  
Importa y utiliza las funciones desde tu archivo principal:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# main.py
import mod

paises, poblaciones = mod.get_population()
print(f"Países: {paises}\nPoblaciones: {poblaciones}")
```
</div>
<br>  

**Ejecución**:
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```bash
cd app
python main.py
# Output: Países: ['Colombia', 'Bolivia'] Poblaciones: [300, 400]
```

</div>
<br>  
---

## Buenas Prácticas: Nombrado Significativo  
Usa nombres que describan claramente el contenido del módulo. Por ejemplo:  

- `mod.py` → `datos_demograficos.py`  
- Actualiza las importaciones en consecuencia:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
import datos_demograficos as dd

resultado = dd.get_population()
```
</div>
<br>  

---

## Funcionalidades Avanzadas en Módulos  
Agrega lógica compleja manteniendo la organización:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# datos_demograficos.py
def filtrar_por_pais(datos, pais):
    return list(filter(lambda item: item['pais'].lower() == pais.lower(), datos))
```
</div>
<br>  

**Uso desde el programa principal**:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
datos = [
    {'pais': 'México', 'poblacion': 128},
    {'pais': 'Argentina', 'poblacion': 45}
]

busqueda = input("Ingrese país: ")
resultado = dd.filtrar_por_pais(datos, busqueda)
print(f"Datos encontrados: {resultado}")
```
</div>
<br>  

---

### 4 Ventajas Clave de la Modularización  
1. **Reutilización de código**: Usa las mismas funciones en múltiples proyectos  
2. **Mantenimiento sencillo**: Corrige errores en un solo archivo  
3. **Legibilidad**: Código organizado por funcionalidades  
4. **Colaboración eficiente**: Diferentes equipos pueden trabajar en módulos separados  


**¡Domina esta técnica y lleva tus proyectos al siguiente nivel!** 🚀

---


# Ejecución de Módulos en Python: Controla Cuándo y Cómo se Corre tu Código  

## Dos Formas de Ejecutar Módulos  
1. **Como script directo**: Desde la terminal con `python archivo.py`  
2. **Como módulo importado**: Usando `import` desde otro archivo  

---

## El Problema de la Ejecución Inesperada  
Cuando un módulo contiene código fuera de funciones, este se ejecuta automáticamente al importarlo. Ejemplo:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# main.py (sin control de ejecución)
data = [1, 2, 3]
print("¡Este mensaje no debería aparecer al importar!")
usuario = input("Ingresa tu nombre: ")  # Se ejecuta incluso al importar
```
</div>
<br>  

**Al importarlo desde otro archivo**:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# ejemplo.py
import main  # ¡Ejecuta el input y el print automáticamente!
```
</div>
<br>  

---

## Solución: `if __name__ == "__main__"`  
Este bloque garantiza que el código solo se ejecute cuando el archivo es el punto de entrada principal.  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# main.py (versión corregida)
def ejecutar_como_script():
    print("Modo script activado ✅")
    usuario = input("Nombre: ")
    print(f"Hola, {usuario}!")

if __name__ == "__main__":
    ejecutar_como_script()
```
</div>
<br>  

### ¿Cómo funciona?  
- **Ejecución directa**: `__name__` es `"__main__"` → Se ejecuta el bloque.  
- **Como módulo**: `__name__` es el nombre del archivo (ej: `"main"`) → No se ejecuta.  

---

## Recomendaciones Clave  
1. **Encapsula la lógica principal en funciones**: Facilita el control de ejecución.  
2. **Prueba ambos modos**: 

   ```bash
   # Como script
   python main.py

   # Como módulo (en otro archivo)
   import main
   ```  

3. **Evita código global**: Todo lo que no sean definiciones (funciones/clases) debe ir dentro del bloque `if __name__`.  

---

## Ejemplo de Flujo Controlado  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# modulo_util.py
def sumar(a, b):
    return a + b

if __name__ == "__main__":
    # Solo se ejecuta al correr el archivo directamente
    print("Prueba de la función sumar:", sumar(5, 3))
```
</div>
<br>  

**Resultado al importar**:  

```python
import modulo_util
print(modulo_util.sumar(2, 2))  # Output: 4 (sin mensajes extras)
```

---

**Conclusión**: Domina el uso de `if __name__ == "__main__"` para crear módulos flexibles y evitar comportamientos inesperados. ¡Tu código ganará en profesionalismo y confiabilidad! 🔧🐍