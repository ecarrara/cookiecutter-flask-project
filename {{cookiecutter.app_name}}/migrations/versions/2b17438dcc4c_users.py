# -*- coding: utf-8 -*-
"""users

Revision ID: 2b17438dcc4c
Revises: None
Create Date: 2015-05-21 10:05:30.799078

"""

# revision identifiers, used by Alembic.
revision = '2b17438dcc4c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=120), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('password', sa.String(length=128), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=False),
        sa.Column('role', sa.Enum('user', 'admin', name='user_roles'),
                  server_default='user', nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)


def downgrade():
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
