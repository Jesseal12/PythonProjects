import mysql.connector
from flask import Flask,request
from flask_cors import CORS

yhteys = mysql.connector.connect(
    host = "127.0.0.1" ,
    database = "flight_game" ,
    user = "jesse",
    password = "jesseblade",
    autocommit = True

)







app = Flask(__name__)
cors = CORS(app)

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
    try:
      if vastaus is None:
          return {"error":"lentokenttää ei löydy"},404
      return vastaus

    except mysql.connector.errors.ProgrammingError as err :
        print('täällä')
        return {"error":str(err)},500

if __name__ =='__main__':
   app.run(use_reloader=True,host='127.0.0.1',port =3000)

#icaoArvo = input("anna  ICAO koodi : ")

