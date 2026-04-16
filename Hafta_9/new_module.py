from modules import (
    simdiki_tarih,
    tarih_bilesenleri,
    gun_adi,
    ay_adi,
    formatli_saat,
    formatli_tarih,
    iso_format,
    haftanin_gunu_index,
    tarih_karsilastir,
    tarih_olustur,
    bugun_tarih,
    gun_farki,
    tarih_to_string,
    string_to_tarih,
    yas_gun
)


import datetime

def main():
    print(" Şu anki tarih:", simdiki_tarih())
    print(" Tarih bileşenleri:", tarih_bilesenleri())

    print("\n Tarih oluşturma:")
    print(tarih_olustur(2025, 5, 17))
    print(tarih_olustur(2025, 5, 17, 14, 30))

    print("\n Gün ve Ay:")
    print("Gün:", gun_adi())
    print("Ay:", ay_adi())

    print("\n Formatlı çıktı:")
    print(formatli_tarih())
    print(formatli_saat())

    print("\n Haftanın günü index:", haftanin_gunu_index())
    print("Bugünün tarihi:", bugun_tarih())

    print("\n Tarih karşılaştırma:")
    t1 = datetime.datetime(2025, 1, 1)
    t2 = datetime.datetime(2024, 1, 1)
    print(tarih_karsilastir(t1, t2))

    print("\n Gün farkı:")
    print(gun_farki(
        datetime.datetime(2025, 1, 10),
        datetime.datetime(2025, 1, 1)
    ))

    print("\n ISO format:")
    print(iso_format(datetime.date(2025, 1, 1)))

    print("\n String dönüşümleri:")
    print(tarih_to_string())
    print(string_to_tarih("2025-04-03"))
   

    print("\n Yaş (gün):")
    print(yas_gun(datetime.datetime(2000, 1, 1)))


if __name__ == "__main__":
    main()