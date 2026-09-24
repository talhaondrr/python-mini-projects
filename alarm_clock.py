from datetime import datetime
import time

alarm_saati = input("Alarm saatini girin (HH:MM formatında): ")

print(f"Alarm {alarm_saati} için kuruldu.")

while True:
    simdi = datetime.now()

    if simdi.strftime("%H:%M") == alarm_saati:
        print("Alarm çalıyor!")
        break

    time.sleep(1)