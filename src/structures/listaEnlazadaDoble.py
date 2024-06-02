class Nodo:
    def __init__(self, data):
        self.data= data
        self.sgte = None
        self.ant = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_al_inicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.sgte = self.cabeza
            self.cabeza.ant = nuevo_nodo
            self.cabeza = nuevo_nodo

    def agregar_al_final(self, data):
        nuevo_nodo = Nodo(data)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.ant = self.cola
            self.cola.sgte = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar_del_inicio(self):
        if self.esta_vacia():
            return None
        nodo_eliminado = self.data
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cabeza = self.cabeza.sgte
            self.cabeza.ant = None
        return nodo_eliminado.data

    def eliminar_del_final(self):
        if self.esta_vacia():
            return None
        nodo_eliminado = self.cola
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cola = self.cola.ant
            self.cola.sgte = None
        return nodo_eliminado.data
    
    def viewData(self):
        requests= {"data":[]}
        tmp= self.cabeza
        while(tmp!=None):
            element=tmp.data
            tmp=tmp.sgte
            requests["data"].append(element)
        return requests
