try:
    sayi = int(input("Bir sayi giriniz: "))
    print("Girilen sayi:", sayi)
except:
    print("Hata olustu!")


try:
    yas = int(input("Yasinizi giriniz: "))
    print("Yasiniz:", yas)
except ValueError:
    print("Lutfen sayi giriniz!")

try:
    sonuc = "Merhaba" + 5
    print(sonuc)
except TypeError:
    print("Farkli veri tipleri toplanamaz!")


try:
    sayi = int(input("Bir sayi gir: "))
    sonuc = 10 / sayi
    print("Sonuc:", sonuc)
except ZeroDivisionError:
    print("0'a bolme hatasi!")


try:
    print(x)
except NameError:
    print("Degisken tanimlanmamis!")


try:
    liste = [10, 20, 30]
    print(liste[5])
except IndexError:
    print("Listede bu index yok!")


try:
    sozluk = {"ad": "Ali", "yas": 25}
    print(sozluk["soyad"])
except KeyError:
    print("Boyle bir anahtar yok!")


try:
    metin = "python"
    metin.buyukYap()
except AttributeError:
    print("Boyle bir metod yok!")


try:
    sayi = int(input("Pozitif sayi gir: "))
    if sayi < 0:
        raise ValueError("Negatif sayi girdiniz!")
    print("Gecerli sayi:", sayi)
except ValueError as hata:
    print("Hata:", hata)



try:
    sayi = int(input("Sayi gir: "))
    sonuc = 10 / sayi
    print("Sonuc:", sonuc)

except ValueError:
    print("Sayi girmediniz!")

except ZeroDivisionError:
    print("0'a bolunmez!")

except Exception:
    print("Bilinmeyen hata olustu!")