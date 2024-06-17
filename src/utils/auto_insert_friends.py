from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

import json

import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from models import UserModel, FriendModel

with open("src/mocks/users.json", "r", encoding="ISO-8859-1") as file:
  users_data = json.load(file)

for user_data in users_data:
  UserModel().post_one_user(user_data["username"], bcrypt.generate_password_hash(user_data["password"]).decode('utf-8'), user_data["name"])

# is_accept
# 1 = accept
# 0 = pendiente
# -1 = rechazado

with open("src/mocks/friend.json", "r", encoding="ISO-8859-1") as file:
  friends_data = json.load(file)

for friend_data in friends_data:
  FriendModel().post_one_friend_request(friend_data["id_applicant"], friend_data["id_receiver"], friend_data["is_accept"])
