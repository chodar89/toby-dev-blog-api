"""Logout API - handle user logout and JWT token"""
from flask import Response
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import Blueprint

from toby_dev_blog.blacklist import BLACKLIST

blp_logout = Blueprint("logout", "logout", url_prefix="/logout")


@blp_logout.route("/")
class LogoutAPI(MethodView):
    """Logout endpoint

    :param MethodView: `Flask` View Class
    :type MethodView: :class:`MethodView`
    """

    @jwt_required
    @blp_logout.response(200, description="User logout")
    def post(self):
        """Logout user and blacklist token"""
        jti = get_jwt_identity()[
            "jti"
        ]  # jti is "JWT ID", a unique identifier for a JWT.
        BLACKLIST.add(jti)
        return Response(status=200)
