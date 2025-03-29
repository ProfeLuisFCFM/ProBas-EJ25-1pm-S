'''
#Formal
fichero = open("dirección","modo")
print("hola mundo",file=fichero)
fichero.close()
#Informal
with open("dirección","modo") as fichero:
    print("holamundo2",file=fichero)
print("prueba",file=fichero)



texto=""
with open("Semana9\\demo.txt","r") as f:
    texto = f.readline()
    
print(texto)

modos = ["w","r","a","wt","wb","rt","rb","at","ab"]
modosPlus = ["w+","r+","a+","wt+","wb+","rt+","rb+","at+","ab+"]


with open("Semana9\\demo.pia","w") as f:
    print("lorem ipsum",file=f)
'''

#a = 123
#b = 12.3
#c = "str"

#print(type(a),type(b),type(c))


