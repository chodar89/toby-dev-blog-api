"""SQLAlchemy model - User"""
import uuid
from datetime import datetime
from typing import Union

from sqlalchemy.dialects.postgresql import UUID

from toby_dev_blog.extensions import bcrypt, db


class User(db.Model):
    """`SQLAlchemy` model - User

    :param db: `SQLAlchemy` DB Model
    :type db: :class:`db.Model`
    """

    __tablename__ = "users"

    def __init__(self, email: str, password: str, **kwargs) -> None:
        """`SQLalchemy` contruct method

        :param email: User email address
        :type email: str
        :param password: User password
        :type password: str
        """
        super().__init__(**kwargs)
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    @classmethod
    def find_by_email(cls, email: str) -> Union["User", None]:
        """Find :class:`User` by email

        :param email: user email
        :type email: str
        :return: Return user object or None
        :rtype: Union["User", None]
        """
        return cls.query.filter(cls.email == email).first()

    def check_password(self, password: str) -> bool:
        """Check if given password match hashed password

        :param password: Passed password
        :type password: str
        :return: `True` if password match, else `False`
        :rtype: bool
        """
        return bcrypt.check_password_hash(self.password, password)
