import requests
import re
import json
from urllib.request import urlopen
import arrow
from datetime import datetime
import datetime as DT
import time


lat = 55.96
lon = -10.76

with open('2023-04-18_09_00_46--2023-04-18_09_15_46.json', 'r') as f:
    data = json.loads(f.read())

dt_start = data["parameters"]["pm18"]["data"][0]["dt"]
dt_end = data["parameters"]["pm18"]["data"][len(data["parameters"]["pm18"]["data"])-1]["dt"]

dt_start = datetime.strptime(dt_start, '%Y-%m-%d %H:%M:%S')
dt_end = datetime.strptime(dt_end, '%Y-%m-%d %H:%M:%S')

response = requests.get(
  'https://api.stormglass.io/v2/weather/point',
  params={
    'lat': lat,
    'lng': lon,
    'params': ','.join(['waveHeight', 'waveDirection','wavePeriod', 'seaLevel', 'iceCover', 'currentDirection', 'currentSpeed']),
    'start': dt_start,
    'end': dt_end
  },
  headers={
    'Authorization': 'f04b164a-c3d8-11ed-a654-0242ac130002-f04b171c-c3d8-11ed-a654-0242ac130002'
  }
)
json_data = response.json()
print (json_data)
for item in json_data["hours"]:
    print(f"Время: {item['time']}")
    print(f"Коэффициент заледенения: {item['iceCover']['noaa']}")
    print(f"Уровень моря: {item['seaLevel']['sg']} км")
    print(f"Высота волны: {item['waveHeight']['meteo']} метров")
    print(f"Направление волны: {item['waveDirection']['meteo']} градусов от северного направления")
    print(f"Период волн: {item['wavePeriod']['meteo']} секунд")
    print(f"Направление течения: {item['currentDirection']['sg']} градусов от северного направления")
    print(f"Скорость течения: {item['currentSpeed']['sg']} метров в секунду")
