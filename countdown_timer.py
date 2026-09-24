import time

sure = int(input("Kaç saniyelik geri sayım olsun? "))

while sure >= 0:
    dakika = sure // 60
    saniye = sure % 60

    print(f"{dakika:02d}:{saniye:02d}")

    time.sleep(1)
    sure -= 1

print("Süre doldu!")