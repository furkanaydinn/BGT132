x = 10

if x > 5:
    print("5'ten büyük")
else:
    print("5'ten küçük veya eşit")

notu = 75

if notu >= 90:
    print("AA")
elif notu >= 80:
    print("BA")
elif notu >= 70:
    print("BB")
else:
    print("Geçemedin")


yas = 25
ehliyet = True

if yas >= 18 and ehliyet:
    print("Araba kullanabilir")

sicaklik = 32

if sicaklik > 30 or sicaklik < 0:
    print("Dikkatli ol")

'''

İç içe koşullar nested-if ler

'''

puan = 85
devam = True

if puan >= 60:
    if devam:
        print("Dersi geçti")
    else:
        print("Devamsızlıktan kaldı")


isim = "Furkan"

if isim == "Furkan":
    print("Hoş geldin Furkan")


sayilar = [1, 3, 5, 7]

if 5 in sayilar:
    print("Listede var")

aktif = True

if aktif:
    print("Sistem aktif")


#Tek satır koşul için
x = 10

sonuc = "Pozitif" if x > 0 else "Negatif"
print(sonuc)

# Hatalı Giriş kontrolü
yas = int(input("Yaşınızı girin: "))

if yas < 0:
    print("Geçersiz yaş")
elif yas < 18:
    print("Yetişkinsiniz")
else:
    print("Yetişkin değilsiniz")


# Çoklu koşul kısa yazım
if 10 < x < 20:
    print("Aralıkta")

# None veri kontrolü
veri = None

if veri is None:
    print("Boş veri")





