"""Application
"""
import logging

from flask import Flask
from flask_smorest import Api

from toby_dev_blog.api.resources import blp_post, blp_user
from toby_dev_blog.extensions import api, bcrypt, db, jwt, ma

log = logging.getLogger(__name__)


def create_app(
    testing: bool = False, cli: bool = False
) -> Flask:  # pylint: disable=W0613
    """Application factory, used to create application"""
    app = Flask("toby_dev_blog")
    app.config.from_object("config")

    if testing is True:
        app.config["TESTING"] = True

    @app.route("/healthcheck", methods=["GET"])
    def healthcheck():  # pylint: disable=W0612
        """Health check endpoint
        :return: Json message and 200 status code
        """
        return ({"status": "ok"}), 200

    configure_extensions(app)
    register_blueprints(api)

    return app


def configure_extensions(app: Flask) -> None:
    """configure flask extensions"""
    db.init_app(app)
    api.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


def register_blueprints(api: Api) -> None:
    """register all blueprints for api"""
    api.register_blueprint(blp_post)
    api.register_blueprint(blp_user)
