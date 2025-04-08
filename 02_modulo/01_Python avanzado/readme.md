# Numpy & Pandas

**Mejorar recomendaciones y análisis de patrones de visualización**  
En el ámbito del streaming de contenido multimedia, optimizar las recomendaciones e identificar los tipos de contenido más demandados es crucial para el éxito empresarial. Analizar los hábitos de visualización de millones de usuarios supone un reto técnico debido al volumen masivo de datos procesados diariamente. Herramientas como **NumPy** y **Pandas** en Python permiten manejar estos datos de forma eficiente y precisa.

**NumPy en el análisis de datos**  
Esta librería es fundamental para trabajar con grandes conjuntos de datos, gracias a su capacidad para ejecutar operaciones matemáticas y estadísticas de alto rendimiento. Sus ventajas incluyen:  
- **Rapidez**: Opera con arrays de forma vectorizada, superando en velocidad a las listas estándar de Python.  
- **Manejo multidimensional**: Simplifica la manipulación de matrices y estructuras complejas.  

**Pandas: Potencia en datos tabulares**  
Construida sobre NumPy, esta herramienta facilita el análisis y manipulación de datos estructurados. Sus principales beneficios son:  
- **Filtrado y agrupación**: Ideal para organizar datos en formato tabular.  
- **DataFrames**: Estructuras que agilizan la exploración y toma de decisiones basadas en datos.  
Además, su dominio abre oportunidades en áreas como *business intelligence* y ciencia de datos.  

**Metodología de aprendizaje**  
El enfoque práctico incluye un proyecto de análisis de ventas en e-commerce, diseñado para aplicar lo aprendido y enriquecer el portafolio profesional.  

**Habilidades a desarrollar**  
- Manipulación eficiente de grandes volúmenes de datos  
- Análisis estadístico detallado  
- Limpieza y preparación de datos  
- Visualización clara de resultados  
- Automatización de procesos repetitivos  

**Configuración inicial**  
Se recomienda usar **Google Colab** o **VS Code**. Instala las librerías con:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# Configura tu entorno de batalla
!pip install numpy pandas matplotlib

```
</div>
<br>



<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# Importa las herramientas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
</div>
<br>



# **Manejo de dimensiones en NumPy**  
Las dimensiones en NumPy son fundamentales para trabajar con datos estructurados. Permiten abordar problemas complejos en ciencia de datos mediante operaciones eficientes. A continuación, se explican los conceptos clave:

![dimensiones](../../assets/img/png/scalar-matrix-matrix.png)
#### **Escalar: Dimensión cero**  
Un escalar es un valor único sin ejes. Por ejemplo, la temperatura de un día específico:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# Ejemplo de escalar
escalar = np.array(42)
print(escalar)  # Salida: 42
print(type(escalar))  # <class 'numpy.ndarray'>
```
</div>
<br>

---

#### **Vector: Dimensión uno**  
Secuencia ordenada de elementos. Útil para series temporales o listas de valores:  




<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
vector = np.array([30, 29, 42, 35, 33, 36, 42])  # Temperaturas semanales
print(vector)
```
</div>
<br>

---



#### **Matriz: Dimensión dos**  
Estructura bidimensional para datos tabulares. Ejemplo: representación de píxeles o registros de ventas:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)
```
</div>
<br>

---

#### **Tensor: Tres o más dimensiones**  
Extensión de matrices para datos complejos, como imágenes en RGB o series temporales multivariadas:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor)
```
</div>
<br>

---

### **Métodos para crear arrays**  
NumPy ofrece múltiples funciones para generar estructuras de datos:  

- **Conversión desde listas/tuplas**  
- **Funciones predefinidas**: `np.zeros`, `np.ones`, `np.arange`  
- **Replicación de arrays existentes**  
- **Lectura de archivos**  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
rango = np.arange(10)  # Array del 0 al 9
identidad = np.eye(3)  # Matriz identidad 3x3
print(rango)
print(identidad)
```
</div>
<br>

---

### **Funciones matemáticas avanzadas**  
Incluyen operaciones para álgebra lineal y generación de datos aleatorios:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
diagonal = np.diag([1, 2, 3, 4])  # Matriz diagonal
aleatoria = np.random.rand(2, 3)   # Valores entre 0 y 1
print(diagonal)
print(aleatoria)
```
</div>
<br>

**Recomendación**: Profundiza en métodos como `np.linalg` para operaciones de álgebra lineal y `np.random` para simulaciones estadísticas. La práctica constante es clave para dominar estas herramientas.