# **Módulo 2: Limpieza y Transformación de Datos**

La limpieza y transformación de datos es una de las etapas más críticas en cualquier proyecto de ciencia de datos. A menudo, los datos brutos que obtenemos no están listos para ser analizados directamente. Contienen errores, inconsistencias, valores faltantes y redundancias que pueden sesgar los resultados o dificultar el análisis. En este módulo, profundizaremos en cada uno de los aspectos clave de la limpieza y transformación de datos, proporcionando ejemplos prácticos y explicaciones detalladas.

---

## **1. Ciclo de Vida de un Proyecto de Ciencia de Datos**

Antes de profundizar en la limpieza y transformación de datos, es importante entender cómo estas actividades se integran en el ciclo de vida completo de un proyecto de ciencia de datos:

1. **Definición del problema**: Identificar claramente el objetivo del proyecto.
2. **Recolección de datos**: Obtener los datos necesarios desde diversas fuentes.
3. **Limpieza y preparación de datos**: Limpiar y transformar los datos para hacerlos aptos para el análisis.
4. **Análisis exploratorio**: Explorar patrones y tendencias en los datos.
5. **Modelado**: Construir modelos predictivos o descriptivos.
6. **Evaluación**: Validar el rendimiento del modelo.
7. **Despliegue**: Implementar el modelo en un entorno real.
8. **Monitoreo**: Supervisar el rendimiento continuo del modelo.

En este módulo, nos enfocaremos en la tercera etapa: **Limpieza y Preparación de Datos**.

---

## **2. Definición del Problema**

El primer paso antes de comenzar con la limpieza de datos es **definir claramente el problema** que queremos resolver. Esto implica:

- **Entender el contexto del negocio**: ¿Qué preguntas estamos tratando de responder? Por ejemplo, si trabajamos en marketing, podríamos estar interesados en segmentar a los clientes para ofrecerles productos personalizados.
  
- **Identificar los datos necesarios**: Una vez definido el problema, debemos identificar qué tipo de datos necesitaremos para resolverlo. Esto podría incluir datos demográficos, transacciones, interacciones en redes sociales, etc.

- **Establecer métricas de éxito**: ¿Cómo mediremos el éxito del proyecto? Por ejemplo, si estamos construyendo un modelo predictivo, podríamos medir su precisión, recall, F1-score, etc.

### **Ejemplo Práctico**
Supongamos que estamos trabajando en un proyecto de predicción de churn (abandono) de clientes en una empresa de telecomunicaciones. El problema podría definirse como:

- **Objetivo**: Predecir qué clientes tienen mayor probabilidad de abandonar el servicio en los próximos meses.
- **Datos necesarios**: Historial de uso del cliente, facturación, soporte técnico, quejas, etc.
- **Métrica de éxito**: Precisión del modelo en predecir correctamente el churn.

---

## **3. Recolección de Datos**

Una vez definido el problema, el siguiente paso es **recolectar los datos** necesarios. Los datos pueden provenir de diversas fuentes, como:

- **Bases de datos SQL**: Usualmente utilizadas para almacenar datos estructurados.
- **APIs**: Servicios web que proporcionan datos en tiempo real.
- **Archivos CSV/Excel**: Comunes en proyectos pequeños o medianos.
- **Web scraping**: Extracción de datos de sitios web.
- **Sensores/IoT**: Datos generados por dispositivos conectados.

### **Herramientas para la Recolección de Datos**
- **Pandas**: Para leer archivos CSV, Excel, JSON, etc.
- **SQLAlchemy**: Para conectarse a bases de datos SQL.
- **Requests**: Para interactuar con APIs.
- **BeautifulSoup/Scrapy**: Para realizar web scraping.

### **Ejemplo Práctico**
Supongamos que tenemos un archivo CSV con datos de clientes de telecomunicaciones. Podemos cargarlo en Python usando Pandas:

```python
import pandas as pd

# Cargar datos desde un archivo CSV
df = pd.read_csv('datos_clientes.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())
```

---

## **4. Manejo de Valores Faltantes y Duplicados**

Uno de los problemas más comunes en los datos es la presencia de **valores faltantes** y **registros duplicados**. Estos problemas deben abordarse antes de continuar con el análisis.

### **Valores Faltantes**
Los valores faltantes pueden aparecer por varias razones:
- Errores en la recolección de datos.
- Falta de respuesta en encuestas.
- Datos perdidos durante la transferencia.

#### **Estrategias para manejar valores faltantes**
1. **Eliminar registros con valores faltantes**:
   ```python
   df.dropna(inplace=True)
   ```
   Esto elimina todas las filas que contienen al menos un valor faltante.

