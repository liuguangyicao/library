from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
test = Table('test', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('test', DATETIME),
)

username_password = Table('username_password', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=64)),
    Column('password', VARCHAR(length=64)),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('post_time', DateTime),
    Column('post_article', UnicodeText(length=50)),
    Column('post_body', UnicodeText(length=280)),
    Column('post_type', Integer),
    Column('post_num', Integer, default=ColumnDefault(0)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['test'].drop()
    pre_meta.tables['username_password'].drop()
    post_meta.tables['post'].columns['post_type'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['test'].create()
    pre_meta.tables['username_password'].create()
    post_meta.tables['post'].columns['post_type'].drop()
