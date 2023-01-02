"""Renaming name column to birthname

Revision ID: fa481f6b55b0
Revises: 791279dd0760
Create Date: 2023-01-02 11:20:17.611265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa481f6b55b0'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='birthname')


def downgrade() -> None:
    op.alter_column('students', 'birthname', new_column_name='name')
