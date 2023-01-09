import requests
import os 
import urllib
import json

def get_loc(ip):
    url = "http://ip-api.com/json/"
    response = urllib.request.urlopen (url + ip)
    data = response.read()
    values = json.loads(data)
    return values['lat'] + values['lon']

print(get_loc('66.249.66.75'))