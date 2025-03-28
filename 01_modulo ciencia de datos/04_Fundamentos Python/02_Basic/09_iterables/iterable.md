## ITERABLES 

Un iterable se define como el objeto que contiene un número contable con valores y este al tener un valor puede recorrer uno a uno los elementos que la contienen como una estructura de datos y operar con ellos, pero a la vez se rigen bajo la instrucción que se le es dada, con lo cual son dependientes de la instrucción a recibir.

Los metodos de su uso son dos `__iter__()` y ``__next__()`` .

Veamos un ejemplo:

>Tenemos una serie de frutas las cuales debemos recorrer una a una para saber cuales son las que están dentro de la lista.

```python
fruit = ("manzana", 'pera', 'banano')
myit = iter(fruit)

print(next(myit))
print(next(myit))
print(next(myit))
```

Ahora vamos a imprimir el resultado una a una con ``print(next(myit))``, con esto controlamos un iterador por print

```python
print(next(myit))
```
_Producción:_

    manzana

```python
print(next(myit))
print(next(myit))
```

_Producción:_

    manzana
    pera

```python
print(next(myit))
print(next(myit))
print(next(myit))
```

_Producción:_

    manzana
    pera
    banano

También podemos utilizar los iterables como una cadena de texto que recorre un texto o una serie de números.

```python
fruit = ("manzana")
myit = iter(fruit)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
```

_Producción:_

    m
    a
    n
    z
    a
    n
    a

Otra forma de realizar un iterador es atraves de for() o un bucle, para ello realizaremos el siguiente ejemplo:

```python
cars = ('chevrolet', 'volvo', 'audi', 'mazda') 
for x in cars:
  print(x)
```

_Produccion:_

    chevrolet
    volvo
    audi
    mazda

Con el iterador también podemos crear una secuencia de números hasta cierto valor que le determinemos.

```python
class MyNumbers:
   def __iter__(self):
     self.a = 1
     return self

   def __next__(self):
     x = self.a
     self.a += 1
     return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
```

_Producción:_

    1
    2
    3
    4
    5

Ahora si queremos que la iteración se detenga en un valor determinador podemos utilizar la declaración StopIteration

```python
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
```

_Producción:_

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10