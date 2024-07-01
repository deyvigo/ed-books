from flask import Blueprint

from controllers.buscador import BuscadorController

buscador_blueprint = Blueprint('buscador', __name__)

@buscador_blueprint.route('/search', methods=['POST'])
def search():
  return BuscadorController.search_by_prefix()