from models.user import UserModel
from flask import jsonify, request

class UserController:
  @staticmethod
  def get_all_user():
    response = UserModel().get_all_user() # () en UserModel porque tiene un constructor
    return jsonify({ 'data': response })
  
  @staticmethod
  def regist_one_user():
    data = request.json
    print(data)
    response = UserModel().post_one_user(data.get('username'), data.get('password'), data.get('name'), data.get('last_name'))
    return response