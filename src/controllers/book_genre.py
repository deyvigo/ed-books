from typing import Dict
from flask import jsonify, request
from models.book_genre import BookGenreModel

from entity import Author, Book, Genre
from models import BookModel, AuthorModel, GenreModel
from structures.GraphGenre.Graph_Genre import *
from structures.GraphGenre.hash import hash

class BookGenreController:
  @staticmethod
  def get_all_book_genre():
    response = BookGenreModel().get_all_book_genre()
    return response

  @staticmethod
  def regist_one_book_genre():
    data = request.json
    response = BookGenreModel().post_one_book_genre(data.get("id_book"), data.get("id_genre"))
    return response
  
  @staticmethod
  def search_by_genre(genre_name):
    genres = GenreModel().get_all_genre().get("data")
    authors = AuthorModel().get_all_author().get("data")
    books = BookModel().get_all_book().get("data")
    books_genres = BookGenreModel().get_all_book_genre().get("data")

    genres_dict: Dict[str, Genre] = {}
    authors_dict: Dict[str, Author] = {}
    books_dict: Dict[str, Book] = {}

    for genre in genres:
      key = genre.get("id_genre")
      if key not in genres_dict:
        gc = Genre(genre.get("genre_name"), genre.get("id_genre"))
        genres_dict[key] = gc

    for author in authors:
      key = author.get("id_author")
      if key not in authors_dict:
        ac = Author(author.get("name"), author.get("id_author"))
        authors_dict[key] = ac

    for book in books:
      key = book.get("id_book")
      if key not in books_dict:
        bc = Book(book.get("id_book"), book.get("name"), book.get("description"), book.get("url_img"))
        bc.author.append(authors_dict[book.get("id_author")])
        books_dict[key] = bc

    for bg in books_genres:
      books_dict[bg.get("id_book")].genres.append(genres_dict[bg.get("id_genre")])

    # creacion del grafo

    G = GraphGenre()
    for g in genres_dict:
      G.add_node(genres_dict[g])

    for b in books_dict:
      G.add_node(books_dict[b])

    for bg in books_genres:
      G.add_edge(books_dict[bg.get("id_book")], genres_dict[bg.get("id_genre")])

    data = G.search_genre(genre_name.lower())

    if data:
      response = [b.to_json() for b in data]
      return { "books": response }, 200
    else:
      return { "books": [] }, 200
  