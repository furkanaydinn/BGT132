# Soru 1
with open("veri.txt", "w") as dosya:
    dosya.write("Merhaba Dünya")


# Soru 2
with open("veri.txt", "r") as dosya:
    icerik = dosya.read()
    print(icerik)


# Soru 3
metin = input("Bir metin giriniz: ")

with open("kullanici.txt", "w") as dosya:
    dosya.write(metin)


# Soru 4
with open("sayilar.txt", "w") as dosya:
    for i in range(1, 11):
        dosya.write(str(i) + "\n")

# Soru 5
with open("sayilar.txt", "r") as dosya:
    for satir in dosya:
        print(satir.strip())


# Soru 6

with open("metin.txt", "r") as dosya:
    for satir in dosya:
        print(satir.upper())

# Soru 7

with open("isimler.txt", "w") as dosya:
    for i in range(5):
        isim = input("İsim giriniz: ")
        dosya.write(isim + "\n")


# Soru 8

with open("isimler.txt", "r") as dosya:
    isimler = dosya.readlines()
    print("Toplam isim:", len(isimler))


# Soru 9

toplam = 0

with open("notlar.txt", "w") as dosya:
    for i in range(5):
        notu = int(input("Not giriniz: "))
        toplam += notu
        dosya.write(str(notu) + "\n")

print("Ortalama:", toplam / 5)


# Soru 10

with open("metin.txt", "r") as dosya:
    metin = dosya.read()
    kelimeler = metin.split()
    print("Kelime sayısı:", len(kelimeler))


# Soru 11

with open("metin.txt", "r") as dosya:
    satirlar = dosya.readlines()
    print("Satır sayısı:", len(satirlar))



# Soru 12

with open("veri.txt", "a") as dosya:
    dosya.write("\nProgramlama öğreniyorum")


# Soru 13

with open("sayilar.txt", "r") as dosya:
    for satir in dosya:
        sayi = int(satir.strip())
        if sayi % 2 == 0:
            print(sayi)

# Soru 14

with open("metin.txt", "r") as kaynak:
    metin = kaynak.read()

metin = metin.replace("a", "e")

with open("yeni.txt", "w") as hedef:
    hedef.write(metin)


# Soru 15

with open("eski.txt", "r") as kaynak:
    veri = kaynak.read()

with open("yeni.txt", "w") as hedef:
    hedef.write(veri)


# Soru 16

cumle = input("Cümle giriniz: ")

with open("veri.txt", "w") as dosya:
    dosya.write(cumle)
    dosya.write("\n" + cumle[::-1])

# Soru 17

sayilar = []

with open("sayilar.txt", "r") as dosya:
    for satir in dosya:
        sayilar.append(int(satir.strip()))

print("En küçük:", min(sayilar))
print("En büyük:", max(sayilar))

# Soru 18

with open("metin.txt", "r") as kaynak, open("numarali.txt", "w") as hedef:
    for i, satir in enumerate(kaynak, 1):
        hedef.write(f"{i}. {satir}")

# Soru 19

import os

dosya_adi = input("Dosya adı giriniz: ")

if os.path.exists(dosya_adi):
    print("Dosya mevcut")
else:
    print("Dosya yok")

# Soru 20

with open("metin.txt", "r") as dosya:
    satirlar = dosya.readlines()

benzersiz = list(set(satirlar))

with open("yeni.txt", "w") as dosya:
    dosya.writelines(benzersiz)

# Soru 21

def yaz(metin):
    with open("veri.txt", "w") as dosya:
        dosya.write(metin)

# kullanım
yaz("Merhaba")

# Soru 22

def oku():
    with open("veri.txt", "r") as dosya:
        print(dosya.read())

oku()

# Soru 23

def toplam_hesapla():
    toplam = 0
    with open("sayilar.txt", "r") as dosya:
        for satir in dosya:
            toplam += int(satir.strip())
    print("Toplam:", toplam)

toplam_hesapla()

# Soru 24

def kelime_say(dosya_adi):
    with open(dosya_adi, "r") as dosya:
        metin = dosya.read()
        return len(metin.split())

print(kelime_say("metin.txt"))

# Soru 25
def kopyala(kaynak, hedef):
    with open(kaynak, "r") as k:
        veri = k.read()
    with open(hedef, "w") as h:
        h.write(veri)

kopyala("eski.txt", "yeni.txt")