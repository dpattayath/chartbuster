from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FactGenreByYear(Base):
    __tablename__ = 'fact_genre_by_year'

    year = Column(Integer, primary_key=True)
    genre = Column(String)
    titles = Column(Integer)

    def __repr__(self):
        return 'Top genre of {} is {} with {} titles'.format(self.year, self.genre, self.titles)
