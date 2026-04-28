# ================================================================
# PYTHON PROGRAMLAMA DİLİNDE DATETIME MODÜLÜ (TARİH VE SAAT İŞLEMLERİ)
# ================================================================
#
# Bu dosya Python programlama dilinde kullanılan "datetime" modülünü
# tanıtmak ve tarih-saat işlemlerini fonksiyonel bir yapı ile
# açıklamak amacıyla hazırlanmıştır.
#
# datetime modülü:
# - Tarih ve saat bilgileri ile çalışmayı sağlar
# - Zaman hesaplamaları yapmaya olanak tanır
# - Formatlama ve dönüştürme işlemlerini destekler
#
#
# ----------------------------------------------------------------
# DATETIME MODÜLÜNÜN TEMEL KULLANIM ALANLARI
# ----------------------------------------------------------------
#
# 1) Güncel tarih ve saat bilgisi alma
#    - datetime.datetime.now()
#    - datetime.date.today()
#
# 2) Tarih bileşenlerine erişim
#    - yıl, ay, gün, saat, dakika, saniye gibi değerler alınabilir
#
# 3) Özel tarih oluşturma
#    - datetime.datetime(yıl, ay, gün, ...)
#
# 4) Tarih formatlama (string'e çevirme)
#    - strftime() fonksiyonu kullanılır
#
# 5) String ifadeyi tarihe çevirme
#    - strptime() fonksiyonu kullanılır
#
# 6) Tarih karşılaştırma işlemleri
#    - iki tarih büyüklük olarak karşılaştırılabilir
#
# 7) Tarih farkı hesaplama
#    - iki tarih arasındaki gün farkı hesaplanabilir
#
# 8) ISO format işlemleri
#    - tarihleri standart ISO formatına dönüştürme
#
#
# ----------------------------------------------------------------
# DATETIME MODÜLÜNÜN TEMEL ÖZELLİKLERİ
# ----------------------------------------------------------------
#
# 1) Nesne Tabanlı Yapı
#    datetime, date ve time gibi farklı sınıflar içerir.
#
# 2) Yüksek Hassasiyet
#    Mikro saniye seviyesine kadar zaman tutabilir.
#
# 3) Esnek Formatlama
#    strftime() ile farklı tarih-saat formatları oluşturulabilir.
#
# 4) Hesaplama Yeteneği
#    Tarihler arasında fark alma, yaş hesaplama gibi işlemler yapılabilir.
#
#
# ----------------------------------------------------------------
# BU DOSYADA NELER VAR
# ----------------------------------------------------------------
#
# Bu dosyada yer alan örnekler:
#
# - Güncel tarih ve saat bilgisini döndüren fonksiyon
# - Tarih bileşenlerini (yıl, ay, gün vb.) parçalayan fonksiyon
# - Parametre ile tarih oluşturma
# - Gün ve ay adını alma
# - Tarih ve saat formatlama işlemleri
# - Haftanın gününü indeks olarak öğrenme
# - Sadece tarih bilgisini alma
# - İki tarihi karşılaştırma
# - İki tarih arasındaki gün farkını hesaplama
# - ISO formatına dönüştürme
# - Tarihi string'e çevirme
# - String ifadeyi datetime nesnesine dönüştürme
# - Gün bazlı yaş hesaplama
#
# ================================================================
#                         ÖRNEKLER
# ================================================================

import datetime


def simdiki_tarih():
    return datetime.datetime.now()

def tarih_bilesenleri():
    x = datetime.datetime.now()
    return {
        "yil": x.year,
        "ay": x.month,
        "gun": x.day,
        "saat": x.hour,
        "dakika": x.minute
    }

def tarih_olustur(yil, ay, gun, saat=0, dakika=0, saniye=0):
    return datetime.datetime(yil, ay, gun, saat, dakika, saniye)

def gun_adi():
    return datetime.datetime.now().strftime("%A")

def ay_adi():
    return datetime.datetime.now().strftime("%B")

def formatli_tarih():
    return datetime.datetime.now().strftime("%d/%m/%Y")

def formatli_saat():
    return datetime.datetime.now().strftime("%H:%M:%S")

def haftanin_gunu_index():
    return datetime.datetime.now().weekday()

def bugun_tarih():
    return datetime.date.today()

def tarih_karsilastir(t1, t2):
    return "t1 daha yeni" if t1 > t2 else "t2 daha yeni"

def gun_farki(t1, t2):
    return (t1 - t2).days

def iso_format(tarih):
    return tarih.isoformat()

def tarih_to_string():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def string_to_tarih(tarih_str):
    return datetime.datetime.strptime(tarih_str, "%Y-%m-%d")

def yas_gun(dogum_tarihi):
    return (datetime.datetime.now() - dogum_tarihi).days


