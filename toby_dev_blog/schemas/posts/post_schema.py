"""Blog Post schemas"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from toby_dev_blog.extensions import db
from toby_dev_blog.models import Post


class PostSchema(SQLAlchemyAutoSchema):
    """Post Schema

    :param SQLAlchemyAutoSchema: marshmallow sqlalchemy schema class
    :type SQLAlchemyAutoSchema: metaclass
    """

    class Meta:
        model = Post
        sqla_session = db.session
        strict = True
        load_instance = True
