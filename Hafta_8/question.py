# Soru 1
metin = input("Metin giriniz: ")
print(metin.upper())


# Soru 2
metin = input("Metin giriniz: ")
print(metin.lower())


# Soru 3
metin = input("Metin giriniz: ")
print(metin.strip())


# Soru 4
metin = input("Metin giriniz: ")
print("a sayısı:", metin.count("a"))


# Soru 5
metin = input("Metin giriniz: ")
if "python" in metin.lower():
    print("Bulundu")


# Soru 6
metin = input("Metin giriniz: ")
print(metin.startswith("Merhaba"))


# Soru 7
metin = input("Metin giriniz: ")
print(metin.endswith("!"))


# Soru 8
metin = input("Metin giriniz: ")
print(metin.replace(" ", "-"))


# Soru 9
metin = input("Metin giriniz: ")
print(metin.split())


# Soru 10
liste = ["python", "veri", "bilim"]
print("_".join(liste))


# Soru 11
metin = input("Metin giriniz: ")
print(metin.replace("a", "e"))


# Soru 12
metin = input("Metin giriniz: ")
print(metin.capitalize())


# Soru 13
metin = input("Metin giriniz: ")
print(metin.title())


# Soru 14
metin = input("Metin giriniz: ")
print(metin.isalpha())


# Soru 15
metin = input("Metin giriniz: ")
print(metin.isdigit())


# Soru 16
metin = input("Metin giriniz: ")
print("Uzunluk:", len(metin))


# Soru 17
metin = input("Metin giriniz: ")
print(metin[::-1])


# Soru 18
metin = input("Metin giriniz: ")
print("Kelime sayısı:", len(metin.split()))


# Soru 19
metin = input("Metin giriniz: ")
kelimeler = metin.split()
en_uzun = max(kelimeler, key=len)
print("En uzun kelime:", en_uzun)


# Soru 20
metin = input("Metin giriniz: ")
kelimeler = metin.split()
yeni = []
for k in kelimeler:
    if k not in yeni:
        yeni.append(k)
print(" ".join(yeni))


# Soru 21
def metin_analiz(metin):
    metin = metin.lower()
    kelimeler = metin.split()
    
    uzun_kelimeler = []
    for k in kelimeler:
        if len(k) > 5:
            uzun_kelimeler.append(k)
    
    print("Toplam kelime:", len(kelimeler))
    print("Uzun kelimeler:", uzun_kelimeler)

metin_analiz(input("Metin giriniz: "))


# Soru 22
def palindrom_kontrol(metin):
    temiz = metin.lower().replace(" ", "")
    if temiz == temiz[::-1]:
        return "Palindrom"
    else:
        return "Palindrom değil"

print(palindrom_kontrol(input("Metin giriniz: ")))


# Soru 23
def harf_frekans(metin):
    metin = metin.lower()
    frekans = {}
    
    for h in metin:
        if h.isalpha():
            frekans[h] = frekans.get(h, 0) + 1
    
    for k,v in frekans.items():
        print(k, ":", v)

harf_frekans(input("Metin giriniz: "))


# Soru 24
def sifre_kontrol(sifre):
    if len(sifre) < 8:
        return "Zayıf şifre"
    
    buyuk = any(c.isupper() for c in sifre)
    kucuk = any(c.islower() for c in sifre)
    rakam = any(c.isdigit() for c in sifre)
    
    if buyuk and kucuk and rakam:
        return "Güçlü şifre"
    else:
        return "Zayıf şifre"

print(sifre_kontrol(input("Şifre giriniz: ")))


# Soru 25
def kelime_filtre(metin):
    kelimeler = metin.split()
    sonuc = []
    
    for k in kelimeler:
        if k.isalpha() and len(k) >= 4:
            sonuc.append(k.lower())
    
    print("Uygun kelimeler:", sonuc)
    print("Adet:", len(sonuc))

kelime_filtre(input("Metin giriniz: "))