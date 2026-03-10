# ================================================================
# PYTHON PROGRAMLAMA DİLİNDE TUPLE, SET VE DICTIONARY
# ================================================================
#
# Bu dosya Python programlama dilinde kullanılan üç temel veri
# yapısını açıklamak amacıyla hazırlanmıştır:
#
# 1) Tuple
# 2) Set
# 3) Dictionary
#
# Bu veri yapıları Python'da verileri saklamak, organize etmek ve
# yönetmek için kullanılır. Her veri yapısının kendine özgü
# özellikleri ve kullanım amaçları bulunmaktadır.
#
#
# Python'da en yaygın kullanılan veri yapıları:
#
# - List
# - Tuple
# - Set
# - Dictionary
#
# Bu dosyada özellikle Tuple, Set ve Dictionary veri yapılarının
# özellikleri, farkları ve hangi durumlarda kullanılmaları
# gerektiği açıklanmaktadır.
#
# ================================================================
# TUPLE (DEMET)
# ================================================================
#
# Tuple, birden fazla veriyi tek bir değişken içerisinde saklamak
# için kullanılan veri yapılarından biridir.
#
# Tuple'lar:
# - Parantez () kullanılarak tanımlanır.
# - Eleman sırası korunur (Ordered).
# - Değiştirilemez (Immutable).
# - Aynı veri tekrar edebilir.
#
#
# ----------------------------------------------------------------
# TUPLE VERİ YAPISININ TEMEL ÖZELLİKLERİ
# ----------------------------------------------------------------
#
# 1) Ordered (Sıralı)
#    Elemanlar belirli bir sıraya sahiptir.
#
# 2) Immutable (Değiştirilemez)
#    Tuple oluşturulduktan sonra elemanları değiştirilemez.
#
# 3) Heterogeneous
#    Farklı veri tipleri aynı tuple içerisinde bulunabilir.
#
# 4) Duplicate Allowed
#    Aynı değer birden fazla kez bulunabilir.
#
#
# ----------------------------------------------------------------
# TUPLE OLUŞTURMA
# ----------------------------------------------------------------
#
# koordinat = (10, 20)
# bilgiler = ("Ahmet", 25, "Ankara")
# karisik = (10, "python", True, 3.14)
#
#
# ----------------------------------------------------------------
# TUPLE NE ZAMAN KULLANILIR?
# ----------------------------------------------------------------
#
# - Değişmemesi gereken veriler saklanacaksa
# - Sabit veri yapıları için
# - Fonksiyonlardan birden fazla değer döndürmek için
#
# Örnek:
#
# def koordinat():
#     return (10, 20)
#
#
# ================================================================
# SET (KÜME)
# ================================================================
#
# Set veri yapısı matematikteki küme mantığı ile çalışır.
#
# Set:
# - Süslü parantez {} ile tanımlanır.
# - Aynı elemandan sadece bir tane bulunur.
# - Elemanlar sırasızdır (Unordered).
# - Elemanlar değiştirilebilir ancak indeks yoktur.
#
#
# ----------------------------------------------------------------
# SET VERİ YAPISININ TEMEL ÖZELLİKLERİ
# ----------------------------------------------------------------
#
# 1) Unordered (Sırasız)
#    Elemanların belirli bir sırası yoktur.
#
# 2) Unique (Tekrarsız)
#    Aynı eleman kümede sadece bir kez bulunur.
#
# 3) Mutable
#    Yeni eleman eklenebilir veya silinebilir.
#
# 4) Index yoktur
#    Set elemanlarına indeks ile erişilemez.
#
#
# ----------------------------------------------------------------
# SET OLUŞTURMA
# ----------------------------------------------------------------
#
# sayilar = {1, 2, 3, 4, 5}
#
# tekrar = {1, 2, 2, 3, 3, 4}
# print(tekrar)
# çıktı: {1,2,3,4}
#
#
# ----------------------------------------------------------------
# SET METOTLARI
# ----------------------------------------------------------------
#
# add()        -> eleman ekler
# remove()     -> eleman siler
# discard()    -> hata vermeden eleman siler
# pop()        -> rastgele eleman siler
# clear()      -> tüm elemanları siler
#
#
# ----------------------------------------------------------------
# SET NE ZAMAN KULLANILIR?
# ----------------------------------------------------------------
#
# - Tekrarsız veri saklamak için
# - Veri kümeleri üzerinde işlem yapmak için
# - Kesişim, birleşim gibi matematiksel işlemler için
#
# Örnek:
#
# A = {1,2,3}
# B = {3,4,5}
#
# print(A & B)   # kesişim
# print(A | B)   # birleşim
#
#
# ================================================================
# DICTIONARY (SÖZLÜK)
# ================================================================
#
# Dictionary veri yapısı anahtar-değer (key-value) mantığı ile
# çalışır.
#
# Dictionary:
# - Süslü parantez {} ile tanımlanır
# - Her anahtar bir değere karşılık gelir
# - Anahtarlar benzersiz olmak zorundadır
#
#
# ----------------------------------------------------------------
# DICTIONARY VERİ YAPISININ TEMEL ÖZELLİKLERİ
# ----------------------------------------------------------------
#
# 1) Key-Value yapısı
#    Her veri bir anahtar ile saklanır.
#
# 2) Mutable
#    Eleman eklenebilir, değiştirilebilir veya silinebilir.
#
# 3) Keys Unique
#    Anahtarlar benzersiz olmak zorundadır.
#
# 4) Hızlı veri erişimi
#    Anahtar üzerinden çok hızlı erişim sağlar.
#
#
# ----------------------------------------------------------------
# DICTIONARY OLUŞTURMA
# ----------------------------------------------------------------
#
# ogrenci = {
#     "isim": "Ahmet",
#     "yas": 22,
#     "bolum": "Bilgisayar Programcılığı"
# }
#
#
# ----------------------------------------------------------------
# DICTIONARY TEMEL İŞLEMLER
# ----------------------------------------------------------------
#
# Eleman erişme:
#
# ogrenci["isim"]
#
#
# Eleman ekleme:
#
# ogrenci["sehir"] = "Ankara"
#
#
# Eleman güncelleme:
#
# ogrenci["yas"] = 23
#
#
# Eleman silme:
#
# del ogrenci["bolum"]
#
#
# ----------------------------------------------------------------
# DICTIONARY METOTLARI
# ----------------------------------------------------------------
#
# keys()      -> anahtarları döndürür
# values()    -> değerleri döndürür
# items()     -> anahtar-değer çiftlerini döndürür
# get()       -> güvenli veri erişimi sağlar
# pop()       -> eleman siler
# clear()     -> tüm sözlüğü temizler
#
#
# ----------------------------------------------------------------
# DICTIONARY NE ZAMAN KULLANILIR?
# ----------------------------------------------------------------
#
# - Veri anahtar-değer şeklinde tutulacaksa
# - Veri tabanı benzeri yapı gerekiyorsa
# - JSON veri yapıları ile çalışırken
#
# Örnek kullanım:
#
# kullanici = {
#     "username": "admin",
#     "password": "1234"
# }
#
#
# ================================================================
# TUPLE, SET VE DICTIONARY ARASINDAKİ FARKLAR
# ================================================================
#
# Tuple
# - Sıralıdır
# - Değiştirilemez
# - Parantez () kullanılır
#
# Set
# - Sırasızdır
# - Tekrarsız veri tutar
# - Süslü parantez {} kullanılır
#
# Dictionary
# - Anahtar-değer yapısı vardır
# - Süslü parantez {} kullanılır
# - Anahtarlar benzersizdir
#
#
# ================================================================
# HANGİ VERİ YAPISI NE ZAMAN KULLANILIR?
# ================================================================
#
# Tuple kullan:
# - Sabit veri varsa
# - Değişmesini istemediğin veri varsa
#
# Set kullan:
# - Tekrarsız veri gerekiyorsa
# - Küme işlemleri yapılacaksa
#
# Dictionary kullan:
# - Anahtar-değer ilişkisi varsa
# - Veri hızlı erişilecekse
#
#
# ================================================================
# BU DOSYADA NELER VAR
# ================================================================
#
# Bu dosyada yer alan konular:
#
# - Tuple veri yapısı
# - Set veri yapısı
# - Dictionary veri yapısı
# - Veri yapılarının özellikleri
# - Temel kullanım örnekleri
# - Veri yapıları arasındaki farklar
# - Hangi veri yapısının hangi durumda kullanılacağı
#
# ================================================================
#                         ÖRNEKLER
# ================================================================

