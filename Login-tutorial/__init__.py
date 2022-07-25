from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db= SQLAlchemy()
login_manager = LoginManager()

def create_app():
  app = Flask(__name__, instance_relative_config=False)

  app.config.from_object('config.Config')

  db.innit_app(app)
  login_manager.innit_app(app)

  with app.app_context():
    from . import routes
    from . import login
    app.register_blueprint(routes.main_bp)
    app.register_blueprint(login.login_bp)

    db.create_all()
    return app
    