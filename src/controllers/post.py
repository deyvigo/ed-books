from flask import request

from models import PostModel
from structures.ListaEnlazada import ListaEnlazada

class PostController:
    @staticmethod
    def get_all_posts_user():
        id = request.args.get('id')
        post_user= ListaEnlazada()
        data=PostModel().get_all_post_table()
        data_post=data['data']
        band=True

        if id is None:
            return {"error": "id son requeridos"}, 400
        for post in data_post:
            if str(post.get("id_user_post"))== str(id):
                post_user.append(post);
                band=False
        response = post_user.viewData()

        if(band):
            return {"data":"No hay posts"}
        return response
    
    @staticmethod
    def get_all_posts_book():
        id = request.args.get('id')
        post_user= ListaEnlazada()
        data=PostModel().get_all_post_table()
        data_post=data['data']
        band=True

        if id is None:
            return {"error": "id son requeridos"}, 400
        for post in data_post:
            if str(post.get("id_book"))== str(id):
                post_user.append(post);
                band=False
        response = post_user.viewData()

        if(band):
            return {"data":"No hay posts"}
        return response
    
    def post_one_post():
        data = request.json
        id_user_post=data.get("id_user_post")
        id_book=data.get("id_book")
        content=data.get("content")
        response = PostModel().post_one_post(id_user_post,id_book,content)
        return response
    
    def delete_post():
        id = request.args.get('id')
        response=PostModel().delete_post(id);
        return response