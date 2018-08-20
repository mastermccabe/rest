import json
import requests
from pprint import pprint

FILE_CONTENT = open('tweets.txt','r')
count = 1

HEADERS = {



    }
URL = "https://mccabe-tonna-test.beekeeper.io/api/2/streams/27197/posts.json"

for row in FILE_CONTENT.read().strip().splitlines():
    print("===========",count,"=============")
    _parsed = json.loads(row)
    # print json.dumps(_parsed ,indent=2,sort_keys=True) //this prints all

    text = json.dumps(_parsed['text']) # Pretty printed
    title = json.dumps(_parsed['user']['name'])
    count=count+1

    payload = { 'text': text, 'title': title }
    or
    payload = {
        'text':_parsed['text'],
        'title':_parsed['user']['name']
    }

    response = requests.request("POST", URL, json=payload, headers=HEADERS)

    print(payload)
    print(response.text)
    # break
    # could check for 200 (success)
    print("========================")
