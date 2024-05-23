from utils.connection import Database
from flask import jsonify

class BookGenreModel:
  def __init__(self):
    self.db = Database().connection()
  
  def __del__(self):
    if self.db:
      self.db.close()

  def get_all_book_genre(self):
    cursor = self.db.cursor()
    try:
      cursor.execute("SELECT * FROM book_genre;")
      response = cursor.fetchall()
      return response
    except:
      return { "error": "Error al consultar la tabla book_genre" }

  def post_one_book_genre(self, id_book, id_genre):
    cursor = self.db.cursor()
    try:
      query = "INSERT INTO book_genre (id_book, id_genre) VALUE (%s, %s);"
      cursor.execute(query, (id_book, id_genre))
      self.db.commit()
      return { "last_row_id": cursor.lastrowid, "row_count": cursor.rowcount }, 200
    except:
      return { "error": "Error al crear en book_genre" }, 500
