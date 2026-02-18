# Klavyeden sıcaklık değerini celcius olarak aliniz
sicaklik = float(input("Sicaklik değerini giriniz. "))
# Alınan değerleri fahreneit, kelvin değerlerine çeviriniz.
sicaklik_fahreneit = sicaklik*1.8 + 32
sicaklik_kelvin = sicaklik + 273.15
# Çok sıcak, orta sıcak, ideal sıcaklık, soğuk şeklinde koşullandırın
# sıcaklık 50 üzeri ise çok sıcak yazsın ve altına kelvin ve fahreinet cinsinden
# sıcaklıkları ekrana yazsın
if(sicaklik >= 50):
    print(f"Çok sıcak, sıcaklığın \nkelvin değeri {sicaklik_kelvin:.2f} fahreinet değeri {sicaklik_fahreneit:.2f} ")
elif(sicaklik < 50 and sicaklik >=30):
    print(f"orta, sıcaklığın \nkelvin değeri {sicaklik_kelvin:.2f} fahreinet değeri {sicaklik_fahreneit:.2f} ")
elif(sicaklik < 30 and sicaklik >=20):
    print(f"ideal sıcaklık, sıcaklığın \nkelvin değeri {sicaklik_kelvin:.2f} fahreinet değeri {sicaklik_fahreneit:.2f} ")
elif(sicaklik<20):
    print(f"SOĞUK, sıcaklığın \nkelvin değeri {sicaklik_kelvin:.2f} fahreinet değeri {sicaklik_fahreneit:.2f} ")


# sıcaklık 30-50 arasında ise orta sıcak yazsın
# altına kelvin ve fahreinet karşılıklarını yazsın

# sıcaklık 20-30 arasında ise ideal sıcaklık yazsın
# altına kelvin ve fahreinet karşılıklarını yazsın

# sıcaklık 20 den düşükse soğuk yazsın
# altına kelvin ve fahreinet karşılıklarını yazsın

# F=(C×1.8​)+32 p
# K=C+273.15