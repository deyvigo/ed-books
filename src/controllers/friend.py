from typing import Dict
from flask import request

from models import UserModel, FriendModel
from entity import Friend
from structures.GraphFriends import GraphFriends, ListaEnlazada, Nodo

class FriendController:
  @staticmethod
  def get_all_friends(id):
    response = FriendModel().get_all_friends(id)
    return response

  @staticmethod
  def get_all_friends_requests(id):
    response = FriendModel().get_all_friends_requests(id)
    return response
  
  @staticmethod
  def post_one_friends_requests():
    data = request.json
    response = FriendModel().post_one_friend_request(data.get("id_applicant"),data.get("id_receiver"))
    return response 
  
  @staticmethod
  def update_friend_status():
    data = request.json
    response = FriendModel().update_friend_status(data.get("id_applicant"),data.get("id_receiver"),data.get("is_accept"))
    return response 
  
  @staticmethod
  def get_list_friends(id):
    response = FriendModel().get_list_friends(id)
    return response 
  
  @staticmethod
  def get_list_friends_requests(id):
    response = FriendModel().get_list_friends_requests(id)
    return response
  
  @staticmethod
  def get_recomended_friends(id_user):
    users = UserModel().get_all_user().get("data")
    friends = FriendModel().get_all_friends_table()["data"]

    lista = ListaEnlazada()
    for friend_pair in friends:
      fpc = Friend(friend_pair["id_friend"], friend_pair["id_applicant"], friend_pair["id_receiver"], friend_pair["is_accept"])
      lista.add_nodo(Nodo(fpc))

    # only is_accept = 1 is for friends -1 and 0 is for states of request
    # lista.show_list()

    lista.delete_by_status([-1, 0])

    # print("Eliminados los -1 y 0")
    # lista.show_list()

    G = GraphFriends()

    for user in users:
      print(user["id_user"])
      G.add_node(user["id_user"])

    init = lista.init
    while (init != None):
      G.add_edge(init.data.id_applicant, init.data.id_receiver)
      init = init.next

    recommended_friends = G.recomended_friends(id_user)
    if not recommended_friends:
      return { "data": [] }, 200
    response = [user for user in users if user["id_user"] in recommended_friends]
    return { "data": response }, 200