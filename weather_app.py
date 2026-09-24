import requests

sehir = input("Şehir adı girin: ")

# 1. Şehrin enlem ve boylamını bul
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={sehir}&count=1&language=tr"

geo_response = requests.get(geo_url)
geo_veri = geo_response.json()

if "results" not in geo_veri:
    print("Şehir bulunamadı.")

else:
    sonuc = geo_veri["results"][0]

    enlem = sonuc["latitude"]
    boylam = sonuc["longitude"]

    # 2. Hava durumunu al
    hava_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={enlem}"
        f"&longitude={boylam}"
        f"&current=temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m"
    )

    hava_response = requests.get(hava_url)
    hava_veri = hava_response.json()

    mevcut = hava_veri["current"]

    print("\nŞehir:", sonuc["name"])
    print("Sıcaklık:", mevcut["temperature_2m"], "°C")
    print("Hissedilen:", mevcut["apparent_temperature"], "°C")
    print("Nem:", mevcut["relative_humidity_2m"], "%")
    print("Rüzgar:", mevcut["wind_speed_10m"], "km/h")