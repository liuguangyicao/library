from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
talk = Table('talk', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('view', BOOLEAN),
    Column('user_username', INTEGER),
    Column('user_id', INTEGER),
)

talk = Table('talk', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('talk_from', Integer),
    Column('talk_to', Integer),
    Column('view', Boolean, default=ColumnDefault(False)),
    Column('datetime', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['talk'].columns['user_id'].drop()
    pre_meta.tables['talk'].columns['user_username'].drop()
    post_meta.tables['talk'].columns['datetime'].create()
    post_meta.tables['talk'].columns['talk_from'].create()
    post_meta.tables['talk'].columns['talk_to'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['talk'].columns['user_id'].create()
    pre_meta.tables['talk'].columns['user_username'].create()
    post_meta.tables['talk'].columns['datetime'].drop()
    post_meta.tables['talk'].columns['talk_from'].drop()
    post_meta.tables['talk'].columns['talk_to'].drop()
