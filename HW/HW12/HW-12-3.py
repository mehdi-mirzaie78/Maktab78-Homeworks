import requests
import datetime

response = requests.get('https://api.sunrise-sunset.org/json?lat=34.3277&lng=47.0778&date=today').json()

# kermanshah: 34.3277° N, 47.0778° E

# ########################## calculating timezone ##################################
now_utc = datetime.datetime.utcnow()
now_local = datetime.datetime.now()
time_zone = now_local - now_utc

sunrise = datetime.datetime.strptime(response['results']['sunrise'], "%I:%M:%S %p")
print('sunrise:', (sunrise + time_zone).time())

sunset = datetime.datetime.strptime(response['results']['sunset'], "%I:%M:%S %p")
print('sunset', (sunset + time_zone).time())
