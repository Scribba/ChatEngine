from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey
from sqlalchemy.types import JSON


metadata = MetaData()

user_profiles = Table(
    "user_profiles",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("data", JSON, nullable=False),
)

conversations = Table(
    "conversations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("user_profiles.id"), nullable=False),
    Column("data", JSON, nullable=False),  # arbitrary conversation metadata
)
