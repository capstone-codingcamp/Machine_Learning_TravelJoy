Berikut adalah README.md yang telah diperbarui dan siap untuk langsung disalin:

```markdown
# TravelJoy: Sistem Rekomendasi Wisata

## 📝 Deskripsi Singkat
TravelJoy adalah sebuah proyek yang bertujuan untuk membangun sistem rekomendasi tempat wisata di Indonesia berdasarkan kategori yang diminati pengguna. Proyek ini mencakup seluruh alur kerja machine learning, mulai dari pembersihan dataset mentah, pembuatan model rekomendasi menggunakan content-based filtering, hingga mengubah model menjadi sebuah API yang dapat diakses secara publik melalui deployment di Hugging Face Spaces menggunakan Docker.

## 📜 Daftar Isi
- [Alur Proyek](#-alur-proyek)
- [Struktur Folder](#%F0%9F%93%81-struktur-folder)
- [Cara Mereplikasi Proyek](#%F0%9F%9A%80-cara-mereplikasi-proyek)
- [Deployment ke Hugging Face Spaces](#%F0%9F%9A%80-deployment-ke-hugging-face-spaces)
- [Cara Menggunakan API](#%F0%9F%9A%80-cara-menggunakan-api)
- [Kontak](#%F0%9F%93%9A-kontak)

## 🌊 Alur Proyek
Proyek ini dibagi menjadi beberapa tahapan utama yang saling berhubungan:

### Pembersihan Dataset (Dataset_cleaning.ipynb)
Tahap awal dimulai dengan proses pembersihan dan persiapan data dari beberapa file CSV yang berisi informasi pariwisata. Proses ini mencakup penggabungan data, penanganan nilai yang hilang (missing values), dan penghapusan data duplikat untuk menghasilkan satu dataset komprehensif yang siap digunakan untuk pemodelan. Dataset yang telah bersih disimpan sebagai `data_wisata.csv`.

### Pembuatan Model Rekomendasi (recommedation_travelling_system.ipynb)
Pada tahap ini, dataset yang telah bersih digunakan untuk membangun model sistem rekomendasi. Model ini menggunakan pendekatan content-based filtering dengan memanfaatkan deskripsi tempat wisata. Deskripsi teks diubah menjadi representasi vektor (embedding) menggunakan model LSTM (Long Short-Term Memory). Cosine similarity dihitung dari vektor embedding untuk mengukur kemiripan antar tempat wisata.

Hasil dari notebook ini adalah:
- `text_embedding_model.keras`: Model embedding yang telah dilatih.
- `cosine_similarity.pkl`: Matriks kesamaan kosinus antar tempat wisata.

### Inferensi & Pembuatan API (app.py)
Model yang telah dilatih kemudian diubah menjadi sebuah API menggunakan FastAPI. `app.py` berisi logika untuk memuat model (`.keras`) dan matriks kesamaan (`.pkl`), serta menyediakan endpoint yang dapat menerima input kategori wisata dari pengguna dan memberikan rekomendasi 10 tempat teratas.

### Pengujian API (Menggunakan Postman)
Sebelum deployment, API diuji secara lokal untuk memastikan fungsionalitasnya berjalan dengan baik. Pengujian dilakukan dengan mengirimkan permintaan POST ke endpoint API menggunakan Postman. Respons yang berhasil ditandai dengan status 200 OK dan berisi data rekomendasi dalam format JSON.

### Deployment (Hugging Face Spaces dengan Docker)
Setelah pengujian API berhasil, proyek dideploy ke Hugging Face Spaces. Metode deployment yang dipilih adalah menggunakan Docker, yang memungkinkan aplikasi berjalan di lingkungan yang terisolasi dan konsisten. Sebuah Dockerfile dibuat untuk mendefinisikan image aplikasi yang berisi semua dependensi dan konfigurasi yang diperlukan.

## 📁 Struktur Folder
Berikut adalah struktur folder yang direkomendasikan untuk proyek ini:

```

TravelJoy/
│
├── Inference/
│   ├── assets/
│   │   ├── data\_wisata.csv
│   │   ├── text\_embedding\_model.keras
│   │   ├── cosine\_similarity.pkl
│   │   └── embedding\_matrix.npy
│   ├── app.py
│   ├── Dockerfile
│   ├── README.md         # Penjelasan khusus untuk folder Inference
│   └── requirements.txt
│
├── Dataset\_cleaning.ipynb
├── recommedation\_travelling\_system.ipynb
└── README.md             # README utama ini

````

## 🚀 Cara Mereplikasi Proyek
Untuk menjalankan proyek ini di lingkungan lokal Anda, ikuti langkah-langkah berikut:

### Prasyarat
- Python 3.8+
- Jupyter Notebook atau JupyterLab
- Postman (untuk pengujian API)

