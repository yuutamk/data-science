# Playgraund Tienda de Tecnología

**Reto: Creador de Mensajes Tecnológicos**  
Debes completar la función `message_creator` para que retorne mensajes específicos según el artículo tecnológico recibido.

**Requerimientos:**
1. La función debe evaluar el string de entrada
2. Retornar mensajes específicos para 3 casos:
   - `computadora`: "Con mi computadora puedo programar usando Python"
   - `celular`: "En mi celular puedo aprender usando la app"
   - `cable`: "¡Hay un cable en mi bota!"
3. Para cualquier otro valor: "Artículo no encontrado"

**Código base:**

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0; height: 0px;">
 
```python
def message_creator(text):
   # Escribe tu solución 👇
   return ''
```
</div>
<br>


**Ejemplo 1 - Computadora**  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0; height: 0px;">

```bash
Input: 'computadora'
Output: Con mi computadora puedo programar usando Python
```
</div>
<br>


**Ejemplo 2 - Celular**  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0; height: 0px;">

```bash
Input: 'celular'
Output: En mi celular puedo aprender usando la app
```
</div>
<br>


**Ejemplo 3 - Cable** 

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0; height: 0px;">

```bash
Input: 'cable'
Output: ¡Hay un cable en mi bota!
```
</div>
<br>


**Ejemplo 4 - Artículo desconocido**  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">
  <div style="display: flex; gap: 6px; padding: 5px;">
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>
  </div>
  <hr style="border: 1px solid black; background: none; margin:0; padding:0; height: 0px;">

```bash
Input: 'ornitorrinco'
Output: Artículo no encontrado
```
</div>
<br>

**Instrucciones de implementación:**
1. Usa condicionales para comparar el input
2. Retorna los mensajes literales exactos mostrados en los ejemplos
3. Considera mayúsculas/minúsculas y signos de puntuación
4. Prueba todos los casos antes de enviar tu solución

¡La implementación debe funcionar para cualquier string que reciba como parámetro!



<h4>
<details value="code">  
<summary>Abrir despues de 4 intentos</summary>  
<h3> Propuesta de solusión </h3>

```python
def message_creator(text):
   if text == 'computadora':
      return 'Con mi computadora puedo programar usando Python'
   elif text == 'celular':
      return 'En mi celular puedo aprender usando la app'
   elif text == 'cable':
      return '¡Hay un cable en mi bota!'
   else:
      return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)
```

</details>
</h4>