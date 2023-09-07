vuodenajat = ("Kevät","Kesä","Syksy","Talvi")
kuukausi = int(input("Anna kuukauden nummero: "))
vuodenaika = int()
if kuukausi <13:
   if kuukausi >2:
       if kuukausi > 5:
           vuodenaika = 0
           if kuukausi > 8:
               vuodenaika = 1
               if kuukausi > 12:
                   vuodenaika = 2
               else:
                   vuodenaika = 3
   else:
    vuodenaika = 3
print(vuodenajat[vuodenaika])