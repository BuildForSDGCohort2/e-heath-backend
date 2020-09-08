"""Initial migration.

Revision ID: 4ba7d8614480
Revises: 
Create Date: 2020-09-08 21:39:24.505401

"""
from alembic import op
import sqlalchemy as sa
from lib.util_sqlalchemy import AwareDateTime as aw


# revision identifiers, used by Alembic.
revision = '4ba7d8614480'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('created_on', aw.AwareDateTime(), nullable=True),
    sa.Column('updated_on', aw.AwareDateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.Enum('admin', 'user', 'doctor', 'nurse', 'matron', 'pharmacist', 'receptionist', 'management', 'finance', name='role_types', native_enum=False), server_default='member', nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False),
    sa.Column('username', sa.String(length=24), nullable=True),
    sa.Column('email', sa.String(length=255), server_default='', nullable=False),
    sa.Column('password', sa.String(length=255), server_default='', nullable=False),
    sa.Column('sign_in_count', sa.Integer(), nullable=False),
    sa.Column('current_sign_in_on', aw.AwareDateTime(), nullable=True),
    sa.Column('current_sign_in_ip', sa.String(length=45), nullable=True),
    sa.Column('last_sign_in_on', aw.AwareDateTime(), nullable=True),
    sa.Column('last_sign_in_ip', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_role'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
