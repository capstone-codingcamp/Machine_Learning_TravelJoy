```markdown
# TravelJoy: Sistem Rekomendasi Wisata

## Deskripsi
TravelJoy adalah proyek yang membangun sistem rekomendasi tempat wisata di Indonesia berdasarkan kategori yang diminati pengguna. Proyek ini mencakup pembersihan dataset, pembuatan model rekomendasi dengan content-based filtering, serta deployment model sebagai API di Hugging Face Spaces menggunakan Docker.

## Daftar Isi
- [Alur Proyek](#alur-proyek)
- [Struktur Folder](#struktur-folder)
- [Cara Mereplikasi Proyek](#cara-mereplikasi-proyek)
- [Deployment ke Hugging Face Spaces](#deployment-ke-hugging-face-spaces)
- [Cara Menggunakan API](#cara-menggunakan-api)
- [Kontak](#kontak)

## Alur Proyek

### 1. Pembersihan Dataset
Proses pembersihan data dilakukan dalam notebook `Dataset_cleaning.ipynb`. Langkah-langkahnya termasuk penggabungan data, penanganan missing values, dan penghapusan data duplikat, menghasilkan dataset yang bersih (`data_wisata.csv`).

### 2. Pembuatan Model Rekomendasi
Notebook `recommendation_travelling_system.ipynb` digunakan untuk membangun model recommendation menggunakan content-based filtering. Deskripsi tempat wisata diubah menjadi embedding dengan model LSTM, dan similarity antar tempat dihitung menggunakan cosine similarity. Hasilnya adalah model (`text_embedding_model.keras`) dan matriks kesamaan (`cosine_similarity.pkl`).

### 3. API Inferensi (FastAPI)
Model yang telah dilatih diubah menjadi API dengan menggunakan FastAPI (`app.py`). API menerima input kategori wisata dan memberikan rekomendasi 10 tempat wisata teratas. API diuji menggunakan Postman untuk memastikan status 200 OK.

### 4. Deployment ke Hugging Face Spaces
Setelah pengujian berhasil, proyek dideploy ke Hugging Face Spaces menggunakan Docker. Docker memastikan aplikasi berjalan konsisten di berbagai lingkungan.

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
│   └── README.md
│
├── Dataset\_cleaning.ipynb
├── recommendation\_travelling\_system.ipynb
└── README.md

````

## Cara Mereplikasi Proyek

### Prasyarat
- Python 3.8+
- Jupyter Notebook
- Postman (untuk pengujian API)

### Langkah-langkah

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
   * Jalankan `recommendation_travelling_system.ipynb` untuk melatih model dan menghasilkan file `text_embedding_model.keras` dan `cosine_similarity.pkl`.

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
   * Kirim permintaan dan pastikan mendapat respons status 200 OK dengan data rekomendasi.

## Deployment ke Hugging Face Spaces

### Prasyarat

* Akun Hugging Face
* Docker terinstal

### Langkah-langkah

1. **Buat Space Baru di Hugging Face**

   * Buat New Space dan pilih Docker sebagai Space SDK.

2. **Clone Repositori Space**

   ```bash
   git lfs install
   git clone https://huggingface.co/spaces/username/TravelJoy
   cd TravelJoy
   ```

3. **Siapkan File Proyek**
   Salin file proyek (`app.py`, `requirements.txt`, `Dockerfile`, dan folder `assets`) ke dalam repositori yang telah di-clone. Pastikan model `.keras` dilacak oleh Git LFS:

   ```bash
   git lfs track "assets/text_embedding_model.keras"
   ```

4. **Buat Dockerfile**
   Buat `Dockerfile` di direktori root dengan isi berikut:

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

Hugging Face akan otomatis membangun image Docker dan menjalankan aplikasi.

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

README ini lebih terstruktur dan lebih fokus pada langkah-langkah penting, sambil menghilangkan informasi yang tidak diperlukan. Anda bisa langsung menyalinnya dan mengganti placeholder sesuai kebutuhan.
```
