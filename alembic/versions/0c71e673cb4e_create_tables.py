"""create tables

Revision ID: 0c71e673cb4e
Revises: 
Create Date: 2020-03-06 18:53:04.906990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c71e673cb4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tasks_manager',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('file_name', sa.String),
        sa.Column('fails', sa.Boolean),
        sa.Column('processing', sa.Boolean),
        sa.Column('error', sa.String)
        
    )

def downgrade():
    op.drop_table('tasks_manager')
