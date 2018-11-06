import os, logging

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()


from rego import models



log_formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s.%(funcName)s [%(pathname)s:%(lineno)d]: %(message)s'
)

login_manager = LoginManager()


def page_not_found(e):
    return render_template('404.html'), 404


def internal_server_error(e):
    return render_template('500.html'), 500


def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)

    # configure the app
    
    app.config.from_mapping(
        SECRET_KEY='secret_here!',
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register app extensions and handlers
    
    for handler in app.logger.handlers:
        handler.setFormatter(log_formatter)

    Bootstrap(app)

    with app.app_context():
        db.init_app(app)
        db.create_all()
        app.db = db
        login_manager.init_app(app)
        login_manager.login_view = "login"

    # Register app blueprints
    from rego import main, fop, orgadm, api

    app.register_blueprint(main.bp)
    app.register_blueprint(fop.bp)
    app.register_blueprint(orgadm.bp)
    api.init(app)

    # Register and define callback and general functions

    from rego.models import User

    
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    
    return app
