from typing import Dict
from flask import request

from models import UserModel, FriendModel
from entity import User
from structures.GraphFriends.Graph_Friends import GraphFriends

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
  def get_recomended_friends(username):
    users = UserModel().get_all_user().get("data")

    users_dict: Dict[str, User] = {}
    G = GraphFriends()

    for user in users:
      key = user.get("id_username") # <- id_username es unico
      uc = User(user.get("id_user"), user.get("name"), user.get("username"), user.get("password"))

      if key not in users_dict:
        users_dict[username] = uc

      G.add_node(uc)

    friends = FriendModel().get_all_friends_table().get("data")

    # TODO: delete all friends by state not friends (-1 or 0)

    for pair in friends:
      user_one = users_dict[pair.get("id_applicant")]
      user_two = users_dict[pair.get("id_receiver")]
      G.add_edge(user_one, user_two)
    
    return { "data": friends }