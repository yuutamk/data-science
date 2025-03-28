name = "Nicolas"
last_name = 'Molina Monroy'

print(name)
print(last_name)


full_name = name + last_name
# full_name = name + " " + last_name
print(full_name)

#quote = 'I'm Nicolas'
quote = "I'm Nicolas"
print(quote)

quote2 = ' she said "hello" '
print(quote2)

# format

template = "Hola mi nombre es " + name + " y mi apellido es " + last_name
print('v1',template)

template = "hola mi nombre es {} y mi apellido es {}".format(name,last_name)
print('v2',template)

template = f"Hola mi nombre es {name} y mi apellido es {last_name}"
print('v3',template)
