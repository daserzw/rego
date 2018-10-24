from flask import render_template, Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def index():
    return render_template('api/index.html')

