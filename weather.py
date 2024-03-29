from bs4 import BeautifulSoup
import requests
from sys import argv
import json
import os

weather = {}

if len(argv) > 2:
    lat = argv[1]
    lon = argv[2]
else:
    lat = 44.918355000000076
    lon = -93.32269499999995

if len(argv) > 3:
    fileLocation = argv[3]
else:
    fileLocation = "."

weather["lat"] = lat
weather["lon"] = lon

request = requests.get(f"https://forecast.weather.gov/MapClick.php?lat={lat}&lon={lon}")
soup = BeautifulSoup(request.content, "html.parser")

F = (soup.select_one("p.myforecast-current-lrg")).string
weather["F"] = F
C = (soup.select_one("p.myforecast-current-sm")).string
weather["C"] = C

condition = soup.select_one("p.myforecast-current").string
weather["Condition"] = condition

table = soup.select("table > tr")
for element in table:
    tds = element.select("td")
    title = tds[0].string.strip()
    value = tds[1].string.strip()
    weather[title.replace(" ","_")] = value
    
imageURL = (soup.select_one("img.pull-left")).get("src")
image = requests.get(f"https://forecast.weather.gov/{imageURL}")

timeDir = weather["Last_update"].replace(":",";")

os.makedirs(f"{fileLocation}\\Weather Dumps\\{lat}, {lon} - {timeDir}")

with open(f"{fileLocation}\\Weather Dumps\\{lat}, {lon} - {timeDir}\\image.png", "wb") as f:
    f.write(image.content)

with open(f"{fileLocation}\\Weather Dumps\\{lat}, {lon} - {timeDir}\\weather.json", "w+", encoding = "utf-8") as f:
    json.dump(weather, f)