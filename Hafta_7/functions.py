# ================================================================
# PYTHON PROGRAMLAMA DİLİNDE FONKSİYONLAR
# ================================================================
#
# Bu dosya Python programlama dilinde kullanılan fonksiyonları
# açıklamak amacıyla hazırlanmıştır.
#
# Fonksiyonlar, belirli bir görevi yerine getiren ve tekrar
# kullanılabilir kod bloklarıdır.
#
#
# ================================================================
# FONKSİYON TANIMLAMA
# ================================================================
#
# Python'da fonksiyonlar "def" anahtar kelimesi ile tanımlanır.
#
# Genel yapı:
#
# def fonksiyon_adi():
#     yapılacak işlemler
#
#
# ================================================================
# PARAMETRELER VE RETURN
# ================================================================
#
# Fonksiyonlara dışarıdan veri göndermek için parametreler kullanılır.
# Fonksiyon sonucunu geri döndürmek için return kullanılır.
#
#
# ----------------------------------------------------------------
# PARAMETRELİ FONKSİYON
# ----------------------------------------------------------------
#
# def fonksiyonAdi(parametre1, parametre2):
#     print(parametre1 + " " + parametre2)
#
#
# ----------------------------------------------------------------
# RETURN KULLANIMI
# ----------------------------------------------------------------
#
# def carp(a, b):
#     return a * b
#
#
# NOT:
# return değeri fonksiyondan dışarıya veri taşır.
#
#
# ================================================================
# VARSAYILAN PARAMETRELER
# ================================================================
#
# Fonksiyonlarda parametrelere varsayılan değer atanabilir.
#
# Eğer kullanıcı değer girmezse, varsayılan değer kullanılır.
#
#
# Örnek:
#
# def selamla(isim="Misafir"):
#     print("Merhaba", isim)
#
# selamla()
# selamla("Ahmet")
#
#
# NOT:
# Varsayılan parametreler en sonda tanımlanmalıdır.
#
#
# ================================================================
# *args ve **kwargs
# ================================================================
#
# Fonksiyonlara değişken sayıda parametre göndermek için kullanılır.
#
#
# ----------------------------------------------------------------
# *args (Pozisyonel parametreler)
# ----------------------------------------------------------------
#
# Birden fazla değeri tuple olarak alır.
#
# def sayilari_topla(*args):
#     toplam = 0
#     for sayi in args:
#         toplam += sayi
#     return toplam
#
# print(sayilari_topla(1,2,3,4,5))
#
#
# ----------------------------------------------------------------
# **kwargs (Anahtar-değer parametreler)
# ----------------------------------------------------------------
#
# Parametreleri dictionary olarak alır.
#
# def bilgileri_yazdir(**kwargs):
#     for anahtar, deger in kwargs.items():
#         print(anahtar, ":", deger)
#
# bilgileri_yazdir(isim="Ahmet", yas=25, sehir="Ankara")
#
#
# ================================================================
# SCOPE (DEĞİŞKEN KAPSAMI)
# ================================================================
#
# Scope, bir değişkenin nereden erişilebilir olduğunu belirler.
#
#
# ----------------------------------------------------------------
# YEREL (LOCAL) DEĞİŞKEN
# ----------------------------------------------------------------
#
# Fonksiyon içinde tanımlanan değişkendir.
# Sadece fonksiyon içinde kullanılabilir.
#
# def fonksiyon():
#     x = 10
#     print(x)
#
#
# ----------------------------------------------------------------
# GLOBAL DEĞİŞKEN
# ----------------------------------------------------------------
#
# Fonksiyon dışında tanımlanır.
# Programın her yerinden erişilebilir.
#
# x = 20
#
# def yazdir():
#     print(x)
#
#
# ----------------------------------------------------------------
# GLOBAL ANAHTAR KELİMESİ
# ----------------------------------------------------------------
#
# Fonksiyon içinde global değişkeni değiştirmek için kullanılır.
#
# x = 10
#
# def degistir():
#     global x
#     x = 50
#
#
# ================================================================
# FONKSİYONLAR NE ZAMAN KULLANILIR?
# ================================================================
#
# - Aynı işlemi tekrar tekrar yapacaksan
# - Kodun daha düzenli olmasını istiyorsan
# - Büyük programları parçalara bölmek istiyorsan
#
#
# ================================================================
# FONKSİYONLARIN AVANTAJLARI
# ================================================================
#
# - Kod tekrarını azaltır
# - Hataları azaltır
# - Okunabilirliği artırır
# - Test etmeyi kolaylaştırır
#
#
# ================================================================
# BU DOSYADA NELER VAR
# ================================================================
#
#
# - Fonksiyon tanımlama
# - Parametreler ve return
# - Varsayılan parametreler
# - *args ve **kwargs kullanımı
# - Scope (yerel ve global değişkenler)
#
# ================================================================


