"""User schemas"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from toby_dev_blog.extensions import db
from toby_dev_blog.models import User


class UserSchema(SQLAlchemyAutoSchema):
    """User Schema

    :param SQLAlchemyAutoSchema: `Marshmallow` sqlalchemy schema class
    :type SQLAlchemyAutoSchema: :class:`SQLAlchemyAutoSchemaz
    """

    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
        load_only = ("password",)
