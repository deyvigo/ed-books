from flask import Blueprint, request
from controllers.friend import FriendController

friend_blueprint = Blueprint('friend', __name__)

@friend_blueprint.route('/list/friends', methods=['GET'])
def get_friends():
   return FriendController.get_friends()

@friend_blueprint.route('/requests/received', methods=['GET'])
def get_received_friends_requests():
   return FriendController.get_received_friends_requests()

#TODO
@friend_blueprint.route('/requests/sent', methods=['GET'])
def get_sent_friends_requests():
   return FriendController.get_sent_friends_requests()

@friend_blueprint.route('/send/friends/requests', methods=['POST'])
def regist_friend_request():
  return FriendController.post_one_friends_requests()

@friend_blueprint.route('/update/request/friends', methods=['PUT', 'DELETE'])
def update_friend_status():
  return FriendController.update_friend_status()

# get friend request received in /requests/received
# @friend_blueprint.route('/list/request', methods=['GET'])
# def get_list_friends_requests():
#    id = request.args.get('id')
#    return FriendController.get_list_friends_requests(id)

@friend_blueprint.route('/friends/recommended', methods=['GET'])
def get_recommended_friends():
  return FriendController.get_recomended_friends()
