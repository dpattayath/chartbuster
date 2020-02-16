from sqlalchemy import create_engine

engine = create_engine('sqlite:///chartbuster.db')

# create fact tables
engine.execute("DROP TABLE IF EXISTS fact_artist_by_year")
engine.execute("CREATE TABLE fact_artist_by_year ("
    "year INTEGER PRIMARY KEY,"
    "artist TEXT NOT NULL,"
    "titles INTEGER NOT NULL);")

engine.execute("DROP TABLE IF EXISTS fact_genre_by_year")
engine.execute("CREATE TABLE fact_genre_by_year ("
    "year INTEGER PRIMARY KEY,"
    "genre TEXT NOT NULL,"
    "titles INTEGER NOT NULL);")

engine.execute("DROP TABLE IF EXISTS fact_song_by_year")
engine.execute("CREATE TABLE fact_song_by_year ("
    "year INTEGER PRIMARY KEY,"
    "song TEXT NOT NULL,"
    "popularity INTEGER NOT NULL);")

print(engine.table_names())
