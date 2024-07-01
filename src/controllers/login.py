
from flask import request
from flask_bcrypt import Bcrypt
from models.user import UserModel

bcrypt = Bcrypt()

class LoginController:
  @staticmethod
  def login():
    data = request.json
    if not data:
        return {"error": "Datos no enviados"}, 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return {"error": "Nombre de usuario o contraseña no proporcionados"}, 400

    user = UserModel().get_one_user(username).get('data')
    if not user:
        return {"error": "Usuario no encontrado"}, 404

    isValid = bcrypt.check_password_hash(user.get('password'), password)

    if not isValid:
      return {"error": "Contraseña incorrecta"}, 400

    return {
        "id_user": user.get('id_user'),
        "username": user.get('username'),
        "name": user.get('name')
    }, 200
