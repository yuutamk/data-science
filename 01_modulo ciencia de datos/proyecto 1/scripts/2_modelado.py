# scripts/2_modelado.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Cargar datos limpios
df = pd.read_csv('./data/rendimiento_estudiantes_limpio.csv')

# Codificar variables categóricas
df = pd.get_dummies(df, columns=['socioeconomic_status', 'access_to_resources'])

# Dividir datos
X = df.drop(['student_id', 'final_grade'], axis=1)
y = df['final_grade']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluar
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5
print(f'RMSE: {rmse:.2f}')  # Debería mostrar ~2.5

# Guardar modelo
joblib.dump(model, './models/modelo_random_forest.pkl')