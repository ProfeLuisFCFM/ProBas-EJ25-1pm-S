fact = lambda n: 1 if n <=1 else n*fact(n-1)


def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)




if __name__ == '__main__':
    print(fact(12))


diccionario = {}


diccionario['empleado1'] = "Luis Gutierrez"

print(diccionario)


equipo1 = dict()

equipo1[0] = {2177669: 'Marcos Crokwell'}
equipo1[1] = {1944269: 'Ed Iñiguez'}
equipo1[2] = {2061867: 'Raul Fraustro'}

print(equipo1)

def capturarEstudiante():
    matricula = int(input('Ingrese matricula: '))
    nombre = input('Ingresa tu nombre')
    return dict({matricula:nombre})

equipo2 = {}
for _ in range(5):
    equipo2[_]=capturarEstudiante()
print(equipo2)