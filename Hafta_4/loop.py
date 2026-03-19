# PYTHON PROGRAMLAMA DİLİNDE DÖNGÜ YAPILARI (LOOP STRUCTURES)

# Döngü yapıları, belirli bir işlem kümesinin önceden tanımlanmış
# bir koşula bağlı olarak tekrarlı biçimde yürütülmesini sağlayan
# kontrol mekanizmalarıdır.

# Python dilinde iki temel döngü yapısı bulunmaktadır:
# 1) for döngüsü
# 2) while döngüsü

# Bir döngü mekanizmasının temel bileşenleri şunlardır:
# - Başlangıç değeri (initialization)
# - Devam koşulu (termination condition)
# - Güncelleme adımı (iteration step: artış/azalış)

# for döngüsü, genellikle yineleme sayısının önceden bilindiği
# durumlarda tercih edilir ve iterasyon aralığı çoğunlukla
# range() fonksiyonu aracılığıyla tanımlanır.

# while döngüsü ise, belirli bir mantıksal koşul (boolean expression)
# True olduğu sürece çalışmaya devam eden, koşul temelli bir
# yineleme yapısıdır.

################ Örnekler #####################


# 1 den 10'a kadar sayıları yazdırma
for i in range(1,10):
    print(i)

# 2'şer 2'şer sayıları yazdırma
# (başlangıç değeri, son değer, artış miktarı)
for i in range(2,101,2):
    print(i)

print("Liste üzerinde dolaşma örneği")
sehir_liste = ["Ankara", "Samsun", "Sinop", "Ordu"]

for sehir in sehir_liste:
    print(sehir)

# While döngüsü örnekler

sayi = 1

while sayi<=10:
    print(sayi)
    sayi+=1


# Kullanıcı 0 girene kadar sayı alma
sayi = int(input("Bir sayı giriniz (Çıkmak için 0): "))

while sayi != 0:
    print("Girdiğiniz sayı:", sayi)
    sayi = int(input("Bir sayı giriniz (Çıkmak için 0): "))


# Break = Bir işlemi veya döngüyü tamamen durdurur.
# Continue = Bulunduğu kod adımını atlar, döngü devam eder.


for i in range(1, 11):
    if i == 5:
        break
    print(i)

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# İç içe döngüler (Nested Loop)
for i in range(1, 6):
    for j in range(1, 6):
        print(i, "x", j, "=", i * j, end="\t")
    print()

# Yıldız deseni
for i in range(1, 6):
    print("*" * i)

# 1 den 100 kadar sayilarin toplami

toplam = 0
for sayi in range(1,101):
    toplam+=sayi

print("Toplam:",toplam)

# faktoriyel hesaplama 
faktoriyel = 1
sayi = int(input("Faktoriyeli hesaplanacak sayiyi giriniz. "))

for i in range(1, sayi+1):
    faktoriyel *= i

print(faktoriyel)

# Sayı tahmin oyunu
import random

rastgele = random.randint(1, 10)

while True:
    tahmin = int(input("1-10 arası tahmin giriniz: "))
    
    if tahmin == rastgele:
        print("Tebrikler bildiniz!")
        break
    else:
        print("Tekrar deneyin.")


# Ters üçgen
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# Dikdortgen desen oluşturma
satir = 4
sutun = 6

for i in range(satir):
    for j in range(sutun):
        print("*", end="")
    print()

# Sayı piramidi oluşturma
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Ters sayı piramidi
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Asal sayi hesaplayan program 
for sayi in range(2, 21):
    asal = True
    
    for i in range(2, sayi):
        if sayi % i == 0:
            asal = False
            break
    
    if asal:
        print(sayi, "asal")

# Boşluklu piramit oluşturma
for i in range(1, 6):
    for bosluk in range(5 - i):
        print(" ", end="")
    
    for yildiz in range(2*i - 1):
        print("*", end="")
    
    print()