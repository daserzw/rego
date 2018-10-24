import os, logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
log_formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s.%(funcName)s [%(pathname)s:%(lineno)d]: %(message)s'
)
login_manager = LoginManager()

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
        login_manager.init_app(app)
        login_manager.login_view = "login"

    # Register app blueprints         
    from rego import main, fop, orgadm, api

    app.register_blueprint(main.bp)
    app.register_blueprint(fop.bp)
    app.register_blueprint(orgadm.bp)
    app.register_blueprint(api.bp)

    # Register and define callback and general functions
    
    from rego.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    @app.errorhandler(404)
    def not_fount(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(e):
        return render_template('500.html'), 500

    
    return app
