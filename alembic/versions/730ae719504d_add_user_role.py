"""add user role

Revision ID: 730ae719504d
Revises:
Create Date: 2026-08-09 17:11:19.482906
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "730ae719504d"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    user_role = sa.Enum(
        "ADMIN",
        "USER",
        name="userrole"
    )

    user_role.create(op.get_bind())

    op.add_column(
        "users",
        sa.Column(
            "role",
            user_role,
            nullable=True
        )
    )

    op.execute(
        "UPDATE users SET role = 'USER' WHERE role IS NULL"
    )

    op.alter_column(
        "users",
        "role",
        nullable=False
    )


def downgrade() -> None:

    op.drop_column(
        "users",
        "role"
    )

    user_role = sa.Enum(
        "ADMIN",
        "USER",
        name="userrole"
    )

    user_role.drop(op.get_bind())