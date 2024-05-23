from utils.connection import Database
from flask import jsonify

class FriendModel:
    def __init__(self):
        self.db= Database().connection()
    
    def __del__(self):
        if self.db:
            self.db.close()
    
    #Mostrar solicitudes de amistad
    def get_all_friendRequest(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT * FROM friend WHERE is_accept = 0;")
            response = cursor.fetchall()
            return response
        except:
            return jsonify({ "error": "Error al consultar la tabla friend"})
        
        finally:
            cursor.close()
            self.db.close()

    #Enviar solicitud de amistad 
    def post_one_friendRequest(self, id_friend, id_applicant, id_receiver, is_accept=0):
        cursor = self.db.cursor()
        try:
            query = "INSERT INTO friend (id_friend, id_applicant, id_receiver, is_accept) VALUE (%s,%s,%s,%s);"
            cursor.execute(query, (id_friend, id_applicant, id_receiver, is_accept))
            print(id_friend, id_applicant, id_receiver, is_accept)
            self.db.commit()
            return jsonify({ "last_row_id": cursor.lastrowid, "rowcount": cursor.rowcount }), 200
        except:
            return jsonify({ "error": "Error al enviar solicitud de amistad" })