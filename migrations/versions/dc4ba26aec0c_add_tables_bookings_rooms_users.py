"""Add tables Bookings, Rooms, Users

Revision ID: dc4ba26aec0c
Revises: 813153550214
Create Date: 2023-11-21 21:28:22.272359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc4ba26aec0c'
down_revision: Union[str, None] = '813153550214'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
