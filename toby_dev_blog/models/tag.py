"""SQLAlchemy model - Tag"""
from datetime import datetime

from toby_dev_blog.extensions import db


class Tag(db.Model):
    """SQLAlchemy model - Tag

    :param db: SQLAlchemy DB Model
    :type db: :class:'db.Model'
    """

    __tablename__ = "tags"

    id = db.Column(db.String(), primary_key=True, unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
