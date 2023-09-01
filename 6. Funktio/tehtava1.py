import random
def noppa():
    x = int(random.randint(1,6))
    return x
while True:
    y=noppa()
    print(y)
    if y == 6:
        break
