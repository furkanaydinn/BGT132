''''
Aritmetik operatörler ile 
temel matematik işlemlerini gerçekleştirebilirsiniz.

Toplama = +
Çıkarma = -
Çarpma = *
Bölme = /
Tam Bölme (ondalıksız) = //
Mod alma = %
Üs alma = **

'''

print(10+7)
print(5-9)
print(9*12)
print(18/3)
print(18//3)
print(150%40)
print(3**4)

'''
Atama operatörleri

x = 10
x+= 10  x = x+10
x-=10   x = x-10
x&= 10  x = x & 10

Daha fazla örnek için
aşağıdaki bağlantıda bulunan tabloyu inceleyiniz
https://www.w3schools.com/python/python_operators_assign.asp

'''

# Aşağıdaki değişkenin durumunu gözlemleyin
x = 5
x+=10
x*=5
x**=3
x/=8
print(x)
print(f"x in değeri {x:.2f}")


'''
Karşılaştırma operatörleri:
eşittir == 
büyük eşit >= 
kücük eşit <=  
eşit değil != 
büyüktür >
küçütür <

True veya False olacak biçimde, mantıksal sonuç verir 

'''

print(16!=8)
print(9>20)
print(8==7)
print(7<15)
print(-20<=0)

'''
Mantıksal operatörler
and, or, not
True veya False biçiminde sonuç verir.

and = ve
or = veya
not = değil

'''

print(8>3 and 7<20)

sayi_1 = 20
sayi_2 = 50

print(sayi_1 > sayi_2 or sayi_2<40)
print(not(sayi_2>sayi_1 and sayi_1<80))

'''
Identity Operatörler
kimlik, aitlik operatörleri
True False biçiminde yanıt döner
Hem bellek adresinin hem de değerin aynı olmasına bakılır.

is operatörü iki değişkenin aynı nesneyi (aynı bellek adresini) gösterip göstermediğini kontrol eder.
is not, iki değişkenin aynı nesne olmadığını kontrol eder.

'''

x = ["car", "truck"]
y = ["car", "truck"]
z = x

print(x is z) # x z dir
print(x is y) 
print(x == y)
print(y is not z) # y z değildir.

'''

Üyelik operatörleri, 
bir dizinin bir nesne içinde 
bulunup bulunmadığını test etmek için kullanılır.

in 
not in

True veya False biçiminde yanıt döner.

'''

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("coffee" not in fruits)

'''

Bitsel(bitwise) operatörler
& = AND
| = OR
^ = XOR
~ = NOT
<< = sola bit kaydırma (sıfır ile doldurma)
>> = sağa bit kaydırma

Detaylı bilgi için aşağıdaki bağlantıyı inceleyin
https://www.w3schools.com/python/python_operators_bitwise.asp 

'''

print(8 & 2)
print(7 | 2)
print(4^3)
print(7>>2) # 7 sayısını 2 lik sayıya çevir sonra 2 bit sağa kaydır.
print(7<<2) # 7 sayısını 2 lik sayıya çevie sonra 2 bit sola kaydır.

# İşlem önceliği matematikte olduğu gibi yapılır
# 1- Parantez alma
# 2- Üs alma
# 3- Çarpma ve bölme
# 4- Toplama ve çıkarma









