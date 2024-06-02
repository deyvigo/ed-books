class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def esta_vacia(self):
        return self.tope is None

    def push(self, data):
        nuevo_nodo = Nodo(data)
        if self.esta_vacia():
            self.tope = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.tope
            self.tope = nuevo_nodo

    def pop(self):
        if self.esta_vacia():
            return None
        else:
            nodo_eliminado = self.tope
            self.tope = self.tope.siguiente
            return nodo_eliminado.data

    def ver_tope(self):
        if self.esta_vacia():
            return None
        else:
            return self.tope.data