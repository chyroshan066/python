import requests
import json
import pprint

# response = requests.get("https://www.codewithharry.com")  # Fetching data to the URL
# response = requests.get("https://bigbagla.com")
'''try:
    response = requests.get("https://www.codewithharry.com", timeout=0.0001) # Setting timeout to 0.0001s
except requests.exceptions.Timeout:  # requests library raises "requests.exceptions.Timeout" exception when timeout occurs
    print("TIMED OUT!")'''
# response.raise_for_status()

data = {
    "name": 'Roshan',
    "body": 'bhai',
    "userId": 1,
  }
data2 = {
    "name": "Rahul",
    "body": "dai",
    "userId": 2,
}
headers = {
    'Content-type': 'application/json; charset=UTF-8',
  }
url = "https://jsonplaceholder.typicode.com/posts"

'''requests.post(url, json=data, headers=headers)  # Getting data from the URL
response2 = requests.post(url, json=data2)'''
# print(response2.text)  # Returns the content of the response in UNICODE
# jsonObj = response2.json()  # Returns JSON object
# print(jsonObj["body"])



print(response)