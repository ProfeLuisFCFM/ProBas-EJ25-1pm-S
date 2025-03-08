modelo = "Hello Kitty"

for _ in modelo:
    print(_)

print(modelo.capitalize())

print(modelo.count('t'))

modelo.encode()

print(modelo.endswith('y'))
print(modelo.startswith('h'))


print(modelo.find(' '))

print('{:.15f}'.format(1))

print(modelo.index('l'))



print(modelo.replace(' ','_').split('_'))

print(modelo.swapcase())


tra = {32:92}

print(modelo.translate(tra))

print(modelo.lower(),modelo.upper())
