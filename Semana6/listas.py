lista1 = ['a',2,21,3.5]
lista2 = list()

print(type(lista1),type(lista2))

lista1.append(lambda a,b: a*b)

print(lista1[4](3,4))

lista2 = lista1.copy()

lista2.append('z')

print(lista1,lista2)

print(lista2.count('z'))

