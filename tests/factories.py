"""Test factories"""
import uuid
from datetime import datetime

import factory

from toby_dev_blog.extensions import bcrypt, db
from toby_dev_blog.models import Post, User


class PostFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Post model factory"""

    class Meta:
        model = Post
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: uuid.uuid4())
    slug = factory.Sequence(lambda n: f"slug-{n + 1}")
    title = "my first post"
    meta_title = "my first post, dev post"
    description = "This post will be about my first post"
    content = "This is my first post"
    is_featured = False
    is_published = True
    read_time = 60
    views = 100
    claps = 65
    published_at = datetime.utcnow()
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    """User model factory"""

    class Meta:
        model = User
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: uuid.uuid4())
    email = factory.Sequence(lambda n: f"email-{n + 1}@gmail.com")
    password = bcrypt.generate_password_hash("I'm-a-strong-password")
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()
