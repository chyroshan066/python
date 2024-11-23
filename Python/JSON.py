import json
import requests

dictionary = {
    "course_name": "Python",
    "fee": 15000
}
response = requests.get("https://www.codewithharry.com")
res_text = response.json
print(res_text)

json_format = json.dumps(dictionary)  # Conversion from python object to JSON

# print(type(json_format))