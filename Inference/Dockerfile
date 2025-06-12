# Gunakan image dasar Python
FROM python:3.9-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Menyalin semua file aplikasi ke dalam container
COPY . /app

# Menginstal dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Menyiapkan port untuk FastAPI (sesuai dengan Hugging Face Spaces)
EXPOSE 7860

# Perintah untuk menjalankan aplikasi menggunakan Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
