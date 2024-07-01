from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import UserModel, PostModel
from controllers.comment import CommentController
from structures.ListaEnlazada import ListaEnlazada

class PostController:
    @staticmethod
    @jwt_required(optional=True)  # Indica que JWT es opcional pero se usa si está presente
    def get_all_posts_user():
        id = request.args.get('id')
        if id is None:
            print("is none")
            current_user = get_jwt_identity()
            if current_user is None:
                return {"error": "ID requerido"}, 400
            id = current_user["id_user"]
            print(id)
            print("Deberia el id estar arriba de esto")
        
        post_user = ListaEnlazada()
        data = PostModel().get_all_post_table()
        users = UserModel().get_all_user()["data"]
        comments = CommentController.get_all_comments()["data"]
        data_post = data['data']
        band = True
        
        for post in data_post:
            if str(post.get("id_user_post")) == str(id):
                for user in users:
                    if post["id_user_post"] == user["id_user"]:
                        post["name"] = user["name"]
                        continue
                post["comments"] = []
                for comment in comments:
                    if post["id_post"] == comment["id_post"]:
                        post["comments"].append(comment)
                post_user.append(post)
                band = False
                
        response = post_user.viewData()
        
        if band:
            return {"data": "No hay posts"}
        return response
    
    @staticmethod
    @jwt_required(optional=True)  # Indica que JWT es opcional pero se usa si está presente
    def get_all_posts_book():
        id = request.args.get('id')
        
        if id is None:
            current_user = get_jwt_identity()
            if current_user is None:
                return {"error": "ID requerido"}, 400
            id = current_user["id_user"]
        
        post_user = ListaEnlazada()
        data = PostModel().get_all_post_table()
        users = UserModel().get_all_user()["data"]
        comments = CommentController.get_all_comments()["data"]
        data_post = data['data']
        band = True
        
        for post in data_post:
            if str(post.get("id_book")) == str(id):
                for user in users:
                    if post["id_user_post"] == user["id_user"]:
                        post["name"] = user["name"]
                        continue
                post["comments"] = []
                for comment in comments:
                    if post["id_post"] == comment["id_post"]:
                        post["comments"].append(comment)
                post_user.append(post)
                band = False
                
        response = post_user.viewData()
        
        if band:
            return {"data": "No hay posts"}
        return response
    
    @staticmethod
    @jwt_required(optional=True)  # Indica que JWT es requerido para acceder a este método
    def post_one_post():
        data = request.json
        id_user_post = data.get("id_user_post")
        id_book = data.get("id_book")
        content = data.get("content")
        response = PostModel().post_one_post(id_user_post, id_book, content)
        return response
    
    @staticmethod
    @jwt_required()  # Indica que JWT es requerido para acceder a este método
    def delete_post():
        id = request.args.get('id')
        response = PostModel().delete_post(id)
        return response
