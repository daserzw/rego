from flask import render_template, Blueprint
from flask_login import login_required, login_user, current_user, logout_user

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')
    
@bp.route('/user_menu')
# @login_required
def user_menu():
    # user = current_user
    # return render_template('user_menu.html', user=user)
    return render_template('user_menu.html')
