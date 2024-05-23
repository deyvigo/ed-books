from flask import Blueprint

from controllers.book_genre import BookGenreController

book_genre_blueprint = Blueprint('book_genre', __name__)

@book_genre_blueprint.route('/book-genre', methods=['GET'])
def get_all_book_genre():
  return BookGenreController.get_all_book_genre()

@book_genre_blueprint.route('/book-genre', methods=['POST'])
def register_book_genre():
  return BookGenreController.regist_one_book_genre()