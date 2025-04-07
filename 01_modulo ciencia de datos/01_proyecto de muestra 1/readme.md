# Estructura de Archivos



```bash
/proyecto_rendimiento
│
├── /data
│   ├── rendimiento_estudiantes.csv
│   └── rendimiento_estudiantes_limpio.csv  # Generado después de la limpieza
│
├── /scripts
│   ├── 1_limpieza_y_eda.py
│   ├── 2_modelado.py
│   └── 4_dashboard_streamlit.py
│
├── /notebooks
│   └── analisis_exploratorio.ipynb 
│
├── /models
│   └── modelo_random_forest.pkl            # Generado al ejecutar 2_modelado.py
│
├── requirements.txt
│
└── README.md
```

# Configuración Inicial
### **1. Crear el entorno virtual:**

En la raíz del proyecto (/proyecto1):
```bash

python -m venv venv
```

#### **2. Activar el entorno virtual:**
- **Windows (PowerShell):**
  ```bash
  .\venv\Scripts\Activate.ps1
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

---


### **Paso 2: Instalar Dependencias**
```bash
pip install -r requirements.txt
```

---

### Configurar la Base de Datos (MySQL/phpMyAdmin)
1. Accede a phpMyAdmin.
2. Crea una nueva base de datos llamada `rendimiento_academico`.
3. Ve a la pestaña **Importar** > Selecciona el archivo `database.sql` (creado con el script SQL proporcionado).
4. Ejecuta la importación.

---

### Ejecutar los Scripts en Orden

#### *1. Limpieza de datos y EDA:*
```bash
python scripts/1_limpieza_y_eda.py
```
- **Resultado:** Genera `data/rendimiento_estudiantes_limpio.csv`.

#### *2. Entrenar el modelo:*
```bash
python scripts/2_modelado.py
```
- **Resultado:** Genera `models/modelo_random_forest.pkl` y muestra el RMSE (~2.5).

#### **3. Ejecutar el dashboard:**
```bash
streamlit run scripts/4_dashboard_streamlit.py
```
- Accede a `http://localhost:8501` en tu navegador.

---

### **Paso 5: Opcional - Ejecutar el Notebook de Análisis**
```bash
jupyter notebook
```
- Navega a `notebooks/analisis_exploratorio.ipynb` y ejecuta todas las celdas.

---


### **Posibles Errores y Soluciones**
1. **`ModuleNotFoundError`**:
   - Asegúrate de que el entorno virtual está activado y las dependencias instaladas.
   - Ejecuta `pip freeze` para verificar las versiones.

2. **Errores con rutas de archivos**:
   - Verifica que la estructura de carpetas coincida exactamente con lo descrito.

3. **Problemas con MySQL**:
   - Revisa que el usuario tenga permisos para crear bases de datos.

