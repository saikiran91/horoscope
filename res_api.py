from flask import Flask
from flask import request, jsonify
from pymongo import MongoClient
from horoscope import *

app = Flask(__name__)
client = MongoClient()


@app.route('/')
def index():
    return "Welcome TO BLACK HOLE", response_ok


def get_horoscope(date):
    db = client.Horoscope
    horoscope = db.daily.find_one({'date': date})
    if horoscope > 0:
        from bson import json_util
        # return json_util.dumps(horoscope), response_ok
        return JSONEncoder().encode(horoscope), response_ok
    else:
        return "Please move along nothing to see here", response_invalid


@app.route('/hma_horoscope', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        date = request.args.get('date')
        return get_horoscope(date)
    else:
        return "ONLY GOD CAN POST", response_invalid


if __name__ == '__main__':
    app.run(debug=True)
