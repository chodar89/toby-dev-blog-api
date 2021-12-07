"""`Post` views - module contains methods to operate on the single and multiple
`Post` objects"""
from flask.views import MethodView
from flask_smorest import Blueprint

from toby_dev_blog.extensions import db
from toby_dev_blog.models import Post
from toby_dev_blog.schemas import PostSchema

blp_post = Blueprint(
    "posts", "posts", url_prefix="/posts", description="Operations on posts"
)


@blp_post.route("/")
class PostListAPI(MethodView):
    """Posts list objects endpoint

    :param MethodView: `Flask` View Class
    :type MethodView: :class:`MethodView`
    """

    @blp_post.response(200, PostSchema(many=True))
    def get(self):
        """Retrive list of posts"""
        return Post.query.all()

    @blp_post.arguments(PostSchema(many=True))
    @blp_post.response(200, PostSchema(many=True))
    def post(self, post_data):
        """Post/create list of posts"""
        db.session.add_all(post_data)
        db.session.commit()
        return post_data


class PostAPI(MethodView):
    """Post object endpoint

    :param MethodView: `Flask` View Class
    :type MethodView: :class:`MethodView`
    """

    def get(self):
        """Retrive single post by slug or id"""
        pass

    def patch(self):
        """Edit single post object"""
        pass

    def delete(self):
        """Delete a post"""
        pass
