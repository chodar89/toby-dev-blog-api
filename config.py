"""Default configuration

Use env var to override
"""
import os

ENV = os.getenv("FLASK_ENV", "development")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY", "changeme")

API_TITLE = "TOBY DEV BLOG API"
API_VERSION = "v1"
OPENAPI_VERSION = "3.0.2"
OPENAPI_JSON_PATH = "api-spec.json"
OPENAPI_URL_PREFIX = "/"
OPENAPI_REDOC_PATH = "/redoc"
OPENAPI_REDOC_URL = (
    "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
)
OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

SQLALCHEMY_DATABASE_URI = os.getenv(
    "TOBY_DEV_BLOG_DB", "sqlite:///../tests/test_toby_blog_db.db"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
