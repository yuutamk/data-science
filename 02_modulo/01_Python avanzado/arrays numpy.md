

### **Métodos para crear arrays en NumPy**  
La librería ofrece múltiples enfoques para generar estructuras de datos eficientes:



**1. Desde estructuras Python**  
Conversión directa de listas o tuplas a arrays:  



<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
# Arrays desde listas
array_1d = np.array([1, 2, 3, 4])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
```
</div>
<br>


---

**2. Funciones predefinidas**  
Generación rápida de arrays con patrones específicos:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
zeros = np.zeros((3, 3))          # Matriz de ceros
secuencia = np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
puntos_equi = np.linspace(0, 1, 5)  # 5 valores entre 0 y 1
```
</div>
<br>

---

 **3. Especificación de tipos de datos**  
Control preciso del formato numérico usando `dtype`:  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
enteros = np.array([1, 2, 3], dtype='int32')        # Enteros 32 bits
flotantes = np.array([1.0, 2.0, 3.0], dtype='d')    # Float64 (equivalente a 'd')
booleanos = np.array([True, False], dtype='bool')    # Valores lógicos
```
</div>
<br>

**Tipos comunes**:  
- `int32` / `int64`: Enteros de 32/64 bits  
- `float32` / `float64`: Precisión simple/doble  
- `complex128`: Números complejos  
- `str`: Cadenas de texto  

---

**4. Manejo de valores NaN**  
Representación de datos faltantes o indefinidos:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">

```python
datos_incompletos = np.array([1, 2, np.nan, 4])  # Array con valor faltante
print(datos_incompletos)  # [ 1.  2. nan  4.]
```
</div>
<br>

**Uso clave**:  
- Identificar valores ausentes en análisis estadísticos  
- Manejar resultados matemáticos no definidos (ej: 0/0)  
- Limpieza de datasets incompletos  

---

**Recomendación**: Utiliza `np.isnan()` para detectar valores NaN en tus arrays y asegurar la integridad de los datos antes de realizar operaciones críticas.