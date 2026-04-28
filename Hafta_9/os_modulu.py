# ================================================================
# PYTHON PROGRAMLAMA DİLİNDE OS MODÜLÜ (DOSYA VE KLASÖR İŞLEMLERİ)
# ================================================================
#
# Bu dosya Python programlama dilinde yer alan "os" modülünü
# tanıtmak ve işletim sistemi ile etkileşim kurmayı sağlayan
# temel fonksiyonları örneklerle açıklamak amacıyla hazırlanmıştır.
#
# os modülü:
# - Dosya ve klasör işlemleri yapmayı sağlar
# - İşletim sistemi ile doğrudan etkileşim kurar
# - Platform bağımsız (Windows, Linux, MacOS) çalışmayı destekler
#
#
# ----------------------------------------------------------------
# OS MODÜLÜNÜN TEMEL KULLANIM AMAÇLARI
# ----------------------------------------------------------------
#
# 1) Çalışma dizini işlemleri
#    - os.getcwd() → mevcut klasörü öğrenme
#    - os.chdir()  → klasör değiştirme
#
# 2) Klasör içeriğini listeleme
#    - os.listdir() → bulunduğun dizindeki dosya ve klasörleri listeler
#
# 3) Klasör oluşturma ve silme
#    - os.mkdir() → yeni klasör oluşturur
#    - os.rmdir() → klasörü siler
#
# 4) Dosya kontrol işlemleri
#    - os.path.exists() → dosya/klasör var mı kontrol eder
#    - os.path.isfile() → dosya mı kontrol eder
#    - os.path.isdir()  → klasör mü kontrol eder
#
# 5) Dosya işlemleri
#    - os.remove() → dosya siler
#    - os.path.getsize() → dosya boyutunu verir
#
# 6) Yol (path) işlemleri
#    - os.path.join() → güvenli yol oluşturma
#
# 7) Ortam değişkenleri (Environment Variables)
#    - os.environ → tüm sistem değişkenlerini verir
#    - os.environ.get() → belirli değişkeni getirir
#
# 8) Dizin ağacı üzerinde gezinme
#    - os.walk() → tüm klasör ve alt klasörleri dolaşır
#
#
# ----------------------------------------------------------------
# OS MODÜLÜNÜN TEMEL ÖZELLİKLERİ
# ----------------------------------------------------------------
#
# 1) Sistem Bağımsızlığı
#    Aynı kod farklı işletim sistemlerinde çalışabilir.
#
# 2) Güçlü Dosya Yönetimi
#    Dosya ve klasör işlemleri programatik olarak kontrol edilir.
#
# 3) Dinamik Yapı
#    Çalışma dizini ve dosya sistemi runtime sırasında değiştirilebilir.
#
# 4) Güvenli Yol Yönetimi
#    os.path.join() ile hatasız ve platform uyumlu yollar oluşturulur.
#
#
# ----------------------------------------------------------------
# BU DOSYADA NELER VAR
# ----------------------------------------------------------------
#
# Bu dosyada yer alan örnekler:
#
# - Mevcut çalışma dizinini öğrenme
# - Klasör içeriğini listeleme
# - Belirli bir dizinin içeriğini görüntüleme
# - Klasör oluşturma ve silme
# - Çalışma dizinini değiştirme
# - Dosya/klasör varlık kontrolü
# - Dosya mı klasör mü kontrolü
# - Dosya boyutu öğrenme
# - Dosya silme işlemi
# - Yol (path) oluşturma
# - Ortam değişkenlerini listeleme
# - PATH değişkenini okuma
# - os.walk() ile dizin ağacını gezme
#
# ================================================================
#                         ÖRNEKLER
# ================================================================



import os

cwd = os.getcwd()
print("Mevcut klasor:", cwd)


dosyalar = os.listdir()
for d in dosyalar:
    print(d)

klasor = "C:/"
icerik = os.listdir(klasor)

for eleman in icerik:
    print(eleman)


os.mkdir("deneme_klasor")
print("Klasor olusturuldu")


os.mkdir("deneme_klasor")
print("Klasor olusturuldu")


os.rmdir("deneme_klasor")
print("Klasor silindi")


os.chdir("C:/")
print("Yeni klasor:", os.getcwd())


if os.path.exists("test.txt"):
    print("Dosya var")
else:
    print("Dosya yok")


yol = "test.txt"

if os.path.isfile(yol):
    print("Bu bir dosya")
elif os.path.isdir(yol):
    print("Bu bir klasor")


boyut = os.path.getsize("test.txt")
print("Dosya boyutu:", boyut, "byte")


if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("Dosya silindi")


yol = os.path.join("C:/", "Users", "Public")
print("Olusan yol:", yol)



env = os.environ

for anahtar, deger in env.items():
    print(anahtar, "=", deger)



path = os.environ.get("PATH")
print("PATH:", path)



for klasor, alt_klasorler, dosyalar in os.walk("."):
    print("Klasor:", klasor)
    print("Alt klasorler:", alt_klasorler)
    print("Dosyalar:", dosyalar)
    print("-----")

