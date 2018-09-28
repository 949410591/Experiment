"""hanhan

Revision ID: 666035b4e06a
Revises: 57bdfdc853f6
Create Date: 2018-09-25 10:29:05.026016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '666035b4e06a'
down_revision = '57bdfdc853f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hanhan', sa.String(length=233), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'hanhan')
    # ### end Alembic commands ###
