from utils.connection import Database
from flask import jsonify

class FriendModel:
    def __init__(self):
        self.db= Database().connection()
    
    def __del__(self):
        if self.db:
            self.db.close()
    
    #Mostrar solicitudes de amistad
    def get_all_friendRequest(self,id_receiver):
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
    def get_all_friend(self,id_applicant):
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


    #Enviar solicitud de amistad 
    def post_one_friendRequest(self, id_applicant, id_receiver, is_accept=0):
        cursor = self.db.cursor()
        try:
            query = "INSERT INTO friend ( id_applicant, id_receiver, is_accept) VALUE (%s,%s,%s);"
            cursor.execute(query, ( id_applicant, id_receiver, is_accept))
            print(id_applicant, id_receiver, is_accept)
            self.db.commit()
            return { "last_row_id": cursor.lastrowid, "rowcount": cursor.rowcount }, 200
        except:
            return { "error": "Error al enviar solicitud de amistad" },500