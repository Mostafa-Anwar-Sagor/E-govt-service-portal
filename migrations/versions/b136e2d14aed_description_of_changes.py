"""Description of changes

Revision ID: b136e2d14aed
Revises: 6cf9fbd8c858
Create Date: 2025-01-03 17:30:45.535350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b136e2d14aed'
down_revision = '6cf9fbd8c858'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.VARCHAR(length=12),
               type_=sa.String(length=14),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.String(length=14),
               type_=sa.VARCHAR(length=12),
               existing_nullable=True)

    # ### end Alembic commands ###