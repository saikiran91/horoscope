from pymongo import MongoClient
from pyhoroscope import Horoscope as horo

sunsigns = ["aries", "taurus", "gemini", "cancer", "leo", "virgo",
            "libra", "scorpio", "stagittarius", "capricorn", "aquarius", "pisces"]
timeframe = ["todays", "weekly", "yearly", "monthly"]

# for sunsign in sunsigns:
#     for j in timeframe:
#         result = eval("horo.get_" + j + "_horoscope(sunsign)")
#         print result
#         print sunsign

client = MongoClient()
db = client.Horoscope
daily = eval("horo.get_todays_horoscope(sunsigns[6])")
result = db.daily.insert_one(daily)
print result.inserted_id
