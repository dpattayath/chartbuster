from flask import Flask, request, make_response, jsonify
from src.models.fact_artist_by_year import FactArtistByYear
from src.services import StatService

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'Welcome to chartbusters!'

@app.route('/api/stat', methods=["GET"])
def stat():
    resultset = []
    year = request.args.get('year', None)
    if year:
        service = StatService()

        topArtist = service.getTopArtistByYear(year)
        if topArtist:
            resultset.append(str(topArtist))

        topGenre = service.getTopGenreByYear(year)
        if  topGenre:
            resultset.append(str(topGenre))

        topSong = service.getTopSongByYear(year)
        if  topGenre:
            resultset.append(str(topSong))

        return jsonify(resultset)

    return ""

app.run(port=5000)

