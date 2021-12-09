"""Init - blueprints"""
from toby_dev_blog.api.resources.login.login_api import blp_login
from toby_dev_blog.api.resources.login.logout_api import blp_logout
from toby_dev_blog.api.resources.login.refresh import blp_refresh
from toby_dev_blog.api.resources.post.post_api import blp_post
from toby_dev_blog.api.resources.user.user_api import blp_user

__all__ = ["blp_post", "blp_user", "blp_login", "blp_logout", "blp_refresh"]
