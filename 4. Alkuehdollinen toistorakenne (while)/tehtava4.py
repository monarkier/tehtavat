import random
x = int(random.randint(1,10))
while True:
    y=int(input("arvaa luku: "))
    if y < x:
        print("liian pieni arvaus")
    elif y > x:
        print("liian suuri arvaus")
    elif y == x:
        print("oikein")
        break