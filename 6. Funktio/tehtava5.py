def parilliset(x):
    a = 0
    for i in range(len(x)):
        if a<len(x):
            if x[a]%2!=0:
                x.remove(x[a])
            else:
                a+=1
    return x
lista = [4, 13, 69, 420, 666]
x = parilliset(lista)
print(x)