from flask import Blueprint, render_template

blog_bp = Blueprint('blog',__name__,url_prefix='/blog',template_folder='templates')

@blog_bp.route("/")
def mostrar():
    return render_template('base.html')


@blog_bp.route("/entrada/<id>")
def mostrar_entrada(id):
    return "<h1>blog de GISELA   : "+id+" </h1>"
