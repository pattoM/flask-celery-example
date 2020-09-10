"""empty message

Revision ID: 4ddeee181a09
Revises: 
Create Date: 2020-09-10 03:48:56.667120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ddeee181a09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emails',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('signup_ip', sa.String(length=20), nullable=True),
    sa.Column('signup_browser', sa.String(length=120), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emails')
    # ### end Alembic commands ###
