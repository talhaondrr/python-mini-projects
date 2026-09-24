import random
import string


def sifre_olustur(uzunluk=12):

    if uzunluk < 4:
        raise ValueError("Şifre uzunluğu en az 4 karakter olmalıdır.")

    tum_karakterler = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    sifre = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    sifre += random.choices(
        tum_karakterler,
        k=uzunluk - 4
    )

    random.shuffle(sifre)

    return "".join(sifre)


uzunluk = int(input("Şifre uzunluğu kaç karakter olsun? "))

sifre = sifre_olustur(uzunluk)

print("Oluşturulan şifre:", sifre)