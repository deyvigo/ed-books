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

  def search(self, id_user, id_book):
    track = self.head
    while (track != None):
      if track.data["id_user"] == id_user and track.data["id_book"] == id_book:
        return track.data["id_book_user"]
      track = track.next
    return None