# scripts/1_limpieza_y_eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv('./data/rendimiento_estudiantes.csv')

# Paso 1: Eliminar duplicados
df = df.drop_duplicates(subset='student_id', keep='first')

# Paso 2: Imputar valores nulos en 'previous_grades'
median_prev_grades = df.groupby('socioeconomic_status')['previous_grades'].transform('median')
df['previous_grades'] = df['previous_grades'].fillna(median_prev_grades)

# Guardar dataset limpio
df.to_csv('./data/rendimiento_estudiantes_limpio.csv', index=False)

# Análisis Exploratorio
sns.pairplot(df, hue='socioeconomic_status')
plt.savefig('./notebooks/correlaciones.png')  # Guardar gráfico
plt.show()