from flask import Blueprint
from controllers.friend import FriendController

friend_blueprint = Blueprint('friend', __name__)

@friend_blueprint.route('/friends', methods=['GET'])
def get_all_friend():
  id_applicant = request.args.get('id_applicant')
  if not id_applicant:
      return {"error": "id_applicant is required"}, 400
  try:
      id_applicant = int(id_applicant)
  except ValueError:
      return {"error": "id_applicant must be an integer"}, 400
  return FriendController.get_all_friend(id_applicant)

@friend_blueprint.route('/friendRequests', methods=['GET'])
def get_all_friendRequest():
  id_applicant = request.args.get('id_applicant')
  if not id_applicant:
      return {"error": "id_applicant is required"}, 400
  try:
      id_applicant = int(id_applicant)
  except ValueError:
      return {"error": "id_applicant must be an integer"}, 400
  return FriendController.get_all_friendRequest()

@friend_blueprint.route('/friendRequest', methods=['POST'])
def regist_friendResquest():
  return FriendController.regist_one_friendRequest()