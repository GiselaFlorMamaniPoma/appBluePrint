from flask import Blueprint, render_template

admin_bp = Blueprint('admin',__name__,url_prefix='/admin',template_folder='templates')

@admin_bp.route("/panel")
def panel():
    return "<h1>BIENVENIDO AL PANEL DE ADMINISTRACION de ---> GISELA FLOR MAMANI POMA </h1>"


