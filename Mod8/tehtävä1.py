import mysql.connector


yhteys = mysql.connector.connect(
    host = "127.0.0.1" ,
    database = "flight_game" ,
    user = "jesse",
    password = "jesseblade",
    autocommit = True

)

def lentoKenttaHaku(koodi):
    sql=f"SELECT * FROM airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    arvo = kursori.fetchall()

    return arvo
icaoArvo = input("anna  ICAO koodi : ")

print(lentoKenttaHaku(icaoArvo))