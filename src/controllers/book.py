from flask import jsonify, request
from models.book import BookModel

class BookController:
  @staticmethod
  def get_all_book():
    response = BookModel().get_all_book()
    return jsonify({ 'data': response })

  @staticmethod
  def regist_one_book():
    data = request.json
    response = BookModel().post_one_book(data.get('autor'), data.get('description'), data.get('url_img'))
    return response
