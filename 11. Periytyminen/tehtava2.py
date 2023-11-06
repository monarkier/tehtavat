import random
class Auto:
    def __init__(self, rekisteritunnus, nopeus):
        self.rekisteritunnus = rekisteritunnus
        self.nopeus = nopeus
        self.matka = 0

    def kiihdytä(self,muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

# Aliluokka Sähköauto
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

# Aliluokka Polttomoottoriauto
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

def main():
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)
    sähköauto.kulje(3)
    polttomoottoriauto.kulje(3)

    print(f"Sähköauton matkamittarilukema: {sähköauto.matka} km")
    print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.matka} km")

if __name__ == "__main__":
    main()