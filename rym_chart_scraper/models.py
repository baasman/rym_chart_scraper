from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float

from . import settings

Base = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_topalbums_table(engine):
    Base.metadata.create_all(engine)


class TopAlbums(Base):

    __tablename__ = 'top_albums'

    id = Column(Integer, primary_key=True)
    Artist = Column('Artist', String)
    Album = Column('Album', String)
    Chart_year = Column('Chart_year', Integer)
    Genre = Column('Genre', String)
    RYMRating = Column('RYMRating', Float)
    Ratings = Column('Ratings', Integer)
    Reviews = Column('Reviews', Integer)
    Date = Column('Date', DateTime)
