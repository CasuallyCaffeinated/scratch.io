"""creating tables

Revision ID: f7823dc468a8
Revises: 
Create Date: 2021-05-24 16:13:50.007220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7823dc468a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gamejams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('theme', sa.String(), nullable=False),
    sa.Column('blurb', sa.Text(), nullable=False),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('github', sa.String(), nullable=True),
    sa.Column('userLimit', sa.Integer(), nullable=False),
    sa.Column('startDate', sa.Date(), nullable=False),
    sa.Column('endDate', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('blurb', sa.String(length=255), nullable=True),
    sa.Column('avatarUrl', sa.String(length=255), nullable=True),
    sa.Column('githubUrl', sa.String(length=255), nullable=True),
    sa.Column('websiteUrl', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('blurb', sa.Text(), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('github', sa.String(), nullable=True),
    sa.Column('recruiting', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('users_games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('gameId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gameId'], ['games.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_games')
    op.drop_table('users')
    op.drop_table('teams')
    op.drop_table('skills')
    op.drop_table('games')
    op.drop_table('gamejams')
    # ### end Alembic commands ###
