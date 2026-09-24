import requests

para_birimleri = {
    "TL": "TRY",
    "TRY": "TRY",
    "DOLAR": "USD",
    "USD": "USD",
    "EURO": "EUR",
    "EUR": "EUR",
    "STERLIN": "GBP",
    "GBP": "GBP"
}

kaynak = input("Hangi para biriminden? ").strip().upper()
hedef = input("Hangi para birimine? ").strip().upper()
miktar = float(input("Miktar: "))

kaynak = para_birimleri.get(kaynak, kaynak)
hedef = para_birimleri.get(hedef, hedef)

url = f"https://api.frankfurter.dev/v2/rate/{kaynak}/{hedef}"

response = requests.get(url, timeout=10)

if response.status_code == 200:
    veri = response.json()

    kur = veri["rate"]
    sonuc = miktar * kur

    print(f"\n1 {kaynak} = {kur:.4f} {hedef}")
    print(f"{miktar:.2f} {kaynak} = {sonuc:.2f} {hedef}")

else:
    print("Döviz bilgisi alınamadı.")
    print("Hata kodu:", response.status_code)
    print("Hata mesajı:", response.text)