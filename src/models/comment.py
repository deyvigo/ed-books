from utils.connection import Database

class CommentModel:
    def __init__(self):
      self.db= Database().connection()
    
    def __del__(self):
      if self.db:
        self.db.close()

    def get_all_comment_table(self):
      cursor = self.db.cursor()
      try:
        query = "SELECT * FROM comment;"
        cursor.execute(query)
        response = cursor.fetchall()
        return { "data": response }
      except:
        return { "error": "Error al consultar la tabla comment" }

    def post_one_comment(self, id_post, id_user_comment, comment):
        cursor = self.db.cursor()
        try:            
            query_insert = "INSERT INTO comment (id_post, id_user_comment, comment) VALUES (%s, %s, %s);"
            cursor.execute(query_insert, (id_post, id_user_comment, comment))
            self.db.commit()
            return { "message": "Comentario creado exitosamente" }, 200
        except Exception as e:
            return { "error": f"Error al crear comentario {e}" }, 500
    
    def delete_comment(self,id_comment):
        cursor = self.db.cursor()
        try:
            query = "DELETE FROM comment WHERE id_comment = %s"
            cursor.execute(query, (id_comment))
            self.db.commit()

            if cursor.rowcount == 0:
                return {"error": "No se encontró la comentario para eliminar"}, 404
            
            return {"message": "Comentario eliminado con éxito"}, 200

        except Exception as e:
            return {"error": "Error al eliminar comentario", "details": str(e)}, 500