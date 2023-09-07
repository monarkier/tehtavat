x = set()
y = False
while True:
    nimi=input("Anna nimi: ")
    y = nimi in x
    x.add(nimi)
    if y == True:
        print("Aiemmin syötetty nimi")
    else:
        print("uusi nimi")
    if nimi == "":
        x.remove("")
        for i in x:
            print(i, "\n")
        break


