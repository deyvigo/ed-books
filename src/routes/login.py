from flask import Blueprint
from controllers.login import LoginController
from flask_jwt_extended import create_access_token

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
  user, status_code = LoginController.login()

  if user.get('error'):
    return {"error": user.get('error')}, status_code
  
  access_token = create_access_token(identity={"username" : user.get('username')})
  user['access_token'] = access_token

  return user , status_code
