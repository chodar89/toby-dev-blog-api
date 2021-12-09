"""Refresh token schema schemas"""
from marshmallow import Schema, fields


class RefreshTokenSchema(Schema):
    """Refresh Token Schema

    :param ma: Marshmallow schema class
    :type ma: :class:`Schema`
    """

    access_token = fields.String(required=True)
