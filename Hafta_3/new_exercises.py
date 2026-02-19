'''

Bir sinema salonunda:

* Tam bilet: 150 TL
* Öğrenci bileti: 100 TL
* 12 yaş altı: %50 indirim

Kullanıcıdan:

* Yaş
* Öğrenci olup olmadığı (E/H)

bilgilerini alarak ödenecek bileti hesaplayan programı yazınız.

📌 Not: Eğer hem öğrenci hem 12 yaş altı ise sadece en büyük indirim uygulanacaktır.

'''

yas = int(input("Kullanicinin yasini giriniz: "))
ogrenciMi = bool(input("Kullanici öğrenci mi: "))

tamBiletFiyati = 150
ogrenciBiletFiyati = 100

if yas < 12:
    fiyat = tamBiletFiyati - tamBiletFiyati // 2
    print("Bilet fiyati", fiyat)

else:
    if ogrenciMi:
        print("Bilet fiyatniz", ogrenciBiletFiyati)

        if yas < 12:
            fiyat = tamBiletFiyati - tamBiletFiyati*3/5
    else:
        print("Bilet fiyatiniz", tamBiletFiyati)
