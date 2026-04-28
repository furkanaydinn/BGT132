# ================================================================
# PYTHON PROGRAMLAMA DİLİNDE RANDOM MODÜLÜ (RASTGELE SAYI ÜRETİMİ)
# ================================================================
#
# Bu dosya Python programlama dilinde kullanılan "random" modülünü
# tanıtmak ve rastgele veri üretimi ile ilgili temel işlemleri
# örneklerle açıklamak amacıyla hazırlanmıştır.
#
# random modülü:
# - Rastgele sayılar üretmek için kullanılır
# - Listeler içerisinden rastgele seçim yapmayı sağlar
# - Oyun, simülasyon ve güvenlik uygulamalarında kullanılır
#
#
# ----------------------------------------------------------------
# RANDOM MODÜLÜNÜN TEMEL KULLANIM ALANLARI
# ----------------------------------------------------------------
#
# 1) Rastgele sayı üretme
#    - random.randint(a, b) → a ile b arasında tam sayı üretir
#    - random.random() → 0 ile 1 arasında ondalıklı sayı üretir
#
# 2) Liste içerisinden rastgele seçim
#    - random.choice() → listeden tek bir eleman seçer
#    - random.sample() → listeden birden fazla eleman seçer
#
# 3) Listeyi karıştırma
#    - random.shuffle() → listenin elemanlarını karıştırır
#
# 4) Rastgele veri üretimi
#    - Şifre oluşturma
#    - Oyun mekanikleri (tahmin oyunları vb.)
#
#
# ----------------------------------------------------------------
# RANDOM MODÜLÜNÜN TEMEL ÖZELLİKLERİ
# ----------------------------------------------------------------
#
# 1) Pseudo-Random (Sözde Rastgelelik)
#    Üretilen sayılar tamamen rastgele değil, algoritmik olarak
#    üretilir ancak rastgele gibi davranır.
#
# 2) Deterministic Yapı
#    Aynı başlangıç değeri (seed) verilirse aynı sonuçlar elde edilir.
#
# 3) Kullanım Kolaylığı
#    Basit fonksiyonlarla hızlıca rastgele veri üretilebilir.
#
# 4) Geniş Kullanım Alanı
#    Oyunlar, simülasyonlar, test verisi üretimi gibi birçok alanda kullanılır.
#
#
# ----------------------------------------------------------------
# BU DOSYADA NELER VAR
# ----------------------------------------------------------------
#
# Bu dosyada yer alan örnekler:
#
# - Belirli aralıkta rastgele tam sayı üretme
# - Liste içerisinden rastgele eleman seçme
# - Liste elemanlarını karıştırma
# - Liste içerisinden rastgele alt küme seçme
# - 0 ile 1 arasında ondalıklı sayı üretme
# - Basit şifre oluşturma mekanizması
# - Kullanıcı etkileşimli sayı tahmin oyunu
#
# ================================================================
#                         ÖRNEKLER
# ================================================================

import random

# Rastgele tam sayı seç
sayi = random.randint(1, 10)
print("Rastgele sayı:", sayi)


# rastgele eleman seçme
meyveler = ["elma", "armut", "muz", "çilek"]
secim = random.choice(meyveler)
print("Seçilen meyve:", secim)


# Dizileri karıştırma
sayilar = [1, 2, 3, 4, 5]
random.shuffle(sayilar)
print("Karıştırılmış liste:", sayilar)



# Dizi içerisinden rastgele alt dizi seçtirme
sayilar = [10, 20, 30, 40, 50]
secim = random.sample(sayilar, 3)
print("Seçilen sayılar:", secim)

# Ondalıklı sayı üretme
sayi = random.random()
print("0 ile 1 arasında sayı:", sayi)


# Basit şifre oluşturma mekanizması
karakterler = "abcdefghijklmnopqrstuvwxyz1234567890"

sifre = ""

for i in range(6):
    sifre += random.choice(karakterler)

print("Oluşturulan şifre:", sifre)

# Sayı tahmin oyunu
tutulan = random.randint(1, 10)
tahmin = int(input("1-10 arasında bir sayı tahmin et: "))

if tahmin == tutulan:
    print("Tebrikler! Bildiniz.")
else:
    print("Yanlış! Doğru sayı:", tutulan)