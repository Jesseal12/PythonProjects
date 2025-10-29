import requests

# 0K = -273.15

pyynto=f"http://api.openweathermap.org/geo/1.0/zip?zip={"02600"},{"358"}&appid={ "3b471b3d712fd3bb80459c6b2cdb37ca "}"

vastaus = requests.get(pyynto)

print(pyynto)