### Langkah-langkah

1. **Clone Repositori**
   ```bash
   git clone https://github.com/username/TravelJoy.git
   cd TravelJoy
````

2. **Instal Dependensi**
   Pastikan Anda memiliki semua library yang dibutuhkan dengan menginstalnya dari file `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Notebook**
   Buka dan jalankan `Dataset_cleaning.ipynb` terlebih dahulu untuk menghasilkan file `data_wisata.csv`. Selanjutnya, jalankan `recommedation_travelling_system.ipynb` untuk melatih model dan menghasilkan file `text_embedding_model.keras` dan `cosine_similarity.pkl`. Pastikan semua file hasil disimpan di dalam folder `assets/`.

4. **Jalankan API Secara Lokal**
   Gunakan Uvicorn untuk menjalankan server FastAPI dari file `app.py`.

   ```bash
   uvicorn app:app --reload
   ```

   API akan berjalan di `http://127.0.0.1:8000`.

5. **Uji API dengan Postman**

   * Buka Postman.
   * Buat permintaan POST ke URL: `http://127.0.0.1:8000/get_recommendations/`
   * Pilih tab `Body`, lalu pilih format `raw` dan `JSON`.
   * Masukkan request body seperti contoh di bawah:

     ```json
     {
       "category": "Cagar Alam"
     }
     ```
   * Kirim permintaan. Anda seharusnya menerima respons dengan status 200 OK beserta daftar rekomendasi tempat wisata.

## 🚀 Deployment ke Hugging Face Spaces

Deployment dilakukan menggunakan Docker untuk memastikan portabilitas dan konsistensi lingkungan.

### Prasyarat

* Akun Hugging Face
* Git LFS (Large File Storage) untuk menyimpan file model yang besar.
* Docker terinstal di komputer Anda.

### Langkah-langkah

1. **Buat Space Baru di Hugging Face**

   * Masuk ke akun Hugging Face Anda dan buat New Space.
   * Beri nama Space Anda (misalnya, TravelJoy).
   * Pilih Docker sebagai Space SDK.

2. **Clone Repositori Space**
   Hugging Face akan menyediakan perintah `git clone` untuk repositori Space Anda.

   ```bash
   git lfs install
   git clone https://huggingface.co/spaces/username/TravelJoy
   cd TravelJoy
   ```

3. **Siapkan File Proyek**
   Salin semua file proyek (`app.py`, `requirements.txt`, `Dockerfile`, dan folder `assets`) ke dalam folder repositori yang baru saja Anda clone. Pastikan file model `.keras` dilacak oleh Git LFS:

   ```bash
   git lfs track "assets/text_embedding_model.keras"
   ```

4. **Buat Dockerfile**
   Buat file bernama `Dockerfile` (tanpa ekstensi) di direktori root dengan isi berikut:

   ```Dockerfile
   # Gunakan base image resmi Python
   FROM python:3.9-slim

   # Set direktori kerja
   WORKDIR /app

   # Salin file requirements dan instal dependensi
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Salin semua file proyek ke dalam container
   COPY . .

   # Jalankan aplikasi menggunakan Uvicorn
   CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
   ```

5. **Push ke Hugging Face**
   Commit dan push semua file ke repositori Hugging Face.

   ```bash
   git add .
   git commit -m "Initial commit: deploy recommendation API"
   git push
   ```

   Hugging Face akan secara otomatis membangun image Docker dan menjalankan aplikasi Anda.

## ⚙️ Cara Menggunakan API

Setelah berhasil dideploy, API dapat diakses melalui URL publik yang disediakan oleh Hugging Face Spaces.

### Endpoint:

`/get_recommendations/`

### Method:

`POST`

### Request Body (JSON):

```json
{
  "category": "Nama Kategori"
}
```

Ganti "Nama Kategori" dengan salah satu kategori berikut: Bahari, Budaya, Cagar Alam, Pusat Perbelanjaan, Taman Hiburan, atau Tempat Ibadah.

### Contoh Response (JSON):

```json
[
  {
    "Place_Name": "Kebun Tanaman Obat Sari Alam",
    "Category": "Cagar Alam",
    "City_x": "Bandung",
    "Rating": 4.9
  },
  ...
]
```

## 📞 Kontak

Jika Anda memiliki pertanyaan atau masukan, silakan hubungi \[Nama Anda] melalui \[Email Anda] atau \[Profil LinkedIn/GitHub Anda].

```

Anda dapat langsung menyalin dan menggunakan README ini. Pastikan untuk mengganti placeholder seperti `username`, `Nama Anda`, `Email Anda`, dan `Profil LinkedIn/GitHub Anda` sesuai dengan informasi Anda.
```
