import utils

keys, values = utils.get_population()
print(keys, values)


print(utils.A)

"""data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

country = input('Type Country => ')

result = utils.population_by_country(data, country)
print(result)
"""


def run():
    keys, values = utils.get_population()
    print(keys, values)


    data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    }
    ]

    country = input('Type Country => ')

    result = utils.population_by_country(data, country)
    print(result)
    

"""if __name__ == '__main__':
  run()"""