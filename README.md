# 🐍 Python Mini Projects

Python becerilerimi geliştirmek amacıyla hazırladığım **20 farklı mini projeden** oluşan çalışma reposudur.

Bu projeler boyunca Python temellerinden başlayarak; fonksiyonlar, OOP, dosya işlemleri, API kullanımı, JSON, hata yönetimi ve harici kütüphaneler gibi konularda pratik yaptım.

---

## 📌 Projeler

| # | Proje | Çalışılan Konular |
|---|---|---|
| 1 | Calculator | `input`, `if/elif/else`, matematiksel işlemler |
| 2 | Tip Calculator | `float`, yüzde hesaplama, f-string |
| 3 | BMI Calculator | Koşullar, hesaplama, formatlama |
| 4 | Dice Roller | `random`, `for` döngüsü |
| 5 | Number Guessing Game | `while`, random, sayaç |
| 6 | Rock Paper Scissors | Koşullar, random, skor sistemi |
| 7 | Email Slicer | String işlemleri, `split()` |
| 8 | Mad Libs Generator | Input, f-string, string işlemleri |
| 9 | Quiz App | List, dictionary, for, skor sistemi |
| 10 | Password Generator | Random, string, fonksiyonlar |
| 11 | Hangman | While, list/set, fonksiyonlar |
| 12 | To-Do List | OOP, class, JSON, dosya işlemleri |
| 13 | Countdown Timer | Time, while, zaman hesaplama |
| 14 | Digital Clock | Datetime, `strftime()` |
| 15 | Alarm Clock | Datetime, while, zaman karşılaştırma |
| 16 | File Renamer | OS, dosya yolları, toplu isim değiştirme |
| 17 | Random Joke Generator | API, requests, JSON |
| 18 | Weather App | API, requests, Open-Meteo |
| 19 | Currency Converter | Döviz API, requests, hata yönetimi |
| 20 | YouTube Downloader | yt-dlp, FFmpeg, sanal ortam |

---

## 🛠️ Kullanılan Teknolojiler

- Python
- Requests
- JSON
- REST API
- yt-dlp
- FFmpeg
- Open-Meteo API
- Frankfurter API
- Git
- GitHub
- Virtual Environment

---

## 📂 Proje Yapısı

```text
python-mini-projects/
│
├── calculator.py
├── tip_calculator.py
├── bmi_calculator.py
├── dice_roller.py
├── number_guessing.py
├── rock_paper_scissors.py
├── email_slicer.py
├── mad_libs.py
├── quiz_app.py
├── password_generator.py
├── hangman.py
├── todo_list.py
├── countdown_timer.py
├── digital_clock.py
├── alarm_clock.py
├── file_renamer.py
├── random_joke.py
├── weather_app.py
├── currency_converter.py
├── youtube_downloader.py
└── README.md
```

---

## 🚀 Kurulum

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/talhaondrr/python-mini-projects.git
```

Proje klasörüne girin:

```bash
cd python-mini-projects
```

Sanal ortam oluşturmak isterseniz:

```bash
python -m venv .venv
```

Windows üzerinde sanal ortamı aktifleştirmek için:

```powershell
.venv\Scripts\activate
```

Gerekli paketleri yükleyin:

```bash
pip install requests yt-dlp
```

Ardından istediğiniz projeyi çalıştırabilirsiniz:

```bash
python calculator.py
```

Örneğin:

```bash
python weather_app.py
```

---

## 🎬 YouTube Downloader

YouTube Downloader projesinde `yt-dlp` kullanılmaktadır.

Kurulum:

```bash
pip install yt-dlp
```

Bazı video formatlarında video ve ses ayrı indirildiği için bunların birleştirilmesi amacıyla **FFmpeg** gereklidir.

Windows:

```powershell
winget install -e --id Gyan.FFmpeg
```

Kurulumu kontrol etmek için:

```powershell
ffmpeg -version
```

> YouTube Downloader yalnızca indirme hakkınız veya izniniz bulunan içeriklerde kullanılmalıdır.

---

## 🌦 Weather App

Weather App projesinde API key gerektirmeyen **Open-Meteo API** kullanılmıştır.

Uygulama:

1. Kullanıcıdan şehir adını alır.
2. Şehrin koordinatlarını bulur.
3. Güncel hava durumu verilerini API üzerinden çeker.
4. Sıcaklık, hissedilen sıcaklık, nem ve rüzgar bilgilerini gösterir.

---

## 💱 Currency Converter

Döviz çevirici projesinde döviz kurlarını almak için **Frankfurter API** kullanılmıştır.

Örnek:

```text
Hangi para biriminden? EUR
Hangi para birimine? TRY
Miktar: 100
```

Uygulama güncel kur bilgisini API üzerinden alarak dönüşümü gerçekleştirir.

---

## 📚 Çalıştığım Python Konuları

Bu projeler boyunca aşağıdaki konularda pratik yaptım:

- Değişkenler
- Veri tipleri
- Kullanıcı girdileri
- `if / elif / else`
- `for` döngüsü
- `while` döngüsü
- Listeler
- Dictionary
- Set
- Fonksiyonlar
- `return`
- OOP
- Class ve Object yapısı
- `self`
- Exception Handling
- `try / except`
- Dosya işlemleri
- JSON
- REST API
- HTTP Requests
- String işlemleri
- Random modülü
- Datetime ve Time
- OS modülü
- Harici Python paketleri
- Virtual Environment
- Git ve GitHub

---

## 🎯 Sonraki Hedef

Bu mini projeler ile Python temellerini pekiştirdikten sonra daha büyük ve gerçek dünya projelerine geçmeyi hedefliyorum.

Özellikle ilgilendiğim alanlar:

- ERP Sistemleri
- Python Backend Development
- SQLite
- PostgreSQL
- REST API
- Veritabanı Tasarımı
- Stok ve Sipariş Yönetimi
- CRM Sistemleri
- Odoo ERP Geliştirme

Bir sonraki hedefim Python ve veritabanı kullanarak kendi **Mini ERP Sistemimi** geliştirmek.

---

## 👨‍💻 Developer

**Talha Önder**

GitHub: [@talhaondrr](https://github.com/talhaondrr)

---

⭐ Bu repo Python öğrenme sürecimde geliştirdiğim mini projeleri ve ilerlememi belgelemek amacıyla oluşturulmuştur.
