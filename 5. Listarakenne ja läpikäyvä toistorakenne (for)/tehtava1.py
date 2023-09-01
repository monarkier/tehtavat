import random
nopat = int(input("anna arpakuutioiden määrä: "))
luku = 0
for x in range(nopat+1):

    luku += random.randint(1,6)

print(luku)