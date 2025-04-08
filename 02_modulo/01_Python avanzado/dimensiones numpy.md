
### **Manejo de dimensiones en NumPy**  
Las dimensiones en NumPy son fundamentales para trabajar con datos estructurados. Permiten abordar problemas complejos en ciencia de datos mediante operaciones eficientes. A continuación, se explican los conceptos clave:

---

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