import random
noppa=int(input("anna nopan suurin silmäluku: "))
def Noppa(x):
    y = random.randint(1,x)
    return y
while True:
    a=Noppa(noppa)
    print(a)
    if a == noppa:
        break