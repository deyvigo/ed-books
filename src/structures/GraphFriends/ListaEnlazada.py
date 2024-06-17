from entity import Friend

class Nodo:
  def __init__(self, data: Friend) -> None:
    self.data = data
    self.next = None

class ListaEnlazada:
  def __init__(self) -> None:
    self.init = None
  
  def add_nodo(self, nodo: Nodo):
    if self.init == None:
      self.init = nodo
    else:
      track = self.init
      while (track.next != None):
        track = track.next

      track.next = nodo

  def show_list(self):
    if self.init == None:
      return
    track = self.init
    while (track != None):
      print(track.data.to_json())
      track = track.next

  def delete_by_status(self, to_delete: list[int]):
    track = self.init
    ant = track
    while (track != None):
      if track.data.is_accept in to_delete:
        # si es el primer elemento
        if track == ant:
          self.init = track.next
          track = self.init
          ant = track
          continue
        else:
          ant.next = track.next
          track = ant
      ant = track
      track = track.next
