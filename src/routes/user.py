from flask import Blueprint
from controllers.user import UserController

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user', methods=['GET'])
def get_all_user():
  return UserController.get_all_user()

@user_blueprint.route('/user', methods=['POST'])
def regist_user():
  return UserController.regist_one_user()