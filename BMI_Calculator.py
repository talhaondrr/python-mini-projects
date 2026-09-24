boy = float(input("Boyunuzu metre cinsinden girin (örneğin: 1.75): "))
kilo = float(input("Kilonuzu kilogram cinsinden girin (örneğin: 70): "))

BMI = kilo / (boy ** 2)

print(f"BMI: {BMI:.2f}")

if BMI < 18.5:
    print("Zayıf")
elif BMI < 25:
    print("Normal kilolu")
elif BMI < 30:
    print("Fazla kilolu")
else:
    print("Obez")