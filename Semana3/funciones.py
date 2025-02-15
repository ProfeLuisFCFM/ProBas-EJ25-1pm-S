#Funcion global

def nombrefuncion(args1, args2, args3):
    text="Todo lo que tenga que hacer la función "+str(args1) 
    text+= " " + str(args2) + " " + str(args3)
    return text
    
#Función de clase, local

class Triangulo():
    def areaTriangulo(self, metodo, parametros):
        self.area = 0    
        if metodo == 1:
            self.area = (parametros['base'] * parametros['altura']) / 2 
        elif metodo == 2:
            x1, y1 = parametros['vertice1']
            x2, y2 = parametros['vertice2']
            x3, y3 = parametros['vertice3']
            self.area = 3**0.5 * abs((x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)) / 2
        elif metodo == 3:
            l1 = parametros['lado1']
            l2 = parametros['lado2']
            l3 = parametros['lado3']
            s = (l1 + l2 + l3) / 2
            self.area = (s * (s - l1) * (s - l2) * (s - l3))**0.5
        return self.area


# Funciones Lambda 

volTetra = lambda a: (2**0.5 / 12) * a**3





class Circulo():

    def __init__(self, angulos=0, rad=1 ):
        self.radio = rad
        self.angulos = angulos

    def sumarNumeros(self,*args):
        print(type(args))
        return sum(args)


if __name__ == '__main__':
    cir = Circulo()
    print(cir.sumarNumeros(1,2,3,4,5,6,7,8,9,10))
    #print("Función Global", nombrefuncion('uno',2,3.0))
    #Tri = Triangulo()
    #param1 = {'base': 1, 'altura': (3**0.5)/2}
    #print(Tri.areaTriangulo(1,param1))
    #param2 = {'vertice1': (0,0), 'vertice2': (0,1), 'vertice3': (0.5,(3**0.5)/2)}
    #print(Tri.areaTriangulo(2,param2))
    #param3 = {'lado1':1, 'lado2': 1, 'lado3': 1}
    #print(Tri.areaTriangulo(3,param3))
    #print("Lambda: ", volTetra(1),"cm3")


