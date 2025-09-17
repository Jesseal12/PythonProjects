import mysql.connector

yhteys = mysql.connector.connect(
    host = "127.0.0.1" ,
    database = "flight_game" ,
    user = "jesse",
    password = "jesseblade",
    autocommit = True

)

def isoCountryHaku(koodi):
    sql = f"SELECT type , count(*) FROM airport WHERE iso_country = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql,(koodi,))
    arvo=kursori.fetchall()
    return arvo

maakoodi = input("Syötä maakoodi : ")

maa = isoCountryHaku(maakoodi)

for row in maa :
    print(f" {row[3]} lentokenttää ")