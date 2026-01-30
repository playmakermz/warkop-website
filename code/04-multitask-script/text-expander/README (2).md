# 📝 Text Expander - Pengembang Kalimat Berbasis Dokumen

Script Python untuk mengembangkan kalimat menjadi paragraf berdasarkan dokumen markdown, **tanpa menggunakan AI/LLM**.

## 🚀 Fitur

- **Markov Chain**: Menggunakan n-gram model untuk generate teks yang koheren
- **TF-IDF Similarity**: Mencari kalimat/paragraf yang mirip dengan input
- **Hybrid Mode**: Kombinasi kedua metode untuk hasil terbaik
- **Mode Interaktif**: Antarmuka command-line yang mudah digunakan

## 📋 Cara Penggunaan

### 1. Persiapan

Letakkan file markdown (`.md`) yang berisi dokumen/novel di folder yang sama dengan script.

```
📁 folder/
├── text_expander.py
├── novel_chapter1.md  ← Dokumen Anda
├── novel_chapter2.md  ← Dokumen tambahan (opsional)
└── README.md
```

### 2. Jalankan Script

```bash
python3 text_expander.py
```

### 3. Gunakan Mode Interaktif

```
🖊️  Input: Matahari terbit dengan indah

📄 Output (4 kalimat):
------------------------------------------------------------
Matahari terbit dengan indah. Burung-burung berkicau merdu
menyambut datangnya hari baru. Embun pagi masih menghiasi
dedaunan yang hijau. Cahaya keemasan menerangi seluruh desa.
------------------------------------------------------------
```

## ⚙️ Perintah Interaktif

| Perintah | Fungsi |
|----------|--------|
| `<kalimat>` | Mengembangkan kalimat menjadi paragraf |
| `analyze <kalimat>` | Analisis kecocokan kata dengan dokumen |
| `method <nama>` | Ubah metode (`markov`, `similarity`, `hybrid`) |
| `sentences <n>` | Ubah jumlah kalimat output (2-10) |
| `help` | Tampilkan bantuan |
| `quit` / `exit` | Keluar dari program |

## 🔧 Metode yang Tersedia

### 1. **Markov Chain** (`method markov`)
- Menggunakan probabilitas transisi antar kata
- Menghasilkan teks yang mengikuti pola bahasa dokumen
- Cocok untuk generate teks kreatif

### 2. **Similarity** (`method similarity`)
- Mencari kalimat dari dokumen yang paling mirip dengan input
- Menggunakan TF-IDF dan Cosine Similarity
- Cocok untuk menemukan konteks yang relevan

### 3. **Hybrid** (`method hybrid`) [Default]
- Kombinasi Markov Chain dan Similarity
- Menghasilkan teks yang koheren dan relevan
- Rekomendasi untuk hasil terbaik

## 📊 Contoh Analisis

```
🖊️  Input: analyze Arya berjalan ke hutan

📊 Analisis:
   Jumlah kata: 4
   Kata cocok: 4 (100.0%)
   Kata yang ditemukan: arya, berjalan, ke, hutan

   Kalimat serupa:
   [0.497] Arya berjalan melewati hutan yang lebat...
   [0.265] Perjalanan ke utara penuh dengan bahaya...
   [0.237] Dengan keberanian, Arya melangkahkan kakinya...
```

## 🔬 Cara Kerja

```
┌─────────────────┐
│ Dokumen (.md)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Document        │  → Ekstrak kalimat, kata, paragraf
│ Processor       │  → Bersihkan markdown syntax
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌──────────┐
│Markov │ │Similarity│
│Chain  │ │Finder    │
└───┬───┘ └────┬─────┘
    │          │
    └────┬─────┘
         │
         ▼
┌─────────────────┐
│ Text Expander   │  → Kombinasi hasil
│ (Hybrid)        │  → Generate paragraf
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Output Paragraf │
└─────────────────┘
```

## 📁 Format Dokumen

Dokumen harus dalam format Markdown dengan struktur:

```markdown
# Chapter 1: Judul Chapter

Paragraf pertama berisi kalimat-kalimat.
Setiap kalimat diakhiri dengan tanda baca.

Paragraf kedua dan seterusnya.

# Chapter 2: Judul Berikutnya

Dan seterusnya...
```

## 💡 Tips

1. **Dokumen lebih panjang = hasil lebih baik**
   - Semakin banyak kalimat dalam dokumen, semakin kaya variasi output

2. **Gunakan bahasa yang konsisten**
   - Jika dokumen berbahasa Indonesia, input juga harus bahasa Indonesia

3. **Coba berbagai metode**
   - Eksperimen dengan `method markov`, `similarity`, dan `hybrid`

4. **Sesuaikan jumlah kalimat**
   - Gunakan `sentences 3` untuk output pendek
   - Gunakan `sentences 8` untuk output panjang

## 🛠️ Dependensi

Script ini menggunakan **Python 3** dengan library standar:
- `re` - Regular expressions
- `random` - Randomization
- `collections` - Counter, defaultdict
- `pathlib` - Path handling
- `math` - Mathematical operations

**Tidak memerlukan library eksternal!**

## 📜 Lisensi

Free to use and modify.
