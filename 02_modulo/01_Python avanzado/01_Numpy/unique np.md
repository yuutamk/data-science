
# Identificación y Conteo de Elementos Únicos con NumPy  

## Análisis de Opiniones de Clientes  
Procesar respuestas como "bueno", "excelente" o "malo" permite tomar decisiones estratégicas. NumPy optimiza este proceso con operaciones eficientes.  

---

## Paso 1: Identificar Elementos Únicos  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
import numpy as np  

respuestas = np.array(['bueno', 'excelente', 'malo', 'bueno', 'excelente', 'bueno', 'malo', 'excelente'])  
elementos_unicos = np.unique(respuestas)  

print(elementos_unicos)  
# Output: ['bueno' 'excelente' 'malo']  
```  
</div>  
<br>  

---

## Paso 2: Contar Frecuencias  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
elementos_unicos, conteos = np.unique(respuestas, return_counts=True)  

print(elementos_unicos)  # ['bueno' 'excelente' 'malo']  
print(conteos)           # [4 3 2]  
```  
</div>  
<br>  

---

## Vistas vs Copias en NumPy  

### Ejemplo 1: Modificación de Vistas  
Las vistas reflejan cambios en el array original:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
x = np.arange(10)        # [0 1 2 3 4 5 6 7 8 9]  
vista = x[1:3]           # [1 2]  

x[1:3] = [10, 11]        # Modifica el array original  
print(vista)              # Output: [10 11]  
```  
</div>  
<br>  

### Ejemplo 2: Uso de Copias  
Las copias son independientes del original:  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
copia = x[1:3].copy()    # [10 11]  
x[1:3] = [12, 13]        # Modifica el original  

print(x)                 # [ 0 12 13  3  4  5  6  7  8  9]  
print(copia)             # [10 11] (no cambia)  
```  
</div>  
<br>  

---

## Buenas Prácticas  
1. **Vistas para optimizar memoria**: Úsalas cuando necesites acceder a subconjuntos sin modificar datos.  
2. **Copias para seguridad**: Crea copias (`array.copy()`) si planeas modificar subconjuntos sin afectar el original.  
3. **Verifica el tipo**: Usa `array.base` para saber si un array es vista o copia.  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
# Ejemplo de verificación  
print(vista.base is x)   # Output: True  
print(copia.base is None) # Output: True  
``` 

</div>  
<br>  


**Conclusión**: NumPy combina eficiencia y flexibilidad. Domina vistas y copias para evitar errores y maximizar rendimiento.