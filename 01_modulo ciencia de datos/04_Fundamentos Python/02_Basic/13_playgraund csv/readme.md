<h1>Calcular el total de gastos de una empresa</h1>



**Reto: Sumatoria de gastos desde CSV**  
Debes implementar la función `read_csv` que procese un archivo CSV y calcule el total de gastos.

**Requerimientos:**
1. Leer el archivo CSV usando el módulo `csv`
2. Extraer valores numéricos de la segunda columna
3. Sumar todos los valores para obtener el total
4. Manejar correctamente la ruta del archivo

**Código base:**

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%;"></span>
  </div>
  <hr style="border: 1px solid black; margin:0;">

```python
import csv

def read_csv(path):
   # Tu código aquí 👇
   total = 0
   return total

response = read_csv('./data.csv')
print(response)
```
</div>
<br>


**Ejemplo de Entrada/Salida**  

```bash
Contenido de data.csv:
Administration,10
Marketing,20
Purchasing,10
Human Resources,20

Output: 60
```


**Instrucciones de implementación:**
1. Usa `csv.reader` para procesar el archivo
2. Ignora posibles encabezados si existen
3. Convierte los valores numéricos a enteros
4. Suma todos los valores de la columna de gastos
5. Prueba con diferentes archivos CSV

<b>
<details>
<summary>Solución (después de 4 intentos)</summary>  
<h6>Propuesta de solución</h6>

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%;"></span>
  </div>
  <hr style="border: 1px solid black; margin:0;">

```python
import csv

def read_csv(path):
   total = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for row in reader:
         total += int(row[1])
   return total

response = read_csv('./data.csv')
print(response)
```

</details>
</h4>
