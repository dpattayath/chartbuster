
from src.fact_models import FactArtistByYear, FactGenreByYear, FactSongByYear
from .config import Session

class QueryService():
    def __init__(self):
        self.session = Session()

    """
    get top artist by year from fact table
    """
    def getTopArtistByYear(self, year: int):
        return self.session.query(FactArtistByYear).filter_by(year=year).first()

    """
    get top genre by year from fact table
    """
    def getTopGenreByYear(self, year: int):
        return self.session.query(FactGenreByYear).filter_by(year=year).first()

    """
    get top songs by year from fact table
    """
    def getTopSongByYear(self, year: int):
        return self.session.query(FactSongByYear).filter_by(year=year).first()
