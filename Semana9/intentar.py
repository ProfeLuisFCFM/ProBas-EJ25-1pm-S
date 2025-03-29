
class Discriminante():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def calculo1(self):
        try:
            div = self.a/self.c
            return div
        except Exception as e:
            print(f"error: {e}")
            return 1
    
    def calculo2(self):
        if self.c == 0:
            raise ZeroDivisionError("Error de división")


d = Discriminante(7,2,0)

print(d.calculo1())

try: 
    print(d.calculo2())
except Exception as ex:
    print(f"Error {ex}")