"""empty message

Revision ID: d28313ebf3b1
Revises: 9166edd3e1c3
Create Date: 2024-11-30 17:49:08.481299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd28313ebf3b1'
down_revision: Union[str, None] = '9166edd3e1c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
