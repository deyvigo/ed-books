import copy
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import UserModel, PostModel, FriendModel, CommentModel
from controllers.comment import CommentController
from structures.ListaEnlazada import ListaEnlazada
from structures.FeedPosts.ListaEnlazada import ListaEnlazada as Le
from entity.Friend import Friend

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

    @staticmethod
    @jwt_required()
    def get_all_posts_friends():
        user = get_jwt_identity()
        id = user["id_user"]
        posts = PostModel().get_all_post_table()["data"]
        friends = FriendModel().get_all_friend()["data"]
        users = UserModel().get_all_user()["data"]
        comments = CommentModel().get_all_comment_table()["data"]
        
        map_users = { user["id_user"] : user for user in users }
        map_comments = {}
        map_posts = {}
        
        for post in posts:
            if post["id_user_post"] not in map_posts:
                map_posts[post["id_user_post"]] = []
                map_posts[post["id_user_post"]].append(post)
            else:
                map_posts[post["id_user_post"]].append(post)
        
        for comment in comments:
            if comment["id_post"] not in map_comments:
                map_comments[comment["id_post"]] = []
                map_comments[comment["id_post"]].append(comment)
            else:
                map_comments[comment["id_post"]].append(comment)
        
        friends_list = Le()
        for friend in friends:
            friends_list.append(Friend(friend["id_friend"], friend["id_applicant"], friend["id_receiver"], friend["is_accept"]))
        
        friends_of_user = friends_list.search(int(id))
        
        response = []
        
        for friend in friends_of_user:
            if friend in map_posts:
                to_append = map_posts[friend]
                for append in to_append:
                    append["user"] = map_users[friend]
                    if append["id_post"] in map_comments:
                        comments = map_comments[append["id_post"]]
                        for comment in comments:
                            comment["user"] = map_users[comment["id_user_comment"]]
                        append["comments"] = map_comments[append["id_post"]]
                    else:
                        append["comments"] = []
                response.append(to_append)
        

        return response
			
