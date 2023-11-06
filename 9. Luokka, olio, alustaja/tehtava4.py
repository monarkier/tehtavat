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

# Luo 10 autoa
autojen_lista = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autojen_lista.append(auto)

kilpailu_käynnissä = True
tunti = 0

while kilpailu_käynnissä:
    for auto in autojen_lista:
        auto.kiihdytä()
        auto.kulje()

    tunti += 1

    for auto in autojen_lista:
        if auto.matka >= 10000:
            kilpailu_käynnissä = False
            break


print("Kilpailun tulokset:")
print("{:<12} {:<15} {:<15} {:<15}".format("Rekisteri", "Huippunopeus(km/h)", "Nopeus(km/h)", "Matka(km)"))
for auto in autojen_lista:
    print("{:<12} {:<15} {:<15} {:<15}".format(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka))