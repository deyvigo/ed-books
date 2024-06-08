from models.friend import FriendModel
from flask import request
from structures.listaEnlazadaDoble import ListaDoble
from structures.ListaEnlazada import ListaEnlazada

class FriendController:
  @staticmethod
  def get_all_friends():
    id = request.args.get('id')
    response = FriendModel().get_all_friends(id)
    return response

  @staticmethod
  def get_all_friends_requests():
    id = request.args.get('id')
    if not id:
        return {"error": "id es requerido"}, 400
    try:
        id = int(id)
    except ValueError:
        return {"error": "id debe ser un entero"}, 400
    response = FriendModel().get_received_friends_requests(id)
    return response
  
  @staticmethod
  def post_one_friends_requests():
    data = request.json
    response = FriendModel().post_one_friend_request(data.get("id_applicant"),data.get("id_receiver"))
    return response 
  
  @staticmethod
  def update_friend_status():
    data = request.json
    response = FriendModel().update_friend_status(data.get("id_applicant"),data.get("id_receiver"),data.get("is_accept"))
    return response 
  
  @staticmethod
  def get_friends():
    id = request.args.get('id')
    data = FriendModel().get_all_friends(id)
    friends = data['data']
    list_friends = ListaDoble()

    for friend in friends:
        if str(friend.get("id_applicant")) == str(id):
            friend_id = friend.get("id_receiver")
        else:
            friend_id = friend.get("id_applicant")
        list_friends.agregar_al_inicio({"id_friend":friend_id})
    data=list_friends.viewData()
    return data 
  
  @staticmethod
  def get_received_friends_requests():
    id = request.args.get('id')
    data= FriendModel().get_received_friends_requests(id)
    requests=data['data'] 
    list_requests= ListaEnlazada()

    for req in requests:
        if str(req.get("id_applicant")) == str(id):
            request_id = req.get("id_receiver")
        else:
            request_id = req.get("id_applicant")
        list_requests.append({"request_id":request_id})
    data=list_requests.viewData()
    return data
  
  @staticmethod
  def get_sent_friends_requests():
    id = request.args.get('id')
    data= FriendModel().get_sent_friends_requests(id)
    requests=data['data'] 
    list_requests= ListaEnlazada()

    for req in requests:
        if str(req.get("id_applicant")) == str(id):
            request_id = req.get("id_receiver")
        else:
            request_id = req.get("id_applicant")
        list_requests.append({"request_id":request_id})
    data=list_requests.viewData()
    return data