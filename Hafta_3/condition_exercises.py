vize_sonuc = float(input("Vize sonucunu giriniz"))
final_sonuc = float(input("Final sınavını giriniz. "))
proje_sonucu = float(input("Proje final notunuzu giriniz. "))

nihai_not = (0.40*vize_sonuc) + (0.30*final_sonuc) + (0.30*proje_sonucu)

if (nihai_not >=  0) and (nihai_not <= 20):
    print(f"Notunuz FF, not ortalamaniz {nihai_not:.2f} ")

elif (nihai_not > 21) and (nihai_not <= 49):
    print(f"Notunuz FD, not ortalamaniz {nihai_not:.2f} ")

elif(nihai_not > 50) and (nihai_not <=55 ):
    print(f"Notunuz DD, not ortalamaniz {nihai_not:.2f} ")

elif(nihai_not > 55) and (nihai_not <=60 ):
    print(f"Notunuz DC, not ortalamaniz {nihai_not:.2f} ")

elif(nihai_not > 60) and (nihai_not <=65 ):
    print(f"Notunuz CC, not ortalamaniz {nihai_not:.2f} ")

elif(nihai_not >= 70) and (nihai_not <=75 ):
    print(f"Notunuz BB, not ortalamaniz {nihai_not:.2f} ")

elif(nihai_not > 75) and (nihai_not <=85 ):
    print(f"Notunuz BA, not ortalamaniz {nihai_not:.2f} ")

elif(nihai_not > 85) and (nihai_not <=100 ):
    print(f"Notunuz AA, not ortalamaniz {nihai_not:.2f} ")

else:
    print("Geçersiz giriş yaptınız")
