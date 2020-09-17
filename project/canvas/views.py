from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

canvas_blueprint = Blueprint('canvas', __name__, template_folder='templates')

@canvas_blueprint.route('/canvas', methods=['GET', 'POST'])
def canvas_overview():
    return render_template('canvas_overview.html')
