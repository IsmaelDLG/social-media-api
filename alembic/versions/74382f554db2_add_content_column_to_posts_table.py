"""add content column to posts table

Revision ID: 74382f554db2
Revises: f9cb6f73604e
Create Date: 2023-08-26 18:02:33.544657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74382f554db2'
down_revision: Union[str, None] = 'f9cb6f73604e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
