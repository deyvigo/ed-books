from typing import Dict
from entity import User

class GraphFriends:
  def __init__(self) -> None:
    self.adjacency_list: Dict[User, list[User]] = {}

  def add_node(self, node: User) -> None:
    if node not in self.adjacency_list:
      self.adjacency_list[node] = []

  def add_edge(self, user_one: User, user_two: User) -> None:
    if user_one in self.adjacency_list and user_two in self.adjacency_list:
      self.adjacency_list[user_one].append(user_two)
      self.adjacency_list[user_two].append(user_one)
    else:
      print("El usuario no está en el grafo.")

  def recomended_friends(self, username):
    user_node: User = None
    friends: list[User] = []
    recomended_friends: list[User] = []

    for user in self.adjacency_list:
      if user.username.lower() == username:
        user_node = user
        break

    # friends of username
    if user_node:
      friends = self.adjacency_list[user_node]
    
    for friend in friends:
      for f in self.adjacency_list[friend]:
        if f != user_node and f not in friends and f not in recomended_friends:
          recomended_friends.append(f)

    return recomended_friends