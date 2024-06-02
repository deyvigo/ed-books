# Cola para las peticiones de amistad

class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def encolar(self, data):
        nuevo_nodo = Nodo(data)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            return None
        else:
            nodo_eliminado = self.primero
            self.primero = self.primero.siguiente
            return nodo_eliminado.data

    def ver_primero(self):
        if self.esta_vacia():
            return None
        else:
            return self.primero.data
