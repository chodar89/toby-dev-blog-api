"""`Post` views - module contains methods to operate on the single and multiple
`Post` objects"""
from flask import Response
from flask.views import MethodView
from flask_smorest import Blueprint

from toby_dev_blog.extensions import db
from toby_dev_blog.models import Post
from toby_dev_blog.schemas import PostPatchSchema, PostSchema

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
    @blp_post.alt_response(422, description="Invalid payload")
    def post(self, post_data: list[Post]):
        """Post/create list of posts"""
        db.session.add_all(post_data)
        db.session.commit()
        return post_data


@blp_post.route("/<string:slug>")
class PostAPI(MethodView):
    """Post object endpoint

    :param MethodView: `Flask` View Class
    :type MethodView: :class:`MethodView`
    """

    @blp_post.response(200, PostSchema)
    @blp_post.alt_response(404, description="Post not found")
    def get(self, slug):
        """Retrive single post by slug"""
        return Post.query.filter(Post.slug == slug).first_or_404()

    @blp_post.arguments(PostPatchSchema)
    @blp_post.response(200, PostSchema)
    @blp_post.alt_response(404, description="Post not found")
    @blp_post.alt_response(422, description="Invalid payload")
    def patch(self, post_data, slug):
        """Edit single post object"""
        post = Post.query.filter(Post.slug == slug).first_or_404()
        post_schema = PostSchema()
        post = post_schema.load(post_data, instance=post, partial=True)
        db.session.add(post)
        db.session.commit()
        return post

    @blp_post.response(204)
    @blp_post.alt_response(404, description="Post not found")
    def delete(self, slug):
        """Delete a post"""
        post = Post.query.filter(Post.slug == slug).first_or_404()
        db.session.delete(post)
        db.session.commit()
        return Response(status=204)
