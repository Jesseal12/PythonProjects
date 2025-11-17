import mysql.connector
from flask import Flask,request
import json

yhteys = mysql.connector.connect(
    host = "127.0.0.1" ,
    database = "flight_game" ,
    user = "jesse",
    password = "jesseblade",
    autocommit = True

)







app = Flask(__name__)


@app.route('/kenttä/<string:koodi>')
def kentta(koodi):
    sql=f"SELECT * FROM airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    arvo = kursori.fetchone()

    vastaus= {
       "ICAO": arvo["ident"],

       "Name": arvo["name"],
       "Municipality":arvo["municipality"]
     }

    return vastaus

if __name__ =='__main__':
   app.run(use_reloader=True,host='127.0.0.1',port =3000)

#icaoArvo = input("anna  ICAO koodi : ")

