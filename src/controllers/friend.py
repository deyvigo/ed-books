from models.friend import FriendModel
from flask import jsonify, request

class FriendController:
  @staticmethod
  def get_all_friend():
    response = FriendModel().get_all_friend()
    return response

  @staticmethod
  def get_all_friendRequest():
    response = FriendModel().get_all_friendRequest()
    return response
  
  @staticmethod
  def regist_one_friendRequest():
    data = request.json
    response = FriendModel().post_one_friendRequest(data.get("id_applicant"),data.get("id_receiver"))
    return response 