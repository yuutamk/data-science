import utils
import read_csv
import charts
import os


current_dir = os.path.dirname(__file__) # Obtener el directorio actual
file_path = os.path.join(current_dir, 'data.csv') # Construir la ruta completa al archivo CSV


def run():
    data = read_csv.read_csv(file_path) # Leer el contenido del archivo CSV
    country = input('Type Country => ')
    
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
    
if __name__ == '__main__':
    run()    