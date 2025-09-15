import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    database="flight_game",
    user="jesse",
    password="jesseblade",
    autocommit=True
)


def haeLentoKentat():
    sql = "SELECT * FROM airport"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()

    return tulos


def haeLentokentta(koodi):
    sql = f"SELECT * FROM airport WHERE ident=%s;"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql,(koodi,))
    tulos = kursori.fetchall()
    return tulos


print(haeLentokentta("EFHK"))
code = input("syötä koodi")
kentta = haeLentokentta(code)
kentat = haeLentoKentat()
for k in kentta :
    print(f"Nimi : {k[3]}")

for kentta in kentat:
    print(f"Nimi : {kentta[3]}")
