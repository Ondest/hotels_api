"""Modifying Bookings, Rooms, Users

Revision ID: 5a9ea383896a
Revises: 0547f65a4280
Create Date: 2023-11-21 21:34:31.205303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a9ea383896a'
down_revision: Union[str, None] = '0547f65a4280'
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
