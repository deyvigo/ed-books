from models.user import UserModel
from flask import jsonify, request
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class UserController:
  @staticmethod
  def get_all_user():
    response = UserModel().get_all_user() # () en UserModel porque tiene un constructor
    return response

  @staticmethod
  def regist_one_user():
    data = request.json
    hash_pass = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
    response = UserModel().post_one_user(data.get('username'), hash_pass, data.get('name'))
    return response
  
