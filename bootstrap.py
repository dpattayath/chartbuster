from sqlalchemy import create_engine

engine = create_engine('sqlite:///chartbuster.db')
connection = engine.connect()

# create fact tables
connection.execute("DROP TABLE IF EXISTS fact_artist_by_year")
connection.execute("CREATE TABLE fact_artist_by_year ("
    "year INTEGER PRIMARY KEY,"
    "artist TEXT NOT NULL,"
    "titles INTEGER NOT NULL);")

connection.execute("DROP TABLE IF EXISTS fact_genre_by_year")
connection.execute("CREATE TABLE fact_genre_by_year ("
    "year INTEGER PRIMARY KEY,"
    "genre TEXT NOT NULL,"
    "titles INTEGER NOT NULL);")

connection.execute("DROP TABLE IF EXISTS fact_song_by_year")
connection.execute("CREATE TABLE fact_song_by_year ("
    "year INTEGER PRIMARY KEY,"
    "song TEXT NOT NULL,"
    "popularity INTEGER NOT NULL);")

print(engine.table_names())

connection.close()
