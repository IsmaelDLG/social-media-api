"""add user table

Revision ID: f8cc1130b02b
Revises: 74382f554db2
Create Date: 2023-08-26 18:06:48.439162

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision: str = 'f8cc1130b02b'
down_revision: Union[str, None] = '74382f554db2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users", 
        Column("id", Integer,primary_key=True, nullable=False),
        Column("email", String, unique=True, nullable=False),
        Column("password", String, nullable=False),
        Column("created_at", TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    )

def downgrade() -> None:
    op.drop_table('posts')
