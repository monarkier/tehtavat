lista = {}
while True:
    print("\n 1 Syötä uusi lentoasema \n 2 hae lentoaseman tiedot \n 3 lopeta \n")
    x = int(input("Mitä haluat tehdä: \n"))
    if x == 3:
        break
    elif x == 1:
        nimi = input("Syötä lentoaseman nimi: \n")
        koodi = input("Syötä lentoaseman ICAO-koodi: \n")
        lista[koodi]=(nimi)
    elif x == 2:
        koodi = input("Syötä lentoaseman ICAO-koodi: \n")
        asema = lista.get(koodi)
        print(asema)