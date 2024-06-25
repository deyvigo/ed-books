from flask import Blueprint

from controllers.book_user import BookUserController

book_user_blueprint = Blueprint("book_user", __name__)

@book_user_blueprint.route("/like/book", methods=["POST"])
def like():
  return BookUserController.like_one_book()

@book_user_blueprint.route("/likes/all", methods=["GET"])
def all_likes_books():
  return BookUserController.get_all_likes_books()

@book_user_blueprint.route("/unlike/book", methods=["DELETE"])
def unlike_book():
  return BookUserController.unlike_one_book()

