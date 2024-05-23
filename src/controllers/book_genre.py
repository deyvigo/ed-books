from flask import jsonify, request
from models.book_genre import BookGenreModel

class BookGenreController:
  @staticmethod
  def get_all_book_genre():
    response = BookGenreModel().get_all_book_genre()
    return jsonify({ 'data': response })

  @staticmethod
  def regist_one_book_genre():
    data = request.json
    response = BookGenreModel().post_one_book_genre(data.get("id_book"), data.get("id_genre"))
    return jsonify(response)