# Version Control Git 

Git adalah version control yang digunakan untuk melakukan tracking perubahan (mirip seperti save data pada game) pada folder project. Dengan git kita bisa melihat siapa yang melakukan perubahan, kapan dilakukan perubahan, dan apa yang diubah. 

Version control system adalah software yang digunakan untuk membantu kita mengetahui history perubahan pada project. Dengan ini kita bisa melihat dan membandingkan perubahan dari file, serta mempermudah kolaborasi dengan orang lain secara lebih efektif. 

Git menggunakan sistem distribusi, yaitu memperbolehkan kita untuk melakukan perubahan saat offline dan "merge" perubahan tersebut saat kita sudah siap dan online. Dengan ini kita sebagai developer tidak perlu terlalu khawatir jika tidak ada koneksi internet. 

## Command Line Git yang Paling Sering Digunakan

- `git init` - Mengaktifkan git pada folder (inisialisasi repository)
- `git add` - Menambahkan perubahan pada "staging area" (area persiapan sebelum di-commit)
- `git commit` - Menyimpan perubahan dengan pesan/judul yang menjelaskan apa yang diubah
- `git push` - Upload repository git ke remote server (misalnya GitHub)
- `git pull` - Mendownload dan menggabungkan perubahan dari repository remote
- `git branch` - Membuat branch baru atau melihat daftar branch yang ada
- `git merge` - Menggabungkan satu branch dengan branch lainnya

  > Merge sebaiknya digunakan ketika target branch akan dibagikan kepada orang lain (shared branch).

Git juga dilengkapi fitur untuk melakukan pull request (untuk kolaborasi dengan orang lain) dan code reviews (melihat atau membandingkan code). Dengan fitur ini kita akan lebih mudah untuk bekerja sama dengan orang lain dalam satu project.

Secara garis besar, git adalah alat yang sangat bermanfaat untuk kita secara jangka panjang dalam pengembangan software. 

## Git dan GitHub 

**Git** adalah suatu version control system yang dirancang untuk menangani berbagai macam bentuk project. Pengembangan awalnya dimulai pada tahun 2005 oleh Linus Torvalds. Git menjadi standar dalam version control untuk source code.

Git dapat membantu kita untuk melacak perubahan pada source code dan bisa membantu kita untuk kembali pada versi sebelumnya jika dibutuhkan. Ini adalah fungsi yang sangat dibutuhkan oleh para developer untuk membantu mereka mengerjakan semua pekerjaan dengan sangat efektif. 

**GitHub** adalah platform berbasis web untuk hosting project source code. GitHub dimulai pada tahun 2008 dan menjadi salah satu platform hosting yang sangat reliable untuk melakukan kolaborasi dalam banyak project, penyelesaian masalah, dan mengelola code.

Pada GitHub, terdapat fitur "Pull Request" dimana kita sebagai user bisa mengajukan perubahan untuk di-review oleh pemilik repository. Setelah di-review, perubahan tersebut bisa diterima atau ditolak. Fitur ini membuat kolaborasi pada GitHub bisa memiliki aturan sesuai dengan apa yang kita inginkan. 

### Perbedaan Git dan GitHub

- **Git** = Software untuk version control yang terinstal di komputer kita
- **GitHub** = Platform online untuk menyimpan dan berbagi repository Git

## Mengenai Savepoint (Commit)

Konsep sederhana dari Git adalah savepoint atau yang biasa disebut "commit". 

Bayangkan seperti pada game, kita bisa melakukan savepoint untuk menyimpan progress kita. Kalau character yang kita gunakan kalah atau ada masalah, kita bisa kembali ke save point sebelumnya. 

Konsep pada Git juga sama seperti itu. Setiap kali kita melakukan commit, Git membuat savepoint yang bisa kita kembalikan kapan saja.

### Melihat History Commit

Untuk melihat history atau daftar commit sebelumnya:
```bash
git log
```

### Berpindah ke Commit Sebelumnya

