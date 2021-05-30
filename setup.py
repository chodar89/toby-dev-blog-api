from setuptools import find_packages, setup

__version__ = "0.1"

setup(
    name="toby_dev_blog",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "flask-restful",
        "flask-migrate",
        "flask-jwt-extended",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "python-dotenv",
        "passlib",
        "apispec[yaml]",
        "apispec-webframeworks",
    ],
    entry_points={
        "console_scripts": ["toby_dev_blog = toby_dev_blog.manage:cli"]
    },
)
