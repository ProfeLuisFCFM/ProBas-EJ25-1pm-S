
class nodo:
    def __init__(self,datos, anterior=None, posterior=None):
        self.Dato = datos
        self.anterior = None
        self.siguiente = None

    Lista = []

uno = nodo('Luis')
dos = nodo('Angel')
dos.anterior = uno
uno.siguiente = dos



