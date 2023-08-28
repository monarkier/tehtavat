x = "python"
y = "rules"
a = 0
while True:

    if a>5:
        print("pääsy evätty")
        break
    kayttaja=str(input("anna käyttäjätunnus"))
    salasana=str(input("anna salasana"))
    if kayttaja == x:
        if salasana == y:
            print("Tervetuloa!")
            break
        else:
            a+=1
    else:
        a+=1

