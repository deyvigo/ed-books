from flask import Blueprint

from controllers.book_genre import BookGenreController

book_genre_blueprint = Blueprint('book_genre', __name__)

@book_genre_blueprint.route('/book-genre', methods=['GET'])
def get_all_book_genre():
  return BookGenreController.get_all_book_genre()

@book_genre_blueprint.route('/book-genre', methods=['POST'])
def register_book_genre():
  return BookGenreController.regist_one_book_genre()

@book_genre_blueprint.route('/search/book/genre/<genre_name>', methods=['GET'])
def search_by_genre(genre_name):
  return BookGenreController.search_by_genre(genre_name)