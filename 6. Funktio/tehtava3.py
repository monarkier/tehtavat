def gallonalitroiksi(x):
    x = x/3.785
    return x
while True:
    x = int(input("Anna gallonamäärä: "))
    if x < 0:
        break
    x=gallonalitroiksi(x)
    print(x)
