"""User login schema schemas"""
from marshmallow import Schema, fields


class LoginSchema(Schema):
    """User Login Schema

    :param ma: Marshmallow schema class
    :type ma: :class:`Schema`
    """

    class Meta:
        load_only = ("email", "password")
        dump_only = ("access_token", "refresh_token")

    email = fields.String(required=True)
    password = fields.String(required=True)
    access_token = fields.String(required=True)
    refresh_token = fields.String(required=True)