# Parametresiz fonksiyon örneği
def selam_ver():
    print("Merhaba Dünya")

selam_ver()

# Varsayılan parametreli örnek
def notOrtalamasiHesapla(vizeNotu=0.0, finalNotu=0.0):
     hesap = (vizeNotu*40)/100 + (finalNotu*60)/100
     return hesap

ortalama = notOrtalamasiHesapla()

print(f"Ortalama not: {ortalama}")

# Birden fazla değer döndürme
def hesapla(a, b):
    return a + b, a * b, a/b

toplam, carpim, bolme = hesapla(3,4)
print("Toplam:", toplam)
print("Çarpım:", carpim)
print("Bolme:", bolme)
     
def usAlma(sayi,us): 
     return sayi**us    

print(usAlma(5,4))

# args kullanımı, birden fazla argüman girilmesi için
def carpim(*sayilar):
    sonuc = 1
    for s in sayilar:
        sonuc *= s
    return sonuc

print(carpim(1,2,3))
print(carpim(5,10,15,20))

# kwargs kullanımı, sozluk yapısı için
def akademik(**argumanlar):
    bilgiler = []
    for k, v in argumanlar.items():
        bilgiler.append(k + ": " + str(v))
    return ", ".join(bilgiler), type(bilgiler)

print(akademik(Name="Furkan", Bolum="Programcılık", Ders="BGT132"))

# Global değişken
# Fonksiyon dışında, önceden tanımlanmış
# Her yerden erişilebilir.

def okulBilgi():
    okul = "OSTİM"
    return okul

print(okulBilgi())

# Local(Yerel) Değişken
# Fonksiyon dışından erişilemez
y = 80
def yeniFonksiyon():
    y = 45
    return y

yeniFonksiyon()
print(y)


def dis_fonksiyon():
    def ic_fonksiyon():
        print("İç fonksiyon çalıştı")
    ic_fonksiyon()

dis_fonksiyon()

topla = lambda a, b: a + b
print(topla(3, 7))

kare = lambda x: x**2
print(kare(6))

sayilar = [1, 2, 3, 4, 5]

def kare_al(x):
    return x**2

sonuc = list(map(kare_al, sayilar))
print(sonuc)

def tek_mi(sayi):
    if sayi % 2 == 1:
        return True
    else:
        return False

print(tek_mi(7))

def faktoriyel(n):
    sonuc = 1
    for i in range(1, n+1):
        sonuc *= i
    return sonuc

print(faktoriyel(5))

# Öz yineleme örneği
def faktoriyel(n):
    if n == 1:
        return 1
    return n * faktoriyel(n-1)


print(faktoriyel(5))

def not_hesapla(notu):
    if notu >= 85:
        return "AA"
    elif notu >= 70:
        return "BB"
    elif notu >= 50:
        return "CC"
    else:
        return "FF"

print(not_hesapla(90))

def menu():
    print("1- Topla")
    print("2- Çıkar")

def hesapla(secim, a, b):
    if secim == 1:
        return a + b
    elif secim == 2:
        return a - b

menu()
sonuc = hesapla(1, 10, 5)
print("Sonuç:", sonuc)