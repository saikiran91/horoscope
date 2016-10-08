from pymongo import MongoClient
from datetime import datetime
from pytz import timezone
import re
from pyhoroscope import Horoscope as horo

sunSigns = ["aries", "taurus", "gemini", "cancer", "leo", "virgo",
            "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
timeFrame = ["todays", "weekly", "yearly", "monthly"]
dayFrame = ["todays", "tomorrow"]
# tomorrow #yesterday
client = MongoClient()


def add_to_mongo(horoscope_list):
    db = client.Horoscope
    dateId = horoscope_list[0].get("date")
    print  dateId
    asia_calcutta = timezone('Asia/Calcutta')
    horoscope_item = {
        'date': dateId,
        'createdAt': datetime.now(asia_calcutta).strftime("%Y-%m-%d %H:%M:%S %z"),
        'horoscope': horoscope_list
    }
    if db.daily.find_one({'date': dateId}) > 0:
        print dateId + " already exist"
    else:
        result = db.daily.insert_one(horoscope_item)
        print dateId + " inserted " + str(result.inserted_id)
        pass


for day in dayFrame:
    horolist = []
    for sunSign in sunSigns:
        horoscopeForSign = eval("horo.get_" + day + "_horoscope(sunSign)")
        horolist.append(horoscopeForSign)
    add_to_mongo(horolist)

# for sunsign in sunsigns:
#     for j in timeframe:
#         result = eval("horo.get_" + j + "_horoscope(sunsign)")
#         print result
#         print sunsign

# db = client.Horoscope
# daily = eval("horo.get_todays_horoscope(sunsigns[1])")
# result = db.daily.insert_one(daily)
# print result.inserted_id


# horoscopeList = []
# for sunSign in sunSigns:
#     horoscopeForSign = eval("horo.get_tomorrow_horoscope(sunSign)")
#     horoscopeList.append(horoscopeForSign)
