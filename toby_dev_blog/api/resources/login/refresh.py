"""Refresh token API - handle refresh JWT token"""
from flask.views import MethodView
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from flask_smorest import Blueprint

from toby_dev_blog.schemas import RefreshTokenSchema

blp_refresh = Blueprint("refresh", "refresh", url_prefix="/refresh")


@blp_refresh.route("/")
class RefreshAPI(MethodView):
    """Refresh endpoint

    :param MethodView: `Flask` View Class
    :type MethodView: :class:`MethodView`
    """

    @jwt_required(refresh=True)
    @blp_refresh.response(200, RefreshTokenSchema)
    def post(self):
        """Refresh JWT token"""
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}
