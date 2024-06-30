from flask import request

from models import CommentModel
from structures.ListaEnlazada import ListaEnlazada

class CommentController:
    @staticmethod
    def get_all_comments_user():
        id = request.args.get('id')
        comment_user= ListaEnlazada()
        data=CommentModel().get_all_comment_table()
        data_comment=data['data']
        band=True

        if id is None:
            return {"error": "id es requerido"}, 400
        for comment in data_comment:
            if str(comment.get("id_user_comment"))== str(id):
                comment_user.append(comment)
                band=False
        response = comment_user.viewData()

        if(band):
            return {"data":"No hay comentarios"}
        return response
    
    @staticmethod
    def get_all_comments_post():
        id = request.args.get('id')
        comment_user= ListaEnlazada()
        data=CommentModel().get_all_comment_table()
        data_comment=data['data']
        band=True

        if id is None:
            return {"error": "id son requeridos"}, 400
        for comment in data_comment:
            if str(comment.get("id_post"))== str(id):
                comment_user.append(comment)
                band=False
        response = comment_user.viewData()

        if(band):
            return {"data":"No hay posts"}
        return response
    
    def post_one_comment():
        data = request.json
        id_user_comment=data.get("id_user_comment")
        id_post=data.get("id_post")
        comment=data.get("comment")
        print(id_user_comment, id_post, comment)
        response = CommentModel().post_one_comment(id_post,id_user_comment,comment)
        return response
    
    def delete_comment():
        id = request.args.get('id')
        response=CommentModel().delete_comment(id);
        return response