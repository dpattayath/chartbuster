from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FactArtistByYear(Base):
    __tablename__ = 'fact_artist_by_year'

    year = Column(Integer, primary_key=True)
    artist = Column(String)
    titles = Column(Integer)

    def __repr__(self):
        return 'Top artist of {} is {} with {} titles'.format(self.year, self.artist, self.titles)
