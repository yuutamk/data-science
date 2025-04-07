matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matriz[0][1])

"""
for element in matriz:
  print(element)
  for item in element:
    print(item)
"""


for row in matriz:
  print(row)
  for column in row:
    print(column)