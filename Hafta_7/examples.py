# Soru 1
def basamak_toplami(sayi):
    toplam = 0
    sayi = abs(sayi)
    while sayi > 0:
        toplam += sayi % 10
        sayi //= 10
    return toplam

print(basamak_toplami(1234))


# Soru 2
def palindrom_mu(sayi):
    s = str(sayi)
    return s == s[::-1]

print(palindrom_mu(121))


# Soru 3
def pozitifler(liste):
    yeni = []
    for i in liste:
        if i > 0:
            yeni.append(i)
    return yeni

liste = [10,20,30,-40,25,-78,-90]
print(pozitifler(liste))


# Soru 4
def buyuk_harf(metin):
    sonuc = ""
    for harf in metin:
        if 'a' <= harf <= 'z':
            sonuc += chr(ord(harf) - 32)
        else:
            sonuc += harf
    return sonuc

print(buyuk_harf("python"))


# Soru 5
def ters_cevir(liste):
    yeni = []
    for i in range(len(liste)-1, -1, -1):
        yeni.append(liste[i])
    return yeni

print(ters_cevir([1,2,3,4]))


# Soru 6
def basamak_sayisi(sayi):
    sayi = abs(sayi)
    sayac = 0
    while sayi > 0:
        sayi //= 10
        sayac += 1
    return sayac

print(basamak_sayisi(12345))


# Soru 7
def ortalama(liste):
    toplam = 0
    sayac = 0
    for i in liste:
        toplam += i
        sayac += 1
    return toplam / sayac

print(ortalama([10,20,30]))


# Soru 8
def ortak_elemanlar(l1, l2):
    ortak = []
    for i in l1:
        if i in l2 and i not in ortak:
            ortak.append(i)
    return ortak

print(ortak_elemanlar([1,2,3], [2,3,4]))


# Soru 9
def rakam_ayikla(metin):
    sonuc = ""
    for i in metin:
        if i.isdigit():
            sonuc += i
    return sonuc

print(rakam_ayikla("a1b2c3"))


# Soru 10
def alfabetik(metin):
    kelimeler = metin.split()
    kelimeler.sort()
    return kelimeler

print(alfabetik("python veri bilim"))


# Soru 11
def mukemmel_sayi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi

print(mukemmel_sayi(6))


# Soru 12
def ikinci_en_buyuk(liste):
    en_buyuk = max(liste)
    liste2 = []
    for i in liste:
        if i != en_buyuk:
            liste2.append(i)
    return max(liste2)

print(ikinci_en_buyuk([10,20,30,40]))


# Soru 13
def en_uzun_kelime(metin):
    kelimeler = metin.split()
    en_uzun = ""
    for k in kelimeler:
        if len(k) > len(en_uzun):
            en_uzun = k
    return en_uzun

print(en_uzun_kelime("python veri bilimi"))


# Soru 14
def binary_cevir(sayi):
    sonuc = ""
    while sayi > 0:
        sonuc = str(sayi % 2) + sonuc
        sayi //= 2
    return sonuc

print(binary_cevir(10))


# Soru 15
def flatten(liste):
    sonuc = []
    for i in liste:
        if isinstance(i, list):
            for j in i:
                sonuc.append(j)
        else:
            sonuc.append(i)
    return sonuc

print(flatten([1,[2,3],[4,5]]))


# Soru 16
def en_kucuk(*args):
    en = args[0]
    for i in args:
        if i < en:
            en = i
    return en

print(en_kucuk(5,2,8,1))


# Soru 17
def ortalama_kwargs(**kwargs):
    toplam = 0
    sayac = 0
    for i in kwargs.values():
        toplam += i
        sayac += 1
    return toplam / sayac

print(ortalama_kwargs(a=10,b=20,c=30))


# Soru 18
def tekrar_et(metin, tekrar=3):
    sonuc = ""
    for i in range(tekrar):
        sonuc += metin
    return sonuc

print(tekrar_et("python"))


# Soru 19
def kontrol(veri):
    if isinstance(veri, int) or isinstance(veri, float):
        return veri**2
    elif isinstance(veri, str):
        return len(veri)

print(kontrol(5))
print(kontrol("python"))


# Soru 20
def hesapla(sayi):
    def kare(x):
        return x**2
    def kup(x):
        return x**3
    
    return kare(sayi), kup(sayi)

print(hesapla(3))