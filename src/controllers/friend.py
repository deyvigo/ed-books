from flask import request
from structures.listaEnlazadaDoble import ListaDoble
from structures.ListaEnlazada import ListaEnlazada as LE

from models import UserModel, FriendModel
from entity import Friend
from structures.GraphFriends import GraphFriends, ListaEnlazada, Nodo

class FriendController:
  @staticmethod
  def post_one_friends_requests():
    data = request.json
    id_applicant=data.get("id_applicant")
    id_receiver=data.get("id_receiver")
    dataFriend = FriendModel().get_all_friend()
    friends = dataFriend['data']
    cont=0

    if id_applicant is None or id_receiver is None :
      return {"error": "id_applicant y id_receiver son requeridos"}, 400

    for friend in friends:
      if (friend.get("id_applicant") == id_applicant and friend.get("id_receiver") == id_receiver) or (friend.get("id_applicant") == id_receiver and friend.get("id_receiver") == id_applicant):
        cont+=1
    if(cont==0):
       response = FriendModel().post_one_friend_request(data.get("id_applicant"),data.get("id_receiver"))
    else:
       return { "error": "Ya existe una solicitud de amistad entre estos usuarios" }, 400
    return response 
  
  #Actualizar estado de la peticion de amistad // is_accept=-1 (Rechazado)  =0 (pendiente) =1 (aceptado)
  @staticmethod
  def update_friend_status():
    data = request.json
    id_friend = data.get("id_friend") # id of friend request

    if id_friend is None:
      return { "error": "id_friend son requeridos" }, 400

    if request.method == "DELETE":
      response = FriendModel().delete_friend(id_friend)
    elif request.method == "PUT":
      response = FriendModel().update_friend_status(id_friend)
    else:
      { "error": f"Error al actualizar la peticion de amistad" }, 500
    return response 
  
  @staticmethod
  def get_friends():
    id = request.args.get('id')

    if id is None:
      return {"error": "id es requerido"}, 400
    
    data = FriendModel().get_all_friend()
    users = UserModel().get_all_user()["data"]
    map_users = {}
    friends = data['data']
    list_friends = ListaDoble()

    for user in users:
      map_users[user["id_user"]] = user

    for friend in friends:
      if (str(friend.get("id_applicant")) == str(id) or str(friend.get("id_receiver")) == str(id)) and str(friend.get("is_accept")) == str(1):
        if str(friend.get("id_applicant")) == str(id):
          friend_id = friend.get("id_receiver")
        else:
          friend_id = friend.get("id_applicant")
        list_friends.agregar_al_inicio(friend_id)
    response = []

    init = list_friends.cabeza

    while (init != None):
      response.append(map_users[init.data])
      init = init.sgte
    return response 

  @staticmethod
  def get_received_friends_requests():
    id = request.args.get('id')

    if id is None:
      return { "error": "id es requerido" }, 400
    
    requests = FriendModel().get_all_friend()["data"]
    list_requests= LE()
    users = UserModel().get_all_user()["data"]

    map_users = {}

    for user in users:
      map_users[user["id_user"]] = user

    for req in requests:
      print(req)
      if str(req.get("id_receiver")) == str(id) and str(req.get("is_accept")) == str(0):
        request_id = req.get("id_applicant")
        list_requests.append(req)
    
    track = list_requests.head
    response = []

    while(track != None):
      response.append(track.data)
      track = track.next
    # data = list_requests.viewData() #TODO

    for fr in response:
      fr["user"] = map_users[fr["id_applicant"]]

    return { "data": response }
  
  @staticmethod
  def get_sent_friends_requests():
    id = request.args.get('id')

    if id is None:
      return {"error": "id es requerido"}, 400
    
    requests = FriendModel().get_all_friend()["data"]
    list_requests= LE()
    users = UserModel().get_all_user()["data"]

    map_users = {}

    for user in users:
      map_users[user["id_user"]] = user

    for req in requests:
      if str(req.get("id_applicant")) == str(id) and str(req.get("is_accept")) == str(0):
        request_id = req.get("id_receiver")
        list_requests.append(req)

    track = list_requests.head
    response = []

    while(track != None):
      response.append(track.data)
      track = track.next

    for fr in response:
      fr["user"] = map_users[fr["id_receiver"]]

    return { "data": response }
  
  def get_list_friends_requests(id):
    response = FriendModel().get_list_friends_requests(id)
    return response
  
  @staticmethod
  def get_recomended_friends(id_user):
    users = UserModel().get_all_user().get("data")
    friends = FriendModel().get_all_friends_table()["data"]

    lista = ListaEnlazada()
    for friend_pair in friends:
      fpc = Friend(friend_pair["id_friend"], friend_pair["id_applicant"], friend_pair["id_receiver"], friend_pair["is_accept"])
      lista.add_nodo(Nodo(fpc))

    # only is_accept = 1 is for friends -1 and 0 is for states of request
    # lista.show_list()

    lista.delete_by_status([-1, 0])

    # print("Eliminados los -1 y 0")
    # lista.show_list()

    G = GraphFriends()

    for user in users:
      G.add_node(user["id_user"])

    init = lista.init
    while (init != None):
      G.add_edge(init.data.id_applicant, init.data.id_receiver)
      init = init.next

    recommended_friends = G.recomended_friends(id_user)
    id_friend_rec = []
    if not recommended_friends:
      return { "data": [] }, 200
    for key, number in recommended_friends.items():
      id_friend_rec.append(key)

    response = [user for user in users if user["id_user"] in id_friend_rec]

    for fr in response:
      fr["message"] = str(recommended_friends[fr["id_user"]]) + " amigo(s) en común"
      
    # response = [user for user in users if user["id_user"] in recommended_friends]
    return { "data": response }, 200
