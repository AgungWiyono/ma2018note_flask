"""empty message

Revision ID: 62c93f06cf4b
Revises: d979a289a713
Create Date: 2018-12-19 13:50:42.935530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62c93f06cf4b'
down_revision = 'd979a289a713'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('folder', sa.Column('description', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('folder', 'description')
    # ### end Alembic commands ###