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


class Talo:
    def __init__(self, alin_kerros, ylimmainen_kerros, hissien_lukumaara):
        self.hissit = [Hissi(alin_kerros, ylimmainen_kerros) for _ in range(hissien_lukumaara)]

    def aja_hissia(self, hissi_numero, kohdekerros):
        if 0 <= hissi_numero < len(self.hissit):
            self.hissit[hissi_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virhe: Tuntematon hissinumero")



alin_kerros = 1
ylimmainen_kerros = 10
hissien_lukumaara = 3

talo = Talo(alin_kerros, ylimmainen_kerros, hissien_lukumaara)


talo.aja_hissia(0, 5)
talo.aja_hissia(1, 8)
talo.aja_hissia(2, 3)
talo.aja_hissia(0, alin_kerros)