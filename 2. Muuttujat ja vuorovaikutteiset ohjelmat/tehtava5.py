leiviskat=float(input("Anna leiviskät:"))
naulat=float(input("Anna naulat:"))
luodit=float(input("Anna luodit:"))
naulat+=leiviskat*20
luodit+=naulat*32
kilogrammat=int(luodit*13.3/1000)
grammat = luodit*13.3-kilogrammat*1000
print("Massa nykymittojen mukaan:",kilogrammat," Kilogrammaa ja ",grammat," grammaa.")