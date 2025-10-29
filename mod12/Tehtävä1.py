import json

import requests



pyyntö = f"https://api.chucknorris.io/jokes/random"
vastaus=requests.get(pyyntö).json()

print(vastaus["value"])