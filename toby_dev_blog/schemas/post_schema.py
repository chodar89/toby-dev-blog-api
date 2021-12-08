"""Blog Post schemas"""
from marshmallow import Schema, fields
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


class PostPatchSchema(Schema):
    """Post PATCH method schema

    :param ma: Marshmallow schema class
    :type ma: :class:`Schema`
    """

    title = fields.String()
    meta_title = fields.String()
    description = fields.String()
    content = fields.String()
    is_featured = fields.Boolean()
    is_published = fields.Boolean()
    read_time = fields.Integer()
