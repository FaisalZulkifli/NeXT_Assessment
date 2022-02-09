from urllib import response
import urllib.request
import json

api_url = 'https://api.wheretheiss.at/v1/satellites/25544'
response = urllib.request.urlopen(api_url)
obj = json.loads(response.read())

longitude = obj['longitude']
print(longitude)
