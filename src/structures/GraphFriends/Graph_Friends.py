from typing import Dict

class GraphFriends:
  def __init__(self) -> None:
    self.adjacency_list: Dict[int, list[int]] = {}

  def add_node(self, node: int) -> None:
    if node not in self.adjacency_list:
      self.adjacency_list[node] = []

  def add_edge(self, user_one: int, user_two: int) -> None:
    if user_one in self.adjacency_list and user_two in self.adjacency_list:
      self.adjacency_list[user_one].append(user_two)
      self.adjacency_list[user_two].append(user_one)
    else:
      print("El usuario no está en el grafo.")

  def recomended_friends(self, id_user):
    friends = self.adjacency_list[int(id_user)]

    if not friends:
      return None

    recommended_friends = {}

    for friend in friends:
      friends_of_friend = self.adjacency_list[friend]
      for fr in friends_of_friend:
        if fr != int(id_user) and fr not in friends:
          if fr not in recommended_friends:
            recommended_friends[fr] = len(set(self.adjacency_list[int(fr)]) & set(self.adjacency_list[int(id_user)]))

    return recommended_friends