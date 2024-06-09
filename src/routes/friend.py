from flask import Blueprint,request
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

@friend_blueprint.route('/friends/update', methods=['POST'])
@friend_blueprint.route('/friends', methods=['POST'])
def update_friend_status():
  return FriendController.update_friend_status()
