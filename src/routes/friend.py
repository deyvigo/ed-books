from flask import Blueprint, request
from controllers.friend import FriendController

friend_blueprint = Blueprint('friend', __name__)

@friend_blueprint.route('/friends', methods=['GET'])
def get_all_friends():
  id = request.args.get('id')
  if not id:
      return {"error": "id es requerido"}, 400
  try:
      id = int(id)
  except ValueError:
      return {"error": "id debe ser un entero"}, 400
  return FriendController.get_all_friends(id)

@friend_blueprint.route('/friends/requests', methods=['GET'])
def get_all_friends_requests():
  id = request.args.get('id')
  if not id:
      return {"error": "id es requerido"}, 400
  try:
      id = int(id)
  except ValueError:
      return {"error": "id debe ser un entero"}, 400
  return FriendController.get_all_friends_requests(id)

@friend_blueprint.route('/friends/requests', methods=['POST'])
def regist_friend_request():
  return FriendController.post_one_friends_requests()

@friend_blueprint.route('/friends/update', methods=['POST'])
@friend_blueprint.route('/friends', methods=['POST'])
def update_friend_status():
  return FriendController.update_friend_status()

@friend_blueprint.route('/list', methods=['GET'])
def get_list_friends():
   id = request.args.get('id')
   return FriendController.get_list_friends(id)

@friend_blueprint.route('/list/request', methods=['GET'])
def get_list_friends_requests():
   id = request.args.get('id')
   return FriendController.get_list_friends_requests(id)

@friend_blueprint.route('/friends/recommended/<username>', methods=['GET'])
def get_recommended_friends(username):
  return FriendController.get_recomended_friends(username.lower())