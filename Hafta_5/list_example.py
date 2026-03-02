# PYTHON PROGRAMLAMA DİLİNDE LİSTELER (LISTS)

# Liste (list), Python dilinde birden fazla veriyi
# tek bir değişken altında saklamaya olanak sağlayan,
# sıralı (ordered) ve değiştirilebilir (mutable) bir veri yapısıdır.

# Listeler:
# - Köşeli parantez [] ile tanımlanır.
# - Farklı veri tiplerini aynı yapı içerisinde barındırabilir.
# - Elemanlarına indeks (index) numarası ile erişilir.
# - 0'dan başlayan indeksleme sistemine sahiptir.

# Liste veri yapısının temel özellikleri:
# - Ordered (Sıralı): Elemanlar belirli bir sıraya sahiptir.
# - Mutable (Değiştirilebilir): Elemanlar sonradan değiştirilebilir.
# - Dynamic (Dinamik): Eleman ekleme ve silme işlemleri mümkündür.

# Liste işlemlerinin temel kategorileri:
# - Eleman ekleme (append, insert, extend)
# - Eleman silme (remove, pop, del)
# - Eleman güncelleme
# - Liste uzunluğu öğrenme (len)
# - Liste dilimleme (slicing)
# - Liste üzerinde döngü ile gezinme
# - Liste metotları (sort, reverse, count, index)
# clear, copy, push, list()
# loop lists
# List Comprehension
# iterable


################ ÖRNEKLER #####################


# Liste tanımlama
sayilar = [10, 20, 30, 40, 50]


# Listeyi ekrana yazdırma
print("Liste:", sayilar)
print("Liste'nin türü",type(sayilar))

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