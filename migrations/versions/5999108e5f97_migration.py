"""migration

Revision ID: 5999108e5f97
Revises: 45ac349e36be
Create Date: 2019-11-29 10:55:25.819014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5999108e5f97'
down_revision = '45ac349e36be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('blog_title', sa.String(), nullable=True),
    sa.Column('blog_content', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog')
    # ### end Alembic commands ###