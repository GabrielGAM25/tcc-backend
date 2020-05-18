"""Create Assessment table

Revision ID: 02_create_assessment
Revises: 01_create_user
Create Date: 2020-05-14 23:45:36.660357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02_create_assessment'
down_revision = '01_create_user'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assessment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('weight', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.Column('fat_percentage', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.Column('neck', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('shoulder', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('torax', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('abdomen', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('waist', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('hip', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('left_arm', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('right_arm', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('left_forearm', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('right_forearm', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('left_thigh', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('right_thigh', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('left_calf', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.Column('right_calf', sa.Numeric(precision=6, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assessment')
    # ### end Alembic commands ###
