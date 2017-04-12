from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
recommend = Table('recommend', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('article', UnicodeText(length=20), default=ColumnDefault(u'')),
    Column('writer', UnicodeText(length=20), default=ColumnDefault(u'')),
    Column('body', UnicodeText(length=120), default=ColumnDefault(u'')),
    Column('image', String(length=30), default=ColumnDefault('')),
    Column('recommend_name', String(length=30), default=ColumnDefault('')),
    Column('click', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['recommend'].columns['click'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['recommend'].columns['click'].drop()
