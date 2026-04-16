
# Dosya Açma / Kapama
# Dosya açma (yazma modu)
dosya = open("ornek.txt", "w")

dosya.write("Merhaba Dünya!")

# Dosya kapatma
dosya.close()

# w = yazma r = okuma a = ekleme
# Dosyaya Yazma
dosya = open("veri.txt", "w")

dosya.write("1. satır\n")
dosya.write("2. satır\n")

dosya.close()

# Dosyadan Okuma


dosya = open("veri.txt", "r")

icerik = dosya.read()
print(icerik)

dosya.close()


# satır satır okumak için

dosya = open("veri.txt", "r")

for satir in dosya:
    print(satir.strip())

dosya.close()

# "with" dosyayı otomatik olarak kapatır 
with open("veri.txt", "r") as dosya:
    icerik = dosya.read()
    print(icerik)

#Hata İhtimalleri (try-except)

try:
    with open("olmayan.txt", "r") as dosya:
        print(dosya.read())
except FileNotFoundError:
    print("Dosya bulunamadı!")

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
