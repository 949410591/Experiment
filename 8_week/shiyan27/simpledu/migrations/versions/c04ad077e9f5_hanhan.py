"""hanhan

Revision ID: c04ad077e9f5
Revises: 666035b4e06a
Create Date: 2018-09-25 10:36:39.838919

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c04ad077e9f5'
down_revision = '666035b4e06a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'hanhan')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hanhan', mysql.VARCHAR(length=233), nullable=True))
    # ### end Alembic commands ###
