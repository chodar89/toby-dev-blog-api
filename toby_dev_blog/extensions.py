"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from flask_marshmallow import Marshmallow
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
api = Api()
