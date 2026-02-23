try:
    vizeNotu = float(input("Vize notunu giriniz: "))
    finalNotu = float(input("Final notunu giriniz: "))
    projeNotu = float(input("Proje notunu giriniz: "))

    if not (0 <= vizeNotu <= 100 and 0 <= finalNotu <= 100 and 0 <= projeNotu <= 100):
        print("Notlar 0 ile 100 arasında olmalıdır.")
    else:
        ortalamaNotu = 0.40 * vizeNotu + 0.30 * finalNotu + 0.30 * projeNotu

        if ortalamaNotu <= 49:
            harf = "FF"
        elif ortalamaNotu <= 55:
            harf = "DD"
        elif ortalamaNotu <= 59:
            harf = "DC"
        elif ortalamaNotu <= 69:
            harf = "CC"
        elif ortalamaNotu <= 79:
            harf = "BB"
        elif ortalamaNotu <= 84:
            harf = "BA"
        else:
            harf = "AA"

        print(f"Not ortalamanız: {ortalamaNotu:.2f} | Harf notunuz: {harf}")

except ValueError:
    print("Lütfen geçerli bir sayısal değer giriniz.")

