luku=int(input("anna luku: "))
onko=bool(True)
for x in range(2,luku//2+1):
    if (luku%x) == 0:
        onko= False
        if (luku/3 )>0:
            onko= False
        else:
            onko= True
if onko==True:
    print(luku," on alkuluku")
elif onko==False:
    print(luku," ei ole alkuluku")