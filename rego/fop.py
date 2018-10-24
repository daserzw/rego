from flask import render_template, Blueprint

bp = Blueprint('fop', __name__, url_prefix='/fop')

@bp.route('/')
def index():
    return render_template('fop/index.html')

