class BankaHesabi:
    def __init__(self, bakiye):
        self.bakiye = bakiye

    def para_cek(self, miktar):
        if miktar > self.bakiye:
            raise ValueError("Yetersiz bakiye!")
        self.bakiye -= miktar
        print("Para cekildi. Yeni bakiye:", self.bakiye)


class VadeliHesap(BankaHesabi):  # kalıtım
    def faiz_ekle(self):
        self.bakiye *= 1.10
        print("Faiz eklendi. Yeni bakiye:", self.bakiye)


# Kullanım
hesap = VadeliHesap(1000)

while True:
    try:
        print("\n1- Para cek")
        print("2- Faiz ekle")
        print("q- Cikis")

        secim = input("Secim: ")

        if secim == "1":
            miktar = float(input("Cekilecek miktar: "))
            hesap.para_cek(miktar)

        elif secim == "2":
            hesap.faiz_ekle()

        elif secim.lower() == "q":
            break

        else:
            print("Hatali secim")

    except ValueError as hata:
        print("HATA:", hata)

    except Exception as e:
        print("Beklenmeyen hata:", e)