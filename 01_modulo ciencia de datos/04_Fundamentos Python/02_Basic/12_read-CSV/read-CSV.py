import csv
import os # Importar el módulo os para trabajar con rutas de archivos


# Metodo 1

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print('******' * 10)
            print(row)

if __name__ == '__main__':
    current_dir = os.path.dirname(__file__) # Obtener el directorio actual
    file_path = os.path.join(current_dir, 'data.csv') # Construir la ruta completa al archivo CSV
    # Llamar a la función read_csv con la ruta del archivo CSV
    read_csv(file_path) # Imprimir el contenido del archivo CSV          
    
# Metodo 2
# constuir un dict con el contenido del csv
"""
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        print(header) 
        
        
        for row in reader:
            iterable = zip(header, row)
            print(list(iterable))
            
            
if __name__ == '__main__':
    current_dir = os.path.dirname(__file__) # Obtener el directorio actual
    file_path = os.path.join(current_dir, 'data.csv') # Construir la ruta completa al archivo CSV
    # Llamar a la función read_csv con la ruta del archivo CSV
    read_csv(file_path) # Imprimir el contenido del archivo CSV """
    
# Metodo 3
"""
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        print(header) 
        
        
        for row in reader:
            iterable = zip(header, row)
            #print(list(iterable))
            country_dict = {key: value for key, value in iterable}
            print(country_dict)
            
            
if __name__ == '__main__':
    current_dir = os.path.dirname(__file__) # Obtener el directorio actual
    file_path = os.path.join(current_dir, 'data.csv') # Construir la ruta completa al archivo CSV
    # Llamar a la función read_csv con la ruta del archivo CSV
    read_csv(file_path) # Imprimir el contenido del archivo CSV"""
"""
# Variante usando la función dict para crear el diccionario
def read_csv(path):        
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        print(header)
            
        for row in reader:
            iterable = zip(header, row)
            country_dict = dict(iterable)  # Usar dict para crear el diccionario
            print(country_dict)

if __name__ == '__main__':
    current_dir = os.path.dirname(__file__) # Obtener el directorio actual
    file_path = os.path.join(current_dir, 'data.csv') # Construir la ruta completa al archivo CSV
    # Llamar a la función read_csv con la ruta del archivo CSV
    read_csv(file_path) # Imprimir el contenido del archivo CSV """   
   
    
# Metodo 4

"""
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        print(header)
        
        data = [] 
        
        
        for row in reader:
            iterable = zip(header, row)
            #print(list(iterable))
            country_dict = {key: value for key, value in iterable}
            #print(country_dict)
            data.append(country_dict)
        return data
            
            
if __name__ == '__main__':
    current_dir = os.path.dirname(__file__) # Obtener el directorio actual
    file_path = os.path.join(current_dir, 'data.csv') # Construir la ruta completa al archivo CSV
    # Llamar a la función read_csv con la ruta del archivo CSV
    data = read_csv(file_path) # Imprimir el contenido del archivo CSV
    print(data) # Imprimir la lista de diccionarios
    #print(data[0]) # Imprimir el primer elemento de la lista de diccionarios
   """ 
    
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

  