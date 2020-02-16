from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models import FactArtistByYear, FactGenreByYear, FactSongByYear
from src.services import CsvDataProcessor

engine = create_engine('sqlite:///chartbuster.db')

Session = sessionmaker(bind=engine)
session = Session()

ds = CsvDataProcessor("data/top10s.csv")
ds.process()

for i, row in ds.artistsByYear().iterrows():
    record = FactArtistByYear(year=row[0],artist=row[1],titles=row[2])
    session.add(record)
query = session.query(FactArtistByYear)
print(query.count())

for i, row in ds.genreByYear().iterrows():
    record = FactGenreByYear(year=row[0],genre=row[1],titles=row[2])
    session.add(record)
query = session.query(FactGenreByYear)
print(query.count())

for i, row in ds.songByYear().iterrows():
    record = FactSongByYear(year=row[0],song=row[1],popularity=row[2])
    session.add(record)
query = session.query(FactSongByYear)
print(query.count())

