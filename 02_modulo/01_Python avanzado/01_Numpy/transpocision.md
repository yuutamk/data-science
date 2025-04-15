# Transformación de Arrays en NumPy: Operaciones Esenciales  

## Transposición de Matrices  
Intercambia filas por columnas para operaciones de álgebra lineal y análisis de datos.  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
import numpy as np  

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
transposed_matrix = matrix.T  

print("Original:\n", matrix)  
print("Transpuesta:\n", transposed_matrix)  
```  
</div>  
<br>  

**Salida**:  
```  
Original:  
 [[1 2 3]  
 [4 5 6]  
 [7 8 9]]  
Transpuesta:  
 [[1 4 7]  
 [2 5 8]  
 [3 6 9]]  
```  

---

## Cambiar la Forma de un Array (`reshape`)  
Reorganiza los elementos sin alterar los datos.  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
array = np.arange(1, 13)  
reshaped = array.reshape(3, 4)  

print("Original:", array)  
print("Reshaped (3x4):\n", reshaped)  
```  
</div>  
<br>  

**Clave**:  
- El número total de elementos debe mantenerse (ej: 12 elementos → 3x4, no 5x3).  

---

## Inversión de Arrays  
Invierte el orden de los elementos para procesamiento de señales o algoritmos.  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
array = np.array([1, 2, 3, 4, 5])  
reversed_array = array[::-1]  

print("Original:", array)  
print("Invertido:", reversed_array)  
```  
</div>  
<br>  

**Salida**:  
```  
Original: [1 2 3 4 5]  
Invertido: [5 4 3 2 1]  
```  

---

## Aplanamiento de Arrays (`flatten`)  
Convierte arrays multidimensionales en unidimensionales para algoritmos lineales.  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
multi_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
flattened = multi_array.flatten()  

print("Original:\n", multi_array)  
print("Aplanado:", flattened)  
```  
</div>  
<br>  

**Nota**:  
- `flatten()` crea una copia. Usa `ravel()` para una vista (si no necesitas copia).  

---

## Consideraciones Finales  
1. **Verifica dimensiones**: Asegúrate de que `reshape` mantiene el total de elementos.  
2. **Copia vs Vista**: `flatten()` copia datos, `ravel()` devuelve una vista.  
3. **Eficiencia**: Usa transposición (`T`) para operaciones matriciales sin duplicar memoria.  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
# Ejemplo de aplanamiento con ravel()  
vista = multi_array.ravel()  
print("Vista (ravel):", vista)  
```

</div>  
<br>  