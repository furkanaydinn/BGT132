# ================================================================
# PYTHON PROGRAMLAMA DİLİNDE LİSTELER (LISTS)
# ================================================================
#
# Bu dosya Python programlama dilinde kullanılan "Liste (List)"
# veri yapısını açıklamak ve temel liste işlemlerini örneklerle
# göstermek amacıyla hazırlanmıştır.
#
# Liste (List), Python'da birden fazla veriyi tek bir değişken
# içerisinde saklamaya olanak sağlayan en temel veri yapılarından
# biridir.
#
# Listeler:
# - Köşeli parantez [] kullanılarak tanımlanır.
# - Birden fazla veri tipini aynı yapı içerisinde barındırabilir.
# - Elemanlara indeks numarası ile erişilebilir.
# - 0'dan başlayan indeksleme sistemine sahiptir.
#
#
# ----------------------------------------------------------------
# LİSTE VERİ YAPISININ TEMEL ÖZELLİKLERİ
# ----------------------------------------------------------------
#
# 1) Ordered (Sıralı)
#    Liste elemanları belirli bir sıraya sahiptir ve bu sıra korunur.
#
# 2) Mutable (Değiştirilebilir)
#    Liste oluşturulduktan sonra elemanlar değiştirilebilir.
#
# 3) Dynamic (Dinamik)
#    Listeye yeni elemanlar eklenebilir veya mevcut elemanlar silinebilir.
#
# 4) Heterogeneous
#    Aynı liste içinde farklı veri tipleri bulunabilir.
#    (int, string, float, boolean vb.)
#
#
# ----------------------------------------------------------------
# LİSTE OLUŞTURMA
# ----------------------------------------------------------------
#
# Liste oluşturmak için köşeli parantez kullanılır.
#
# Örnek:
#
# sayilar = [10, 20, 30]
# bolumler = ["programlama", "mekatronik", "makine"]
# karisik_liste = [10, "python", 3.14, True]
#
#
# ----------------------------------------------------------------
# LİSTE İŞLEMLERİNİN TEMEL KATEGORİLERİ
# ----------------------------------------------------------------
#
# 1) Eleman ekleme
#    - append()
#    - insert()
#    - extend()
#
# 2) Eleman silme
#    - remove()
#    - pop()
#    - del
#
# 3) Eleman güncelleme
#    - indeks kullanılarak değer değiştirilebilir
#
# 4) Liste uzunluğu öğrenme
#    - len() fonksiyonu kullanılır
#
# 5) Liste dilimleme (Slicing)
#    - listenin belirli aralıkları alınabilir
#
# 6) Liste üzerinde döngü ile gezinme
#    - for döngüsü
#    - while döngüsü
#
# 7) Liste metotları
#    - sort()
#    - reverse()
#    - count()
#    - index()
#    - clear()
#    - copy()
#
#
# ----------------------------------------------------------------
# LIST COMPREHENSION
# ----------------------------------------------------------------
#
# Python'da liste üretmenin kısa ve güçlü bir yoludur.
#
# Genel kullanım şekli:
#
# newlist = [expression for item in iterable if condition]
#
# Bu yapı sayesinde döngü ve koşul kullanarak hızlı bir şekilde
# yeni listeler oluşturulabilir.
#
#
# ----------------------------------------------------------------
# BU DOSYADA NELER VAR
# ----------------------------------------------------------------
#
# Bu dosyada yer alan örnekler:
#
# - Liste oluşturma
# - Liste elemanlarına erişim
# - Eleman ekleme ve silme işlemleri
# - Liste güncelleme
# - Liste dilimleme (slicing)
# - Döngüler ile liste kullanımı
# - List comprehension örnekleri
#
# ================================================================
#                         ÖRNEKLER
# ================================================================

# Liste tanımlama
sayilar = [10, 20, 30, 40, 50]

# Listeyi ekrana yazdırma
print("Liste:", sayilar)
print("Liste'nin türü",type(sayilar))

# Liste elemanlarına index numarasıyla erişebilirsiniz.
# İlk eleman
print("İlk eleman:", sayilar[0])

# Son eleman
print("Son eleman:", sayilar[-1])

sayilar = [1, 2, 3]

# append() -> Sona eleman ekler
sayilar.append(4)
print("Append sonrası:", sayilar)

# insert() -> Belirli indekse ekler
sayilar.insert(1, 99)
print("Insert sonrası:", sayilar)

