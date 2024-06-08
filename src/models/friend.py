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


    def get_received_friends_requests(self,id):
        cursor = self.db.cursor()
        try:
            query = "SELECT * FROM friend WHERE is_accept = 0 AND id_receiver = %s;"
            cursor.execute(query, (id))
            response = cursor.fetchall()
            return { 'data': response }
        except:
            return { "error": "Error al consultar la tabla friend"} 
        finally:
            cursor.close()
            self.db.close()

    #Mostrar solicitudes de amistad
    def get_sent_friends_requests(self,id):
        cursor = self.db.cursor()
        try:
            query = "SELECT * FROM friend WHERE is_accept = 0 AND id_applicant = %s;"
            cursor.execute(query, (id))
            response = cursor.fetchall()
            return { 'data': response }
        except:
            return { "error": "Error al consultar la tabla friend"} 
        finally:
            cursor.close()
            self.db.close()

    #Mostrar amigos
    def get_all_friends(self,id):
        cursor = self.db.cursor()
        try:
            query = "SELECT * FROM friend WHERE is_accept = 1 AND (id_applicant = %s OR id_receiver=%s);"
            cursor.execute(query, (id,id))
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
            # Verificar si ya existe una solicitud de amistad con las mismas IDs
            query_check = "SELECT COUNT(*) FROM friend WHERE (id_applicant = %s AND id_receiver = %s) OR (id_applicant = %s AND id_receiver = %s);"
            cursor.execute(query_check, (id_applicant, id_receiver,id_receiver,id_applicant))
            result = cursor.fetchone()
            count = result["COUNT(*)"]            
            
            if count > 0:
                return { "error": "Ya existe una solicitud de amistad entre estos usuarios" }, 400
            
            # Si no existe, insertar la nueva solicitud de amistad
            query_insert = "INSERT INTO friend (id_applicant, id_receiver, is_accept) VALUES (%s, %s, %s);"
            cursor.execute(query_insert, (id_applicant, id_receiver, is_accept))
            self.db.commit()
            return { "message": "Solicitud de amistad enviada exitosamente" }, 200
        except IndexError as ie:
            print("Error al acceder al resultado de la consulta:", ie)
            return { "error": "Error al enviar solicitud de amistad" }, 500
        except:
            return { "error": "Error al enviar solicitud de amistad" }, 500
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
                action = "eliminar"
            else:
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