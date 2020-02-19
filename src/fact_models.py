import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FactArtistByYear(Base):
    __tablename__ = 'fact_artist_by_year'

    year = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(100))
    titles = db.Column(db.SmallInteger)

    def __repr__(self):
        return 'Top artist of {} is {} with {} titles'.format(self.year, self.artist, self.titles)


class FactGenreByYear(Base):
    __tablename__ = 'fact_genre_by_year'

    year = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100))
    titles = db.Column(db.SmallInteger)

    def __repr__(self):
        return 'Top genre of {} is {} with {} titles'.format(self.year, self.genre, self.titles)


class FactSongByYear(Base):
    __tablename__ = 'fact_song_by_year'

    year = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String(255))
    popularity = db.Column(db.SmallInteger)

    def __repr__(self):
        return 'Top song of {} is {} with {} popularity'.format(self.year, self.song, self.popularity)
