# ================================================================
# PYTHON'DA MATCH-CASE YAPISI (STRUCTURAL PATTERN MATCHING)
# ================================================================
#
# Bu dosya, Python 3.10 ve sonrasında kullanılabilen "match-case"
# kontrol yapısını örneklerle açıklamak amacıyla hazırlanmıştır.
#
# match-case yapısı, klasik if-elif-else zincirine alternatif olarak
# geliştirilen ve daha okunabilir bir çoklu durum kontrolü sağlayan
# yapısal örüntü eşleme (structural pattern matching) mekanizmasıdır.
# 
# diğer dillerdeki switch-case yapısına benzer
#
#
# ----------------------------------------------------------------
# TEMEL AMAÇ
# ----------------------------------------------------------------
# - Bir değişkenin değerine göre farklı blokların çalıştırılması
# - Çoklu eşleşme kontrolü yapılması
# - Veri yapıları (tuple, list, dictionary) üzerinde desen eşlemesi
# - Daha okunabilir ve sürdürülebilir kontrol akışı oluşturulması
#
# ----------------------------------------------------------------
# GENEL SÖZDİZİMİ
# ----------------------------------------------------------------
#
# match ifade:
#     case desen1:
#         işlem
#     case desen2:
#         işlem
#     case _:
#         varsayılan işlem
#
# "_" ifadesi default (diğer tüm durumlar) anlamına gelir.
#
# ----------------------------------------------------------------
# MATCH-CASE ÖZELLİKLERİ
# ----------------------------------------------------------------
# 1) Sabit değer eşleştirme
# 2) Birden fazla değer eşleştirme (|)
# 3) Koşullu eşleştirme (guard ifadesi)
# 4) Tuple desen eşlemesi
# 5) Liste desen eşlemesi
# 6) Dictionary desen eşlemesi
# 7) Tür (type) eşlemesi
#
# ----------------------------------------------------------------
# IF-ELIF İLE FARKI
# ----------------------------------------------------------------
# - match-case daha okunabilir çoklu durum kontrolü sağlar.
# - Yapısal veri eşlemesi yapabilir.
# - Karmaşık if-elif bloklarını sadeleştirebilir.
#
# ----------------------------------------------------------------
# NOT
# ----------------------------------------------------------------
# Bu dosyada yer alan örnekler:
# - Temel kullanım
# - Menü sistemi
# - Sayı analizi
# - Tuple, liste ve sözlük eşlemesi
# - Guard (if) kullanımı
#
# Bu yapı yalnızca Python 3.10 ve üzeri sürümlerde çalışmaktadır.
#
# ================================================================


# Basit Menü Örneği
secim = input("Bir sayı giriniz (1-3): ")

match secim:
    case "1":
        print("Toplama işlemi seçildi")
    case "2":
        print("Çıkarma işlemi seçildi")
    case "3":
        print("Çarpma işlemi seçildi")
    case _:
        print("Geçersiz seçim")

# Gün İsmi Kontrolü
gun = input("Gün giriniz: ").lower()

match gun:
    case "cumartesi" | "pazar":
        print("Hafta sonu")
    case "pazartesi" | "salı" | "çarşamba" | "perşembe" | "cuma":
        print("Hafta içi")
    case _:
        print("Geçersiz gün")


# Sayı Analizi
koordinat = (0, 5)

match koordinat:
    case (0, 0):
        print("Orijin")
    case (0, y):
        print(f"Y ekseni üzerinde, y = {y}")
    case (x, 0):
        print(f"X ekseni üzerinde, x = {x}")
    case (x, y):
        print(f"Nokta: ({x},{y})")


# Liste Pattern Matching
liste = [1, 2, 3]

match liste:
    case []:
        print("Boş liste")
    case [x]:
        print(f"Tek eleman: {x}")
    case [x, y]:
        print(f"İki eleman: {x}, {y}")
    case [x, y, *rest]:
        print(f"İlk iki: {x}, {y} | Diğerleri: {rest}")


# Sözlük (Dictionary) Pattern Matching
kisi = {"isim": "Ali", "yas": 25}

match kisi:
    case {"isim": isim, "yas": yas}:
        print(f"{isim} adlı kişi {yas} yaşında")
    case _:
        print("Geçersiz veri")

# Guard if match-case örneği
notu = int(input("Notunuzu giriniz: "))

match notu:
    case x if 90 <= x <= 100:
        print("Harf Notu: AA")
    case x if 80 <= x < 90:
        print("Harf Notu: BA")
    case x if 70 <= x < 80:
        print("Harf Notu: BB")
    case x if 60 <= x < 70:
        print("Harf Notu: CC")
    case x if 50 <= x < 60:
        print("Harf Notu: DD")
    case x if 0 <= x < 50:
        print("Harf Notu: FF")
    case _:
        print("Geçersiz not girdiniz")


