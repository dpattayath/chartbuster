
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models import FactArtistByYear, FactGenreByYear, FactSongByYear
from src.services import CsvDataProcessor

class StatService():
    def __init__(self):
        engine = create_engine('sqlite:///chartbuster.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def getTopArtistByYear(self, year: int):
        return self.session.query(FactArtistByYear).filter_by(year=year).first()

    def getTopGenreByYear(self, year: int):
        return self.session.query(FactGenreByYear).filter_by(year=year).first()

    def getTopSongByYear(self, year: int):
        return self.session.query(FactSongByYear).filter_by(year=year).first()
