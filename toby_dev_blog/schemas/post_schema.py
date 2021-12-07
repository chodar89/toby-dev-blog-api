"""Blog Post schemas"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from toby_dev_blog.extensions import db
from toby_dev_blog.models import Post


class PostSchema(SQLAlchemyAutoSchema):
    """Post Schema

    :param SQLAlchemyAutoSchema: `Marshmallow` sqlalchemy schema class
    :type SQLAlchemyAutoSchema: :class:`SQLAlchemyAutoSchemaz
    """

    class Meta:
        model = Post
        sqla_session = db.session
        load_instance = True
