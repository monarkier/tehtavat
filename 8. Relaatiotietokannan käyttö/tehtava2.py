import mysql.connector
yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'salasana',
    autocommit = True
)
def haelentokenttia(x):
    list = ("balloonport","closed","heliport","large_airport","medium_airport","seaplane_base","small_airport")
    #bp=0, c=1, hp=2, la=3, ma=4, sb=5, sa=6
    kursori = yhteys.cursor()

    for i in list:
        b = "SELECT count(type) FROM airport WHERE iso_country="
        b += '"'+x+'"'
        b += "AND type="
        b+= '"'+i+'"'
        kursori.execute(b)
        print( i," : ",kursori.fetchall())
        

koodi=input("anna lentokentän maakoodi: ")
haelentokenttia(koodi)