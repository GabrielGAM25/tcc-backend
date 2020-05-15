"""Create Assessment

Revision ID: 1628849ddec4
Revises: 9318034acbdc
Create Date: 2020-05-14 23:45:36.660357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1628849ddec4'
down_revision = '9318034acbdc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assessment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('weight', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('fat_percentage', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('neck', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('shoulder', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('torax', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('abdomen', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('waist', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('hip', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('left_arm', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('right_arm', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('left_forearm', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('right_forearm', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('left_thigh', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('right_thigh', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('left_calf', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('right_calf', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assessment')
    # ### end Alembic commands ###
