from flask import jsonify, request
from models.author import AuthorModel

class AuthorController:
  @staticmethod
  def get_all_author():
    response = AuthorModel().get_all_author()
    return jsonify({ 'data': response })

  @staticmethod
  def post_one_author():
    data = request.json
    response = AuthorModel().post_one_author(data.get("name"))
    return response

