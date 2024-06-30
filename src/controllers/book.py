from flask import jsonify, request
from models.book import BookModel
from models.author import AuthorModel
from models.book_genre import BookGenreModel
from models.genre import GenreModel

class BookController:
  @staticmethod
  def get_all_book():
    response = BookModel().get_all_book()
    return response
  
  @staticmethod
  def get_one_book(id):
    response = BookModel().get_one_book(id)
    authors = AuthorModel().get_all_author()["data"]
    map_author = {}
    for author in authors:
      id_author = author["id_author"]
      if id_author not in map_author:
        map_author[id_author] = author

    book = response["data"]
    book["author"] = map_author[book["id_author"]]
    del book["id_author"]

    book_genres = BookGenreModel().get_all_book_genre()["data"]
    map_book_genres = {}
    for genre in book_genres:
      id_book = genre["id_book"]
      if id_book not in map_book_genres:
        map_book_genres[id_book] = []
      map_book_genres[id_book].append(genre)

    genres = GenreModel().get_all_genre()["data"]
    map_genres = {}
    for genre in genres:
      id_genre = genre["id_genre"]
      if id_genre not in map_genres:
        map_genres[id_genre] = genre


    id_genre = map_book_genres[book["id_book"]][0]["id_genre"]

    print(id_genre)

    book["genres"] = map_genres[id_genre]

    return response

  @staticmethod
  def regist_one_book():
    data = request.json
    response = BookModel().post_one_book(data.get('name'), data.get('author'), data.get('description'), data.get('url_img'))
    return response
