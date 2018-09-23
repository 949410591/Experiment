from flask import Flask
from .config import configs
from .models import db
def register_blueprints(app):
	from .handlers import course, admin, front
	app.register_blueprint(course)
	app.register_blueprint(admin)
	app.register_blueprint(front)

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(configs.get(config))
	db.init_app(app)
	register_blueprints(app)

	return app