# Tuple tanımı
koordinat = (10, 20)
print("Koordinat:", koordinat)

# Tuple elemanlara erişim
sehirler = ("Ankara", "Samsun", "Sinop")

print(sehirler[0])
print(sehirler[1])

# Farklı türde veri elemanları
bilgi = ("Ahmet", 21, 3.45, True)

print(bilgi)

# Tuple veri parçalama
ogrenci = ("Ali", 22, "Bilgisayar Programcılığı")

isim, yas, bolum = ogrenci

print("İsim:", isim)
print("Yaş:", yas)
print("Bölüm:", bolum)

# ================================================================
# TUPLE ÖRNEKLERİ
# ================================================================

# Tuple (Demet) oluşturma
koordinat = (10, 20)
print("Koordinat:", koordinat)


# Tuple elemanlara erişim
sehirler = ("Ankara", "İstanbul", "İzmir")

print(sehirler[0])
print(sehirler[1])


# Farklı veri türlerinden oluşan tuple
bilgi = ("Ahmet", 21, 3.45, True)

print(bilgi)


# Tuple parçlama (unpacking)
ogrenci = ("Ali", 22, "Bilgisayar Programcılığı")

isim, yas, bolum = ogrenci

print("İsim:", isim)
print("Yaş:", yas)
print("Bölüm:", bolum)


