import requests
from numpy.ma.core import append

# 0K = -273.15
Zip = 'fabb0cc2e2f9a8dadb383c3a9f99a27c'
zipcode = '02600'
isoCode = 'FI'
pyynto=f"https://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{isoCode}&appid={Zip}"



vastaus = requests.get(pyynto).json()
lat = vastaus["lat"]
lon = vastaus["lon"]
desiredValues = []
print(vastaus)
pyynto2=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Zip}"
vastaus2= requests.get(pyynto2).json()
print(vastaus2)
desiredValues.append(vastaus2["main"]["temp"])
saa = vastaus2["weather"][0]["description"]



print(desiredValues)
print(saa)
print(f"{vastaus2["main"]["temp"]-273.15:0.2f} C astetta")