"""Conftest
"""
import os

import pytest
from dotenv import load_dotenv
from pytest_factoryboy import register

from tests.factories import PostFactory, UserFactory
from toby_dev_blog.app import create_app
from toby_dev_blog.extensions import db as db_


@pytest.fixture
def load_env():
    """Load test environment"""
    load_dotenv(".testenv")


@pytest.fixture(scope="session")
def app():
    """app"""
    load_dotenv(".testenv")
    app = create_app(testing=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("TEST_DATABASE_URI")
    return app


@pytest.fixture
def db(app):
    """DB"""
    db_.app = app
    with app.app_context():
        db_.create_all()

    yield db_

    db_.session.close()
    db_.drop_all()


@pytest.fixture
def client(app):
    """Client"""
    testing_client = app.test_client()

    yield testing_client


register(PostFactory, "post")
register(UserFactory, "user")
