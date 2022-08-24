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

# module
# ##############################################################################
def sun_rise_set(timezone_name: str, latitude: str, longitude: str) -> dict[datetime.time]:
    response = requests.get('https://api.sunrise-sunset.org/json', params={'lat': latitude, 'lng': longitude}).json()
    tz = pytz.timezone(timezone_name)
    time_zone = tz.utcoffset(dt=datetime.datetime.utcnow())
    sunrise = datetime.datetime.strptime(response['results']['sunrise'], "%I:%M:%S %p")
    sunset = datetime.datetime.strptime(response['results']['sunset'], "%I:%M:%S %p")
    result = {'sunrise': str((sunrise + time_zone).time()), 'sunset': str((sunset + time_zone).time())}
    return result


print(sun_rise_set('Asia/Tehran', '34.3277', '47.0778'))
