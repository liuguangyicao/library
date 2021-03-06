from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
talk = Table('talk', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('talk_from', Integer),
    Column('talk_to', String(length=64)),
    Column('view', Boolean, default=ColumnDefault(False)),
    Column('datetime', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['talk'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['talk'].drop()
