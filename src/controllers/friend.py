from models.friend import FriendModel
from flask import request

class FriendController:
  @staticmethod
  def get_all_friend(id_applicant):
    response = FriendModel().get_all_friend(id_applicant)
    return response

  @staticmethod
  def get_all_friendRequest(id_applicant):
    response = FriendModel().get_all_friendRequest(id_applicant)
    return response
  
  @staticmethod
  def regist_one_friendRequest():
    data = request.json
    response = FriendModel().post_one_friendRequest(data.get("id_applicant"),data.get("id_receiver"))
    return response 