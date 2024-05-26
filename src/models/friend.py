from utils.connection import Database
from flask import jsonify

class FriendModel:
    def __init__(self):
        self.db= Database().connection()
    
    def __del__(self):
        if self.db:
            self.db.close()
    
    #Mostrar solicitudes de amistad
    def get_all_friends_requests(self,id_receiver):
        cursor = self.db.cursor()
        try:
            query = "SELECT * FROM friend WHERE is_accept = 0 AND id_receiver = %s;"
            cursor.execute(query, (id_receiver,))
            response = cursor.fetchall()
            return { 'data': response }
        except:
            return { "error": "Error al consultar la tabla friend"} 
        finally:
            cursor.close()
            self.db.close()

    #Mostrar amigos
    def get_all_friends(self,id_applicant):
        cursor = self.db.cursor()
        try:
            query = "SELECT * FROM friend WHERE is_accept = 1 AND id_applicant = %s;"
            cursor.execute(query, (id_applicant,))
            response = cursor.fetchall()
            return { 'data': response }
        except:
            return { "error": "Error al consultar la tabla friend"},500
        finally:
            cursor.close()
            self.db.close()


    #Enviar solicitud de amistad // is_accept =0 pendiente
    def post_one_friend_request(self, id_applicant, id_receiver, is_accept=0):
        cursor = self.db.cursor()
        try:
            query = "INSERT INTO friend ( id_applicant, id_receiver, is_accept) VALUE (%s,%s,%s);"
            cursor.execute(query, ( id_applicant, id_receiver, is_accept))
            print(id_applicant, id_receiver, is_accept)
            self.db.commit()
            return { "last_row_id": cursor.lastrowid, "rowcount": cursor.rowcount }, 200
        except:
            return { "error": "Error al enviar solicitud de amistad" },500
        finally:
            cursor.close()
            self.db.close()
    

    #Actualizar estado de la peticion de amistad // is_accept=-1 (Rechazado)  =0 (pendiente) =1 (aceptado)
    def update_friend_status(self, id_applicant, id_receiver, is_accept):
        cursor = self.db.cursor()
        try:
            if is_accept == -1:
                query = "DELETE FROM friend WHERE id_applicant = %s AND id_receiver = %s;"
                cursor.execute(query, (id_applicant, id_receiver))
                action = "eliminada"
            else:
                query = "UPDATE friend SET is_accept = %s WHERE id_applicant = %s AND id_receiver = %s AND is_accept = 0;"
                cursor.execute(query, (is_accept, id_applicant, id_receiver))
                action = "actualizada"
            self.db.commit()
            if cursor.rowcount == 0:
                return {"error": f"No hay peticion de amistad para {action}"}, 404
            return {"message": f"Peticion de amistad {action} con éxito"}, 200
        except Exception as e:
            return {"error": f"Error al {action} la peticion de amistad", "details": str(e)}, 500
        finally:
            cursor.close()
            self.db.close()