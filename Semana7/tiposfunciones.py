# funciones normales -> Funciones Globales
# fucniones de clase -> Funciones Locales
# funciones lambda -> Funciones en linea

def Nomfunct(args):
    return False

def Discriminante(a,b,c,z=0):
    return b**2 - 4*a*c

def FormulaGeneral(a,b,c):
    d = Discriminante(a,b,c)
    if d > 0:
        x1 = (-b + d**0.5)/2*a
        x2 = (-b - d**0.5)/2*a
    elif d == 0:
        x1 = x2 = -b/2*a
    else:
        x1 = (-b + ((-1*d)**0.5*complex('0+1j')))/2*a
        x2 = (-b - ((-1*d)**0.5*complex('0+1j')))/2*a
    return x1,x2

#print(FormulaGeneral(1,2,1),"caso d=0")
#print(FormulaGeneral(1,4,1),"caso d>0")
#print(FormulaGeneral(1,1,1),"caso d<0")

### Funciones Locales

#class NombreClass(MamaClass):
#    def __init__(self):
#        pass

class Persona():
    def __init__(self,Nombre,ApPaterno,ApMaterno,FechaNac):
        self.Nombre = Nombre
        self.ApPaterno = ApPaterno
        self.ApMaterno = ApMaterno
        self.FechaNac = FechaNac
    
    def setFecha(self, fecha):
        self.FechaNac = fecha

class CURP(Persona):
    def __init__(self, Nombre, ApPaterno, ApMaterno, FechaNac,Edo,Genero,CVUnica):
        super().__init__(Nombre, ApPaterno, ApMaterno, FechaNac)
        self.Edo = Edo 
        self.Genero = Genero
        self.CVunica = CVUnica

    def GenCURP(Self):
        return 'GURL930316HNLTSD08'
        

Luis = CURP('Luis','Gutierrez','Rodriguez',16031993,'NL','H','08')

Luis.setFecha(15032025)

#print(Luis.GenCURP())

Jaime = Persona('Jaime','Cisneros','Carrizales',19091999)





#### Funciones en línea

discriminante = lambda b,c,a=10: b**2 - 4*a*c
import tiposfunciones as fdp
if __name__ =='__main__':
    print(discriminante(1,1,1))
    print(FormulaGeneral(1,2,1),"caso d=0")
    print(FormulaGeneral(1,4,1),"caso d>0")
    print(FormulaGeneral(1,1,1),"caso d<0")