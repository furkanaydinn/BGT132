class Arac:
    def __init__(self, hiz):
        self.hiz = hiz

    def hareket_et(self):
        print("Arac hareket ediyor")


class Araba(Arac):
    def hareket_et(self):
        print(f"Araba {self.hiz} km/h hizla gidiyor")


class Ucak(Arac):
    def hareket_et(self):
        print(f"Ucak {self.hiz} km/h hizla ucuyor")


araclar = [Araba(120), Ucak(800)]

for a in araclar:
    a.hareket_et()