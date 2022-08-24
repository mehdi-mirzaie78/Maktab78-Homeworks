# 2022-08-24 18:11:45
# Created By Mark --*
##########################################
from bs4 import BeautifulSoup
import requests
from unidecode import unidecode
from datetime import datetime
import json

response = requests.get('https://www.time.ir/').content

soup = BeautifulSoup(response, 'lxml')
keys = ("azane_sobh", "tolooe_khorshid", "azane_zohr", "ghoroobe_khorshid", "azane_maghreb", "nime_shab")

values = (unidecode(i.text) for i in soup.find_all("span", "inlineBlock ltr text-nowrap"))
values = (datetime.strptime(i, '%H : %M').time().strftime('%I : %M %p') for i in values)

z = zip(keys, values)
result = {k: v for k, v in z}

with open('oghat_shari.json', 'w') as f:
    json.dump(result, f, indent=2)
