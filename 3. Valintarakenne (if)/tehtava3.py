sex=input('Anna "biologinen sukupuoli": ')
hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))
if sex=="nainen":
    if hemoglobiini < 117:
        print("sinulla on anemia")
    elif hemoglobiini > 175:
        print("hemoglobiinisi on korkea")
    else:
        print("hemoglobiinisi on normaali")
elif sex=="mies":
    if hemoglobiini < 134:
        print("sinulla on anemia")
    elif hemoglobiini > 195:
        print("hemoglobiinisi on korkea")
    else:
        print("hemoglobiinisi on normaali")

