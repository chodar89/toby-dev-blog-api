"""Commands
"""
import click
from flask.cli import FlaskGroup

from toby_dev_blog.app import create_app
from toby_dev_blog.extensions import db


def create_toby_dev_blog():
    """Create app"""
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_toby_dev_blog)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init"""


@cli.command("create_all")
def create_all():
    """Populate database"""
    click.echo("creating all")
    db.create_all()
    click.echo("created all")


if __name__ == "__main__":
    cli()
