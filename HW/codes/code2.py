# import json


# my_dict = {"a": "A", "b": "B"}
# new = json.dumps(my_dict)

# print(type(new))
import requests
import json

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url).json()

print(type(response))
def save_to_json(filename='new.json'):
    with open('new.json', 'w') as file:
        json.dump(response, file)

for user in response:
    print(user['name'])

