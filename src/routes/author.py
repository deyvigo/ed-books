from flask import Blueprint
from controllers.author import AuthorController

author_blueprint = Blueprint('author', __name__)

@author_blueprint.route('/author', methods=['GET'])
def get_all_author():
  return AuthorController.get_all_author()

@author_blueprint.route('/author', methods=['POST'])
def post_one_author():
  return AuthorController.post_one_author()