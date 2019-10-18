import urllib.request
import json

appid = ''
with open('weather.json','r') as f:
    appid = json.loads(f.read())['appid']
url = 'http://api.openweathermap.org/data/2.5/weather?q=London'+'&appid='+appid

with urllib.request.urlopen(url) as response:
   html = response.read()
   print(json.loads(html))
