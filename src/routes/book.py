from flask import Blueprint

from controllers.book import BookController


book_blueprint = Blueprint('book', __name__)

@book_blueprint.route('/book', methods=['GET'])
def get_all_book():
  return BookController.get_all_book()

@book_blueprint.route('/book', methods=['POST'])
def register_book():
  return BookController.regist_one_book()
