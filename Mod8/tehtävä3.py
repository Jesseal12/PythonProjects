import mysql.connector
##from geopy.geocoders import Nominatim
yhteys = mysql.connector.connect(

    host="127.0.0.1" ,
    database = "flight_game",
    user= "jesse",
    password = "jesseblade",
    autocommit= True
)


def airport1(icao):
    sql = f"SELECT latitude_deg , longitude_deg FROM airport WHERE ident = %s "
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql,(icao,))
    tulos = kursori.fetchall()
    return tulos

def airport1(icao2):
    sql = f"SELECT latitude_deg , longitude_deg FROM airport WHERE ident = %s "
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql,(icao2,))
    tulos2 = kursori.fetchall()
    return tulos2

