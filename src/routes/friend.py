from flask import Blueprint
from controllers.friend import FriendController

friend_blueprint = Blueprint('friend', __name__)

@friend_blueprint.route('/friend', methods=['GET'])
def get_all_friend():
  return FriendController.get_all_friend()

@friend_blueprint.route('/friendRequest', methods=['GET'])
def get_all_friendRequest():
  return FriendController.get_all_friendRequest()

@friend_blueprint.route('/friendRequest', methods=['POST'])
def regist_friendResquest():
  return FriendController.regist_one_friendRequest()