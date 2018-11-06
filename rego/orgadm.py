from flask import render_template, Blueprint
from rego.forms import RegisterEntityForm, RegisterOrganizationForm

bp = Blueprint('orgadm', __name__, url_prefix='/orgadm')

@bp.route('/')
def index():
    return render_template('orgadm/index.html')

@bp.route('/register_entity', methods=['GET', 'POST'])
def register_entity():
    form = RegisterEntityForm()
    # if form.validate_on_submit():
      # <todo>
    return render_template('orgadm/register_entity.html', form=form)

@bp.route('/register_org', methods=['GET', 'POST'])
def register_org():
    form = RegisterOrganizationForm()
    # if form.validate_on_submit():
        # <todo>
    return render_template('orgadm/register_org.html', form=form)