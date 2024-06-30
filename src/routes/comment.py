from flask import Blueprint
from controllers.comment import CommentController

comment_blueprint = Blueprint('comment', __name__)

@comment_blueprint.route('/comments/user', methods=['GET'])
def get_posts_user():
   return CommentController.get_all_comments_user()

@comment_blueprint.route('/comments/post', methods=['GET'])
def get_posts_book():
   return CommentController.get_all_comments_post()

@comment_blueprint.route('/comment/create', methods=['POST'])
def delete_post():
   return CommentController.post_one_comment()

@comment_blueprint.route('/comment/delete', methods=['DELETE'])
def create_post():
   return CommentController.delete_comment()