Untuk berpindah ke savepoint (commit) sebelumnya:
```bash
git checkout [commit_id]  # Manual menggunakan ID commit
git checkout main  # atau master, untuk kembali ke commit paling baru
```

Catatan: Sekarang lebih disarankan menggunakan `git switch` daripada `git checkout` untuk berpindah branch.

## Mengenai Staging Area

Staging area adalah area persiapan sebelum melakukan commit. Konsepnya seperti ini:

1. **Working Directory** - Tempat kamu bekerja dan mengedit file
2. **Staging Area** - File yang sudah siap untuk di-commit
3. **Repository** - Tempat penyimpanan permanent setelah commit

Workflow-nya:
```bash
git add file.txt       # Pindahkan file ke staging area
git commit -m "pesan"  # Simpan permanent ke repository
```

## Mengenai Branch

Branch adalah cabang terpisah dari project utama. Ini sangat berguna untuk:
- Mengembangkan fitur baru tanpa mengganggu kode utama
- Melakukan eksperimen
- Memperbaiki bug secara terpisah

Cara kerja branch:
```bash
git branch feature-login      # Buat branch baru
git checkout feature-login    # Pindah ke branch tersebut
# atau gunakan shortcut:
git checkout -b feature-login # Buat dan langsung pindah
```

Setelah selesai mengembangkan fitur di branch, kita bisa menggabungkannya kembali ke branch utama menggunakan merge atau rebase.

## Mengenai Rebase

Rebase digunakan ketika terdapat perbedaan antara kode di local dan di repository remote.

Skenarionya seperti ini:
- Kamu bekerja di local dan melakukan beberapa commit
- Temanmu melakukan push ke repository remote
- Sekarang repository remote sudah lebih baru dari local kamu

Untuk mengatasi ini, gunakan:
```bash
git add .
git commit -am 'perubahan baru'
git pull --rebase
```

Selama tidak terdapat conflict pada baris kode yang sama antara versi baru dan lama, maka masalah akan dapat diselesaikan dengan sangat mudah.

## Mengenai Rebase (Jika Terdapat Conflict pada Baris)

Jika ada conflict, Git akan secara otomatis memberikan tanda seperti ini pada file yang conflict:

```
<<<<<<< HEAD
halo saya mau conflict disini
=======
halo saya dari branch belakang apa bisa
>>>>>>> ca838f0 (conf)
```

Penjelasan:
- `<<<<<<< HEAD` = Kode dari repository remote (versi terbaru di server)
- `=======` = Pemisah antara dua versi
- `>>>>>>> ca838f0` = Kode dari local kamu (commit ID: ca838f0)

Cara menyelesaikannya:
1. Pilih kode mana yang mau dipakai (atau gabungkan keduanya)
2. Hapus tanda `<<<<<<<`, `=======`, dan `>>>>>>>`
3. Simpan file
4. Lakukan `git add` dan `git rebase --continue`

## Perbedaan Rebase dan Merge

Ada dua cara untuk menggabungkan perubahan di Git:

```bash
git pull --rebase    # Menggunakan rebase
git pull --no-rebase # Menggunakan merge (default)
```

### Perbandingan

| Aspek | Rebase | Merge |
|-------|--------|-------|
| History | Menulis ulang history menjadi linear | Menyimpan history apa adanya |
| Penggunaan | Disarankan untuk branch private/personal | Disarankan untuk branch public/shared |
| Conflict | Menyelesaikan conflict pada satu branch yang sama | Menyelesaikan conflict dari branch yang berbeda |
| Hasil | Git history lebih bersih dan rapi | Git history mempertahankan semua jejak |

### Kapan Menggunakan Rebase vs Merge?

**Gunakan Rebase ketika:**
- Bekerja di branch personal yang belum di-push ke remote
- Ingin membuat history commit lebih bersih dan linear
- Project open source yang mensyaratkan clean history
- Kamu bekerja sendiri di branch tersebut

**Gunakan Merge ketika:**
- Bekerja di branch yang sudah dibagikan dengan tim
- Ingin menjaga semua history dan jejak kolaborasi
- Melakukan Pull Request di GitHub
- Project dengan banyak collaborator

