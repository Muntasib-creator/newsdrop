"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}

# Get the next migration number
import os
import re

def get_next_migration_number():
    versions_dir = os.path.join(os.path.dirname(__file__), 'versions')
    if not os.path.exists(versions_dir):
        return '001'
    
    existing_files = [f for f in os.listdir(versions_dir) if f.endswith('.py')]
    if not existing_files:
        return '001'
    
    # Extract numbers from existing files
    numbers = []
    for f in existing_files:
        match = re.match(r'(\d+)_', f)
        if match:
            numbers.append(int(match.group(1)))
    
    if not numbers:
        return '001'
    
    next_num = max(numbers) + 1
    return f"{next_num:03d}"

# Store the next migration number
next_migration_number = get_next_migration_number()

def upgrade() -> None:
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    ${downgrades if downgrades else "pass"} 