# scripts/4_dashboard_streamlit.py
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar modelo y datos
model = joblib.load('./models/modelo_random_forest.pkl')
df = pd.read_csv('./data/rendimiento_estudiantes_limpio.csv')

# Configurar el dashboard
st.set_page_config(page_title="Predicción de Rendimiento Académico", layout="wide")

# Título
st.title("Dashboard de Predicción de Rendimiento Estudiantil")

# Sección 1: Input de usuario
with st.sidebar:
    st.header("Ingresa los datos del estudiante")
    study_hours = st.slider("Horas de estudio semanales", 0.0, 20.0, 6.0)
    attendance = st.slider("Asistencia (%)", 0.0, 100.0, 85.0)
    socioeconomic_status = st.selectbox("Nivel socioeconómico", ["low", "medium", "high"])
    previous_grades = st.slider("Calificaciones previas", 0.0, 100.0, 75.0)
    access_to_resources = st.radio("Acceso a recursos educativos", ["yes", "no"])

# Sección 2: Predicción
if st.sidebar.button("Predecir calificación final"):
    input_data = pd.DataFrame([{
        'study_hours': study_hours,
        'attendance': attendance,
        'socioeconomic_status': socioeconomic_status,
        'previous_grades': previous_grades,
        'access_to_resources': access_to_resources
    }])
    
    # Codificar variables categóricas
    input_encoded = pd.get_dummies(input_data)
    
    # Asegurar todas las columnas del modelo
    model_columns = model.feature_names_in_
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    
    # Realizar predicción
    prediction = model.predict(input_encoded[model_columns])
    
    # Mostrar resultado
    st.success(f"Calificación final predicha: **{prediction[0]:.1f}**")

# Sección 3: Visualizaciones
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribución de Calificaciones Finales")
    fig, ax = plt.subplots()
    sns.histplot(df['final_grade'], kde=True, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Correlación entre Horas de Estudio y Calificaciones")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='study_hours', y='final_grade', hue='socioeconomic_status', ax=ax)
    st.pyplot(fig)