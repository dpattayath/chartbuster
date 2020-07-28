# README #

Chartbuster is an app that consumes a kaggle data set of spotify top chart busters and expose stats via a flask api.

### Dataset ###

Spotify top songs per year during the period 2010 - 2019.

https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year/data#


### About the app ###

This app consumes kaggle spotify dataset (offline version) using pandas and create fact tables for artist, genre and popularity based on year. There are 3 stages for the app:

* migrate - creates fact tables
* loader - consumes dataset using pandas and import to db (sqllite)
* app - expose flask api that will return the stat of the dataset based on year.

http://localhost:5000/api/stat?year=2019


### Installation instructions ###

~~~~
cd chartbuster
docker-compose build
docker-compose up
~~~~

### Known issues ###

* Since database used is sqllite, multiple thread executions can cause the flask app to crash.
* Possible solutions include flask-sqlalchemy or using a multi-thread transactional database such as postgres or mysql.
