import datetime
import math






simdi = datetime.datetime.now()
print(simdi)


x = datetime.datetime.now()

print("Yıl:", x.year)
print("Ay:", x.month)
print("Gün:", x.day)
print("Saat:", x.hour)
print("Dakika:", x.minute)

tarih = datetime.datetime(2025, 5, 17)
print(tarih)

tarih = datetime.datetime(2025, 5, 17, 14, 30, 0)
print(tarih)

x = datetime.datetime.now()
print(x.strftime("%A"))

x = datetime.datetime.now()
print(x.strftime("%B"))

x = datetime.datetime.now()

print(x.strftime("%d/%m/%Y"))
print(x.strftime("%H:%M:%S"))

x = datetime.datetime.now()
print(x.weekday())   # Pazartesi = 0

bugun = datetime.date.today()
print(bugun)


t1 = datetime.datetime(2025, 1, 1)
t2 = datetime.datetime(2024, 1, 1)

if t1 > t2:
    print("t1 daha yeni")
else:
    print("t2 daha yeni")




t1 = datetime.datetime(2025, 1, 10)
t2 = datetime.datetime(2025, 1, 1)

fark = t1 - t2
print("Gün farkı:", fark.days)


d = datetime.date(2025, 1, 1)
print(d.isoformat())


x = datetime.datetime.now()

metin = x.strftime("%Y-%m-%d %H:%M")
print(metin)


tarih_str = "2025-04-03"
tarih = datetime.datetime.strptime(tarih_str, "%Y-%m-%d")

print(tarih)


dogum = datetime.datetime(2000, 1, 1)
simdi = datetime.datetime.now()

fark = simdi - dogum
print("Yaş (gün):", fark.days)