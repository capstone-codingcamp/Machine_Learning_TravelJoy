TravelJoy: Sistem Rekomendasi Wisata📝 Deskripsi SingkatTravelJoy adalah sebuah proyek yang bertujuan untuk membangun sistem rekomendasi tempat wisata di Indonesia berdasarkan kategori yang diminati pengguna. Proyek ini mencakup seluruh alur kerja machine learning, mulai dari pembersihan dataset mentah, pembuatan model rekomendasi menggunakan content-based filtering, hingga mengubah model menjadi sebuah API yang dapat diakses secara publik melalui deployment di Hugging Face Spaces menggunakan Docker.📜 Daftar IsiAlur ProyekStruktur FolderCara Mereplikasi ProyekDeployment ke Hugging Face SpacesCara Menggunakan APIKontak🌊 Alur ProyekProyek ini dibagi menjadi beberapa tahapan utama yang saling berhubungan:Pembersihan Dataset (Dataset_cleaning.ipynb)Tahap awal dimulai dengan proses pembersihan dan persiapan data dari beberapa file CSV yang berisi informasi pariwisata.Proses ini mencakup penggabungan data, penanganan nilai yang hilang (missing values), dan penghapusan data duplikat untuk menghasilkan satu dataset komprehensif yang siap digunakan untuk pemodelan.Dataset yang telah bersih disimpan sebagai data_wisata.csv.Pembuatan Model Rekomendasi (recommedation_travelling_system.ipynb)Pada tahap ini, dataset yang telah bersih digunakan untuk membangun model sistem rekomendasi.Model ini menggunakan pendekatan content-based filtering dengan memanfaatkan deskripsi tempat wisata. Deskripsi teks diubah menjadi representasi vektor (embedding) menggunakan model LSTM (Long Short-Term Memory).Cosine similarity dihitung dari vektor embedding untuk mengukur kemiripan antar tempat wisata.Hasil dari notebook ini adalah:text_embedding_model.keras: Model embedding yang telah dilatih.cosine_similarity.pkl: Matriks kesamaan kosinus antar tempat wisata.Inferensi & Pembuatan API (app.py)Model yang telah dilatih kemudian diubah menjadi sebuah API menggunakan FastAPI.app.py berisi logika untuk memuat model (.keras) dan matriks kesamaan (.pkl), serta menyediakan endpoint yang dapat menerima input kategori wisata dari pengguna dan memberikan rekomendasi 10 tempat teratas.Pengujian API (Menggunakan Postman)Sebelum deployment, API diuji secara lokal untuk memastikan fungsionalitasnya berjalan dengan baik.Pengujian dilakukan dengan mengirimkan permintaan POST ke endpoint API menggunakan Postman. Respons yang berhasil ditandai dengan status 200 OK dan berisi data rekomendasi dalam format JSON.Deployment (Hugging Face Spaces dengan Docker)Setelah pengujian API berhasil, proyek dideploy ke Hugging Face Spaces.Metode deployment yang dipilih adalah menggunakan Docker, yang memungkinkan aplikasi berjalan di lingkungan yang terisolasi dan konsisten.Sebuah Dockerfile dibuat untuk mendefinisikan image aplikasi yang berisi semua dependensi dan konfigurasi yang diperlukan.📁 Struktur FolderBerikut adalah struktur folder yang direkomendasikan untuk proyek ini:TravelJoy/
│
├── Inference/
│   ├── assets/
│   │   ├── data_wisata.csv
│   │   ├── text_embedding_model.keras
│   │   ├── cosine_similarity.pkl
│   │   └── embedding_matrix.npy
│   ├── app.py
│   ├── Dockerfile
│   ├── README.md         # Penjelasan khusus untuk folder Inference
│   └── requirements.txt
│
├── Dataset_cleaning.ipynb
├── recommedation_travelling_system.ipynb
└── README.md             # README utama ini

🚀 Cara Mereplikasi ProyekUntuk menjalankan proyek ini di lingkungan lokal Anda, ikuti langkah-langkah berikut:PrasyaratPython 3.8+Jupyter Notebook atau JupyterLabPostman (untuk pengujian API)Langkah-langkahClone Repositorigit clone https://github.com/username/TravelJoy.git
cd TravelJoy
Instal DependensiPastikan Anda memiliki semua library yang dibutuhkan dengan menginstalnya dari file requirements.txt.pip install -r requirements.txt
Jalankan NotebookBuka dan jalankan Dataset_cleaning.ipynb terlebih dahulu untuk menghasilkan file data_wisata.csv.Selanjutnya, jalankan recommedation_travelling_system.ipynb untuk melatih model dan menghasilkan file text_embedding_model.keras dan cosine_similarity.pkl.Pastikan semua file hasil disimpan di dalam folder assets/.Jalankan API Secara LokalGunakan Uvicorn untuk menjalankan server FastAPI dari file app.py.uvicorn app:app --reload
API akan berjalan di http://127.0.0.1:8000.Uji API dengan PostmanBuka Postman.Buat permintaan POST ke URL: http://127.0.0.1:8000/get_recommendations/Pilih tab Body, lalu pilih format raw dan JSON.Masukkan request body seperti contoh di bawah:{
  "category": "Cagar Alam"
}
Kirim permintaan. Anda seharusnya menerima respons dengan status 200 OK beserta daftar rekomendasi tempat wisata.部署 Deployment ke Hugging Face SpacesDeployment dilakukan menggunakan Docker untuk memastikan portabilitas dan konsistensi lingkungan.PrasyaratAkun Hugging FaceGit LFS (Large File Storage) untuk menyimpan file model yang besar.Docker terinstal di komputer Anda.Langkah-langkahBuat Space Baru di Hugging FaceMasuk ke akun Hugging Face Anda dan buat New Space.Beri nama Space Anda (misalnya, TravelJoy).Pilih Docker sebagai Space SDK.Clone Repositori SpaceHugging Face akan menyediakan perintah git clone untuk repositori Space Anda.# Pastikan Anda telah menginstal Git LFS
git lfs install

git clone https://huggingface.co/spaces/username/TravelJoy
cd TravelJoy
Siapkan File ProyekSalin semua file proyek (app.py, requirements.txt, Dockerfile, dan folder assets) ke dalam folder repositori yang baru saja Anda clone.Pastikan file model .keras dilacak oleh Git LFS:git lfs track "assets/text_embedding_model.keras"
Buat DockerfileBuat file bernama Dockerfile (tanpa ekstensi) di direktori root dengan isi berikut:# Gunakan base image resmi Python
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
Push ke Hugging FaceCommit dan push semua file ke repositori Hugging Face.git add .
git commit -m "Initial commit: deploy recommendation API"
git push
Hugging Face akan secara otomatis membangun image Docker dan menjalankan aplikasi Anda.⚙️ Cara Menggunakan APISetelah berhasil dideploy, API dapat diakses melalui URL publik yang disediakan oleh Hugging Face Spaces.Endpoint: /get_recommendations/Method: POSTRequest Body (JSON):{
  "category": "Nama Kategori"
}
Ganti "Nama Kategori" dengan salah satu kategori berikut: Bahari, Budaya, Cagar Alam, Pusat Perbelanjaan, Taman Hiburan, atau Tempat Ibadah.Contoh Response (JSON):[
  {
    "Place_Name": "Kebun Tanaman Obat Sari Alam",
    "Category": "Cagar Alam",
    "City_x": "Bandung",
    "Rating": 4.9
  },
  ...
]
📞 KontakJika Anda memiliki pertanyaan atau masukan, silakan hubungi [Nama Anda] melalui [Email Anda] atau [Profil LinkedIn/GitHub Anda].
