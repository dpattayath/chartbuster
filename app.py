from flask import Flask, request, make_response, jsonify
from src.query_service import QueryService

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'Welcome to chartbusters!'

@app.route('/api/stat', methods=["GET"])
def stat():
    resultset = []
    year = request.args.get('year', None)
    if year:
        service = QueryService()

        topArtist = service.getTopArtistByYear(year)
        if topArtist:
            resultset.append(str(topArtist))

        topGenre = service.getTopGenreByYear(year)
        if  topGenre:
            resultset.append(str(topGenre))

        topSong = service.getTopSongByYear(year)
        if  topGenre:
            resultset.append(str(topSong))

        return make_response(jsonify(resultset), 200)

    return make_response(jsonify(""), 204)

# run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

