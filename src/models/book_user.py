from utils.connection import Database

class BookUserModel:
  def __init__(self) -> None:
    self.db = Database().connection()

  def __del__(self) -> None:
    if self.db:
      self.db.close()
    
  def get_all_likes_book(self):
    cursor = self.db.cursor()
    try:
      sql = "SELECT id_book_user, id_user, id_book FROM book_user;"
      cursor.execute(sql)
      response = cursor.fetchall()
      return { "data": response }, 200
    except Exception as e:
      return { "error": "Error al consultar la tabla book_user", "details": e }, 500
    
  def post_one_like_book(self, id_user, id_book):
    cursor = self.db.cursor()
    try:
      sql = "INSERT INTO book_user (id_book, id_user) VALUES (%s, %s);"
      cursor.execute(sql, (id_book, id_user))
      self.db.commit()
      return { "last_row_id": cursor.lastrowid, "row_count": cursor.rowcount }, 200
    except Exception as e:
      return { "error": "Error al consultar la tabla book_user", "details": e }, 500
    
  def delete_by_id(self, id_book_user):
    cursor = self.db.cursor()
    try:
      sql = "DELETE FROM book_user WHERE id_book_user = %s;"
      cursor.execute(sql, (id_book_user,))
      self.db.commit()
      if cursor.rowcount == 0:
        return { "error": "No se encontró el like al libro solicitado" }, 404
      return { "message": "like eliminado exitosamente" }, 200
    except Exception as e:
      return { "error": "Error al eliminar de la tabla book_user" }, 500