# 🥗 CalorieSnap

**CalorieSnap** adalah aplikasi web cerdas yang dibangun dengan Streamlit untuk menghitung kalori dan makronutrien dari makanan. Aplikasi ini memanfaatkan kekuatan AI generatif (Google Gemini) untuk menganalisis makanan baik dari **foto** maupun **deskripsi teks**.

## 🚀 Fitur Utama

* **📸 Analisis Foto:** Unggah foto atau gunakan kamera Anda untuk mengidentifikasi makanan dan mendapatkan estimasi nutrisi secara instan.
* **✍️ Analisis Teks:** Cukup ketik deskripsi makanan Anda (misalnya: "sepiring nasi goreng, telur mata sapi, dan kerupuk") untuk mendapatkan rincian nutrisi.
* **📊 Rincian Nutrisi:** Dapatkan estimasi total **Kalori (kkal)**, **Protein (g)**, **Karbohidrat (g)**, dan **Lemak (g)**.
* **🧩 Rincian Komponen:** Lihat perincian setiap komponen yang terdeteksi dalam makanan Anda (misalnya: "Nasi Putih - 1 Piring").
* **🧾 Riwayat Analisis:** Semua hasil analisis Anda secara otomatis disimpan di tab "Riwayat" untuk ditinjau kembali.

## 🛠️ Teknologi yang Digunakan

* **Framework:** Streamlit
* **Bahasa:** Python
* **AI & Model:** Google Gemini API (`gemini-2.5-flash-preview-09-2025`)

## ⚙️ Instalasi & Pengaturan

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

**1. Clone Repositori**
```bash
git clone https://github.com/Olaf29/caloriesnap-app.git
cd caloriesnap-app
```

**2. Buat dan Aktifkan Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instal Dependensi**
```bash
pip install -r requirements.txt
```

**4. Atur Kunci API (Secrets)**

Buat folder .streamlit di direktori root proyek.
Di dalam folder .streamlit, buat file bernama secrets.toml.
Tambahkan kunci API Anda ke file tersebut:
```bash
# .streamlit/secrets.toml
GEMINI_API_KEY = "MASUKKAN_KUNCI_API_ANDA_DI_SINI"
```

## ▶️ Cara Menjalankan Aplikasi
Setelah instalasi selesai, jalankan aplikasi menggunakan perintah Streamlit:
```bash
streamlit run app.py
```
Buka browser Anda dan navigasikan ke http://localhost:8501 untuk melihat aplikasi beraksi.

## 📁 Struktur Proyek
```text
CalorieSnap/
├── .streamlit/
│   └── secrets.toml     # Menyimpan API key (rahasia)
├── images/
│   ├── ckal2.png        # Ikon aplikasi
│   └── shidqi.png       # Avatar pengembang
├── venv/                # Virtual environment (diabaikan .gitignore)
├── .gitignore           # File yang diabaikan oleh Git
├── app.py               # File utama aplikasi Streamlit (UI dan navigasi)
├── connect_api.py       # Logika koneksi dan konfigurasi model Gemini
├── formatting.py        # Fungsi bantuan untuk menampilkan hasil dan UI
├── image_processing.py  # Logika untuk memproses input gambar
├── requirements.txt     # Daftar dependensi Python
├── style.css            # File CSS kustom untuk styling
└── teks_processing.py   # Logika untuk memproses input teks
```

## 🧑‍💻 Pengembang
Proyek ini dibuat dan dikelola oleh:
Shidqi Naufal
