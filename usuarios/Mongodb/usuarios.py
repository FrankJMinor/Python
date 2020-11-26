from flask import Blueprint
from Models.Mongodb.model import Usuarios

usuarios_bp = Blueprint('usuarios_bp', __name__)

@usuarios_bp.route('/crearUsuario')
def list():
    usuarios = Usuarios.query()
    return usuarios