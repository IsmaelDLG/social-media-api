"""add relationship users-posts

Revision ID: d279cc4ccd55
Revises: f8cc1130b02b
Create Date: 2023-08-26 20:29:46.357968

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd279cc4ccd55'
down_revision: Union[str, None] = 'f8cc1130b02b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
