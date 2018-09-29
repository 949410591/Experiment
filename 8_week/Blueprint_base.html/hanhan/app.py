from flask import Flask
from flask_migrate import Migrate
from .config import configs
from .models import db




def register_blueprint(app):
    from .handlers import user, course, front
    app.register_blueprint(user)
    app.register_blueprint(course)
    app.register_blueprint(front)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    Migrate(app, db)
    register_blueprint(app)

    return app
