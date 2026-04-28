
class Vehicle:

    def __init__(self, aracTipi, yakitTipi, hiz, fiyat):
        self.aracTipi = aracTipi
        self.yakitTipi = yakitTipi
        self.hiz = hiz
        self.fiyat = fiyat

    def bilgi_goster(self):
        print(f"Arac tipi: {self.aracTipi}")
        print(f"Aracın yakıt tipi: {self.yakitTipi}")
        print(f"Aracin hizi: {self.hiz}")
        print(f"Aracin fiyati: {self.fiyat}")


    def hiz_artir(self, miktar):
        if miktar < 0:
             raise ValueError("Negatif hiz artisi olmaz!")
        self.hiz += miktar
        return self.hiz
    

    
arac1 = Vehicle("Araba", "Benzin", 120,5000)
arac2 = Vehicle("Uçak", "Jet Yakıtı", 800,5000000)

araclar = [arac1, arac2]

for a in araclar:
    a.bilgi_goster()
    a.hareket_et()
    print("------")
        

