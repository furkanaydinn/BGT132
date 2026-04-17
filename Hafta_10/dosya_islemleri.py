# ================================================================
#                DOSYA İŞLEMLERİ (FILE OPERATIONS)
# ================================================================
#
# Bu bölümde Python programlama dilinde dosya işlemleri incelenmektedir.
# Dosya işlemleri, verilerin kalıcı olarak saklanması ve daha sonra
# tekrar kullanılabilmesi açısından büyük önem taşır.
#
# Python’da dosyalar:
# - Oluşturulabilir
# - Yazılabilir
# - Okunabilir
# - Güncellenebilir
#
# Temel dosya modları:
# - "w" → Yazma (dosyayı sıfırlar veya oluşturur)
# - "r" → Okuma (dosya mevcut olmalıdır)
# - "a" → Ekleme (var olan dosyanın sonuna yazar)
#
# ================================================================
# 1. DOSYA AÇMA VE KAPAMA (open / close)
# ================================================================
#
# open() fonksiyonu ile dosya açılır.
# close() fonksiyonu ile dosya kapatılır.
#
# Not:
# Dosya kapatılmazsa veri kaybı veya bellek sızıntısı oluşabilir.


dosya = open("Hafta_10\ornek.txt", "w")  # Dosya yazma modunda açılır
dosya.write("Merhaba Dünya!")   # Dosyaya veri yazılır
dosya.close()                   # Dosya kapatılır



# ================================================================
# 2. DOSYAYA YAZMA (WRITE)
# ================================================================
#
# write() fonksiyonu ile dosyaya veri yazılır.
# "\n" ifadesi yeni satır oluşturur.
#

dosya = open("veri.txt", "w")

dosya.write("1. satır\n")
dosya.write("2. satır\n")

dosya.close()


# ================================================================
# 3. DOSYADAN OKUMA (READ)
# ================================================================
#
# read() fonksiyonu dosyanın tamamını okur ve string olarak döndürür.
#

dosya = open("veri.txt", "r")

icerik = dosya.read()
print(icerik)

dosya.close()


# ================================================================
# 4. SATIR SATIR OKUMA
# ================================================================
#
# Dosya üzerinde döngü kurularak satır satır okuma yapılabilir.
# strip() → satır sonundaki boşluk ve \n karakterini temizler.
#

dosya = open("veri.txt", "r")

for satir in dosya:
    print(satir.strip())

dosya.close()



# read() ile okuma ile satır satır okuma arasındaki fark nedir?
# Cevap: 


# ================================================================
# 5. WITH KULLANIMI (OTOMATİK KAPAMA)
# ================================================================
#
# with yapısı dosyayı otomatik olarak kapatır.
# Bu yöntem daha güvenli ve önerilen kullanımdır.
#

with open("veri.txt", "r") as dosya:
    icerik = dosya.read()
    print(icerik)


# ================================================================
# 6. HATA YÖNETİMİ (TRY-EXCEPT)
# ================================================================
#
# Dosya işlemlerinde en sık karşılaşılan hata:
# - Dosya bulunamaması (FileNotFoundError)
#
# try-except yapısı ile programın çökmesi engellenir.
#

try:
    with open("olmayan.txt", "r") as dosya:
        print(dosya.read())
except FileNotFoundError:
    print("Dosya bulunamadı!")


# ================================================================
# 7. UYGULAMA: YAZ + OKU
# ================================================================
#
# Dosyaya veri yazma ve ardından okuma işlemi birlikte uygulanır.
#

try:
    # Dosyaya yaz
    with open("notlar.txt", "w") as dosya:
        dosya.write("BGT132 Yazılım Geliştirme Teknolojileri\n")
        dosya.write("Dosya işlemleri gerçekleştirildi\n")

    # Dosyadan oku
    with open("notlar.txt", "r") as dosya:
        for satir in dosya:
            print(satir.strip())

except Exception as hata:
    print("Bir hata oluştu:", hata)