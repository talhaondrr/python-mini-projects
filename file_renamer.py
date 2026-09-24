import os

klasor = input("Klasör yolunu girin: ")
yeni_isim = input("Yeni dosya adı ne olsun? ")

dosyalar = os.listdir(klasor)

sayac = 1

for dosya in dosyalar:
    eski_dosya_yolu = os.path.join(klasor, dosya)

    # Klasörleri değil, sadece dosyaları değiştir
    if os.path.isfile(eski_dosya_yolu):

        # Dosyanın uzantısını al
        _, uzanti = os.path.splitext(dosya)

        # Yeni dosya adını oluştur
        yeni_dosya_adi = f"{yeni_isim}_{sayac}{uzanti}"

        yeni_dosya_yolu = os.path.join(
            klasor,
            yeni_dosya_adi
        )

        # Dosyanın adını değiştir
        os.rename(eski_dosya_yolu, yeni_dosya_yolu)

        print(f"{dosya} -> {yeni_dosya_adi}")

        sayac += 1

print("Tüm dosyaların isimleri değiştirildi.")