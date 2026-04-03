metin = "  Yazılım Geliştirme Teknolojileri  "

# Büyük / küçük harf
print(metin.upper())
print(metin.lower())

# Boşluk temizleme
print(metin.strip())

# Parçalama
kelimeler = metin.split()
print(kelimeler)

# Birleştirme
yeni_metin = "-".join(kelimeler)
print(yeni_metin)

# Değiştirme
print(metin.replace("Python", "Java"))

# Sayma
print(metin.count("o"))

# Başlıyor mu / bitiyor mu
print(metin.startswith("  Py"))
print(metin.endswith("yorum  "))

sayilar = [7,9,11,16,18,20]
etiket = ["cift" if x % 2 == 0 else "tek" for x in sayilar]
print(etiket)

kelimeler = ["python", "java", "c++"]

buyuk = [kelime.upper() for kelime in kelimeler]
print(buyuk)

ogrenci = {
    "Ali": 85,
    "Ayşe": 72,
    "Mehmet": 48
}

for isim, notu in ogrenci.items():
    if notu >= 70:
        print(isim, "geçti")


matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satir in matris:
    for eleman in satir:
        print(eleman, end=" ")


ogrenciler = {
    "Ali": {"not": 85, "şehir": "Ankara"},
    "Ayşe": {"not": 72, "şehir": "İstanbul"}
}

for isim, bilgiler in ogrenciler.items():
    print(isim)
    for anahtar, deger in bilgiler.items():
        print("  ", anahtar, ":", deger)


matris = [[1, 2], [3, 4], [5, 6]]

duz_liste = [eleman for satir in matris for eleman in satir]
print(duz_liste)