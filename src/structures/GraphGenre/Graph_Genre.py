from entity.Genre import Genre
from entity.Book import Book

class Node:
  def __init__(self, data: Genre | Book) -> None:
    self.data = data

  def __repr__(self) -> str:
    return self.data.__repr__()

class GraphGenre:
  def __init__(self) -> None:
    self.adjacency_list = {}

  def add_node(self, node: Node) -> None:
    if node not in self.adjacency_list:
      self.adjacency_list[node] = []
  
  def add_edge (self, book: Book, genre: Genre) -> None:
    if book in self.adjacency_list and genre in self.adjacency_list:
      self.adjacency_list[book].append(genre)
      self.adjacency_list[genre].append(book)
    else:
      print("Alguno de los nodos no existe.")

  def search_genre (self, genre_name):
    genre_node = None # <-- to Genre
    response = []

    for node in self.adjacency_list:
      if isinstance(node, Genre) and node.genre_name.lower() == genre_name:
        genre_node = node
        break
    
    if genre_node:
      # print(f"El genero {genre_node.genre_name} está en el grafo.")
      # print(f"Libros conectados")
      return self.adjacency_list[genre_node]
      # for book in self.adjacency_list[genre_node]:
      #   print(f"{book.to_json()}")
    else:
      return None