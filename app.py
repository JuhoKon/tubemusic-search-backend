from flask import Flask, request, jsonify
from ytmusicapi import YTMusic

ytmusic = YTMusic()
app = Flask(__name__)


@app.route('/search/', methods=['POST'])
def search_songs():

    search_results = ytmusic.search(
        (request.json.get('search')), filter="songs")
    return jsonify(search_results)


@app.route('/artistsearch/', methods=['POST'])
def search_artists():
    search_results = ytmusic.search(
        (request.json.get('search')), filter="artists")
    return jsonify(search_results)


@app.route('/get_artist/', methods=['POST'])
def get_artist():
    search_results = ytmusic.get_artist(
        (request.json.get('browseid')))
    return jsonify(search_results)


@app.route('/get_playlist/', methods=['POST'])
def get_playlist():

    print(request.json.get('browseid'))
    search_results = ytmusic.get_playlist(
        (request.json.get('browseid')), limit=5000)
    return jsonify(search_results)


@app.route('/get_album/', methods=['POST'])
def get_album():

    search_results = ytmusic.get_album(
        (request.json.get('browseid')))
    return jsonify(search_results)


@app.route('/get_artist_albums/', methods=['POST'])
def get_artist_albums():

    browseid = request.json.get('browseid')
    params = request.json.get("params")

    search_results = ytmusic.get_artist_albums(
        browseid, params)
    return jsonify(search_results)


@app.route('/get_video_watchlist/', methods=['POST'])
def get_video_watchlist():
    videoId = request.json.get('videoid')
    search_results = ytmusic.get_watch_playlist(
        videoId=videoId, limit=1)
    return jsonify(search_results)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    print("Hello I AM SERVER")
    app.run(threaded=True, port=5000)
