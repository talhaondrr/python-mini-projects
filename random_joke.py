import requests
import time

from deep_translator import GoogleTranslator
from deep_translator.exceptions import TooManyRequests


url = "https://v2.jokeapi.dev/joke/Any?type=single"

response = requests.get(url)

if response.status_code == 200:

    veri = response.json()

    ingilizce_saka = veri["joke"]

    print("\nİngilizce:")
    print(ingilizce_saka)

    try:
        turkce_saka = GoogleTranslator(
            source="en",
            target="tr"
        ).translate(ingilizce_saka)

        print("\nTürkçe:")
        print(turkce_saka)

    except TooManyRequests:
        print("\nÇeviri servisi şu anda çok fazla istek alıyor.")
        print("Biraz bekleyip tekrar deneyin.")

else:
    print("Şaka alınırken bir hata oluştu.")