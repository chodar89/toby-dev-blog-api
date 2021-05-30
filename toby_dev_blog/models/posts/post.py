"""SQLAlchemy model - Post"""
import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID

from toby_dev_blog.extensions import db


class Post(db.Model):
    """SQLAlchemy model - Post

    :param db: db Model class, inherits from SQLAlchemy
    :type db: metaclass
    """

    __tablename__ = "posts"
    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    slug = db.Column(db.SlugField())
    title = db.Column(db.String(), nullable=False)
    meta_title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    is_featured = db.Column(db.Bool(), default=False, nullable=False)
    is_published = db.Column(db.Bool(), default=True, nullable=False)
    read_time = db.Column(db.Integer(), default=0, nullable=False)
    views = db.Column(db.Bool(), default=0, nullable=False)
    claps = db.Column(db.Bool(), default=0, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
