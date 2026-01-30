# 🌐 Web Crawler Python - Pencari URL Berdasarkan Kata Kunci

Script Python untuk melakukan web crawling dan mencari halaman web yang berhubungan dengan kata kunci tertentu.

## ✨ Fitur

- 🔍 Pencarian berdasarkan kata kunci
- 📊 Limitasi jumlah hasil (contoh: maksimal 5 web)
- 💾 Menyimpan hasil ke file text
- 🖥️ Mode interaktif dan command-line
- 🔄 Dukungan multiple search engine (DuckDuckGo & Bing)

## 📦 Instalasi

```bash
# Install library yang diperlukan
pip install requests beautifulsoup4
```

## 🚀 Cara Penggunaan

### Mode Interaktif (Tanpa Argumen)

```bash
python web_crawler.py
```

Script akan meminta input:
- Kata kunci pencarian
- Jumlah maksimal hasil
- Nama file output (opsional)

### Mode Command Line

```bash
# Contoh dasar
python web_crawler.py -k "pemrograman python untuk pemula" -m 5

# Dengan nama file output
python web_crawler.py -k "tutorial machine learning" -m 10 -o hasil_ml.txt

# Menggunakan Bing sebagai mesin pencari
python web_crawler.py -k "belajar coding" -m 3 -e bing
```

### Argumen yang Tersedia

| Argumen | Keterangan | Default |
|---------|------------|---------|
| `-k`, `--keyword` | Kata kunci pencarian | - |
| `-m`, `--max` | Jumlah maksimal hasil | 5 |
| `-o`, `--output` | Nama file output | auto-generated |
| `-e`, `--engine` | Mesin pencari (duckduckgo/bing) | duckduckgo |
| `-d`, `--delay` | Jeda antar request (detik) | 1.0 |

## 📝 Contoh Penggunaan

### Contoh 1: Mencari Tutorial Python

```bash
python web_crawler.py -k "pemrograman python object oriented untuk pemula" -m 5
```

**Output di terminal:**
```
============================================================
🌐 WEB CRAWLER - PENCARI URL BERDASARKAN KATA KUNCI
============================================================

🚀 Memulai crawling dengan mesin pencari: duckduckgo

🔍 Mencari: 'pemrograman python object oriented untuk pemula'
📊 Maksimal hasil: 5
--------------------------------------------------
✅ [1] Tutorial OOP Python untuk Pemula...
   🔗 https://www.petanikode.com/python-oop/
✅ [2] Mengenal Object Oriented Programming...
   🔗 https://www.dicoding.com/blog/oop-python/
...

============================================================
📋 RINGKASAN HASIL CRAWLING
============================================================
🔑 Kata Kunci  : pemrograman python object oriented untuk pemula
📊 Jumlah URL  : 5
⏰ Waktu       : 2026-01-30 10:30:45
```

### Contoh 2: Mode Interaktif

```bash
$ python web_crawler.py

============================================================
🌐 WEB CRAWLER - PENCARI URL BERDASARKAN KATA KUNCI
============================================================

📝 Mode Interaktif
----------------------------------------
🔑 Masukkan kata kunci pencarian: belajar javascript dasar
📊 Jumlah maksimal hasil [5]: 3
💾 Nama file output (kosongkan untuk otomatis): 
```

## 📄 Format Output File

Hasil pencarian akan disimpan dalam format text seperti berikut:

```
============================================================
HASIL WEB CRAWLING
============================================================

Kata Kunci  : pemrograman python object oriented untuk pemula
Jumlah Hasil: 5
Waktu       : 2026-01-30 10:30:45

------------------------------------------------------------
DAFTAR URL:
------------------------------------------------------------

[1] https://www.petanikode.com/python-oop/
[2] https://www.dicoding.com/blog/mengenal-oop/
[3] https://www.pythonindo.com/tutorial-oop/
[4] https://www.codepolitan.com/belajar-python-oop
[5] https://www.belajarpython.com/tutorial/oop

============================================================
Dihasilkan oleh Web Crawler Python
============================================================
```

## ⚙️ Struktur Script

```
WebCrawler Class
├── __init__()          # Inisialisasi crawler
├── search_duckduckgo() # Pencarian via DuckDuckGo
├── search_bing()       # Pencarian via Bing
├── crawl()             # Fungsi utama crawling
├── save_results()      # Simpan hasil ke file
└── display_summary()   # Tampilkan ringkasan
```

## ⚠️ Catatan Penting

1. **Rate Limiting**: Script memiliki delay bawaan untuk menghindari blocking
2. **Etika Crawling**: Gunakan secara bertanggung jawab
3. **Network**: Pastikan koneksi internet stabil
4. **Proxy**: Jika menggunakan proxy, sesuaikan konfigurasi di script

## 🔧 Troubleshooting

**Error: Connection refused**
- Periksa koneksi internet
- Coba ganti mesin pencari dengan opsi `-e`

**Hasil pencarian sedikit**
- Coba kata kunci yang lebih umum
- Tingkatkan jumlah maksimal hasil

## 📜 Lisensi

Script ini bebas digunakan untuk keperluan pembelajaran dan pribadi.

---
*Dibuat dengan ❤️ menggunakan Python*
