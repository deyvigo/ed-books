from flask import Blueprint
from controllers.post import PostController

post_blueprint = Blueprint('post', __name__)

@post_blueprint.route('/posts/user', methods=['GET'])
def get_posts_user():
   return PostController.get_all_posts_user()

@post_blueprint.route('/posts/book', methods=['GET'])
def get_posts_book():
   return PostController.get_all_posts_books()

@post_blueprint.route('/post/create', methods=['POST'])
def delete_post():
   return PostController.post_one_post()

@post_blueprint.route('/post/delete', methods=['POST'])
def create_post():
   return PostController.delete_post()

