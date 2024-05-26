from flask import Blueprint,request
from controllers.friend import FriendController

friend_blueprint = Blueprint('friend', __name__)

@friend_blueprint.route('/friends', methods=['GET'])
def get_all_friends():
  id_applicant = request.args.get('id_applicant')
  if not id_applicant:
      return {"error": "id_applicant es requerido"}, 400
  try:
      id_applicant = int(id_applicant)
  except ValueError:
      return {"error": "id_applicant debe ser un entero"}, 400
  return FriendController.get_all_friends(id_applicant)

@friend_blueprint.route('/friends/Requests', methods=['GET'])
def get_all_friends_requests():
  id_receiver = request.args.get('id_receiver')
  if not id_receiver:
      return {"error": "id_receiver es requerido"}, 400
  try:
      id_receiver = int(id_receiver)
  except ValueError:
      return {"error": "id_receiver debe ser un entero"}, 400
  return FriendController.get_all_friends_requests(id_receiver)

@friend_blueprint.route('/friends/Requests', methods=['POST'])
def regist_friend_request():
  return FriendController.regist_one_friends_requests()

@friend_blueprint.route('/friends/Requests', methods=['POST'])
@friend_blueprint.route('/friends', methods=['POST'])
def update_friend_status():
  return FriendController.update_friend_status()