import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from fact_models import FactArtistByYear, FactGenreByYear, FactSongByYear
from data_processor import DataProcessor
from config import Session, dataSource

session = Session()

dirname = os.path.dirname(__file__)
ds = DataProcessor(os.path.join(dirname, dataSource))
ds.process()

for i, row in ds.artistsByYear().iterrows():
    record = FactArtistByYear(year=row[0],artist=row[1],titles=row[2])
    try:
        session.add(record)
        session.commit()
    except IntegrityError:
        print('FactArtistByYear Record exists for year {}'.format(row[0]))
        session.rollback()
query = session.query(FactArtistByYear)
print('{} records exist in FactArtistByYear'.format(query.count()))

for i, row in ds.genreByYear().iterrows():
    record = FactGenreByYear(year=row[0],genre=row[1],titles=row[2])
    try:
        session.add(record)
        session.commit()
    except IntegrityError:
        print('FactGenreByYear Record exists for year {}'.format(row[0]))
        session.rollback()
query = session.query(FactGenreByYear)
print('{} records exist in FactGenreByYear'.format(query.count()))

for i, row in ds.songByYear().iterrows():
    record = FactSongByYear(year=row[0],song=row[1],popularity=row[2])
    try:
        session.add(record)
        session.commit()
    except IntegrityError:
        print('FactSongByYear Record exists for year {}'.format(row[0]))
        session.rollback()
query = session.query(FactSongByYear)
print('{} records exist in FactSongByYear'.format(query.count()))
