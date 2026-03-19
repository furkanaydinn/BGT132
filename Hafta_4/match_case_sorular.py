# Soru 1

operator = input("İşlem (+, -, *, /): ")
sayi1 = int(input("1. sayı: "))
sayi2 = int(input("2. sayı: "))

match operator:
    case "+":
        print("Sonuç:", sayi1 + sayi2)
    case "-":
        print("Sonuç:", sayi1 - sayi2)
    case "*":
        print("Sonuç:", sayi1 * sayi2)
    case "/":
        if sayi2 == 0:
            print("Sıfıra bölme hatası")
        else:
            print("Sonuç:", sayi1 / sayi2)
    case _:
        print("Geçersiz operatör!")

# Soru 2

veri = 10

match type(veri).__name__:
    case "int":
        print("Bu bir tam sayıdır")
    case "float":
        print("Bu bir ondalıklı sayıdır")
    case "str":
        print("Bu bir metin ifadesidir")
    case _:
        print("Bilinmeyen veri türü")

# Soru 3

while True:
    print("1 - Hoşgeldiniz mesajı")
    print("2 - İki sayının toplamını hesapla")
    print("0 - Çıkış")

    secim = int(input("Seçiminiz: "))

    match secim:
        case 1:
            print("Hoşgeldiniz!")
        case 2:
            s1 = int(input("1. sayı: "))
            s2 = int(input("2. sayı: "))
            print("Toplam:", s1 + s2)
        case 0:
            print("Program sonlandırıldı")
            break
        case _:
            print("Geçersiz seçim!")

# Soru 4

while True:
    print("1 - Hoşgeldiniz mesajı")
    print("2 - İki sayının toplamını hesapla")
    print("0 - Çıkış")

    secim = int(input("Seçiminiz: "))

    match secim:
        case 1:
            print("Hoşgeldiniz!")
        case 2:
            s1 = int(input("1. sayı: "))
            s2 = int(input("2. sayı: "))
            print("Toplam:", s1 + s2)
        case 0:
            print("Program sonlandırıldı")
            break
        case _:
            print("Geçersiz seçim!")

