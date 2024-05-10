from flask import Flask
from routes import user_blueprint
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)

app.register_blueprint(user_blueprint)

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
  app.run(debug=True)