2. **Rellenar valores faltantes**:
   - Con un valor constante:
     ```python
     df.fillna(0, inplace=True)
     ```
   - Con la media, mediana o moda:
     ```python
     df['edad'].fillna(df['edad'].mean(), inplace=True)
     ```

3. **Interpolación**:
   La interpolación es útil cuando los datos tienen una secuencia temporal o espacial.
   ```python
   df['valor'] = df['valor'].interpolate()
   ```

### **Registros Duplicados**
Los registros duplicados pueden distorsionar el análisis, especialmente en modelos de aprendizaje automático.

#### **Eliminar duplicados**
```python
df.drop_duplicates(inplace=True)
```

---

## **5. Filtrado y Selección de Datos**

A menudo, no necesitamos todos los datos disponibles. Es posible que solo necesitemos ciertas columnas o filas que cumplan con ciertas condiciones.

### **Filtrado de Datos**
Podemos filtrar datos basados en condiciones específicas. Por ejemplo, si queremos seleccionar solo los clientes mayores de 30 años:

```python
df_filtrado = df[df['edad'] > 30]
```

### **Selección de Columnas**
Si solo necesitamos ciertas columnas, podemos seleccionarlas:

```python
df_seleccionado = df[['nombre', 'edad', 'ingresos']]
```

---

## **6. Transformación de Columnas**

La transformación de columnas implica modificar los datos existentes o crear nuevas características (features) que puedan mejorar el rendimiento del modelo.

### **Crear Nuevas Columnas**
Podemos crear nuevas columnas basadas en cálculos o transformaciones de columnas existentes. Por ejemplo, si queremos calcular el ingreso mensual promedio:

```python
df['ingreso_mensual'] = df['ingreso_anual'] / 12
```

### **Modificar Columnas Existentes**
Podemos aplicar funciones a columnas existentes para modificar sus valores. Por ejemplo, convertir todos los nombres a mayúsculas:

```python
df['nombre'] = df['nombre'].apply(lambda x: x.upper())
```

---

## **7. Unión y Concatenación de DataFrames**

En muchos casos, necesitaremos combinar múltiples conjuntos de datos para obtener una vista completa.

### **Unión de DataFrames**
La unión permite combinar dos DataFrames basados en una columna común (clave).

```python
df_unido = pd.merge(df1, df2, on='id_cliente')
```

### **Concatenación de DataFrames**
La concatenación permite apilar DataFrames vertical u horizontalmente.

```python
df_concatenado = pd.concat([df1, df2], axis=0)  # Apilado verticalmente
```

---

## **8. Manejo de Conjuntos de Datos**

El manejo de conjuntos de datos implica trabajar con diferentes tipos de datos, tanto reales como sintéticos.

### **Conjuntos de Datos Reales**
Los datos reales provienen de fuentes del mundo real, como bases de datos empresariales, encuestas, sensores, etc. Estos datos suelen ser ruidosos y requieren limpieza extensa.

### **Conjuntos de Datos Sintéticos**
Los datos sintéticos son generados artificialmente para pruebas o simulaciones. Son útiles cuando no se dispone de datos reales o cuando se quiere proteger la privacidad.

#### **Generación de Datos Sintéticos**
Podemos generar datos sintéticos usando bibliotecas como `numpy` o `faker`.

```python
import numpy as np
import pandas as pd

# Generar datos sintéticos
data = {
    'edad': np.random.randint(18, 65, size=100),
    'ingreso': np.random.normal(50000, 15000, size=100)
}
df_sintetico = pd.DataFrame(data)
```

---

## **9. Conjuntos de Datos Reales y Sintéticos**

Finalmente, es importante destacar que los **conjuntos de datos reales** suelen ser más complejos y desordenados que los sintéticos. Sin embargo, los datos sintéticos son útiles para probar algoritmos y modelos en un entorno controlado.

### **Ejemplo Práctico**
Supongamos que estamos trabajando con un conjunto de datos real de clientes de telecomunicaciones. Podríamos seguir estos pasos:

1. **Cargar los datos** desde un archivo CSV.
2. **Limpiar los datos**: Eliminar valores faltantes, duplicados y corregir inconsistencias.
3. **Transformar los datos**: Crear nuevas columnas o modificar las existentes.
4. **Unir datos adicionales**: Si tenemos información adicional sobre los clientes, como historial de compras, podemos unirla al conjunto principal.
5. **Guardar el conjunto limpio** para su posterior análisis.

---

## **Conclusión**

