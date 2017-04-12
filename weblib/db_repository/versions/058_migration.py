from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
seat = Table('seat', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('num', Integer),
    Column('floor', Integer),
    Column('elec', Integer),
    Column('water', Integer),
    Column('sun', Integer),
    Column('lift', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['seat'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['seat'].drop()
