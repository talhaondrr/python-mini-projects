def duzelt(metin):
    return (
        metin.strip()
        .replace("İ", "i")
        .replace("I", "i")
        .replace("ı", "i")
        .replace("Ş", "s")
        .replace("ş", "s")
        .replace("Ç", "c")
        .replace("ç", "c")
        .replace("Ğ", "g")
        .replace("ğ", "g")
        .replace("Ö", "o")
        .replace("ö", "o")
        .replace("Ü", "u")
        .replace("ü", "u")
        .lower()
    )   


sorular = [
    {
        "soru": "Türkiye'nin başkenti neresidir?",
        "cevap": "Ankara"
    },
    {
        "soru": "2 + 2 kaçtır?",
        "cevap": "4"
    },
    {
        "soru": "Dünyanın uydusu nedir?",
        "cevap": "Ay"
    },
    {
        "soru": "Türkiye'nin en kalabalık şehri hangisidir?",
        "cevap": "İstanbul"
    }
]


skor = 0


for soru in sorular:
    print()
    print(soru["soru"])

    cevap = input("Cevabınızı girin: ")

    if duzelt(cevap) == duzelt(soru["cevap"]):
        print("Doğru!")
        skor += 1
    else:
        print(f"Yanlış! Doğru cevap: {soru['cevap']}")


print()
print(f"Toplam skorunuz: {skor}/{len(sorular)}")