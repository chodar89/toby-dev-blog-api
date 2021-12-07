"""Test :class:`User' methods"""
from toby_dev_blog.models import User


def test_check_password__correct(app, client):
    user = User("email@gmail.com", "I'm-a-strong-password")
    assert user.check_password("I'm-a-strong-password") is True


def test_check_password__incorrect(app, client):
    user = User("email@gmail.com", "I'm-a-strong-password")
    assert user.check_password("Incorrect password") is False
