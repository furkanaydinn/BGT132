
class Dikdortgen:
    en = 10 # sınıf değişkeni (özelliği) 
    boy = 5 # sınıf değişkeni (özelliği) 


birinciDortgen = Dikdortgen() # Nesne oluşturma (Sınıf üzerinden nesne oluşturulur)
ikinciDortgen = Dikdortgen()
ucuncuDortgen = Dikdortgen()

print(f"Birinci dikdortgen icin en bilgisi: {birinciDortgen.en}\nBirinci dikdortgen icin boy bilgisi: {birinciDortgen.boy} ")

# Nesne silmek istenirse aşağıdaki kod çalıştırılır
# Nesne silindikten sonra, erişim olmaz
# del birinciDortgen

# Constructor (Yapıcı metod) üzerinden örnek değişken oluşturma

class Araba:
    pass

a1 = Araba()
print(type(a1))



