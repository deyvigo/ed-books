from flask import Blueprint
from controllers.user import UserController

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user', methods=['GET'])
def get_all_user():
  return UserController.get_all_user()

@user_blueprint.route('/user/<int:id>', methods=['GET'])
def get_one_user(id):
  return UserController.get_one_user(id)

@user_blueprint.route('/user', methods=['POST'])
def regist_user():
  return UserController.regist_one_user()

@user_blueprint.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
  return UserController.delete_one_user(id)

@user_blueprint.route('/user<int:id>', methods=['PUT'])
def update_user(id):
  return UserController.update_one_user(id)
