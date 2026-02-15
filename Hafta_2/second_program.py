# Veri Türleri (int, float, str, bool, None)
# int (tam sayı)
yas = 25
print("Yaş:", yas)
print("Türü:", type(yas))

# float (ondalıklı sayı)
boy = 1.78
print("Boy:", boy)
print("Türü:", type(boy))

# str (metin)
isim = "Ahmet"
print("İsim:", isim)
print("Türü:", type(isim))

# bool (True / False)
ogrenci_mi = True
print("Öğrenci mi?", ogrenci_mi)
print("Türü:", type(ogrenci_mi))

# None (boş değer)
adres = None
print("Adres:", adres)
print("Türü:", type(adres))

# Aritmetik işlemler
a = 10
b = 3

print("Toplama:", a + b)
print("Çıkarma:", a - b)
print("Çarpma:", a * b)
print("Bölme:", a / b)
print("Tam Bölme:", a // b)
print("Kalan:", a % b)
print("Üs alma:", a ** b)

# String işlemleri
metin = "Python"

# Büyük / küçük harf
print(metin.upper())
print(metin.lower())

# Uzunluk
print("Uzunluk:", len(metin))

# Birleştirme
isim = "Ali"
soyisim = "Yılmaz"
tam_isim = isim + " " + soyisim
print("Tam isim:", tam_isim)

# Parçalama (indexing)
print("İlk harf:", metin[0])
print("Son harf:", metin[-1])

# Dilimleme (slicing)
print("İlk 3 harf:", metin[0:3])

# Tür Dönüşümü İşlemleri (Type Casting)
# String → int
sayi_str = "100"
sayi_int = int(sayi_str)
print(sayi_int + 50)

# int → float
x = 5
y = float(x)
print(y)

# float → int
z = 3.9
print(int(z))  # Ondalık kısmı siler

# int → str
numara = 123
numara_str = str(numara)
print("Numara: " + numara_str)

# Kullanıcıdan (klavyeden) veri girdisi
# Kullanıcıdan isim alma
isim = input("İsminizi girin: ")
print("Merhaba", isim)

# Kullanıcıdan sayı alma
yas = int(input("Yaşınızı girin: "))
print("5 yıl sonraki yaşınız:", yas + 5)


