# README #

Chartbuster is an app that works based on a kaggle spotify data set and is purely for training purposes and non-commerical use.

### Dataset ###

Spotify top songs per year in the world between 2010-2019.

https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year/data#


### About the app ###

This app uses kaggle dataset (offline version), process it using pandas library and create fact tables for artist, genre and popularity based on year. There are 3 stages for the app:

* migrate - creates fact tables
* loader - loads and process dataset using pandas and import to sqllite
* app - expose an api that will return the stat of the dataset based on year.

http://localhost:5000/api/stat?year=2019

Since these are fact tables, every time the environment is up, it will rebuild and re-process the data.

### Installation instructions ###

~~~~
cd chartbuster
docker-compose build
docker-compose up
~~~~

### Known issues ###

* Since database used is sqllite, multiple thread executions can cause the flask app to crash.
* Possible solutions include flask-sqlalchemy or using a multi-thread transactional database such as postgres or mysql.

### Next stages
* DB migration to Mysql
