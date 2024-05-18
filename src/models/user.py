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
      cursor.execute("SELECT * FROM user;")
      response = cursor.fetchall()
      return response
    except:
      return jsonify({ "error": "Error al consultar la tabla user"})
    
  def post_one_user(self, username, password, name, last_name):
    cursor = self.db.cursor()
    try:
      query = "INSERT INTO user (username, password, name, last_name) VALUE (%s,%s,%s,%s);"
      cursor.execute(query, (username, password, name, last_name))
      self.db.commit()
      return jsonify({ "last_row_id": cursor.lastrowid, "rowcount": cursor.rowcount }), 200
    except:
      return jsonify({ "error": "Error al crear el usuario" }), 500
