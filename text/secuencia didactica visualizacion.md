
## **Planificación Detallada**  

### **Sesión 1: Introducción al Ciclo de Vida y Definición del Problema**  
**Duración:** 2 horas.  
**Temas:**  
1.1 Ciclo de Vida de un Proyecto de Ciencia de Datos.  
1.2 Definición del Problema.  

**Actividades:**  
1. **Explicación teórica** (30 min):  
   - Presentar las 8 etapas del ciclo de vida (usar diagramas interactivos).  
   - Ejemplo práctico: Definir un problema de predicción de churn.  
2. **Ejercicio grupal** (1 hora):  
   - Los estudiantes definirán un problema ficticio (ej: predecir ventas mensuales).  
   - Deberán detallar: objetivo, datos necesarios y métricas de éxito.  
3. **Discusión y retroalimentación** (30 min).  

**Producto:** Documento con la definición del problema (formato tabla).  
**Evaluación:** Participación en la discusión y claridad del documento.  

---

### **Sesión 2: Recolección de Datos y Manejo de Valores Faltantes**  
**Duración:** 2 horas.  
**Temas:**  
1.3 Recolección de Datos.  
1.4 Manejo de Valores Faltantes y Duplicados.  

**Actividades:**  
1. **Demostración práctica** (30 min):  
   - Cargar datos desde un CSV usando Pandas (`pd.read_csv`).  
   - Identificar valores faltantes con `df.isnull().sum()`.  
2. **Ejercicio individual** (1 hora):  
   - Limpiar un dataset con valores faltantes (usar estrategias: eliminación, relleno con media).  
   - Eliminar duplicados con `df.drop_duplicates()`.  
3. **Revisión en pares** (30 min).  

**Producto:** Código Python funcional y dataset limpio.  
**Evaluación:** Correcta aplicación de métodos de limpieza.  

---

### **Sesión 3: Filtrado, Selección y Transformación de Columnas**  
**Duración:** 2 horas.  
**Temas:**  
1.5 Filtrado y Selección de Datos.  
1.6 Transformación de Columnas.  

**Actividades:**  
1. **Explicación con ejemplos** (30 min):  
   - Filtrar datos por condiciones (ej: `df[df['edad'] > 30]`).  
   - Crear nuevas columnas (ej: convertir ingresos anuales a mensuales).  
2. **Ejercicio práctico** (1 hora):  
   - Filtrar un dataset para seleccionar registros específicos.  
   - Modificar una columna categórica (ej: estandarizar formatos de texto).  
3. **Presentación de resultados** (30 min).  

**Producto:** DataFrame transformado con nuevas columnas y filtros aplicados.  
**Evaluación:** Originalidad en las transformaciones y correcto uso de sintaxis.  

---

### **Sesión 4: Unión de DataFrames y Manejo de Conjuntos de Datos**  
**Duración:** 2 horas.  
**Temas:**  
1.7 Unión y Concatenación de DataFrames.  
1.8 Manejo de Conjuntos de Datos.  

**Actividades:**  
1. **Demostración guiada** (30 min):  
   - Unir dos DataFrames con `pd.merge()` usando una columna clave.  
   - Concatenar verticalmente con `pd.concat()`.  
2. **Ejercicio en equipos** (1 hora):  
   - Combinar datasets de ventas y clientes para crear una vista unificada.  
   - Generar un informe breve sobre inconsistencias detectadas.  
3. **Discusión de desafíos** (30 min).  

**Producto:** Dataset unificado y informe de inconsistencias.  
**Evaluación:** Capacidad para resolver errores durante la unión.  

---

### **Sesión 5: Conjuntos de Datos Reales vs. Sintéticos**  
**Duración:** 2 horas.  
**Temas:**  
1.9 Conjuntos de Datos Reales y Sintéticos.  

**Actividades:**  
1. **Explicación comparativa** (30 min):  
   - Ventajas y desventajas de datos reales vs. sintéticos.  
   - Generar datos sintéticos con NumPy y Faker.  
2. **Práctica creativa** (1 hora):  
   - Crear un dataset sintético de estudiantes (edad, calificaciones, etc.).  
   - Compararlo con un dataset real proporcionado.  
3. **Reflexión grupal** (30 min): ¿En qué casos usar datos sintéticos?  

**Producto:** Dataset sintético y tabla comparativa.  
**Evaluación:** Calidad y realismo del dataset sintético.  

---

### **Sesión 6: Integración y Evaluación Final**  
**Duración:** 2 horas.  
**Actividades:**  
1. **Proyecto integrador** (1.5 horas):  
   - Limpiar, transformar y unir múltiples datasets (reales y sintéticos).  
   - Generar un informe ejecutivo con hallazgos clave.  
2. **Presentación y retroalimentación** (30 min).  

**Producto:** Proyecto final con código, datasets procesados e informe.  
**Evaluación:** Cumplimiento de objetivos, claridad del informe y manejo técnico.  

---


## **Resumen de Tiempos**  
| Sesión | Tema | Duración |  
|--------|------|----------|  
| 1 | Ciclo de Vida y Definición del Problema | 2h |  
| 2 | Recolección y Valores Faltantes | 2h |  
| 3 | Filtrado y Transformación | 2h |  
| 4 | Unión de DataFrames | 2h |  
| 5 | Datos Reales vs. Sintéticos | 2h |  
| 6 | Evaluación Final | 2h |  
**Total:** 12 horas (dentro del rango de 8-16 horas).  
