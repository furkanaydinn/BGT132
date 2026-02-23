# Soru 1 - Sinema Bilet Otomasyonu
yas = int(input("Yaşınızı giriniz: "))
ogrenci = input("Öğrenci misiniz? (E/H): ").strip().upper()

tam_bilet = 150
ogrenci_bilet = 100

if yas < 0:
    print("Geçersiz yaş girdiniz.")

else:
    # 12 yaş altı %50 indirim
    if yas < 12:
        fiyat = tam_bilet * 0.5
        print(f"12 yaş altı indirimi uygulandı.")
        print(f"Ödenecek tutar: {fiyat:.2f} TL")

    # Öğrenci bileti
    elif ogrenci == "E":
        fiyat = ogrenci_bilet
        print("Öğrenci bileti uygulandı.")
        print(f"Ödenecek tutar: {fiyat:.2f} TL")

    # Tam bilet
    elif ogrenci == "H":
        fiyat = tam_bilet
        print("Tam bilet ücreti uygulandı.")
        print(f"Ödenecek tutar: {fiyat:.2f} TL")

    else:
        print("Öğrenci bilgisi hatalı girildi. Lütfen E veya H giriniz.")


# Soru 2 - Vücut Kitle İndeksi (BMI) Hesaplama

boy = float(input("Boyunuzu metre cinsinden giriniz: "))
kilo = float(input("Kilonuzu kg cinsinden giriniz: "))

bmi = kilo / (boy * boy)

print(f"BMI değeriniz: {bmi:.2f}")

if bmi < 18.5:
    print("Kategori: Zayıf")
elif bmi <= 24.9:
    print("Kategori: Normal")
elif bmi <= 29.9:
    print("Kategori: Fazla kilolu")
else:
    print("Kategori: Obez")


# Soru 3 - Online Sınav Değerlendirme
vize = float(input("Vize notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

ortalama = vize * 0.4 + final * 0.6

print(f"Ortalama: {ortalama:.2f}")

if final < 50:
    print("Final 50'nin altında olduğu için Kaldı")
elif ortalama >= 60:
    print("Geçti")
else:
    print("Kaldı")


# Soru 4 - Banka Hesap İşlemi
bakiye = float(input("Mevcut bakiyenizi giriniz: "))
cekilecek = float(input("Çekmek istediğiniz tutarı giriniz: "))

gunluk_limit = 5000

if cekilecek > gunluk_limit:
    print("Limit aşıldı")
elif cekilecek > bakiye:
    print("İşlem reddedildi - Yetersiz bakiye")
else:
    bakiye -= cekilecek
    print("İşlem başarılı")
    print(f"Yeni bakiye: {bakiye:.2f} TL")


# Soru 5 - Sayı Analiz Programı
sayi = int(input("Bir tam sayı giriniz: "))

# Pozitif / Negatif / Sıfır
if sayi > 0:
    print("Pozitif sayı")
elif sayi < 0:
    print("Negatif sayı")
else:
    print("Sıfır")

# Çift / Tek
if sayi % 2 == 0:
    print("Çift sayı")
else:
    print("Tek sayı")

# Bölünebilirlik kontrolleri
if sayi % 3 == 0:
    print("3'e bölünüyor")

if sayi % 2 == 0:
    print("2'ye bölünüyor")

if sayi % 3 == 0 and sayi %2 == 0:
    print("6'ya bölünüyor")

# 10'dan büyük mü?
if sayi > 10:
    print("10'dan büyük")


# Soru 6 - Elektrik Faturası Hesaplama
tuketim = float(input("Aylık elektrik tüketimini (kWh) giriniz: "))

if tuketim <= 150:
    fatura = tuketim * 1.5
elif tuketim <= 300:
    fatura = tuketim * 2.0
else:
    fatura = tuketim * 2.8

print(f"Toplam fatura: {fatura:.2f} TL")


# Soru 7 - Ürün İndirim Hesaplama

tutar = float(input("Alışveriş tutarını giriniz: "))

if tutar > 5000:
    indirim = 0.30
elif tutar > 2000:
    indirim = 0.20
elif tutar > 1000:
    indirim = 0.10
else:
    indirim = 0

odenek = tutar * (1 - indirim)

print(f"Ödenecek tutar: {odenek:.2f} TL")


# Soru 8 - Araç Yakıt hesaplama 
mesafe = float(input("Gidilen mesafe (km): "))
tuketim = float(input("Araç tüketimi (litre/100 km): "))
litre_fiyat = float(input("Litre fiyatı: "))

toplam_litre = (mesafe / 100) * tuketim
maliyet = toplam_litre * litre_fiyat

print(f"Toplam yakıt maliyeti: {maliyet:.2f} TL")

if maliyet > 2000:
    print("Uzun yol")
else:
    print("Şehir içi tüketim")


# Soru 9 - Basit vergi hesaplama
maas = float(input("Brüt maaşınızı giriniz: "))

if maas <= 20000:
    vergi_orani = 0.10
elif maas <= 40000:
    vergi_orani = 0.20
else:
    vergi_orani = 0.30

vergi = maas * vergi_orani
net_maas = maas - vergi

print(f"Vergi tutarı: {vergi:.2f} TL")
print(f"Net maaş: {net_maas:.2f} TL")