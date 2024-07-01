from entity.Friend import Friend

class Node:
  def __init__(self, data: Friend) -> None:
    self.data = data
    self.next = None

class ListaEnlazada:
  def __init__(self) -> None:
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def search(self, data: int):
    current = self.head
    to_return = set()
    while current:
      if current.data.id_applicant == data and current.data.is_accept == 1:
        to_return.add(current.data.id_receiver)
      if current.data.id_receiver == data and current.data.is_accept == 1:
        to_return.add(current.data.id_applicant)
      current = current.next
    return to_return