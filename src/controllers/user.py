from models.user import UserModel
from flask import request
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class UserController:
  @staticmethod
  def get_all_user():
    response = UserModel().get_all_user() # () en UserModel porque tiene un constructor
    return response
  
  @staticmethod
  def get_one_user(id):
    response = UserModel().get_one_user(id)
    return response

  @staticmethod
  def regist_one_user():
    data = request.json
    user = UserModel().get_one_user(data.get('username'))
    
    if user.get('data') is not None:
      return { "error": "El usuario ya existe" }, 400
    
    # hasheo de contraseña
    hash_pass = bcrypt.generate_password_hash(data.get('password'), 10).decode('utf-8')
    response = UserModel().post_one_user(data.get('username'), hash_pass, data.get('name'))
    return response
  
  @staticmethod
  def delete_one_user(id):
    response = UserModel().delete_one_user(id)
    return response

  @staticmethod
  def update_one_user(id):
    data = request.json

    if not data:
      return { "error": "Datos no enviados" }, 400

    hash_pass = bcrypt.generate_password_hash(data.get('password'), 10).decode('utf-8')

    response = UserModel().update_one_user(id, hash_pass, data.get('name'))
    return response

