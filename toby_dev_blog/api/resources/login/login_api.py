"""Login API - handle user login and JWT token"""
from flask import abort
from flask.views import MethodView
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_smorest import Blueprint

from toby_dev_blog.models import User
from toby_dev_blog.schemas import LoginSchema

blp_login = Blueprint("login", "login", url_prefix="/login")


@blp_login.route("/")
class LoginAPI(MethodView):
    """Posts list objects endpoint

    :param MethodView: `Flask` View Class
    :type MethodView: :class:`MethodView`
    """

    @blp_login.arguments(LoginSchema)
    @blp_login.response(200, LoginSchema)
    @blp_login.alt_response(401, description="Invalid credentials")
    def post(self, login_data):
        """Login user and issue jwt token"""
        user = User.find_by_email(login_data)
        if user and user.check_password(login_data["password"]):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        abort(401, "Invalid credentials")
