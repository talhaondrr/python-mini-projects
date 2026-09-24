import random

number = random.randint(1, 100)

guess = int(input("1 ile 100 arasında bir sayı tahmin edin: "))

tahmin_sayisi = 1

while guess != number:

    tahmin_sayisi = tahmin_sayisi + 1

    if guess < number:
        print("Daha büyük bir sayı tahmin edin.")
    else:
        print("Daha küçük bir sayı tahmin edin.")

    guess = int(input("1 ile 100 arasında bir sayı tahmin edin: "))

print("Tebrikler, doğru bildiniz!")
print(f"{tahmin_sayisi} tahminde bildiniz.")