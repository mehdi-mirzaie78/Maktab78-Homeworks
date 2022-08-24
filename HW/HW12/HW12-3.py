import requests
import datetime
import pytz

response = requests.get('https://api.sunrise-sunset.org/json?lat=34.3277&lng=47.0778&date=today').json()

# kermanshah: 34.3277° N, 47.0778° E

# ############################ calculating timezone ############################
# Solution 1
now_utc = datetime.datetime.utcnow()
now_local = datetime.datetime.now()
time_zone = now_local - now_utc

# # Solution 2 for calculating timezone
# tz = pytz.timezone('Asia/Tehran')
# time_zone = tz.utcoffset(dt=datetime.datetime.utcnow())

# ######################### converting to local time ###########################
sunrise = datetime.datetime.strptime(response['results']['sunrise'], "%I:%M:%S %p")
print('Sunrise:', (sunrise + time_zone).time())

sunset = datetime.datetime.strptime(response['results']['sunset'], "%I:%M:%S %p")
print('Sunset:', (sunset + time_zone).time())
