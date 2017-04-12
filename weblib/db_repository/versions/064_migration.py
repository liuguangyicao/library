from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
trade = Table('trade', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('trade_type', String(length=5)),
    Column('body', UnicodeText(length=120), default=ColumnDefault(u'')),
    Column('time', DateTime),
    Column('view', Integer),
    Column('image_name', String(length=30)),
    Column('user_username', String(length=64)),
    Column('old_pay', String(length=10)),
    Column('new_pay', String(length=10)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['trade'].columns['image_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['trade'].columns['image_name'].drop()
