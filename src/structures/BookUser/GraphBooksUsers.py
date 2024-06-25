from typing import Dict, Set, Tuple

class GraphBooksUses:
  def __init__(self) -> None:
    self.adjacency_list: Dict[str, list[str]] = {}

  # node = str(node_id + type)
  def add_node(self, node: str): 
    if node not in self.adjacency_list:
      self.adjacency_list[node] = []

  def add_edge(self, node_from: str, node_to: str):
    if node_from in self.adjacency_list and node_to in self.adjacency_list:
      self.adjacency_list[node_from].append(node_to)
      self.adjacency_list[node_to].append(node_from)
    else:
      print("Los nodos no están en el grafo")

  # list of ids if book that were liked
  def recomended_friend_by_book_liked_user(self, node_user: str):
    books_liked = self.adjacency_list[node_user]

    recommended_friends: Set[Tuple[str, str]] = set()
    already_recommended: Set[str] = set()

    for book in books_liked:
      users = self.adjacency_list[book]
      for user in users:
        if user not in already_recommended and user != node_user:
          recommended_friends.add((user, book))
          already_recommended.add(user)
    return recommended_friends
