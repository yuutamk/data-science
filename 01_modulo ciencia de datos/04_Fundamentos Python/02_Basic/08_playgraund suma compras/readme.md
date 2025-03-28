<h1>Calcular la suma de todas las compras</h1>



**Reto: Suma de órdenes de compra**  
Debes implementar la función `get_total` que calcule la suma total de todas las órdenes usando un módulo separado.

**Requerimientos:**
1. Crear módulo `my_functions.py` con lógica de cálculo
2. La función principal debe usar el módulo creado
3. Manejar correctamente estructuras de datos tipo diccionario




**Ejemplo de Entrada/Salida** 

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0; height: 0px;"> 

```python
Input: 
[
  {"customer_name": "Nicolas", "total": 100, "delivered": True},
  {"customer_name": "Zulema", "total": 120, "delivered": False},
  {"customer_name": "Santiago", "total": 20, "delivered": False}
]

Output: 240
```
</div>
<br>



**Código base (main.py):**

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0; height: 0px;">

```python
def get_total(orders):
  # Tu código aquí 👇
  return 0

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)
```
</div>
<br>

**Instrucciones de implementación:**
1. Crea un nuevo archivo `my_functions.py`
2. Implementa la lógica de cálculo en el módulo
3. Importa y usa las funciones necesarias en `main.py`
4. Asegúrate de sumar solo el campo `total` de cada orden
5. Prueba con diferentes conjuntos de datos

<h4>
<details>
<summary>Solución (después de 4 intentos)</summary>  
<h3>Propuesta de solución</h3>

**my_functions.py**

```python
def get_totals(orders):
   return [order['total'] for order in orders]

def calc_total(totals):
   return sum(totals)
```

**main.py**
```python
from my_functions import get_totals, calc_total

def get_total(orders):
  totals = get_totals(orders)
  return calc_total(totals)

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)
```
</details>
</h4>


