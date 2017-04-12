from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
trade = Table('trade', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('trade_type', VARCHAR(length=5)),
    Column('body', TEXT(length=120)),
    Column('time', DATETIME),
    Column('view', INTEGER),
    Column('user_username', INTEGER),
    Column('old_pay', VARCHAR(length=10)),
    Column('new_pay', VARCHAR(length=10)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['trade'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['trade'].create()
