from flask import Flask
from flask_jwt_extended import JWTManager
from config import config
from routes import login_blueprint, user_blueprint, book_blueprint, author_blueprint, genre_blueprint, book_genre_blueprint, friend_blueprint, book_user_blueprint
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(config['development'])
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(user_blueprint)
app.register_blueprint(book_blueprint)
app.register_blueprint(author_blueprint)
app.register_blueprint(genre_blueprint)
app.register_blueprint(book_genre_blueprint)
app.register_blueprint(friend_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(book_user_blueprint)

# @app.route("/", methods = ["GET"])
# def hello ():
#   cursor = db.cursor()

#   try:
#     cursor.execute('SELECT * FROM user;')
#     response = cursor.fetchall()
#     db.close()
#   except:
#     return { "error": "Ha ocurrido un error en la base de datos." }

#   return jsonify({ 'data': response })

if __name__ == "__main__":
  app.run()