sayilar = [10, 20, 30, 40]

# remove() -> Değer ile siler
sayilar.remove(20)

# pop() -> İndeks ile siler
sayilar.pop(1)

print("Silme sonrası:", sayilar)

notlar = [50, 60, 70]

# 2. elemanı güncelleme
notlar[1] = 85

print("Güncellenmiş liste:", notlar)

liste = [5, 10, 15, 20]

print("Liste uzunluğu:", len(liste))

sayilar = [0, 1, 2, 3, 4, 5]

# 1. indexten 4. indexe kadar (4 hariç)
print("Dilim:", sayilar[1:4])

# Baştan 3. indexe kadar
print("İlk üç eleman:", sayilar[:3])

isimler = ["Ali", "Ayşe", "Mehmet"]

for isim in isimler:
    print("Öğrenci:", isim)

sayilar = [4, 2, 8, 1]

# Sıralama
sayilar.sort()
print("Sıralı:", sayilar)

# Ters çevirme
sayilar.reverse()
print("Ters:", sayilar)

matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrisin 2. satırı:", matris[1])
print("Matrisin 2. satır 3. sütun:", matris[1][2])


a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
print("append sonrası:", a)

c = [1, 2, 3]
c.extend(b)
print("extend sonrası:", c)

# Liste tanımlama
sayilar = [10, 20, 30, 40, 50]

# 2. indeksteki elemanı silme
del sayilar[2]

print("Eleman silindikten sonra:", sayilar)

liste = [1, 2, 3]

del liste
# print(liste)  # Hata verir çünkü liste artık yoktur.

notlar = [50, 60, 70, 60, 80, 60]

adet = notlar.count(60)

print("60 sayısı", adet, "kez geçmektedir.")


meyveler = ["elma", "armut", "muz", "kiraz"]

konum = meyveler.index("muz")

print("Muzun indeksi:", konum)

veriler = [100, 200, 300]

veriler.clear()

print("Liste içeriği:", veriler)


# Copy metodu kopyalar
liste1 = [1, 2, 3]
liste2 = liste1.copy()

liste2.append(4)

print("Orijinal liste:", liste1)
print("Kopya liste:", liste2)

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)


# Öğrenci not listesi
notlar = [70, 85, 90, 70, 60]

# count()
print("70 sayısı", notlar.count(70), "kez var.")

# index()
print("90 sayısının indeksi:", notlar.index(90))

# copy()
yedek = notlar.copy()

# append()
notlar.append(100)

# del
del notlar[0]

print("Güncel liste:", notlar)

# clear()
yedek.clear()

print("Yedek liste:", yedek)

# While döngüsü ile listenin elemanlarını tersten yazdırma
numbers = [1, 2, 3, 4, 5]

i = len(numbers) - 1
while i >= 0:
    print(numbers[i])
    i -= 1
    
# List comprehension ile sayıları iki katına çıkarma
numbers = [1, 2, 3, 4, 5]

double_list = [x * 2 for x in numbers]

print(double_list)

# List comprehension ile çift sayıları seçme
numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

# Liste elemanlarının uzunluklarını bulma
words = ["python", "java", "csharp", "go"]

lengths = [len(word) for word in words]

print(lengths)

# Belirli bir harf ile başlayan kelimeleri seçme
words = ["apple", "banana", "avocado", "cherry", "apricot"]

newlist = [x for x in words if x.startswith("a")]

print(newlist)

# Liste elemanlarını büyük harfe çevirme
cities = ["ankara", "istanbul", "izmir"]

newlist = [city.upper() for city in cities]

print(newlist)

# Sayıların karelerini alma
numbers = [1,2,3,4,5]

squares = [x**2 for x in numbers]

print(squares)

# Eğer sayı tek ise 0 yaz, çift ise sayı yaz
numbers = [1,2,3,4,5,6]

newlist = [x if x % 2 == 0 else 0 for x in numbers]

print(newlist)

# Listeyi dolaşarak 50'den büyük sayıları yazdırma
numbers = [23, 65, 12, 90, 34, 77]

for n in numbers:
    if n > 50:
        print(n)

# Liste elemanlarını indexleri ile birlikte yazdırma
names = ["Ali", "Ayşe", "Mehmet", "Zeynep"]

for i in range(len(names)):
    print(i, names[i])

# Liste içindeki sayıları stringe çevirme
numbers = [10, 20, 30, 40]

newlist = [str(x) for x in numbers]

print(newlist)