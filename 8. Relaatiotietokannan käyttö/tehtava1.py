import mysql.connector
yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'salasana',
    autocommit = True
)
def haelentokentta(x):
    sql = "SELECT name, municipality FROM airport WHERE ident="
    sql += '"'+x+'"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
koodi=input("anna lentokentän ICAO-koodi: ")
haelentokentta(koodi)