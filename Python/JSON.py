import json
import requests
from pprint import pprint

dictionary = {
    "course_name": "Python",
    "fee": 15000
}
json_format = json.dumps(dictionary)  # Conversion from python object to JSON
# print(type(json_format))

response = requests.get("https://jsonplaceholder.typicode.com/posts")
dict_format = json.loads(response.text)  # Converts JSON object to dict
# pprint(dict_format["title"])
for item in dict_format:
    if item["id"] == 5:
        print(item["title"])

