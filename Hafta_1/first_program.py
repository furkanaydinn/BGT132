# Python da tekli yorum satırı yapmak isterseniz, # işaretini kullanabilirsiniz.
# Yorum satırları program tarafından çalıştırılmaz.

'''

Çoklu yorum satırı yapmak isterseniz, üç tırnak işaretini kullanabilirsiniz. 
Hem tekli yorum satırı, 
hem de çoklu yorum satırları 
kod'un, programın ne görev yaptığını açıklamak için kullanılabilir.
Bu sayede, kodunuza tekrar dönüp bakmak istediğinizde, yorum satırları size ne yaptığınızı hatırlatır.
Ya da kodunuzu daha iyi anlamak için başkalarına açıklama yaparken de yorum satırlarından faydalanabilirsiniz.
Sizden sonra aynı programı geliştirecek olan kişiler için de yorum satırları oldukça faydalı olacaktır.

'''

# Aşağıdaki kod, "Yazılım Geliştirme Teknolojileri Dersi" ifadesini ekrana yazdırır.
# Print metodu ekrana çıktı verir.
# Print() metodu ile birden fazla ifadeyi birleştirip yazdırabilirsiniz.
print("Yazılım Geliştirme Teknolojileri Dersi")
print("Bilgisayar" + " " + "Programcılığı" + " " +  "Bölümü")

# Çıktıları formatlayabiliriz.
print("Yazılım Geliştirme Teknolojileri Dersi, {} bölümü {}. sınıf öğrencileri tarafından alınır.".format("bilgisayar programcılığı", 1))

# Değişken tanimi nasil yapilir
# Değişken tanımı için bazı standart tanımlar vardır

# Snake case: degisken_ismi => kelimeler arasına alt çizgi konulur ve tüm harfler küçük yazılır.
# Camel case: degiskenIsmi  => ilk harf küçük, sonra gelen kelimelerin ilk harfleri büyük yazılır
# Pascal case: DegiskenIsmi  => Her bir kelimenin ilk harfi büyük yazılır.
# Kebab case: degisken-ismi  => Kelimeler arasına tire konulur ve tüm harfler küçük yazılır.

# Bu standart tanımlamalar kodun okunabilirliğini artırır.
# degisken ismi = deger biçiminde tanımlanır. Şöyle ki:

ogrenci_adi = "Ahmet"
ogrenci_soyadi = "Yılmaz"
ogrenci_numarasi = 12345

# Değişkenler kullanılarak ekrana yazdırma işlemi (F-string formatlama yöntemi)
print(f"Öğrenci Adı: {ogrenci_adi}, Öğrenci Soyadı: {ogrenci_soyadi}, Öğrenci Numarası: {ogrenci_numarasi}")

# Değişken türleri
kayit_tarihi = "2023-09-01"    # => String veri tipi      Metinsel veri tipi
kayit_sayisi = 30              # => Integer veri tipi     Tam sayı veri tipi
not_ortalaması = 85.5          # => Float veri tipi       Ondalıklı sayı veri tipi
uslu_sayi = 5e8                # => Float veri tipi       Ondalıklı sayı veri tipi
kayit_durum = True             # => Boolean veri tipi     Mantıksal veri tipi (True veya False değer alır)
bos_degisken = None            # => NoneType veri tipi    Hiçbir değeri olmayan değişken

print(kayit_tarihi)
print(kayit_sayisi)
print(not_ortalaması)
print(uslu_sayi)
print(kayit_durum)
print(bos_degisken)


# Birden fazla değişkeni tek satırda tanımlama
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Birden fazla değişkene aynı değeri tanımlama
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Type() metodu ile değişkenin veri tipini öğrenebilirsiniz.
print(type(kayit_tarihi))
print(type(kayit_sayisi))
print(type(not_ortalaması))
print(type(uslu_sayi))
print(type(kayit_durum))
print(type(bos_degisken))

print(20)
print(False)
print("Merhaba Dünya")



