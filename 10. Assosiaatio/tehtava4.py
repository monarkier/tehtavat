import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self):
        muutos = random.randint(-10, 15)
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self):
        self.matka += self.nopeus

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä()
            auto.kulje()

    def tulosta_tilanne(self):
        print("{:<12} {:<15} {:<15} {:<15}".format("Rekisteri", "Huippunopeus (km/h)", "Nopeus (km/h)", "Matka (km)"))
        for auto in self.autot:
            print("{:<12} {:<15} {:<15} {:<15}".format(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

def main():
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(auto)

    suuri_romuralli = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    while not suuri_romuralli.kilpailu_ohi():
        suuri_romuralli.tunti_kuluu()
        tunti += 1
        if tunti % 10 == 0:
            suuri_romuralli.tulosta_tilanne()

    suuri_romuralli.tulosta_tilanne()

if __name__ == "__main__":
    main()