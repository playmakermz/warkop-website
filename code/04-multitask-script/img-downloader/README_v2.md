# 🖼️ Advanced Image Crawler & Downloader v2.0

Script Python untuk crawling dan download gambar dengan dukungan **gallery-dl** untuk akses resolusi penuh pada situs yang memerlukan autentikasi.

## ✨ Fitur Utama

- 🔐 **Autentikasi** - Login untuk akses resolusi penuh (Pixiv, Twitter, Instagram, dll)
- 🎨 **gallery-dl Integration** - Menggunakan gallery-dl untuk download yang lebih handal
- 📁 **Config File** - Simpan kredensial dengan aman di file terpisah
- 🔄 **Fallback System** - Otomatis fallback ke crawler manual jika diperlukan
- 🌐 **Multi-Site Support** - Mendukung 10+ situs populer
- 📷 **High Resolution** - Download gambar dengan resolusi penuh

## 📋 Situs yang Didukung

| Situs | Tipe Autentikasi | Keterangan |
|-------|------------------|------------|
| Pixiv | Username/Password atau Refresh Token | Full support dengan ugoira |
| Twitter/X | Cookies atau Auth Token | Termasuk video |
| Instagram | Username/Password atau Session ID | Stories & Highlights |
| DeviantArt | OAuth (Client ID/Secret) | Original quality |
| ArtStation | Tidak perlu login | Public content |
| Danbooru | API Key | Full resolution |
| Imgur | Client ID | Albums & galleries |
| Tumblr | API Key | Blog content |
| Flickr | API Key | Photo streams |
| Reddit | Client Credentials | Subreddit images |

## 🚀 Instalasi

### 1. Install Dependencies Dasar

```bash
pip install -r requirements.txt
```

### 2. Install gallery-dl (Direkomendasikan)

```bash
# Via pip
pip install gallery-dl

# Atau via script
python image_crawler_advanced.py --install-gallery-dl
```

### 3. Setup Kredensial (Opsional tapi Direkomendasikan)

```bash
# Mode interaktif
python image_crawler_advanced.py --setup

# Atau edit langsung config.json
```

## 📖 Cara Penggunaan

### Mode Interaktif

```bash
python image_crawler_advanced.py
```

Menu akan muncul:
1. Download gambar dari URL
2. Setup kredensial
3. Lihat konfigurasi
4. Keluar

### Command Line

```bash
# Download dari URL
python image_crawler_advanced.py https://www.pixiv.net/en/users/12345

# Dengan kedalaman crawling
python image_crawler_advanced.py https://example.com -d 2

# Dengan output folder khusus
python image_crawler_advanced.py https://example.com -o ./my_downloads

# Setup kredensial
python image_crawler_advanced.py --setup
```

## 🔐 Setup Autentikasi

### Pixiv

**Opsi 1: Username & Password**
```json
"pixiv": {
    "username": "email@example.com",
    "password": "your_password"
}
```

**Opsi 2: Refresh Token (Lebih Aman)**

1. Install `gppt`: `pip install gppt`
2. Jalankan: `gppt login`
3. Login dengan browser
4. Copy refresh token ke config:
```json
"pixiv": {
    "refresh_token": "your_refresh_token_here"
}
```

### Twitter/X

**Opsi 1: Cookies File**

1. Install browser extension "Get cookies.txt" atau "EditThisCookie"
2. Login ke Twitter di browser
3. Export cookies ke file `cookies/twitter_cookies.txt`
4. Format Netscape cookies (txt)

**Opsi 2: Auth Token**

1. Login ke Twitter di browser
2. Buka Developer Tools (F12) > Application > Cookies
3. Cari cookie `auth_token`
4. Copy value ke config:
```json
"twitter": {
    "auth_token": "your_auth_token_here"
}
```

### Instagram

**Opsi 1: Username & Password**
```json
"instagram": {
    "username": "your_username",
    "password": "your_password"
}
```

**Opsi 2: Session ID**

