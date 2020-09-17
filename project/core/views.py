# core/views.py
from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():#shift to index one basic is not deleted
    #more to come
    return render_template('index.html')

@core.route('/info')
def info():
    return render_template('/info.html')

@core.route('/kontakt')
def kontakt():
    return render_template('/kontakt.html')

@core.route('/impressum')
def impressum():
    return render_template('/impressum.html')
