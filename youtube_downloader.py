import yt_dlp

url = input("YouTube video linkini girin: ")

ayarlar = {
    "noplaylist": True,
    "outtmpl": "%(title)s.%(ext)s"
}

try:
    with yt_dlp.YoutubeDL(ayarlar) as ydl:
        ydl.download([url])

    print("Video başarıyla indirildi!")

except Exception as hata:
    print("Bir hata oluştu:")
    print(hata)