1. Login ke Instagram di browser
2. Buka Developer Tools > Application > Cookies
3. Cari cookie `sessionid`
4. Copy value ke config:
```json
"instagram": {
    "session_id": "your_session_id_here"
}
```

### DeviantArt

1. Buka https://www.deviantart.com/developers/
2. Register aplikasi baru
3. Copy Client ID dan Client Secret:
```json
"deviantart": {
    "client_id": "12345",
    "client_secret": "abc123..."
}
```

### Imgur

1. Buka https://api.imgur.com/oauth2/addclient
2. Register aplikasi (pilih "OAuth 2 authorization without a callback URL")
3. Copy Client ID:
```json
"imgur": {
    "client_id": "your_client_id"
}
```

### Reddit

1. Buka https://www.reddit.com/prefs/apps
2. Klik "create another app..."
3. Pilih "script"
4. Copy credentials:
```json
"reddit": {
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "user_agent": "ImageCrawler/2.0 by YourUsername"
}
```

## 📂 Struktur File

```
image_crawler/
├── image_crawler_advanced.py    # Script utama
├── config.json                  # File konfigurasi & kredensial
├── requirements.txt             # Dependencies
├── README.md                    # Dokumentasi
├── cookies/                     # Folder untuk cookies
│   └── twitter_cookies.txt
└── downloaded_images/           # Output folder default
    └── [domain]/
        └── [images...]
```

## ⚙️ Konfigurasi

### Settings

| Setting | Default | Keterangan |
|---------|---------|------------|
| `output_directory` | `./downloaded_images` | Folder output |
| `max_workers` | `5` | Thread untuk parallel download |
| `request_delay` | `0.5` | Delay antar request (detik) |
| `request_timeout` | `30` | Timeout request (detik) |
| `use_gallery_dl` | `true` | Gunakan gallery-dl jika tersedia |
| `fallback_to_crawler` | `true` | Fallback ke crawler manual |

### gallery-dl Options

```json
"gallery_dl_options": {
    "pixiv": {
        "ugoira": true,      // Download animasi
        "metadata": true,     // Simpan metadata
        "tags": true          // Simpan tags
    },
    "twitter": {
        "retweets": false,    // Include retweets
        "videos": true,       // Download video
        "cards": false        // Download cards
    }
}
```

## 🔧 Troubleshooting

### gallery-dl tidak ditemukan
```bash
pip install gallery-dl
# atau
python image_crawler_advanced.py --install-gallery-dl
```

### Login gagal (Pixiv)
- Coba gunakan refresh token sebagai gantinya
- Pastikan tidak ada 2FA aktif atau gunakan app password

### Gambar resolusi rendah
- Pastikan kredensial sudah benar
- Beberapa gambar memang hanya tersedia resolusi rendah
- Cek log untuk error autentikasi

### Rate limited
- Tingkatkan `request_delay` di config
- Tunggu beberapa menit sebelum mencoba lagi

### Cookies expired
- Export ulang cookies dari browser
- Login ulang dan update session_id

## ⚠️ Catatan Penting

### Keamanan
- **JANGAN** share file `config.json` yang berisi kredensial
- Tambahkan `config.json` ke `.gitignore` jika menggunakan git
- Gunakan refresh token / session ID daripada password jika memungkinkan

### Legalitas
- Hormati copyright dan terms of service
- Jangan download konten untuk redistribusi tanpa izin
- Gunakan untuk personal use saja

### Rate Limiting
- Script sudah dilengkapi delay otomatis
- Jangan jalankan terlalu banyak request dalam waktu singkat
- Beberapa situs mungkin memblokir IP jika terlalu agresif

## 📝 Changelog

### v2.0
- Integrasi gallery-dl
- Sistem autentikasi dengan config file
- Support untuk 10+ situs
- Fallback ke manual crawler
- Mode interaktif yang lebih baik

### v1.0
- Initial release
- Manual crawler dengan BeautifulSoup
- Basic image detection

---

**Dibuat dengan ❤️ menggunakan Python, BeautifulSoup, dan gallery-dl**
