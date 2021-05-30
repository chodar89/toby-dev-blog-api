"""Post views"""
from flask.views import MethodView
from flask_smorest import Blueprint

blp_post = Blueprint(
    "posts", "posts", url_prefix="/posts", description="Operations on posts"
)


@blp_post.route("/")
class PostListAPI(MethodView):
    """Posts list objects endpoint

    :param MethodView: Flask View Class
    :type MethodView: metaclass
    """

    def get(self):
        """Retrive list of posts"""
        return "POST LIST"

    def post(self):
        """Post/create list of posts"""
        return "POST LIST"