La limpieza y transformación de datos es una etapa fundamental en cualquier proyecto de ciencia de datos. Aunque puede parecer tediosa, es crucial para garantizar que los datos sean precisos y estén listos para el análisis. En este módulo, hemos cubierto desde la recolección de datos hasta la transformación y unión de DataFrames, proporcionando ejemplos prácticos en Python.

Recuerda que la práctica es clave. Usa herramientas como Google Colab y Pandas para experimentar con tus propios conjuntos de datos. ¡Buena suerte en tu camino hacia la ciencia de datos! 🚀


---

# **Ciclo de Vida de un Proyecto de Ciencia de Datos: Análisis Exploratorio, Modelado, Evaluación, Despliegue y Monitoreo**

En el módulo anterior, profundizamos en la limpieza y transformación de datos, una etapa crucial para preparar los datos antes del análisis. Ahora, continuaremos explorando las siguientes fases del ciclo de vida de un proyecto de ciencia de datos: **Análisis Exploratorio**, **Modelado**, **Evaluación**, **Despliegue** y **Monitoreo**. Cada una de estas etapas es fundamental para garantizar que el proyecto sea exitoso y que los modelos construidos sean útiles y confiables.

---

## **1. Análisis Exploratorio de Datos (EDA)**

El **Análisis Exploratorio de Datos (EDA)** es una fase crítica en cualquier proyecto de ciencia de datos. Su objetivo es comprender mejor los datos, identificar patrones, tendencias y relaciones entre variables, así como detectar anomalías o problemas potenciales en los datos. Este proceso ayuda a formular hipótesis y guiar el desarrollo del modelo.

### **Objetivos del EDA**
- **Conocer la distribución de los datos**: Entender cómo están distribuidas las variables numéricas y categóricas.
- **Identificar valores atípicos (outliers)**: Detectar puntos de datos que se desvían significativamente del resto.
- **Explorar correlaciones**: Identificar relaciones entre variables.
- **Detectar patrones y tendencias**: Observar si hay patrones temporales, espaciales o de otro tipo.
- **Validar suposiciones**: Asegurarse de que los datos cumplen con las suposiciones necesarias para el modelado.

### **Herramientas Comunes para el EDA**
- **Pandas**: Para manipulación y análisis básico de datos.
- **Matplotlib/Seaborn**: Para visualización de datos.
- **NumPy**: Para cálculos estadísticos.
- **Scipy**: Para pruebas estadísticas avanzadas.

### **Pasos Clave en el EDA**

#### **1.1 Resumen Estadístico**
El primer paso es obtener un resumen estadístico de los datos. Esto incluye medidas como media, mediana, desviación estándar, mínimo y máximo.

```python
import pandas as pd

# Resumen estadístico
print(df.describe())
```

#### **1.2 Visualización de Datos**
La visualización es clave para entender la distribución de los datos y las relaciones entre variables.

- **Histogramas**: Para ver la distribución de una variable numérica.
  ```python
  import matplotlib.pyplot as plt

  df['edad'].hist(bins=30)
  plt.title('Distribución de Edades')
  plt.xlabel('Edad')
  plt.ylabel('Frecuencia')
  plt.show()
  ```

- **Diagramas de dispersión**: Para explorar relaciones entre dos variables.
  ```python
  plt.scatter(df['edad'], df['ingresos'])
  plt.title('Relación entre Edad e Ingresos')
  plt.xlabel('Edad')
  plt.ylabel('Ingresos')
  plt.show()
  ```

- **Mapas de calor**: Para visualizar correlaciones entre variables.
  ```python
  import seaborn as sns

  corr = df.corr()
  sns.heatmap(corr, annot=True, cmap='coolwarm')
  plt.title('Mapa de Calor de Correlaciones')
  plt.show()
  ```

#### **1.3 Detección de Outliers**
Los outliers pueden distorsionar el análisis y deben ser tratados cuidadosamente.

- **Boxplots**: Para identificar valores atípicos.
  ```python
  sns.boxplot(x=df['ingresos'])
  plt.title('Boxplot de Ingresos')
  plt.show()
  ```

#### **1.4 Análisis de Variables Categóricas**
Para variables categóricas, podemos usar gráficos de barras o tablas de frecuencia.

```python
df['categoria'].value_counts().plot(kind='bar')
plt.title('Distribución de Categorías')
plt.show()
```

---

## **2. Modelado**

Una vez que hemos comprendido los datos mediante el EDA, el siguiente paso es **construir modelos predictivos o descriptivos**. El modelado implica seleccionar algoritmos adecuados, entrenarlos con los datos y ajustarlos para obtener el mejor rendimiento posible.

### **Tipos de Modelos**
- **Modelos Predictivos**: Predicen una variable objetivo basándose en otras variables (regresión, clasificación).
- **Modelos Descriptivos**: Explican patrones o relaciones en los datos (clustering, reglas asociativas).

