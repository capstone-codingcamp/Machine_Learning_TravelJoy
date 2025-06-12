from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import tensorflow as tf

# --- Register custom model class to avoid error when loading
class TextEmbeddingModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, sequence_length, **kwargs):
        super(TextEmbeddingModel, self).__init__(**kwargs)
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=sequence_length)
        self.lstm = tf.keras.layers.LSTM(128, return_sequences=False)
        self.dense = tf.keras.layers.Dense(128)

    def call(self, inputs):
        x = self.embedding(inputs)
        x = self.lstm(x)
        return self.dense(x)

    def get_config(self):
        config = super(TextEmbeddingModel, self).get_config()
        config.update({
            'vocab_size': self.embedding.input_dim,
            'embedding_dim': self.embedding.output_dim,
            'sequence_length': self.embedding.input_length,
        })
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)


# --- 1. Memuat model TensorFlow yang telah dilatih (format .keras)
try:
    # Memuat model yang disimpan dalam format .keras dan mendaftarkan custom layer
    loaded_model = tf.keras.models.load_model(
        'assets/text_embedding_model.keras',  # Ganti dengan path model Anda (format .keras)
        custom_objects={'TextEmbeddingModel': TextEmbeddingModel}  # Register custom class here
    )
    print("TensorFlow model loaded successfully.")
except Exception as e:
    print(f"Error loading TensorFlow model: {e}")

# Memuat cosine similarity matrix
try:
    cosine_similarity_matrix = joblib.load("assets/cosine_similarity.pkl")
    print("Cosine Similarity Matrix loaded successfully.")
except Exception as e:
    print(f"Error loading cosine similarity model: {e}")

# Membaca dataset dan melakukan pembersihan
df = pd.read_csv("assets/data_wisata.csv")  # Ganti dengan path file Anda
df = df.dropna(subset=['Description', 'Rating', 'Category'])
df = df.drop_duplicates(subset=['Place_Id', 'Description']).reset_index(drop=True)

# Membuat aplikasi FastAPI
app = FastAPI()

# Mendefinisikan model input menggunakan Pydantic
class CategoryInput(BaseModel):
    category: str

# Fungsi untuk mendapatkan embedding deskripsi tempat wisata
def get_description_embedding(description):
    # Tokenisasi dan padding teks sebelum prediksi
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000)
    tokenizer.fit_on_texts(df['Description'])  # Pastikan tokenizer menggunakan data training yang sama
    seq = tokenizer.texts_to_sequences([description])
    padded = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=100)
    return loaded_model.predict(padded)[0]  # Menggunakan model yang dimuat untuk prediksi

# Fungsi rekomendasi berdasarkan input kategori
def rekomendasi_top10_kategori(kategori_input):
    # Filter data sesuai kategori
    df_kategori = df[df['Category'].str.lower() == kategori_input.lower()].copy()

    if df_kategori.empty:
        return f"❌ Tidak ditemukan tempat wisata dengan kategori: '{kategori_input}'"

    # Ambil index relatif (berdasarkan posisi di df yang sudah reset_index)
    idx_kategori = df_kategori.index.tolist()

    # Subset similarity matrix
    similarity_scores = cosine_similarity_matrix[idx_kategori][:, idx_kategori]

    # Hitung rata-rata similarity dari tiap tempat ke tempat lain
    avg_similarity = similarity_scores.mean(axis=1)

    # Tambahkan skor similarity ke dataframe kategori
    df_kategori['avg_similarity'] = avg_similarity

    # Urutkan berdasarkan rating tertinggi dan similarity
    df_top = df_kategori.sort_values(by=['Rating', 'avg_similarity'], ascending=False)

    # Tampilkan 10 tempat wisata teratas
    return df_top[['Place_Name', 'Category', 'City_x', 'Rating']].head(10)

# Mendefinisikan route untuk rekomendasi
@app.post("/get_recommendations/")
async def get_recommendations(input_data: CategoryInput):
    kategori_user = input_data.category

    # Mendapatkan rekomendasi berdasarkan kategori yang diminta
    output_top10 = rekomendasi_top10_kategori(kategori_user)
    
    if isinstance(output_top10, str):  # Jika tidak ada hasil ditemukan
        return {"message": output_top10}

    return output_top10.to_dict(orient="records")  # Mengembalikan hasil dalam format JSON

# Jalankan API dengan perintah:
# uvicorn app:app --reload
