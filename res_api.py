from flask import Flask
from flask import request, jsonify
from pymongo import MongoClient
from horoscope import *

app = Flask(__name__)
client = MongoClient()


@app.route('/')
def index():
    return "Welcome TO BLACK HOLE", response_ok


def get_horoscope_for_date(date):
    db = client.Horoscope
    horoscope = db.daily.find({'_id': False}, {'date': {'$in': date}})  # find('_id' : { $in : [1,2,3,4] } })
    if horoscope.count() > 0:
        from bson import json_util
        return json_util.dumps(horoscope, default=json_util.default), response_ok
        # return JSONEncoder().encode(horoscope), response_ok
    else:
        return "Please move along nothing to see here", response_invalid


def get_horoscope_for_day():
    db = client.Horoscope
    horolist = db.daily.find().sort([['_id', -1]]).limit(3)  # get last 3 createad items

    if horolist.count() > 0:
        from bson import json_util
        return json_util.dumps(horolist, default=json_util.default), response_ok
        # return JSONEncoder().encode(horolist), response_ok
    else:
        return "Please move along nothing to see here", response_invalid

    pass


@app.route('/hma_horoscope_for_date', methods=['GET', 'POST'])
def getHoroscope():
    if request.method == 'GET':
        date = request.args.getlist('date')
        return get_horoscope_for_date(date)
    else:
        return "ONLY GOD CAN POST", response_invalid


@app.route('/hma_horoscope_for_tty', methods=['GET', 'POST'])
def get_three_day_horoscope():
    if request.method == 'GET':
        return get_horoscope_for_day()
    else:
        return "ONLY GOD CAN POST", response_invalid


if __name__ == '__main__':
    app.run(host="192.168.1.38",port=5010,debug=True)
