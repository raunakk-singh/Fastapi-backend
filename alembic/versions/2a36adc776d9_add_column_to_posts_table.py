"""add column to posts table

Revision ID: 2a36adc776d9
Revises: 2fd936f78e33
Create Date: 2026-10-11 17:33:22.533971

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a36adc776d9'
down_revision: Union[str, Sequence[str], None] = '2fd936f78e33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
