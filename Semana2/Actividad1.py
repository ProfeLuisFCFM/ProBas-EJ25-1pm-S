# Ciclos

#For es una cantidad de iteraciones predefinidas
#While, debemos tener miedo y respeto

Otravariable = [0,1,1,2,3,5,8,13,21,34,55,89,144]

for variable in Otravariable:
    print(variable)

#ctrlñctrl = bool(input(""))
from random import randint
sentinel = True
mensajes = ["estás seguro","estás advertidp?", "Borrando historial de chrome"]

while sentinel:
    print("1. Hola!\n2. Genera un número aleatorio:\n3.Salir")
    op = int(input("Opción: "))
    if op == 1:
        print("Hola guapa!")
    elif op == 2:
        print("Tu numero es", randint(1,100))
    else: 
        print("Adios")
        sentinel = False
        break



#ayudaa = bool(1)
#while ayudaa: 
#    print("Ten Ten ten")



lista1 = []
lista2 = list()


lista1.append(12)
lista1.append(None)
lista1.clear()  #[]
lista1.copy() 

lista2 = lista1.copy() 

lista2.append("Cola")

lista1.count()
lista1.extend(lista2)

lista2 = lista2 + lista1

lista1 = [1,2,3,4,5,6,7,8,9,10,6]

lista1.index(6)
lista1.pop()
lista1.remove("\n")
lista1.reverse() #Hola aloH
lista2.sort() #ordena la lista 

sum()
max()
min()
abs()
