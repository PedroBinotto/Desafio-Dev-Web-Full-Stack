from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskapp.config import Config

db = SQLAlchemy()

from flaskapp.main.routes import main
from flaskapp.errors.handlers import errors

# from flaskapp.models import MyModelView, User, Post, Comment, Tag, TagRelation

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app
