from entity.User import User
from utils.connection import Database
from flask import jsonify

class UserModel:
  def __init__(self):
    self.db = Database().connection()

  def __del__(self):
    if self.db:
      self.db.close()

  def get_all_user(self):
    cursor = self.db.cursor()
    try:
      cursor.execute("SELECT id_user, name, username FROM user;")
      response = cursor.fetchall()
      return { "data": response }
    except:
      return { "error": "Error al consultar la tabla user" } # <-- devolver objeto no json

  def get_one_user(self, username):
    cursor = self.db.cursor()
    try:
      query = "SELECT * FROM user WHERE username = %s;"
      cursor.execute(query, (username,))
      response = cursor.fetchone()
      return { "data": response}
    except:
      return { "error": "Error al consultar la tabla user" }

  def post_one_user(self, username, password, name):
    cursor = self.db.cursor()
    try:
      query = "INSERT INTO user (username, password, name) VALUE (%s,%s,%s);"
      cursor.execute(query, (username, password, name))
      self.db.commit()
      return { "last_row_id": cursor.lastrowid, "row_count": cursor.rowcount }, 200
    except:
      return { "error": "Error al crear el usuario" }, 500

  def delete_one_user(self, id):
    cursor = self.db.cursor()
    try:
      query = "DELETE FROM user WHERE id_user = %s;"
      cursor.execute(query, (id,))
      self.db.commit()
      return { "row_count": cursor.rowcount }, 200
    except:
      return { "error": "Error al eliminar el usuario" }, 500
  
  def update_one_user(self, id, password, name):
    cursor = self.db.cursor()
    try:
      query = "UPDATE user SET password = %s, name = %s WHERE id_user = %s;"
      cursor.execute(query, (password, name, id))
      self.db.commit()
      return { "row_count": cursor.rowcount }, 200
    except:
      return { "error": "Error al actualizar el usuario" }, 500