## Cara Manual Alternatif (Jika Rebase Terlalu Ribet)

Jika terdapat conflict antara local dan repository yang terlalu rumit, kamu bisa lakukan cara manual:

1. Copy kode yang kamu rasa penting dari local
2. Masukkan kode tersebut secara manual ke dalam repository melalui editor
3. Hapus keseluruhan kode di local
4. Clone ulang kode dari repository

Catatan: Cara ini kurang efisien tapi bisa jadi solusi darurat untuk pemula.

## Praktik: Uji Coba Merge

Mari kita praktikkan merge dengan langkah berikut:

### Langkah 1: Setup Awal
```bash
# Buat repository kosong di GitHub
# Clone repository ke local
git clone [url-repository]

# Masuk ke folder repository
cd [nama-folder]
```

### Langkah 2: Membuat dan Bekerja di Branch Baru
```bash
# Buat branch baru
git branch feature-update

# Pindah ke branch baru
git checkout feature-update

# Lakukan perubahan data, misalnya pada README.md
# Edit file menggunakan text editor

# Add dan commit perubahan
git add .
git commit -m "update README di branch feature"

# Push branch baru ke remote
git push origin feature-update
# Jika error, gunakan:
git push --set-upstream origin feature-update
```

### Langkah 3: Merge ke Branch Main
```bash
# Kembali ke branch main
git checkout main

# Cek apakah ada perubahan (seharusnya belum ada)
cat README.md

# Lakukan merge
git merge feature-update

# Push hasil merge
git push origin main
```

## Uji Coba Kedua: Menyelesaikan Conflict

Mari kita praktikkan cara mengatasi conflict:

### Skenario:
1. Pada branch `main`, lakukan perubahan pada file README (baris ke-5 misalnya)
2. Pada branch `feature-update`, lakukan perubahan pada file yang sama di baris yang sama
3. Lakukan pull request dari branch baru dan lihat cara penyelesaiannya

### Langkah Detail:

```bash
# Di branch main
git checkout main
echo "Perubahan dari main" >> README.md
git add README.md
git commit -m "update dari main"
git push origin main

# Di branch feature-update
git checkout feature-update
echo "Perubahan dari feature" >> README.md
git add README.md
git commit -m "update dari feature"
git push origin feature-update

# Coba merge (akan ada conflict)
git checkout main
git merge feature-update
# Git akan memberitahu ada conflict

# Buka file README.md dan selesaikan conflict
# Setelah selesai:
git add README.md
git commit -m "resolve conflict"
git push origin main
```

## Tips Penting untuk Pemula

1. **Selalu pull sebelum push**
   ```bash
   git pull origin main
   git push origin main
   ```

2. **Gunakan branch untuk fitur baru**
   Jangan langsung coding di branch main

3. **Commit sesering mungkin**
   Lebih baik banyak commit kecil daripada satu commit besar

4. **Tulis commit message yang jelas**
   Contoh yang baik: "Tambah fitur login dengan email"
   Contoh yang buruk: "update"

5. **Backup sebelum rebase**
   Jika masih pemula, lebih aman menggunakan merge dulu

## Kesimpulan

Git adalah tools yang powerful untuk version control. Memang butuh waktu untuk terbiasa, tapi setelah paham konsep dasarnya, Git akan sangat membantu dalam pengembangan project, baik sendiri maupun tim.

Kunci utamanya:
- **Commit** = Savepoint
- **Branch** = Cabang kerja terpisah
- **Merge** = Gabungkan perubahan (simpan semua history)
- **Rebase** = Gabungkan perubahan (rapikan history)
- **Pull** = Download perubahan dari remote
- **Push** = Upload perubahan ke remote

### Reference
- https://www.simplilearn.com/git-rebase-vs-merge-article
- https://binarysiddhant.hashnode.dev/demystifying-git-pull-rebase-and-git-pull-no-rebase
- https://git-scm.com/doc (Dokumentasi resmi Git)
- https://docs.github.com/en (Dokumentasi resmi GitHub)
