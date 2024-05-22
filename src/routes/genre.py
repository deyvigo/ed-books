from flask import Blueprint
from controllers.genre import GenreController

genre_blueprint = Blueprint('genre', __name__)

@genre_blueprint.route('/genre', methods=['GET'])
def get_all_genre():
  return GenreController.get_all_genre()

@genre_blueprint.route('/genre', methods=['POST'])
def post_one_genre():
  return GenreController.post_one_genre()