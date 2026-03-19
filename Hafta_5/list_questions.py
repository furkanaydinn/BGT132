# Soru 1
tamsayılar = [2,4,6,8,10]
tamsayılar.append(20)
tamsayılar.append(30)

print(tamsayılar)

# Soru 2
languages = ["C","Java","C#","Javascript"]
languages.insert(2,"Python")

print(languages)

# Soru 3
dizi1 = ["Elma", "Armut", "Kivi"]
dizi2 = ["biber","karnabahar","enginar"]

dizi1.extend(dizi2)

print(dizi1)

# Soru 4
dersler = ["BGT132","BGP201","BGP105","BGT205"]

dersler.remove("BGP201")
print(dersler)

# Soru 5
liste = [10, 20, 30, 40, 50]

liste.pop()      
liste.pop(2)     

print(liste)

# Soru 6

liste = [10, 20, 30, 40, 50]

del liste[3]

print(liste)

del liste

# Soru 7

liste = [10, 20, 30, 40]

liste[2] = 99

print(liste)

# Soru 8

liste = []

for i in range(5):
    sayi = int(input("Sayı giriniz: "))
    liste.append(sayi)

print("Uzunluk:", len(liste))

# Soru 9

liste = [0,1,2,3,4,5,6,7,8,9]

print(liste[:5])
print(liste[-3:])
print(liste[2:8])

# Soru 10

liste = [1, 2, 3, 4]

for eleman in liste:
    print(eleman)

# Soru 11

liste = [1,2,3,4,5,6]

ciftler = []

for sayi in liste:
    if sayi % 2 == 0:
        ciftler.append(sayi)

print(ciftler)

# Soru 12

sayilar = [45, 12, 78, 3, 56]

sayilar.sort()
print(sayilar)

sayilar.reverse()
print(sayilar)

# Soru 13

liste = []

for i in range(5):
    sayi = int(input("Sayı gir: "))
    liste.append(sayi)

print(liste.count(60))

# Soru 14

liste = [1,2,3,4,5]

toplam = 0

for sayi in liste:
    toplam += sayi

print(toplam)

# Soru 15

liste = [10, 60, 30, 80]

yeni = []

for sayi in liste:
    if sayi > 50:
        yeni.append(sayi)

print(yeni)

# Soru 16

liste = [1,2,3,4,5]

for sayi in liste:
    if sayi % 2 != 0:
        print(sayi)

# Soru 17

liste = [10, 50, 30, 80, 20]

en_buyuk = liste[0]

for sayi in liste:
    if sayi > en_buyuk:
        en_buyuk = sayi

print(en_buyuk)

# Soru 18

liste = [10, 50, 30, 80, 20]

en_kucuk = liste[0]

for sayi in liste:
    if sayi < en_kucuk:
        en_kucuk = sayi

print(en_kucuk)

# Soru 19

liste = []
negatifler = []

for i in range(10):
    sayi = int(input("Sayı gir: "))
    liste.append(sayi)

for sayi in liste:
    if sayi < 0:
        negatifler.append(sayi)

print(negatifler)

# Soru 20

liste = [3,6,7,9,10]

for sayi in liste:
    if sayi % 3 == 0:
        print(sayi)

# Soru 21

liste = [1,2,3,2,4]

tekrar_var = False

for sayi in liste:
    if liste.count(sayi) > 1:
        tekrar_var = True
        break

print(tekrar_var)

# Soru 22

liste = [1,-2,3,-4,5]

pozitif = 0
negatif = 0

for sayi in liste:
    if sayi >= 0:
        pozitif += 1
    else:
        negatif += 1

print("Pozitif:", pozitif)
print("Negatif:", negatif)

# Soru 23

liste = [1,2,3,4]

yeni = []

for sayi in liste:
    yeni.append(sayi ** 2)

print(yeni)

# Soru 24

liste = [5, 15, 25, 55, 45]

for sayi in liste:
    if 10 <= sayi <= 50:
        print(sayi)

# Soru 25

liste = [1,2,3,4,5]

aranan = int(input("Sayı gir: "))

bulundu = False

for sayi in liste:
    if sayi == aranan:
        bulundu = True
        break

print(bulundu)