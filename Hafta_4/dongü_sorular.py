# Soru 1
for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:4}",end=" ")
    print()

# Soru 2
for i in range(1,4):
    for j in range(1,4):
        print(f"({i},{j})", end="\t")
    print()

# Soru 3
for i in range(1,100):
    if i%3 == 0 and i%5 == 0:
        print(i)

# Soru 4
sayi = int(input("Bir sayı girin: "))

# asal olup olmadığının kotrolü
if sayi < 2:
    print(f"{sayi} asal değildir.")
else:
    asal_mi = True
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            asal_mi = False
            break

    if asal_mi:
        print(f"{sayi} asal bir sayıdır.")
    else:
        print(f"{sayi} asal değildir.")

# Soru 5
sayilar = []

# 5 sayı al
for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)

# En büyük sayıyı bul
en_buyuk = max(sayilar)

print(f"Girdiğiniz sayıların en büyüğü: {en_buyuk}")

# Soru 6
toplam = 0

while True:
    sayi = int(input("Bir sayı girin (negatif sayı ile bitirin): "))
    
    if sayi < 0:
        break  
    toplam += sayi  

print(f"Girdiğiniz sayıların toplamı: {toplam}")

# Soru 7
toplam = 0
for i in range(2,2,50):
    toplam +=i

print("Çift sayılar toplami",toplam)

# Soru 8
sayi = int(input("Faktoriyeli alinacak sayiyi giriniz "))

if sayi < 0:
    print("Negatif sayinin faktoriyeli hesaplanamaz")

if sayi == 0:
    faktoriyel = 1

faktoriyel = 1
for i in range(1,sayi+1):
    faktoriyel *=i

print(faktoriyel)

# Soru 9

toplam = 0

for i in range(10):
    notu = int(input(f"{i+1}. öğrencinin notu: "))
    toplam += notu

ortalama = toplam / 10

print("Ortalama:", ortalama)

# Soru 10

for sayi in range(2, 101):
    asal = True

    for i in range(2, sayi):
        if sayi % i == 0:
            asal = False
            break

    if asal:
        print(sayi)

# Soru 11

while True:
    print("1- Toplama")
    print("2- Çıkarma")
    print("0- Çıkış")

    secim = int(input("Seçiminiz: "))

    if secim == 0:
        print("Programdan çıkılıyor...")
        break

    sayi1 = int(input("1. sayı: "))
    sayi2 = int(input("2. sayı: "))

    if secim == 1:
        print("Sonuç:", sayi1 + sayi2)
    elif secim == 2:
        print("Sonuç:", sayi1 - sayi2)
    else:
        print("Geçersiz seçim!")

# Soru 12

a = 0
b = 1

while a <= 100:
    print(a)
    a, b = b, a + b


