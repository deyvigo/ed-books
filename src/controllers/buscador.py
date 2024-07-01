from structures.Buscador.buscador import Trie
from models import BookModel, UserModel

from flask import request

class BuscadorController:
  @staticmethod
  def search_by_prefix():
    body = request.json

    if "prefix" not in body:
      return { "message": "Prefix not found" }, 400
    
    prefix = body["prefix"]

    books = BookModel().get_all_book()["data"]
    users = UserModel().get_all_user()["data"]

    trie = Trie()
    map_items = {}

    for book in books:
      book["link"] = f"/main/libros/{book['id_book']}"
      map_items[book["name"].lower()] = book

    for user in users:
      user["link"] = f"/main/perfil/{user['id_user']}"
      map_items[user["name"].lower()] = user

    for name in map_items.keys():
      trie.insert(name)


    results = []

    nombres = trie.search(prefix.lower())
    results = [map_items[nombre] for nombre in nombres]

    return { "message": results }
