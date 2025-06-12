# TravelJoy: Sistem Rekomendasi Wisata

TravelJoy adalah proyek untuk membangun sistem rekomendasi tempat wisata di Indonesia berdasarkan kategori yang diminati pengguna. Proyek ini mencakup pembersihan dataset, pembuatan model rekomendasi menggunakan content-based filtering, dan deployment API di Hugging Face Spaces menggunakan Docker.

## Alur Proyek

1. **Pembersihan Dataset**  
   Proses pembersihan data dilakukan dalam notebook `Dataset_cleaning.ipynb`. Data wisata digabung, dibersihkan dari nilai yang hilang, dan duplikat, menghasilkan dataset bersih (`data_wisata.csv`).

2. **Pembuatan Model Rekomendasi**  
   Dalam notebook `recommendation_travelling_system.ipynb`, model rekomendasi dibuat dengan pendekatan content-based filtering. Deskripsi wisata diubah menjadi embedding dengan LSTM dan dihitung menggunakan cosine similarity.

3. **API Inferensi (FastAPI)**  
   Model yang dilatih diubah menjadi API dengan FastAPI dalam file `app.py`. API ini menerima input kategori wisata dan memberikan 10 rekomendasi tempat teratas.

4. **Pengujian API**  
   API diuji dengan Postman untuk memastikan bahwa respons yang diberikan adalah 200 OK dan berisi data rekomendasi.

5. **Deployment ke Hugging Face Spaces**  
   Proyek dideploy menggunakan Docker di Hugging Face Spaces untuk membuat API yang dapat diakses publik.

## Struktur Folder

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
│   ├── requirements.txt
│
├── Dataset\_cleaning.ipynb
├── recommendation\_travelling\_system.ipynb
└── README.md

````

## Cara Mereplikasi Proyek

1. **Clone Repositori**
   ```bash
   git clone https://github.com/username/TravelJoy.git
   cd TravelJoy
````

2. **Instal Dependensi**

   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Notebook**

   * Jalankan `Dataset_cleaning.ipynb` untuk menghasilkan `data_wisata.csv`.
   * Jalankan `recommendation_travelling_system.ipynb` untuk melatih model dan menghasilkan `text_embedding_model.keras` dan `cosine_similarity.pkl`.

4. **Jalankan API Secara Lokal**

   ```bash
   uvicorn app:app --reload
   ```

   API akan berjalan di `http://127.0.0.1:8000`.

5. **Uji API dengan Postman**

   * URL: `http://127.0.0.1:8000/get_recommendations/`
   * Body (JSON):

     ```json
     {
       "category": "Cagar Alam"
     }
     ```
   * Kirim permintaan dan pastikan mendapat respons status 200 OK.

## Deployment ke Hugging Face Spaces

1. **Buat Space Baru di Hugging Face**
   Buat Space di Hugging Face dan pilih Docker sebagai SDK.

2. **Clone Repositori Space**

   ```bash
   git lfs install
   git clone https://huggingface.co/spaces/username/TravelJoy
   cd TravelJoy
   ```

3. **Siapkan File Proyek**
   Salin file proyek (`app.py`, `requirements.txt`, `Dockerfile`, dan folder `assets`) ke dalam repositori yang telah di-clone. Pastikan file model `.keras` dilacak oleh Git LFS:

   ```bash
   git lfs track "assets/text_embedding_model.keras"
   ```

4. **Buat Dockerfile**
   Buat file `Dockerfile` di direktori root dengan isi berikut:

   ```Dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
   ```

5. **Push ke Hugging Face**

   ```bash
   git add .
   git commit -m "Initial commit: deploy recommendation API"
   git push
   ```

## Cara Menggunakan API

Setelah deployment berhasil, API dapat diakses melalui URL publik yang disediakan oleh Hugging Face Spaces.

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

### Contoh Response (JSON):

```json
[
  {
    "Place_Name": "Kebun Tanaman Obat Sari Alam",
    "Category": "Cagar Alam",
    "City_x": "Bandung",
    "Rating": 4.9
  }
]
```

## Kontak

Jika Anda memiliki pertanyaan atau masukan, silakan hubungi \[Nama Anda] melalui \[Email Anda] atau \[Profil LinkedIn/GitHub Anda].

```

README ini lebih sederhana, rapi, dan terfokus pada langkah-langkah utama tanpa detail yang berlebihan, siap untuk digunakan di GitHub.
```
