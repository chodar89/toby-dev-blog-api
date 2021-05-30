"""Application
"""
from flask import Flask, jsonify
from marshmallow import ValidationError

from toby_dev_blog.api.resources import blp_post
from toby_dev_blog.extensions import api, db, ma


def create_app(testing=False, cli=False):  # pylint: disable=W0613
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
    configure_errors(app)
    register_blueprints(api)

    return app


def configure_extensions(app):
    """configure flask extensions"""
    db.init_app(app)
    api.init_app(app)
    ma.init_app(app)


def configure_errors(app):
    """Configure global errors"""

    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation(err):  # pylint: disable=W0612
        """Validate schema error"""
        return jsonify(err.messages), 400


def register_blueprints(api):
    """register all blueprints for api"""
    api.register_blueprint(blp_post)
