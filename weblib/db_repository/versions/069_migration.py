from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
seat = Table('seat', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('num', INTEGER),
    Column('floor', INTEGER),
    Column('elec', INTEGER),
    Column('water', INTEGER),
    Column('sun', INTEGER),
    Column('lift', INTEGER),
)

sort = Table('sort', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('sort_type', INTEGER),
    Column('body', TEXT(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['seat'].drop()
    pre_meta.tables['sort'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['seat'].create()
    pre_meta.tables['sort'].create()
