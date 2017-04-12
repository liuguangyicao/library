from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
userinfo = Table('userinfo', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', UnicodeText(length=16), default=ColumnDefault(u'')),
    Column('sexy', UnicodeText(length=4), default=ColumnDefault(u'')),
    Column('code', String(length=15), default=ColumnDefault('')),
    Column('qq', String(length=15), default=ColumnDefault('')),
    Column('tele', String(length=15), default=ColumnDefault('')),
    Column('email', String(length=40), default=ColumnDefault('')),
    Column('introduce', UnicodeText(length=120), default=ColumnDefault(u'')),
    Column('image', Boolean, default=ColumnDefault(False)),
    Column('image_name', String(length=20)),
    Column('user_username', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['userinfo'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['userinfo'].drop()
