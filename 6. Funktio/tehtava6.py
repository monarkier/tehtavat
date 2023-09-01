import math
x=0
def pizzanneliometrihinta(halkaisija,hinta):
    toiseen=float(halkaisija)*float(halkaisija)
    pintaala=math.pi*toiseen
    x=(hinta/pintaala)*100
    return x
pizza=99999999
x=0
while x<2:
    halkaisija=(input("Anna pizzan halkaisija: "))
    hinta=int(input("Anna pizzan hinta: "))

    if (pizza>pizzanneliometrihinta(halkaisija,hinta)):
        pizza=pizzanneliometrihinta(halkaisija,hinta)
    x+=1
print(pizza)

