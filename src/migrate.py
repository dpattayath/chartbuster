import sqlalchemy as db
from config import engine
from fact_models import FactArtistByYear, FactGenreByYear, FactSongByYear

metadata = db.MetaData()

models = [
    FactArtistByYear.__table__,
    FactGenreByYear.__table__,
    FactSongByYear.__table__
]

metadata.create_all(engine, tables=models, checkfirst=True)

print(engine.table_names())
