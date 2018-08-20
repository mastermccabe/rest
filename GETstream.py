import requests
import json
from pprint import pprint

URL = "https://mccabe-tonna-test.beekeeper.io/api/2/streams/27197/posts.json"

PAYLOAD = {
    'title':'title',
    'text':'text'
}
HEADERS = {

    }

RESPONSE = requests.request("GET", URL, json=PAYLOAD, headers=HEADERS)

# print RESPONSE.text

for row in json.loads(RESPONSE.text):
    print json.dumps(row,indent=4, sort_keys = True)
    # print json.dumps(row['text'])
    # print json.dumps(row['title'])
