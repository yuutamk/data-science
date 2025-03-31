# 📊 CSV en Python: Domina el Arte de Manipular Datos  

Los archivos CSV son el pan de cada día en el análisis de datos. Aprende a leerlos, transformarlos y extraer insights valiosos con Python.  

---

## 🔍 ¿Dónde Conseguir Datasets?  
**Kaggle** es tu aliado. Sigue estos pasos:  
1. Regístrate en [Kaggle](https://www.kaggle.com/).  
2. Busca *"World Population Dataset"*.  
3. Descarga y descomprime el archivo.  
4. Renombra el CSV a `poblacion_mundial.csv`.  

---

## 📂 Lectura Básica de CSV  
### Paso 1: Importar el módulo `csv`  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
import csv  
```  
</div>  
<br>  

### Paso 2: Leer el archivo  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
def leer_csv(ruta):  
    with open(ruta, 'r') as archivo:  
        lector = csv.reader(archivo, delimiter=',')  
        datos = []  
        for fila in lector:  
            datos.append(fila)  
        return datos  
```  
</div>  
<br>  

---

## 🛠 Transformar CSV en Diccionarios  
### Paso 3: Usar encabezados como claves  
<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
def csv_a_diccionarios(ruta):  
    with open(ruta, 'r') as archivo:  
        lector = csv.reader(archivo, delimiter=',')  
        encabezados = next(lector)  # Primera fila  
        datos = []  
        for fila in lector:  
            pais = {clave: valor for clave, valor in zip(encabezados, fila)}  
            datos.append(pais)  
        return datos  
```  
</div>  
<br>  

**Ejemplo de salida**:

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
{  
    'País': 'Colombia',  
    'Población': '51.52 millones',  
    'Año': '2023'  
}  
```  

</div>  
<br>  

---

## 🚀 Ejecutar como Script Independiente  

Configura tu archivo para uso dual (módulo y programa):  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
if __name__ == "__main__":  
    datos = csv_a_diccionarios('poblacion_mundial.csv')  
    print(datos[0])  # Muestra el primer país  
```  
</div>  
<br>  

---

## 💡 Consejos para Profesionales  
1. **Manejo de errores**: Añade `try/except` para archivos corruptos.  
2. **Pandas**: Para datasets grandes, usa `pandas.read_csv()`.  
3. **Visualización**: Convierte los datos a DataFrame para gráficos con `matplotlib`.  

<div style="background: #1E1E1E; padding: 10px; border-radius: 8px; width: fit-content; font-family: monospace; color: white;">  
  <div style="display: flex; gap: 6px; padding: 5px;">  
    <span style="width: 12px; height: 12px; background: #FF5F57; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #FFBD2E; border-radius: 50%; display: inline-block;"></span>  
    <span style="width: 12px; height: 12px; background: #27C93F; border-radius: 50%; display: inline-block;"></span>  
  </div>  
  <hr style="border: 1px solid black; background: none; margin:0; padding:0;  height: 0px; ">  

```python  
# Ejemplo con Pandas:  
import pandas as pd  
df = pd.read_csv('poblacion_mundial.csv')  
print(df.head())  
```  

</div>  
<br> 

---

**Desafío Final**:  
- Descarga un dataset de tu interés.  
- Crea un script que filtre países con población > 100 millones.  
- Genera un gráfico de barras con los resultados.  

**¡Convierte datos en conocimiento y domina el arte del análisis!** 🐍🔍