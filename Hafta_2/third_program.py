isim = input("İsminiz: ")
yas = int(input("Yaşınız: "))
boy = float(input("Boyunuz (Ör: 1.75): "))
kilo = float(input("Kilonuzu girin (örn: 70.5): "))

vucut_kitle_indeksi = kilo / (boy ** 2)


print("Merhaba", isim)
print("Yaşınız:", yas)
print("Boyunuz:", boy)

print("10 yıl sonraki yaşınız:", yas + 10)

print("Kilonuz:", kilo)
print("Vücut Kitle İndeksiniz:", vucut_kitle_indeksi)