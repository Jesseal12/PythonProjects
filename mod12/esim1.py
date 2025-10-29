import json

import requests

hakusana = input("Anna hakusana : ")
pyyntö = f"https://api.tvmaze.com/search/shows?q=" + hakusana

#sarjat = requests.get(pyyntö).json()
try:
 vastaus = requests.get(pyyntö)
 if not vastaus.ok :
     print("Joking meni pieleen")
     sarjat = requests.get(pyyntö).json()
     if len(sarjat)== 0:
         raise Exception
     for sarja in sarjat :
            print(sarja["show"]["name"])
except requests.exceptions.RequestException as e:
      print(f"Haussa tapahtui joking virhe")


except Exception as e:
       print(e)


print("Toimii")

#print(json.dumps(vastaus,indent=2))

#print(vastaus[0]["show"]["name"])

#for sarja in sarjat :
 #   print(sarja["show"]["name"])
