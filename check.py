from pymongo import MongoClient

client = MongoClient()


def get_horoscope(date):
    db = client.Horoscope
    horoscope = db.daily.find_one({'date': date})
    if horoscope > 0:
        return horoscope
    else:
        return "nothing"

print get_horoscope("14-09-2016")