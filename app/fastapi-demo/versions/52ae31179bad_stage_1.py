"""stage 1

Revision ID: 52ae31179bad
Revises: 
Create Date: 2022-05-07 22:54:30.470974

"""
from lib2to3.pgen2.token import COLON
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String, Integer
from sqlalchemy.schema import Sequence, CreateSequence

# revision identifiers, used by Alembic.
revision = "52ae31179bad"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('create schema "fast-api-demo"')
    op.execute(CreateSequence(Sequence("table_sid_seq")))
    op.create_table(
        "student_data",
        Column(
            "s_id",
            Integer,
            nullable=False,
            server_default=sa.text("nextval('table_sid_seq'::regclass)"),
        ),
        Column("name", String, nullable=False),
        Column("degree", String, nullable=False),
        Column("section", String, nullable=False),
        schema="fastapi-demo",
    )


def downgrade():
    op.drop_table("student_data", schema="fastapi-demo")
    op.execute('drop schema "fast-api-demo" cascade')
    pass
