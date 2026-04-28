import math

class Ucgen:
    
    def __init__(self,kenar):
        self.kenar = kenar

    
    def hesapla(self):

      while True:
          print("\n----- Alan ve Cevre Hesabı yapılacak üçgeni seçiniz: -------\n")
          print("1-Dik ucgen\n")
          print("2-Eskenar ucgen\n")
          print("çıkmak için q ya basiniz\n")

          secim = input("Seçiminiz: ")

          if secim == "1":
              yukseklik = float(input("Dik ucgenin yukseklği: "))
              hipotenus = math.sqrt(self.kenar**2 + yukseklik**2)
              alan = self.kenar * yukseklik / 2.0
              cevre = self.kenar + yukseklik + hipotenus
              print("Dik ucgen alani {}, cevresi {}".format(alan,cevre))

          elif secim == "2":
              alan = (math.pow(self.kenar,2)) * math.sqrt(3) / 4.0
              cevre = self.kenar * 3
              print("Eskenar ücgen alani {}, cevresi {} ".format(alan,cevre))
              break
          
          elif secim.lower() == "q":
              break
          
          else:
              print("Hatali secim")
              
          

birinciUcgen = Ucgen(6)
birinciUcgen.hesapla()

ikinciUcgen = Ucgen(8)
ikinciUcgen.hesapla()
            
            