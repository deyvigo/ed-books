from utils.connection import Database
from structures.listaEnlazadaDoble import ListaDoble
from structures.ListaEnlazada import ListaEnlazada

class FriendModel:
    def __init__(self):
        self.db= Database().connection()
    
    def __del__(self):
        if self.db:
            self.db.close()
    
    #Mostrar solicitudes de amistad
    def get_all_friend(self):
        cursor = self.db.cursor()
        try:
            query = "SELECT * FROM friend;"
            cursor.execute(query)
            response = cursor.fetchall()
            return { 'data': response }
        except:
            return { "error": "Error al consultar la tabla friend"} 
        finally:
            cursor.close()
            self.db.close()

    #Enviar solicitud de amistad // is_accept =0 pendiente
    def post_one_friend_request(self, id_applicant, id_receiver, is_accept=0):
        cursor = self.db.cursor()
        try:            
            query_insert = "INSERT INTO friend (id_applicant, id_receiver, is_accept) VALUES (%s, %s, %s);"
            cursor.execute(query_insert, (id_applicant, id_receiver, is_accept))
            self.db.commit()
            return { "message": "Solicitud de amistad enviada exitosamente" }, 200
        except:
            return { "error": "Error al enviar solicitud de amistad" }, 500
        finally:
            cursor.close()
            self.db.close()

    def update_friend_status(self, id_applicant, id_receiver, is_accept):
        cursor = self.db.cursor()
        try:
            query = "UPDATE friend SET is_accept = %s WHERE id_applicant = %s AND id_receiver = %s"
            cursor.execute(query, (is_accept, id_applicant, id_receiver))
            action = "actualizar"
            self.db.commit()
            if cursor.rowcount == 0:
                return {"error": f"No hay peticion de amistad para {action}"}, 404
            return {"message": f"Peticion de amistad {action} con éxito"}, 200
        except Exception as e:
            return {"error": f"Error al {action} la peticion de amistad", "details": str(e)}, 500
        finally:
            cursor.close()
            self.db.close()
    
    def delete_friend(self, id_applicant, id_receiver):
        cursor = self.db.cursor()
        try:
            query = "DELETE FROM friend WHERE id_applicant = %s AND id_receiver = %s"
            cursor.execute(query, (id_applicant, id_receiver))
            self.db.commit()

            if cursor.rowcount == 0:
                return {"error": "No se encontró la petición de amistad para eliminar"}, 404
            
            return {"message": "Petición de amistad eliminada con éxito"}, 200

        except Exception as e:
            return {"error": "Error al eliminar la petición de amistad", "details": str(e)}, 500

        finally:
            cursor.close()
            self.db.close()