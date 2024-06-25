from flask import request
from models import BookUserModel
from structures.BookUser.ListaEnlazada import ListaEnlazada

class BookUserController:
  @staticmethod
  def like_one_book():
    id_user = request.json["id_user"]
    id_book = request.json["id_book"]

    if id_user == None or id_book == None:
      return { "error": "id_user, id_book son requeridos" }, 400

    # si ya existe
    all_likes = BookUserModel().get_all_likes_book()[0]["data"]
    lista_all_likes = ListaEnlazada()

    for al in all_likes:
      lista_all_likes.append(al)

    exists = lista_all_likes.search(id_user, id_book)

    if exists != None:
      return { "message": "Ya se dio like a este libro" }, 200

    response = BookUserModel().post_one_like_book(id_user, id_book)
    return response
  
  @staticmethod
  def unlike_one_book():
    id_user = request.json["id_user"]
    id_book = request.json["id_book"]

    if id_user == None or id_book == None:
      return { "error": "id_user, id_book son requeridos" }, 400
    
    all_likes = BookUserModel().get_all_likes_book()[0]["data"]
    lista_all_likes = ListaEnlazada()

    for al in all_likes:
      lista_all_likes.append(al)

    id_like_to_delete = lista_all_likes.search(id_user, id_book)
    
    if id_like_to_delete == None:
      return { "error": "No se ha encontrado un registro para eliminar" }, 404

    response = BookUserModel().delete_by_id(id_like_to_delete)
    return response

  @staticmethod
  def get_all_likes_books():
    response = BookUserModel().get_all_likes_book()
    return response