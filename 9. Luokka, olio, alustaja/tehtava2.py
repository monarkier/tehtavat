class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.nopeus=0
        self.matka=0

    def kiihdyta(self,kmh):
        if self.nopeus+kmh < self.huippunopeus and self.nopeus+kmh>0:
            self.nopeus+=kmh
        elif self.nopeus+kmh > self.huippunopeus:
            self.nopeus=self.huippunopeus
        else:
            self.nopeus=0

auto=Auto("ABC-123",142)
auto.kiihdyta(+30)
auto.kiihdyta(+70)
auto.kiihdyta(+50)
print(auto.nopeus)

auto.kiihdyta(-200)
print(auto.nopeus)

print(auto.rekisteritunnus,auto.huippunopeus,auto.nopeus,auto.matka)