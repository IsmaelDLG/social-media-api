"""create posts table

Revision ID: f9cb6f73604e
Revises: 
Create Date: 2023-08-26 17:54:48.368419

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP



# revision identifiers, used by Alembic.
revision: str = 'f9cb6f73604e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
def upgrade() -> None:
    op.create_table("posts", 
        Column("id", Integer,primary_key=True, nullable=False),
        Column("title", String, nullable=False),
        Column("content", String, nullable=False),
        Column("published", Boolean, server_default='TRUE', nullable=False),
        Column("created_at", TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')),
    )
    
def downgrade() -> None:
    op.drop_table('posts')