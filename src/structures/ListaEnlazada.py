class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, data):
        temp = self.head

        
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def viewData(self):
        requests= {"data":[]}
        tmp= self.head
        while(tmp!=None):
            element=tmp.data
            tmp=tmp.next
            requests["data"].append(element)
        return requests