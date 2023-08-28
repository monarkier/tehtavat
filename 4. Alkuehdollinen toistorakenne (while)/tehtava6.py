import math
import random
N = int(input("anna arvottavien pisteiden määrä: "))
a=0

n = 0
while a<N:
    x= float(random.randint(-1,1))
    y= float(random.randint(-1,1))
    if (x/2+y/2)<1:
        n+=1
    pi = 4*n/N

    a+=1
pi = 4*n/N
print (pi)