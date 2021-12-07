"""`User` endpoints"""
from flask.views import MethodView
from flask_smorest import Blueprint

from toby_dev_blog.extensions import db
from toby_dev_blog.models import User
from toby_dev_blog.schemas import UserSchema

blp_user = Blueprint(
    "users", "users", url_prefix="/users", description="Operations on users"
)


@blp_user.route("/")
class UserListAPI(MethodView):
    """User list objects endpoint

    :param MethodView: `Flask` View Class
    :type MethodView: :class:`MethodView`
    """

    @blp_user.response(200, UserSchema(many=True))
    def get(self):
        """Retrive list of users"""
        return User.query.all()

    @blp_user.arguments(UserSchema(many=True), location="json")
    @blp_user.response(200, UserSchema(many=True))
    def post(self, user_data):
        """Post/create list of users"""
        db.session.add_all(user_data)
        db.session.commit()
        return user_data