# Tuple uzunluğu
sayilar = (5, 10, 15, 20, 25)

print("Tuple uzunluğu:", len(sayilar))

# Count metodu
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

# index metod

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)



# ================================================================
# SET ÖRNEKLERİ
# ================================================================

# Küme (set) oluşturma
sayilar = {1, 2, 3, 4, 5}

print("Set:", sayilar)


# Tekrar eden elemanların kaldırılması
sayilar = {1, 2, 2, 3, 3, 4, 5}

print("Tekrarsız küme:", sayilar)


# Kümeye eleman ekleme
meyveler = {"elma", "armut"}

meyveler.add("muz")

print(meyveler)


# Küme (set) den eleman silme
meyveler.remove("armut")
print(meyveler)


# Discard metodu
sayilar = {10, 20, 30, 40}
print("İlk küme:", sayilar)

sayilar.discard(20)
print("20 silindikten sonra:", sayilar)


# Kümede olmayan bir eleman silinmek istendiğinde hata vermez
sayilar.discard(100)

print("100 silinmeye çalışıldı:", sayilar)

# pop metodunun küme (set) veri yapısında kullanımı
meyveler = {"elma", "armut", "muz", "kiraz"}

print("İlk küme:", meyveler)
silinen = meyveler.pop()

print("Silinen eleman:", silinen)
print("Kalan küme:", meyveler)


# clear metodu kullanımı. Verilerin kümeden silinmesi
renkler = {"kırmızı", "mavi", "yeşil", "sarı"}
print("İlk küme:", renkler)

renkler.clear()
print("Temizlendikten sonra:", renkler)



# Küme işlemleri
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Kesişim:", A & B)
print("Birleşim:", A | B)
print("Fark:", A - B)



# ================================================================
# DICTIONARY ÖRNEKLERİ
# ================================================================

# Dictionary veri yapısı
ogrenci = {
    "isim": "Mehmet",
    "yas": 21,
    "bolum": "Bilgisayar Programcılığı"
}

print(ogrenci)

# Dictionary eleman ekleme
print("İsim:", ogrenci["isim"])
print("Yaş:", ogrenci["yas"])

# Yeni eleman ekleme
ogrenci["sehir"] = "Ankara"

print(ogrenci)

# Eleman güncelleme
ogrenci["yas"] = 22

print(ogrenci)

# Dictionary eleman silme
del ogrenci["bolum"]

print(ogrenci)


# Dictionary kullanımı
for anahtar, deger in ogrenci.items():
    print(anahtar, ":", deger)


# keys kullanımı
print("Anahtarlar:", ogrenci.keys())


# values kullanımı
print("Değerler:", ogrenci.values())


# items kullanımı
print("Anahtar-Değer Çiftleri:", ogrenci.items())


# get kullanımı
print(ogrenci.get("isim"))
print(ogrenci.get("not", "Anahtar bulunamadı"))


# Öğrenci Bilgi sistemi
ogrenciler = {
    "1001": {"isim": "Ali", "not": 85},
    "1002": {"isim": "Ayşe", "not": 90},
    "1003": {"isim": "Mehmet", "not": 78}
}

for numara, bilgi in ogrenciler.items():
    print(numara, bilgi["isim"], bilgi["not"])


# Pop metodu kullanımı
print("İlk sözlük:", ogrenciler)
silinen = ogrenciler.pop("yas")

print("Silinen değer:", silinen)
print("Güncel sözlük:", ogrenciler)