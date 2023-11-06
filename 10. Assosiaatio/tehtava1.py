class Hissi:
    def __init__(self, alin_kerros, ylimmainen_kerros):
        self.alin_kerros = alin_kerros
        self.ylimmainen_kerros = ylimmainen_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylimmainen_kerros:
            self.nykyinen_kerros += 1
        print(f'Hissi on kerroksessa {self.nykyinen_kerros}')

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f'Hissi on kerroksessa {self.nykyinen_kerros}')

    def siirry_kerrokseen(self, kohdekerros):
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

h=Hissi(1,8)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(h.alin_kerros)
