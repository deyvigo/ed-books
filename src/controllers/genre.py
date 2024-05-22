from flask import jsonify, request
from models.genre import GenreModel

class GenreController:
  @staticmethod
  def get_all_genre():
    response = GenreModel().get_all_genre()
    return jsonify({ 'data': response })

  @staticmethod
  def post_one_genre():
    data = request.json
    response = GenreModel().post_one_genre(data.get("genre_name"))
    return response
