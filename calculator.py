İlksayi = int(input("İlk sayıyı girin: "))
IkinciSayi = int(input("İkinci sayıyı girin: "))
islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /): ")
if islem == "+":
    sonuc = İlksayi + IkinciSayi
    print("Sonuç: ", sonuc)
elif islem == "-":
    sonuc = İlksayi - IkinciSayi
    print("Sonuç: ", sonuc)
elif islem == "*":
    sonuc = İlksayi * IkinciSayi
    print("Sonuç: ", sonuc)
elif islem == "/":
    if IkinciSayi != 0:
        sonuc = İlksayi / IkinciSayi
        print("Sonuç: ", sonuc)
    else:
        print("Hata: Bir sayıyı sıfıra bölemezsiniz.")
        