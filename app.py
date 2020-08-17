from flask import Flask, request, jsonify
from ytmusicapi import YTMusic

ytmusic = YTMusic()
app = Flask(__name__)


@app.route('/search/', methods=['POST'])
def hello_world():

    search_results = ytmusic.search(
        (request.json.get('search')), filter="songs")
    return jsonify(search_results)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    print("Hello I AM SERVER")
    app.run(threaded=True, port=5000)
