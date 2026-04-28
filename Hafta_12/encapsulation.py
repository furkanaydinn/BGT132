
# Temel (Base) Sınıf
class Pokemon:
    def __init__(self, isim, can, seviye):
        self.__isim = isim        # private
        self.__can = can          # private
        self.__seviye = seviye    # private

    # GETTER
    def get_isim(self):
        return self.__isim

    def get_can(self):
        return self.__can

    def get_seviye(self):
        return self.__seviye

    # SETTER
    def set_can(self, yeni_can):
        if yeni_can < 0:
            self.__can = 0
        else:
            self.__can = yeni_can

    # Genel saldırı 
    def saldir(self):
        print(f"{self.__isim} saldırı yaptı!")


# Inheritance Ateş Pokemonu
class AtesPokemon(Pokemon):
    def __init__(self, isim, can, seviye, ates_gucu):
        super().__init__(isim, can, seviye)
        self.__ates_gucu = ates_gucu

    def ates_saldir(self):
        print(f"{self.get_isim()} ateş saldırısı yaptı! Güç: {self.__ates_gucu}")

    # OVERRIDE
    def saldir(self):
        print(f"{self.get_isim()} alev topu fırlattı")


# Inheritance Su Pokemonu
class SuPokemon(Pokemon):
    def __init__(self, isim, can, seviye, su_gucu):
        super().__init__(isim, can, seviye)
        self.__su_gucu = su_gucu

    def su_saldir(self):
        print(f"{self.get_isim()} su saldırısı yaptı! Güç: {self.__su_gucu}")

    # OVERRIDE
    def saldir(self):
        print(f"{self.get_isim()} su dalgası gönderdi")



# Pokemon oluştur
charizard = AtesPokemon("Charizard", 100, 5, 80)
blastoise = SuPokemon("Blastoise", 120, 5, 70)

# Encapsulation testi (direkt erişim olmaz)
# print(charizard.__can)  # HATA verir

# Getter ile erişim
print("Charizard Can:", charizard.get_can())

# Setter ile güncelleme
charizard.set_can(-50)  # negatif olamaz
print("Charizard Güncel Can:", charizard.get_can())

print("\n--- SAVAŞ BAŞLIYOR ---\n")

# Saldırılar
charizard.saldir()
charizard.ates_saldir()

blastoise.saldir()
blastoise.su_saldir()