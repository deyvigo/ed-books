from utils.connection import Database
from flask import jsonify

class BookModel:
  def __init__(self):
    self.db = Database().connection()
  
  def __del__(self):
    if self.db:
      self.db.close()

  def get_all_book(self):
    cursor = self.db.cursor()
    try:
      cursor.execute("SELECT * FROM book;")
      response = cursor.fetchall()
      return { "data": response }
    except:
      return { "error": "Error al consultar la tabla book" }

  def post_one_book(self, name, id_author, description, url_img):
    cursor = self.db.cursor()
    try:
      query = "INSERT INTO book (name, id_author, description, url_img) VALUE (%s, %s, %s, %s);"
      cursor.execute(query, (name, id_author, description, url_img))
      self.db.commit()
      return { "last_row_id": cursor.lastrowid, "row_count": cursor.rowcount }, 200
    except:
      return { "error": "Error al crear el libro" }, 500

