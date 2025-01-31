"""empty message

Revision ID: 54c633812ce8
Revises: 826bc8e86b58
Create Date: 2020-08-06 13:38:21.952358

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '54c633812ce8'
down_revision = '826bc8e86b58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_username', table_name='user')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', mysql.VARCHAR(collation='utf8_croatian_ci', length=64), nullable=True))
    op.create_index('ix_user_username', 'user', ['username'], unique=True)
    # ### end Alembic commands ###
