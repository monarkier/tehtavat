import mysql.connector
import geopy.distance

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='salasana',
    autocommit=True
)


def haelentokenttia(x,y):
    sql1 = "SELECT longitude_deg, latitude_deg FROM airport WHERE ident="
    sql1 += '"'+x+'"'
    sql2 = "SELECT longitude_deg, latitude_deg  FROM airport WHERE ident="
    sql2 += '"' + y + '"'
    kursori=yhteys.cursor()
    kursori.execute(sql1)
    airport1 = kursori.fetchone()
    kursori.execute(sql2)
    airport2 = kursori.fetchone()
    print(geopy.distance.distance(airport1,airport2).km)
    #print(airport1,airport2)


koodi1 = input("anna ensimmäisen lentokentän ICAO-koodi: ")
koodi2 = input("anna toisen lentokentän ICAO-koodi: ")
haelentokenttia(koodi1,koodi2)