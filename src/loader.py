import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fact_models import FactArtistByYear, FactGenreByYear, FactSongByYear
from data_processor import DataProcessor
from config import Session

session = Session()

dirname = os.path.dirname(__file__)
ds = DataProcessor(os.path.join(dirname, "data/top10s.csv"))
ds.process()

for i, row in ds.artistsByYear().iterrows():
    record = FactArtistByYear(year=row[0],artist=row[1],titles=row[2])
    session.add(record)
    session.commit()

query = session.query(FactArtistByYear)
print(query.count())

for i, row in ds.genreByYear().iterrows():
    record = FactGenreByYear(year=row[0],genre=row[1],titles=row[2])
    session.add(record)
    session.commit()

query = session.query(FactGenreByYear)
print(query.count())

for i, row in ds.songByYear().iterrows():
    record = FactSongByYear(year=row[0],song=row[1],popularity=row[2])
    session.add(record)
    session.commit()

query = session.query(FactSongByYear)
print(query.count())