### **Pasos en el Modelado**

#### **2.1 División de Datos**
Es importante dividir los datos en conjuntos de entrenamiento y prueba para evaluar el rendimiento del modelo.

```python
from sklearn.model_selection import train_test_split

X = df.drop('target', axis=1)  # Variables independientes
y = df['target']               # Variable dependiente

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

#### **2.2 Selección del Algoritmo**
Dependiendo del problema, podemos elegir diferentes algoritmos:
- **Regresión Lineal**: Para problemas de regresión.
- **Árboles de Decisión**: Para problemas de clasificación o regresión.
- **K-Means**: Para clustering.
- **Redes Neuronales**: Para problemas más complejos.

#### **2.3 Entrenamiento del Modelo**
Usamos el conjunto de entrenamiento para entrenar el modelo.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

#### **2.4 Predicción**
Una vez entrenado, el modelo puede hacer predicciones sobre nuevos datos.

```python
y_pred = model.predict(X_test)
```

---

## **3. Evaluación**

La **evaluación** del modelo es crucial para determinar su rendimiento y fiabilidad. Dependiendo del tipo de problema (clasificación, regresión, etc.), usamos diferentes métricas.

### **Métricas Comunes**
- **Clasificación**:
  - **Accuracy**: Proporción de predicciones correctas.
  - **Precision, Recall, F1-Score**: Para problemas de clasificación desbalanceados.
  
  ```python
  from sklearn.metrics import classification_report

  print(classification_report(y_test, y_pred))
  ```

- **Regresión**:
  - **Mean Absolute Error (MAE)**: Error absoluto medio.
  - **Mean Squared Error (MSE)**: Error cuadrático medio.
  - **R² Score**: Coeficiente de determinación.

  ```python
  from sklearn.metrics import mean_squared_error, r2_score

  mse = mean_squared_error(y_test, y_pred)
  r2 = r2_score(y_test, y_pred)

  print(f'MSE: {mse}, R²: {r2}')
  ```

---

## **4. Despliegue**

El **despliegue** implica implementar el modelo en un entorno real donde pueda interactuar con usuarios o sistemas. Esto puede incluir la creación de APIs, integración con aplicaciones web o móviles, o incluso la automatización de decisiones.

### **Pasos en el Despliegue**
1. **Exportar el modelo**: Guardar el modelo entrenado para su uso posterior.
   ```python
   import joblib

   joblib.dump(model, 'modelo_entrenado.pkl')
   ```

2. **Crear una API**: Usar frameworks como Flask o FastAPI para exponer el modelo como un servicio.
   ```python
   from flask import Flask, request, jsonify
   import joblib

   app = Flask(__name__)
   model = joblib.load('modelo_entrenado.pkl')

   @app.route('/predict', methods=['POST'])
   def predict():
       data = request.json
       prediction = model.predict([data['features']])
       return jsonify({'prediction': prediction.tolist()})

   if __name__ == '__main__':
       app.run(debug=True)
   ```

3. **Integración con sistemas existentes**: Conectar el modelo con bases de datos, sistemas ERP, CRM, etc.

---

## **5. Monitoreo**

Finalmente, una vez que el modelo está en producción, es crucial **monitorear su rendimiento** continuamente. Los modelos pueden degradarse con el tiempo debido a cambios en los datos o en el entorno.

### **Indicadores de Monitoreo**
- **Drift de datos**: Cambios en la distribución de los datos de entrada.
- **Precisión del modelo**: Verificar si las predicciones siguen siendo precisas.
- **Latencia**: Tiempo que tarda el modelo en hacer predicciones.

### **Herramientas de Monitoreo**
- **Prometheus/Grafana**: Para monitorear métricas en tiempo real.
- **MLflow**: Para gestionar ciclos de vida de modelos y monitorear su rendimiento.

---

## **Conclusión**

El ciclo de vida de un proyecto de ciencia de datos es un proceso iterativo que abarca desde la definición del problema hasta el monitoreo continuo del modelo en producción. Cada etapa es crucial para garantizar que los modelos sean precisos, útiles y confiables. En este blog, hemos cubierto en detalle las fases de **Análisis Exploratorio**, **Modelado**, **Evaluación**, **Despliegue** y **Monitoreo**, proporcionando ejemplos prácticos en Python.

Recuerda que la ciencia de datos no es solo sobre construir modelos, sino también sobre entender los datos, validar resultados y asegurar que los modelos sigan funcionando correctamente en el tiempo. ¡Sigue practicando y explorando nuevas técnicas! 🚀