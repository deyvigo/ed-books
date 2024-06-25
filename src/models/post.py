from utils.connection import Database

class PostModel:
    def __init__(self):
      self.db= Database().connection()
    
    def __del__(self):
      if self.db:
        self.db.close()

    def get_all_post_table(self):
      cursor = self.db.cursor()
      try:
        query = "SELECT * FROM post;"
        cursor.execute(query)
        response = cursor.fetchall()
        return { "data": response }
      except:
        return { "error": "Error al consultar la tabla post" }

    def post_one_post(self, id_user_post, id_book, content):
        cursor = self.db.cursor()
        try:            
            query_insert = "INSERT INTO post (id_user_post, id_book, content) VALUES (%s, %s, %s);"
            cursor.execute(query_insert, (id_user_post, id_book, content))
            self.db.commit()
            return { "message": "Solicitud de post creado exitosamente" }, 200
        except:
            return { "error": "Error al crear post" }, 500
    
    def delete_post(self,id_post):
        cursor = self.db.cursor()
        try:
            query = "DELETE FROM post WHERE id_post = %s"
            cursor.execute(query, (id_post))
            self.db.commit()

            if cursor.rowcount == 0:
                return {"error": "No se encontró la post para eliminar"}, 404
            
            return {"message": "Post eliminado con éxito"}, 200

        except Exception as e:
            return {"error": "Error al eliminar post", "details": str(e)}, 500