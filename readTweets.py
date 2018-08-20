import json
import requests
from pprint import pprint

FILE_CONTENT = open('tweets.txt','r')

for row in FILE_CONTENT.read().strip().splitlines():
    _parsed = json.loads(row)
    # print json.dumps(_parsed, indent=4, sort_keys = True)
    print json.dumps(_parsed['text'])
