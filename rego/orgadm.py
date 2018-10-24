import functools

from flask import render_template, Blueprint
from rego.forms import EntityForm, OrganizationForm

bp = Blueprint('orgadm', __name__, url_prefix='/orgadm')

@bp.route('/')
def index():
    return render_template('orgadm/index.html')

@bp.route('/register_entity', methods=['GET', 'POST'])
def register_entity():
    form = EntityForm()
    return render_template('orgadm/register_entity.html', form=form)

@bp.route('/register_org', methods=['GET', 'POST'])
def register_org():
    form = OrganizationForm()
    return render_template('orgadm/register_org.html', form=form)