lista = [0]
for x in lista:
    luku = input("anna lukuja: ")
    if luku=="":
        print(lista[0],lista[1],lista[2],lista[3],lista[4])
        break
    luku=int(luku)
    lista.append(luku)
    lista.sort(reverse=True)
