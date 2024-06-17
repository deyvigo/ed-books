from flask import Blueprint, request
from controllers.friend import FriendController

friend_blueprint = Blueprint('friend', __name__)

@friend_blueprint.route('/friends', methods=['GET'])
def get_friends():
   return FriendController.get_friends()

@friend_blueprint.route('/requests/received', methods=['GET'])
def get_received_friends_requests():
   return FriendController.get_received_friends_requests()

@friend_blueprint.route('/requests/sent', methods=['GET'])
def get_sent_friends_requests():
   return FriendController.get_sent_friends_requests()

@friend_blueprint.route('/friends/requests', methods=['POST'])
def regist_friend_request():
  return FriendController.post_one_friends_requests()

#TODO
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

@friend_blueprint.route('/friends/recommended/<id_user>', methods=['GET'])
def get_recommended_friends(id_user):
  return FriendController.get_recomended_friends(id_user)
