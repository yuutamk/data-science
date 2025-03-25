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