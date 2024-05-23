from utils.connection import Database
from flask import jsonify

class GenreModel:
  def __init__(self):
    self.db = Database().connection()

  def __del__(self):
    if self.db:
      self.db.close()
  
  def get_all_genre(self):
    cursor = self.db.cursor()
    try:
      cursor.execute("SELECT * FROM genre;")
      response = cursor.fetchall()
      return { "data": response }
    except:
      return { "error": "Error al consultar la tabla genre" }
    
  def post_one_genre(self, name):
    cursor = self.db.cursor()
    try:
      query = "INSERT INTO genre (genre_name) VALUE (%s);"
      cursor.execute(query, (name))
      self.db.commit()
      return { "last_row_id": cursor.lastrowid, "row_count": cursor.rowcount }, 200
    except:
      return { "error": "Error al crear el libro" }, 500
