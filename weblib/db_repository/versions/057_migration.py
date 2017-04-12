from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
sent = Table('sent', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('sent_body', UnicodeText(length=280)),
    Column('sent_time', DateTime),
    Column('sent_from_id', Integer),
    Column('sent_to_id', Integer),
    Column('post_type', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['sent'].columns['post_type'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['sent'].columns['post_type'].drop()
