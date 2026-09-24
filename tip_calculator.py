Hesap = float(input("Hesap tutarını girin: "))
TipOranı = float(input("Tip oranını girin (örneğin: 15): "))
Tip = Hesap * (TipOranı / 100)
ToplamTutar = Hesap + Tip
print("Toplam tutar: ", ToplamTutar)
print("Tip: ", Tip)
