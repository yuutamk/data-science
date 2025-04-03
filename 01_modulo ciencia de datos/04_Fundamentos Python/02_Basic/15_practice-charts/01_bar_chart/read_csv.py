import csv
import os # Importar el módulo os para trabajar con rutas de archivos


# Metodo 4


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        
        
        data = [] 
        
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data
            
            
if __name__ == '__main__':
    current_dir = os.path.dirname(__file__) # Obtener el directorio actual
    file_path = os.path.join(current_dir, 'data.csv') # Construir la ruta completa al archivo CSV
    # Llamar a la función read_csv con la ruta del archivo CSV
    data = read_csv(file_path) # Imprimir el contenido del archivo CSV
    print(data) # Imprimir la lista de diccionarios
    #print(data[0]) # Imprimir el primer elemento de la lista de diccionarios
 
    
# Metodo 5

# constuir un dict con el contenido del csv
"""
def read_csv(path):
    with open(path, 'r') as csvfile:
        fileCSV = csv.DictReader(csvfile, delimiter=',')  # Utilizar DictReader para construir el diccionario directamente
        data = [row for row in fileCSV]  # Crear una lista de diccionarios a partir del contenido del CSV
        return data

if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)  # Obtener el directorio actual
    file_path = os.path.join(current_dir, 'data.csv')  # Construir la ruta completa al archivo CSV
    data = read_csv(file_path)  # Leer el contenido del archivo CSV
    print(data)  # Imprimir la lista de diccionarios"""

  