import random

zarlar = int(input("Kaç zar atmak istiyorsunuz? "))

if zarlar == 0:
    print("Zar atılmadı.")

elif zarlar < 0:
    print("Geçersiz bir sayı girdiniz. Lütfen pozitif bir sayı girin.")

else:
    for i in range(zarlar):
        zar = random.randint(1, 6)
        print(f"{i + 1}. zar: {zar}")