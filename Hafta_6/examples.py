# Bu belge tuple, set ve dictionary 
# veri tipleri için
# örnek kodlar içermektedir.
# examples.txt dosyasında yer alan soruların cevapları
# bu dosyada yer almaktadır.

# Soru 1
sayilar = []

for i in range(5):
    sayi_al = int(input(f"{i+1}.sayiyi giriniz: "))
    sayilar.append(sayi_al)

sayilar = tuple(sayilar)
print(sayilar)

# Soru 2
sayilar = (12, 45, 7, 23, 56, 9)
print("En büyük sayi",max(sayilar))

# Soru 3
sayilar = (10, 15, 20, 25, 30, 35)

for sayi in sayilar:
    if sayi % 2 == 0:
        print(sayi)

# Soru 4
sayilar = (5, 8, 11, 14, 17, 20)

toplam = 0

for sayi in sayilar:
    if sayi % 2 != 0:
        toplam += sayi

print("Tek sayıların toplamı:", toplam)

# Soru 5
veriler = (3, 6, 9, 12, 15)

for i in range(len(veriler)-1, -1, -1):
    print(veriler[i])

# Soru 6

veriler = (10, 20, 10, 30, 10, 40)

adet = veriler.count(10)

print("10 sayısı", adet, "kez geçiyor")

# Soru 7

sayilar = (5, 12, 7, 18, 3, 20)

yeni_liste = []

for sayi in sayilar:
    if sayi > 10:
        yeni_liste.append(sayi)

print(yeni_liste)

# Soru 8

kelimeler = ("python", "programlama", "veri", "bilim")

for kelime in kelimeler:
    print(kelime.upper())

# Soru 9

sayilar = (2, 4, 6, 8, 10)

for sayi in sayilar:
    print(sayi ** 2)

# Soru 10

sayilar = (1, 2, 3, 4, 5)

yeni_liste = [sayi * 2 for sayi in sayilar]

print(yeni_liste)

# Soru 11

sayilar = [1,2,3,2,4,5,3,6]

tekrarsiz = list(set(sayilar))

print(tekrarsiz)

# Soru 12

A = {1,2,3,4}
B = {3,4,5,6}

kesisim = A & B

print(kesisim)

# Soru 13

A = {1,2,3}
B = {4,5,6}

birlesim = A | B

print(birlesim)

# Soru 14

sayilar = {2,5,7,9,12,15}

for sayi in sayilar:
    if sayi > 5:
        print(sayi)

# Soru 15

renkler = {"kırmızı","mavi","yeşil","sarı"}

for renk in renkler:
    print(renk)

# Soru 16

sayilar = set()

for i in range(5):
    sayi = int(input(f"{i+1}. sayiyi giriniz: "))
    sayilar.add(sayi)

print(sayilar)

# Soru 17

sayilar = {3,6,9,12,15,18}

yeni_set = set()

for sayi in sayilar:
    if sayi % 2 == 0:
        yeni_set.add(sayi)

print(yeni_set)

# Soru 18

sayilar = {4,7,2,9,5}

toplam = sum(sayilar)

print(toplam)

# Soru 19

sayilar = {12,45,7,23,56,9}

print(max(sayilar))

# Soru 20

sayilar = {1,2,3,4,5}

yeni_set = {sayi * 2 for sayi in sayilar}

print(yeni_set)

# Soru 21

ogrenci = {
    "isim": "Ali",
    "yas": 20,
    "bolum": "Bilgisayar"
}

print(ogrenci)

# Soru 22

ogrenci = {"isim":"Ali","yas":20,"bolum":"Bilgisayar"}

print(ogrenci.keys())

# Soru 23

print(ogrenci.values())

# Soru 24

for anahtar, deger in ogrenci.items():
    print(anahtar, ":", deger)

# Soru 25

notlar = {
    "Ali":45,
    "Ayşe":78,
    "Mehmet":90,
    "Zeynep":40
}

for isim, notu in notlar.items():
    if notu < 50:
        print(isim)

# Soru 26

notlar = {"Ali":60,"Ayşe":75,"Mehmet":80,"Zeynep":55}

ortalama = sum(notlar.values()) / len(notlar)

print("Ortalama:", ortalama)

# Soru 27

notlar = {}

for i in range(3):
    isim = input("Öğrenci adı: ")
    notu = int(input("Notu: "))
    notlar[isim] = notu

print(notlar)

# Soru 28

notlar = {"Ali":60,"Ayşe":75,"Mehmet":90,"Zeynep":85}

en_yuksek = max(notlar, key=notlar.get)

print(en_yuksek)

# Soru 29

notlar = {"Ali":60,"Ayşe":75,"Mehmet":80}

for kisi in notlar:
    notlar[kisi] += 10

print(notlar)

# Soru 30

notlar = {"Ali":85,"Ayşe":72,"Mehmet":48,"Zeynep":91}

for isim, notu in notlar.items():
    if notu >= 85:
        harf = "AA"
    elif notu >= 70:
        harf = "BB"
    elif notu >= 50:
        harf = "CC"
    else:
        harf = "FF"
    
    print(f"{isim} : {notu} -> {harf}")