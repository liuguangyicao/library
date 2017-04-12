from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
userinfo = Table('userinfo', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', TEXT(length=16)),
    Column('sexy', TEXT(length=4)),
    Column('code', VARCHAR(length=15)),
    Column('qq', VARCHAR(length=15)),
    Column('tele', VARCHAR(length=15)),
    Column('email', VARCHAR(length=40)),
    Column('introduce', TEXT(length=120)),
    Column('user_username', INTEGER),
    Column('image', BOOLEAN),
    Column('image_name', VARCHAR(length=20)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['userinfo'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['userinfo'].create()
