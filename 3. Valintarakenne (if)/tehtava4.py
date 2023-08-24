vuosi = int(input("ilmoita vuosiluku: "))
if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("on karkausvuosi")
        else:
            print("ei ole karkausvuosi")
    else:
        print("on karkausvuosi")
else:
    print("ei ole karkausvuosi")