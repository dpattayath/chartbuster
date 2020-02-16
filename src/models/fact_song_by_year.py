from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FactSongByYear(Base):
    __tablename__ = 'fact_song_by_year'

    year = Column(Integer, primary_key=True)
    song = Column(String)
    popularity = Column(Integer)

    def __repr__(self):
        return 'Top song of {} is {} with {} popularity'.format(self.year, self.song, self.popularity)
