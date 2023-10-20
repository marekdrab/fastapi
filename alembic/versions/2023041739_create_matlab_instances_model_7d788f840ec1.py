"""create_matlab_instances_model

Revision ID: 7d788f840ec1
Revises: 03a5f76375ee
Create Date: 2023-04-17 22:39:23.222926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7d788f840ec1"
down_revision = "03a5f76375ee"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "matlab_instances",
        sa.Column("id", sa.UUID(as_uuid=False), nullable=False),
        sa.Column("matlab_instance", sa.String(length=50), nullable=False),
        sa.Column("user_email", sa.String(length=254), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("matlab_instance"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("matlab_instances")
    # ### end Alembic commands ###
