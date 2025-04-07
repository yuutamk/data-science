"""
El ciclo for como en otros lenguajes se utiliza para que se repita las veces que se estime, ya sea por el usuario, desarrollador o incluso por el mismo programa, pero si sintaxis no es la misma que en otros lenguajes, donde declaramos el ciclo for y la variable del ciclo de la siguiente manera 

> for variable

Para posterior indicarle en qué función o parámetro se va a basar para que repita el ciclo

> for variable in (puede ser una lista, tupla, una función o un rango)

Dependiendo el parámetro que le pasemos este ciclo se repetirá las veces que sean necesarias
"""


'''
for element in range(1, 21):
  print(element)

'''

my_list = [23, 45, 67, 89 ,43]
for element in my_list:
  print(element)

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)


product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}

"""
for element in product:
  print(element)

for element in product:
  print(product[element])

"""


for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)


# lista de diccionarios
people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

for person in people:
  print('name =>', person['name'])