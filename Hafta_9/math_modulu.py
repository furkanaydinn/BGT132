import math

sayi = 25
sonuc = math.sqrt(sayi)

print("Karekök:", sonuc)

sonuc = math.pow(2, 3)
print("Sonuç:", sonuc)

print("Yukarı yuvarlama:", math.ceil(4.2))
print("Aşağı yuvarlama:", math.floor(4.8))
print("Pi değeri:", math.pi)
print("Mutlak değer:", math.fabs(-10))
print("Faktöriyel:", math.factorial(5))
print("Tam kısmı:", math.trunc(4.9))

nokta1 = (0, 0)
nokta2 = (3, 4)

mesafe = math.dist(nokta1, nokta2)
print("Mesafe:", mesafe)