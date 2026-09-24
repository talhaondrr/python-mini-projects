import random

kelimeler = ["python", "programlama", "bilgisayar", "yazılım", "algoritma"]


def kelimeyi_goster(kelime, tahminler):
    return " ".join(
        harf if harf in tahminler else "_"
        for harf in kelime
    )


def oyun():
    kelime = random.choice(kelimeler)
    tahminler = set()
    hak = 6

    while hak > 0:
        print("\nKelime:", kelimeyi_goster(kelime, tahminler))
        print(f"Kalan hak: {hak}")

        tahmin = input("Bir harf tahmin edin: ").strip().lower()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Lütfen sadece bir harf girin.")
            continue

        if tahmin in tahminler:
            print("Bu harfi zaten tahmin ettiniz.")
            continue

        tahminler.add(tahmin)

        if tahmin in kelime:
            print("Doğru tahmin!")
        else:
            print("Yanlış tahmin!")
            hak -= 1

        if all(harf in tahminler for harf in kelime):
            print("\nKelime:", kelimeyi_goster(kelime, tahminler))
            print(f"Tebrikler! Kelimeyi buldunuz: {kelime}")
            return

    print(f"\nKaybettiniz! Doğru kelime: {kelime}")


oyun()