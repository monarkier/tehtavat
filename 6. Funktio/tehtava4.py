def summa(x):
    a = 0
    for i in range(len(x)):
        a += x[i]
    return a
lista = [4,13,69,420,666]
x = summa(lista)
print(x)