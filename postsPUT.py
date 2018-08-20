import json
import requests
from pprint import pprint
# -*- coding: utf-8 -*-

HEADERS = {

    }


URL = "https://mccabe-tonna-test.beekeeper.io/api/2/posts/3255934"


PAYLOAD = {
    'text':'Time to start building in our country, with American workers &amp; with American iron, aluminum &amp; steel. It is time to\u2026 https://t.co/rGZCRyeCMZ',
    'title':'Update 2',
    'sticky':'false'
    }




response = requests.request("PUT", URL, json=PAYLOAD, headers=HEADERS)

print PAYLOAD
print(response.text)
