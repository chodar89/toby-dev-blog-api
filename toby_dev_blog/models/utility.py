"""Utility function for SQLAlchemy models"""

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.compiler import compiles


@compiles(UUID, "sqlite")
def compile_uuid_sqlite(type_, compiler, **kw):
    """
    Overrides `UUID` with `String` for `Sqlite` database.
    Used for automated test enviroment.
    """
    return "String"
