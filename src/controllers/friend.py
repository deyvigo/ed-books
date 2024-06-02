from models.friend import FriendModel
from flask import request

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