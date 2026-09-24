import random

choices = ["taş", "kağıt", "makas"]

oyuncu_skor = 0
bilgisayar_skor = 0

while oyuncu_skor < 3 and bilgisayar_skor < 3:

    computer = random.choice(choices)

    player = input("Taş, kağıt veya makas seçin: ").lower()

    if player not in choices:
        print("Geçersiz seçim!")
        continue

    print("Bilgisayarın seçimi:", computer)

    if player == computer:
        print("Berabere!")

    elif player == "taş":
        if computer == "kağıt":
            print("Bu turu kaybettiniz!")
            bilgisayar_skor += 1
        else:
            print("Bu turu kazandınız!")
            oyuncu_skor += 1

    elif player == "kağıt":
        if computer == "makas":
            print("Bu turu kaybettiniz!")
            bilgisayar_skor += 1
        else:
            print("Bu turu kazandınız!")
            oyuncu_skor += 1

    elif player == "makas":
        if computer == "taş":
            print("Bu turu kaybettiniz!")
            bilgisayar_skor += 1
        else:
            print("Bu turu kazandınız!")
            oyuncu_skor += 1

    print(f"Skor: Sen {oyuncu_skor} - {bilgisayar_skor} Bilgisayar")
    print("--------------------")

if oyuncu_skor == 3:
    print("Tebrikler! Oyunu kazandınız!")
else:
    print("Bilgisayar oyunu kazandı!")