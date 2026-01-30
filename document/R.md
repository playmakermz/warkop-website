# Panduan Belajar Bahasa R

## Daftar Isi

1. [Pengenalan R Language](#pengenalan-r-language)
2. [Instalasi dan Setup](#instalasi-dan-setup)
   - [Instalasi di Ubuntu](#instalasi-di-ubuntu)
   - [Menjalankan R Console](#menjalankan-r-console)
   - [Menjalankan R Script](#menjalankan-r-script)
3. [Dasar-Dasar R Programming](#dasar-dasar-r-programming)
   - [Operasi Matematika Dasar](#operasi-matematika-dasar)
   - [Membuat Array/Vector](#membuat-arrayvector)
   - [Membuat Data Frame](#membuat-data-frame)
   - [Membuat Matriks](#membuat-matriks)
   - [Membuat Tabel](#membuat-tabel)
4. [Mengelola Environment](#mengelola-environment)
   - [Mencari Object dengan ls()](#mencari-object-dengan-ls)
   - [Mengatur Working Directory](#mengatur-working-directory)
5. [Operasi Matriks](#operasi-matriks)
   - [Perkalian Matriks](#perkalian-matriks)
   - [Transpose Matriks](#transpose-matriks)
   - [Inverse Matriks](#inverse-matriks)
   - [Penjumlahan Matriks](#penjumlahan-matriks)
6. [Loop dan Percabangan](#loop-dan-percabangan)
   - [For Loop](#for-loop)
   - [While Loop](#while-loop)
   - [Conditional Statement](#conditional-statement)
7. [Visualisasi Data](#visualisasi-data)
   - [Membuat Layout Plot](#membuat-layout-plot)
   - [Sunflower Plot](#sunflower-plot)
   - [Scatter Plot](#scatter-plot)
   - [Regresi Linear](#regresi-linear)
   - [Histogram](#histogram)
   - [Distribusi Normal](#distribusi-normal)
8. [Import dan Export Data](#import-dan-export-data)
   - [Membaca File Text](#membaca-file-text)
   - [Membaca File CSV](#membaca-file-csv)
9. [Statistik Deskriptif](#statistik-deskriptif)
   - [Mean (Rata-rata)](#mean-rata-rata)
   - [Median (Nilai Tengah)](#median-nilai-tengah)
   - [Standard Deviation](#standard-deviation)
   - [Coefficient of Variation](#coefficient-of-variation)
10. [Latihan dan Referensi](#latihan-dan-referensi)

---

## Pengenalan R Language

R adalah bahasa pemrograman dan environment yang powerful untuk analisis statistik, visualisasi data, dan machine learning. R sangat populer di kalangan data scientist, statistician, dan researcher karena:

**Keunggulan R:**
- **Open Source**: Gratis dan bisa dimodifikasi
- **Rich Libraries**: Ribuan package untuk berbagai keperluan analisis
- **Visualisasi Powerful**: Bisa membuat grafik dan chart yang sangat detail
- **Community Support**: Komunitas besar yang aktif membantu

**Kapan Menggunakan R:**
- Analisis statistik dan data mining
- Machine learning dan predictive modeling
- Visualisasi data yang kompleks
- Research dan academic projects

---

## Instalasi dan Setup

### Instalasi di Ubuntu

Untuk install R di Ubuntu, cukup jalankan command berikut di terminal:

```bash
sudo apt install r-base
```

Command ini akan menginstall R beserta dependencies yang diperlukan.

**Verifikasi Instalasi:**
```bash
R --version
```

### Menjalankan R Console

Untuk masuk ke R interactive console, ketik:

```bash
R
```

Setelah masuk, kamu akan lihat R prompt (`>`). Di sini kamu bisa langsung eksekusi R commands.

**Keluar dari R Console:**

```r
q()
```

Atau bisa juga:

```r
quit()
```

Saat keluar, R akan tanya apakah mau save workspace. Pilih sesuai kebutuhan:
- `y` (yes) untuk save
- `n` (no) untuk tidak save
- `c` (cancel) untuk batal keluar

### Menjalankan R Script

Jika kamu punya file R script (`.r` atau `.R`), jalankan dengan command:

```bash
Rscript namafile.r
```

**Contoh:**
```bash
Rscript analysis.r
```

---

## Dasar-Dasar R Programming

### Operasi Matematika Dasar

R bisa digunakan langsung sebagai calculator.

**Mencari Akar Kuadrat dengan sqrt():**

```r
# Mencari akar dari 9
sqrt(9)  # Output: 3

# Mencari akar dari 16
sqrt(16)  # Output: 4

# Mencari akar dari 2
sqrt(2)  # Output: 1.414214
```

**Operasi Matematika Lainnya:**

```r
# Penjumlahan
5 + 3  # Output: 8

# Pengurangan
10 - 4  # Output: 6

# Perkalian
6 * 7  # Output: 42

# Pembagian
20 / 4  # Output: 5

# Perpangkatan
2^3  # Output: 8

# Modulo (sisa pembagian)
10 %% 3  # Output: 1
```

### Membuat Array/Vector

Di R, array atau vector dibuat menggunakan function `c()` (combine).

```r
# Membuat vector berisi angka 2 sampai 15
x <- c(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

# Membuat vector dengan angka negatif dan positif
y <- c(-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8)

# Membuat vector dengan decimal
z <- c(1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0)

# Membuat vector dengan nilai tertentu
p <- c(3, 7, 8, 15)

# Membuat vector dengan nilai berulang
q <- rep(9, times = 6)  # Mengulang angka 9 sebanyak 6 kali

# Menampilkan isi vector q
print(q)  # Output: 9 9 9 9 9 9
```

**Penjelasan:**
- `c()` adalah function untuk combine (menggabungkan) nilai menjadi vector
- `rep()` untuk repeat (mengulang) nilai tertentu
- `<-` adalah operator assignment di R (sama seperti `=`)

**Tips:** Di R, lebih umum pakai `<-` daripada `=` untuk assignment.

### Membuat Data Frame

Data frame adalah struktur data 2 dimensi mirip tabel di Excel. Ini adalah struktur data yang paling sering dipakai untuk analisis.

**Contoh Simple:**

```r
# Membuat data frame dengan kolom "nama" dan "usia"
dataframe <- data.frame(
  nama = c("Andi", "Budi", "Cindy", "Dini"),
  usia = c(25, 30, 27, 24)
)

# Menampilkan isi data frame
print(dataframe)
```

**Output:**
```
   nama usia
1  Andi   25
2  Budi   30
3 Cindy   27
4  Dini   24
```

**Contoh Lebih Kompleks:**

```r
# Membuat variabel terpisah
jurusan <- c("Komputer", "Fisika", "Komputer", "Fisika", "Komputer", "Fisika", "Komputer", "Fisika")
asal_daerah <- c("Bogor", "Bogor", "Bandung", "Bandung", "Bogor", "Bogor", "Bandung", "Bandung")
usia <- c(25, 25, 25, 25, 26, 26, 26, 26)

# Menggabungkan variabel menjadi data frame
df <- data.frame(jurusan, asal_daerah, usia)

# Menampilkan data frame
print(df)
```

**Mengakses Data Frame:**

```r
# Melihat struktur data frame
str(df)

# Melihat 6 baris pertama
head(df)

# Melihat 6 baris terakhir
tail(df)

# Mengakses kolom tertentu
df$jurusan
df$usia

# Mengakses baris tertentu
df[1, ]  # Baris pertama

# Mengakses sel tertentu
df[1, 2]  # Baris 1, kolom 2
```

### Membuat Matriks

Matriks adalah struktur data 2 dimensi dengan tipe data yang sama di semua elemen.

```r
# Membuat matriks A (3 baris x 4 kolom)
A <- matrix(
  c(7, 8, 9, 10, 11, 12, 13, 14, 14, 16, 17, 18), 
  nrow = 3, 
  ncol = 4, 
  byrow = TRUE
)

# Membuat matriks B (4 baris x 2 kolom)
B <- matrix(
  c(10, 14, 11, 15, 12, 16, 13, 17), 
  nrow = 4, 
  ncol = 2, 
  byrow = TRUE
)

# Menampilkan kedua matriks
print(A)
print(B)
```

**Penjelasan Parameter:**
- `nrow`: Jumlah baris
- `ncol`: Jumlah kolom
- `byrow = TRUE`: Isi matriks per baris (default adalah per kolom)

**Matriks A akan terlihat seperti:**
```
     [,1] [,2] [,3] [,4]
[1,]    7    8    9   10
[2,]   11   12   13   14
[3,]   14   16   17   18
```

### Membuat Tabel

Tabel bisa dibuat dengan data frame yang punya row names.

**Contoh Tabel Quarter:**

```r
# Membuat tabel dengan data per quarter
quarter <- data.frame(
  Qtr1 = c(-11, -7, -3, 1, 5, 9),
  Qtr2 = c(-10, -6, -2, 2, 6, 10),
  Qtr3 = c(-9, -5, -1, 3, 7, 11),
  Qtr4 = c(-8, -4, 0, 4, 8, " "),
  row.names = c(2010:2015)  # Row names harus di akhir
)

# Menampilkan tabel
print(quarter)
```

**Output:**
```
     Qtr1 Qtr2 Qtr3 Qtr4
2010  -11  -10   -9   -8
2011   -7   -6   -5   -4
2012   -3   -2   -1    0
2013    1    2    3    4
2014    5    6    7    8
2015    9   10   11     
```

**Visualisasi Tabel:**

| Tahun | Qtr1 | Qtr2 | Qtr3 | Qtr4 |
|-------|------|------|------|------|
| 2010  | -11  | -10  | -9   | -8   |
| 2011  | -7   | -6   | -5   | -4   |
| 2012  | -3   | -2   | -1   | 0    |
| 2013  | 1    | 2    | 3    | 4    |
| 2014  | 5    | 6    | 7    | 8    |
| 2015  | 9    | 10   | 11   |      |

**Contoh Tabel Data Bulanan:**

```r
# Membuat kolom untuk setiap bulan
Jan <- c("", 21)
Feb <- c(10, 22)
Mar <- c(11, 23)
Apr <- c(12, 24)
May <- c(13, 25)
Jun <- c(14, 26)
Jul <- c(15, 27)
Aug <- c(16, 28)
Sep <- c(17, 29)
Oct <- c(18, 30)
Nov <- c(19, "")
Dec <- c(20, "")

# Menggabungkan menjadi data frame
dataset <- data.frame(Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec)

# Memberikan label baris
rownames(dataset) <- c("2020", "2021")

# Menampilkan ke terminal
print(dataset)
```

---

## Mengelola Environment

### Mencari Object dengan ls()

Function `ls()` digunakan untuk melihat semua object (variabel, function, dll) yang ada di environment R saat ini.

**Basic Usage:**

```r
# Melihat semua object
ls()
```

**Mencari Object dengan Pattern:**

```r
# Mencari object yang mengandung huruf "y"
ls(pat = "y")
```

**Penjelasan:**
- `ls()` akan menampilkan list semua object yang sudah kita buat
- Parameter `pat = "y"` untuk mencari object yang namanya mengandung huruf "y"
- Ini sangat berguna untuk cek apakah nama variabel sudah dipakai atau belum

**Contoh Output:**

Jika kita punya variabel `x`, `y`, `data`, dan `my_data`, maka:

```r
ls()  # Output: "data" "my_data" "x" "y"

ls(pat = "y")  # Output: "my_data" "y"
```

**Menghapus Object:**

```r
# Hapus satu object
rm(x)

# Hapus beberapa object
rm(x, y, z)

# Hapus semua object
rm(list = ls())
```

### Mengatur Working Directory

Working directory adalah folder dimana R akan mencari dan menyimpan file.

**Masalah Umum dengan Backslash:**

```r
# SALAH - akan error
setwd("C:\B")

# BENAR - pakai double backslash
setwd("C:\\B")

# ATAU pakai forward slash (lebih simple)
setwd("C:/B")
```

**Penjelasan:**
- Di R, `\` adalah escape character (punya makna khusus)
- Untuk represent backslash literal, harus pakai `\\`
- Lebih simple pakai `/` yang langsung bisa dibaca

**Working Directory di Linux:**

```r
# Pindah ke folder home
setwd("/home/yukina")

# Lihat file dan folder di directory saat ini
list.files()

# Atau pakai
dir()
```

**Function Berguna untuk Directory:**

```r
# Lihat working directory saat ini
getwd()

# Cek apakah file/folder ada
file.exists("data.csv")

# Buat folder baru
dir.create("new_folder")
```

---

## Operasi Matriks

### Perkalian Matriks

Ada beberapa jenis perkalian di R:

**Element-wise Multiplication (Perkalian Per Element):**

```r
A <- matrix(c(1, 2, 3, 4), nrow = 2)
B <- matrix(c(5, 6, 7, 8), nrow = 2)

# Perkalian element-wise
C <- A * B
```

**Matrix Multiplication (Perkalian Matriks):**

```r
# Deklarasi matriks M
M <- matrix(
  c(9, 2, 8, 3, 0, 10, 7, 6, 0, 0, 10, 9, 0, 0, 0, 12), 
  nrow = 4, 
  ncol = 4, 
  byrow = TRUE
)

# Deklarasi matriks identitas I
I <- matrix(
  c(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1), 
  nrow = 4, 
  ncol = 4, 
  byrow = TRUE
)

# Perkalian matriks (matrix multiplication)
hasil <- M %*% I

# Tampilkan hasil
print(hasil)
```

**Penjelasan:**
- `*` untuk perkalian element-wise
- `%*%` untuk perkalian matriks (matrix multiplication)
- Perkalian matriks dengan identitas akan menghasilkan matriks yang sama

### Transpose Matriks

Transpose menukar baris menjadi kolom dan sebaliknya.

```r
# Deklarasi matriks M
M <- matrix(
  c(9, 2, 8, 3, 0, 10, 7, 6, 0, 0, 10, 9, 0, 0, 0, 12), 
  nrow = 4, 
  ncol = 4, 
  byrow = TRUE
)

# Transpose matriks
hasil <- t(M)

# Tampilkan hasil
print(hasil)
```

**Contoh:**

Matriks awal:
```
     [,1] [,2] [,3] [,4]
[1,]    9    2    8    3
[2,]    0   10    7    6
[3,]    0    0   10    9
[4,]    0    0    0   12
```

Setelah transpose:
```
     [,1] [,2] [,3] [,4]
[1,]    9    0    0    0
[2,]    2   10    0    0
[3,]    8    7   10    0
[4,]    3    6    9   12
```

### Inverse Matriks

Inverse matriks adalah kebalikan dari matriks. Jika matriks A dikalikan dengan inverse-nya, hasilnya adalah matriks identitas.

```r
# Deklarasi matriks M
M <- matrix(
  c(9, 2, 8, 3, 0, 10, 7, 6, 0, 0, 10, 9, 0, 0, 0, 12), 
  nrow = 4, 
  ncol = 4, 
  byrow = TRUE
)

# Mencari inverse matriks
hasil <- solve(M)

# Tampilkan hasil
print(hasil)
```

**Catatan:**
- Tidak semua matriks punya inverse
- Matriks harus square (jumlah baris = jumlah kolom)
- Determinant matriks harus tidak nol

**Verifikasi:**

```r
# M * inverse(M) harus menghasilkan matriks identitas
verifikasi <- M %*% hasil
print(round(verifikasi, 10))  # Round untuk menghilangkan floating point error
```

### Penjumlahan Matriks

```r
# Deklarasi matriks N
N <- matrix(c(2, 1, 8, 6, 7, 2), nrow = 2, byrow = TRUE)

# Deklarasi matriks E
E <- matrix(c(0, 0, 0, 0, 6, 3), nrow = 2, byrow = TRUE)

# Penjumlahan matriks
N4 <- N + E

# Tampilkan hasil
print(N4)
```

**Operasi Matriks Lainnya:**

```r
# Pengurangan
hasil <- N - E

# Perkalian dengan scalar
hasil <- 2 * N

# Pembagian element-wise
hasil <- N / E
```

---

## Loop dan Percabangan

### For Loop

For loop digunakan untuk melakukan iterasi sejumlah tertentu.

**Basic For Loop:**

```r
# Loop dari 1 sampai 30
for (i in 1:30) {
  print(i)
}
```

**Penjelasan:**
- `i` adalah iteration counter atau loop variable
- `1:30` membuat sequence dari 1 sampai 30
- Setiap iterasi, nilai `i` akan berubah dari 1, 2, 3, ... sampai 30

**Loop dengan Vector:**

```r
# Loop melalui vector
buah <- c("apel", "jeruk", "mangga", "pisang")

for (item in buah) {
  print(paste("Saya suka", item))
}
```

**Contoh: Mencari Nilai Genap:**

```r
# Inisialisasi vector kosong
nilai_genap <- c()

# Loop untuk mencari nilai genap
for (i in 1:10) {
  if (i %% 2 == 0) {
    nilai_genap <- c(nilai_genap, i)
  }
}

# Tampilkan hasil
print(nilai_genap)  # Output: 2 4 6 8 10
```

**Penjelasan:**
- `i %% 2` adalah modulo (sisa pembagian)
- Jika sisa pembagian dengan 2 adalah 0, berarti bilangan genap
- `c(nilai_genap, i)` menambahkan `i` ke vector `nilai_genap`

### While Loop

While loop akan terus berjalan selama kondisi terpenuhi.

```r
# Inisialisasi variabel
sum <- 0

# While loop dengan nested for loop
while (TRUE) {
  for (i in 1:10) {
    sum <- sum + i
  }
  
  # Break jika sum >= 110
  if (sum >= 110) {
    break
  }
}

# Tampilkan hasil
print(sum)  # Output: 110
```

**Penjelasan:**
- `while (TRUE)` membuat infinite loop
- `break` untuk keluar dari loop
- Loop ini akan:
  1. Jalankan for loop yang menambah 1+2+3+...+10 = 55
  2. Cek apakah sum >= 110
  3. Jika belum, ulangi lagi
  4. Setelah 2x iterasi (55 + 55 = 110), loop berhenti

**While Loop dengan Counter:**

```r
count <- 1

while (count <= 5) {
  print(paste("Iterasi ke", count))
  count <- count + 1
}
```

### Conditional Statement

```r
# If statement
x <- 10

if (x > 5) {
  print("x lebih besar dari 5")
}

# If-else
if (x %% 2 == 0) {
  print("x adalah bilangan genap")
} else {
  print("x adalah bilangan ganjil")
}

# If-else if-else
nilai <- 85

if (nilai >= 90) {
  print("Grade: A")
} else if (nilai >= 80) {
  print("Grade: B")
} else if (nilai >= 70) {
  print("Grade: C")
} else {
  print("Grade: D")
}
```

---

## Visualisasi Data

### Membuat Layout Plot

Layout berguna untuk menampilkan beberapa plot dalam satu window.

```r
# Membuat layout dengan ukuran berbeda
layout(
  matrix(c(1, 2, 2, 3, 3, 4), nrow = 3, ncol = 2), 
  heights = c(1, 2)
)

# Menampilkan layout (untuk preview)
layout.show(4)
```

**Penjelasan:**
- `matrix(c(1, 2, 2, 3, 3, 4), nrow = 3, ncol = 2)` mendefinisikan posisi plot
- Angka 1, 2, 3, 4 adalah nomor plot
- Plot 2 dan 3 akan lebih besar karena mengambil 2 cell
- `heights = c(1, 2)` mengatur tinggi relatif setiap baris

**Contoh Penggunaan dengan Plot:**

```r
# Setup layout
layout(matrix(c(1, 2, 2, 3, 3, 4), nrow = 3, ncol = 2))

# Plot 1
plot(1:10, main = "Plot 1")

# Plot 2
plot(1:20, main = "Plot 2")

# Plot 3
plot(1:30, main = "Plot 3")

# Plot 4
plot(1:15, main = "Plot 4")
```

### Sunflower Plot

Sunflower plot berguna untuk visualisasi data yang memiliki many overlapping points.

```r
# Data contoh
x <- c(2, 1, 2, 4, 1, 2, 3, 4, 2, 3, 1)
y <- c(4, 3, 4, 4, 3, 4, 5, 4, 4, 5, 3)

# Membuat sunflower plot
sunflowerplot(
  x,
  y,
  main = "Diskusi 5",
  xlab = "X",
  ylab = "Y"
)
```

**Penjelasan:**
- Sunflower plot menampilkan "kelopak" pada titik yang overlap
- Semakin banyak kelopak, semakin banyak data point di posisi tersebut
- Berguna saat ada banyak data dengan nilai yang sama

### Scatter Plot

Scatter plot untuk melihat hubungan antara 2 variabel.

**Basic Scatter Plot:**

```r
# Data contoh: Kecepatan dan Jarak
jarak <- c(2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26, 54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85)

kecepatan <- c(4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23)

# Membuat scatter plot
plot(
  jarak, 
  kecepatan,
  main = "Scatter Plot: Kecepatan vs Jarak",
  xlab = "Jarak (meter)",
  ylab = "Kecepatan (km/h)",
  pch = 19,  # Bentuk titik (filled circle)
  col = "blue"  # Warna titik
)
```

**Parameter Plot yang Berguna:**

```r
# pch - Bentuk titik
# 1: circle, 16: filled circle, 19: solid circle
# 2: triangle, 3: plus, 4: cross

# col - Warna
# "red", "blue", "green", dll
# Atau pakai hex: "#FF0000"

# cex - Ukuran titik
# Default = 1, lebih besar = titik lebih besar
```

### Regresi Linear

Menambahkan garis tren (regression line) pada scatter plot.

```r
# Data (sama seperti contoh sebelumnya)
jarak <- c(2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26, 54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85)

kecepatan <- c(4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23)

# Membuat scatter plot
plot(
  jarak, 
  kecepatan,
  main = "Scatter Plot dengan Regresi Linear",
  xlab = "Jarak (meter)",
  ylab = "Kecepatan (km/h)",
  pch = 19,
  col = "blue"
)

# Membuat model regresi linear
model <- lm(kecepatan ~ jarak)

# Menambahkan garis regresi ke plot
abline(model, col = "red", lwd = 2)

# Melihat summary model
summary(model)
```

**Penjelasan:**
- `lm()` membuat linear model (regresi linear)
- Formula `kecepatan ~ jarak` artinya: kecepatan sebagai fungsi dari jarak
- `abline()` menambahkan garis ke plot
- `lwd` adalah line width (ketebalan garis)

**Informasi dari Summary:**

```r
# Melihat coefficients (intercept dan slope)
coefficients(model)

# Melihat R-squared (seberapa baik model fit)
summary(model)$r.squared

# Prediksi nilai baru
predict(model, data.frame(jarak = 50))
```

### Histogram

Histogram untuk melihat distribusi frekuensi data.

```r
# Data kecepatan
kecepatan <- c(4, 4, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 20, 20, 21, 22, 23, 24, 24, 24, 25, 25)

# Membuat histogram
hist(
  kecepatan,
  main = "Histogram Kecepatan Mobil",
  xlab = "Kecepatan (km/h)",
  ylab = "Frekuensi",
  col = "blue",
  border = "black",
  breaks = 10  # Jumlah bins/kelas
)
```

**Parameter Histogram:**

```r
# breaks - Jumlah atau posisi bins
breaks = 10  # 10 bins
breaks = seq(0, 30, by = 5)  # Custom bins

# freq - Frekuensi atau density
freq = TRUE  # Menampilkan frekuensi (default)
freq = FALSE  # Menampilkan density

# Menambahkan density curve
hist(kecepatan, freq = FALSE, col = "lightblue")
lines(density(kecepatan), col = "red", lwd = 2)
```

### Distribusi Normal

Membuat plot distribusi normal standar.

```r
# Membuat sequence dari -1 sampai 1 dengan 100 titik
x <- seq(-1, 1, length.out = 100)

# Menghitung density distribusi normal untuk setiap nilai x
y <- dnorm(x)

# Parameter distribusi
mu <- 0      # Mean
sigma <- 1   # Standard deviation

# Mengatur margin plot
par(mar = c(12, 4, 12, 2))  # (bottom, left, top, right)

# Membuat plot
plot(
  x, 
  y, 
  type = "l",  # Line plot
  lwd = 2,     # Line width
  col = "gray",
  xlab = "", 
  ylab = "Kepadatan",
  main = bquote("Fungsi Kepadatan Distribusi Normal Standar, " ~ mu == .(mu) ~ ", " ~ sigma == .(sigma))
)
```

**Penjelasan:**
- `dnorm()` adalah density function untuk distribusi normal
- `type = "l"` membuat line plot
- `bquote()` untuk menampilkan formula matematika dengan nilai variabel

**Variasi Distribusi Normal:**

```r
# Distribusi normal dengan parameter berbeda
x <- seq(-5, 5, length.out = 200)

# Normal(0, 1) - Standar
y1 <- dnorm(x, mean = 0, sd = 1)

# Normal(0, 2)
y2 <- dnorm(x, mean = 0, sd = 2)

# Normal(2, 1)
y3 <- dnorm(x, mean = 2, sd = 1)

# Plot multiple curves
plot(x, y1, type = "l", col = "blue", lwd = 2, ylab = "Density")
lines(x, y2, col = "red", lwd = 2)
lines(x, y3, col = "green", lwd = 2)

legend("topright", 
       legend = c("N(0,1)", "N(0,2)", "N(2,1)"),
       col = c("blue", "red", "green"),
       lwd = 2)
```

---

## Import dan Export Data

### Membaca File Text

**Menggunakan scan():**

```r
# Membaca data dari file text
scanMatriks <- scan("data2.txt")

# Mengubah menjadi matriks
hasil <- matrix(scanMatriks, nrow = 4, ncol = 10, byrow = TRUE)

# Menampilkan hasil
print(hasil)
```

**Penjelasan:**
- `scan()` membaca data numerik dari file text
- Data harus dipisah dengan whitespace (spasi, tab, newline)
- Setelah dibaca, data bisa diubah menjadi matriks atau struktur lain

**Menggunakan read.table():**

```r
# Membaca file dengan header
data <- read.table("data.txt", header = TRUE)

# Membaca file tanpa header
data <- read.table("data.txt", header = FALSE)

# Membaca dengan separator tertentu
data <- read.table("data.txt", sep = ",")
```

### Membaca File CSV

CSV (Comma-Separated Values) adalah format file yang paling umum untuk data.

```r
# Membaca file CSV dengan header
data <- read.csv("penjualan.csv", header = TRUE)

# Melihat data di viewer (RStudio)
View(data)

# Menampilkan di console
print(data)

# Melihat beberapa baris pertama
head(data)

# Melihat struktur data
str(data)

# Summary statistik
summary(data)
```

**Export ke CSV:**

```r
# Membuat data frame
df <- data.frame(
  nama = c("Andi", "Budi", "Citra"),
  nilai = c(85, 90, 88)
)

# Export ke CSV
write.csv(df, "hasil.csv", row.names = FALSE)
```

**Tips untuk CSV:**

```r
# Jika ada masalah dengan separator
data <- read.csv("file.csv", sep = ";")  # Untuk separator titik koma

# Jika ada masalah dengan decimal
data <- read.csv("file.csv", dec = ",")  # Untuk decimal koma

# Skip beberapa baris awal
data <- read.csv("file.csv", skip = 2)

# Hanya baca beberapa baris
data <- read.csv("file.csv", nrows = 100)
```

---

## Statistik Deskriptif

### Mean (Rata-rata)

Mean adalah nilai rata-rata dari data.

**Cara Manual:**

```r
# Data kecepatan
kecepatan <- c(4, 4, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 20, 20, 21, 22, 23, 24, 24, 24, 25, 25)

# Hitung jumlah data
banyak <- length(kecepatan)

# Hitung mean secara manual
mean_manual <- sum(kecepatan) / banyak
print(mean_manual)
```

**Menggunakan Function mean():**

```r
# Lebih simple pakai function
mean_kecepatan <- mean(kecepatan)
print(mean_kecepatan)

# Output: 15.22
```

**Mean dengan NA (Missing Values):**

```r
# Data dengan NA
data <- c(5, 10, NA, 15, 20)

# Mean tanpa handling NA akan return NA
mean(data)  # Output: NA

# Mean dengan remove NA
mean(data, na.rm = TRUE)  # Output: 12.5
```

### Median (Nilai Tengah)

Median adalah nilai tengah saat data diurutkan.

```r
# Data kecepatan (sama seperti sebelumnya)
kecepatan <- c(4, 4, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 20, 20, 21, 22, 23, 24, 24, 24, 25, 25)

# Hitung median
median_kecepatan <- median(kecepatan)
print(median_kecepatan)

# Output: 16
```

**Penjelasan:**
- Jika jumlah data ganjil, median adalah nilai tengah
- Jika jumlah data genap, median adalah rata-rata dari 2 nilai tengah

**Perbandingan Mean vs Median:**

```r
# Data dengan outlier
data <- c(1, 2, 3, 4, 5, 100)

mean(data)    # 19.17 (terpengaruh outlier)
median(data)  # 3.5 (tidak terpengaruh outlier)
```

### Standard Deviation

Standard deviation (simpangan baku) mengukur sebaran data.

```r
# Data kecepatan
kecepatan <- c(4, 4, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 20, 20, 21, 22, 23, 24, 24, 24, 25, 25)

# Hitung standard deviation
sd_kecepatan <- sd(kecepatan)
print(sd_kecepatan)

# Output: 5.287644
```

**Interpretasi:**
- SD kecil = data cenderung dekat dengan mean
- SD besar = data lebih tersebar

**Variance (Varians):**

```r
# Variance adalah SD kuadrat
var_kecepatan <- var(kecepatan)
print(var_kecepatan)

# Atau
var_kecepatan <- sd_kecepatan^2
```

### Coefficient of Variation

Coefficient of Variation (CV) adalah ukuran variabilitas relatif.

```r
# Data untuk ujian Matematika
nilai_matematika_fatoni <- 90
mean_matematika <- 65
sd_matematika <- 10

# Data untuk ujian Bahasa Inggris
nilai_inggris_fatoni <- 45
mean_inggris <- 70
sd_inggris <- 8

# Rumus CV: (SD / Mean) * 100%
cv_matematika <- (sd_matematika / mean_matematika) * 100
cv_inggris <- (sd_inggris / mean_inggris) * 100

# Menampilkan hasil
print(paste("Koefisien keragaman untuk Matematika:", cv_matematika, "%"))
print(paste("Koefisien keragaman untuk Bahasa Inggris:", cv_inggris, "%"))
```

**Output:**
```
[1] "Koefisien keragaman untuk Matematika: 15.3846153846154 %"
[1] "Koefisien keragaman untuk Bahasa Inggris: 11.4285714285714 %"
```

**Interpretasi:**
- CV Matematika (15.38%) > CV Inggris (11.43%)
- Artinya: nilai matematika lebih bervariasi dibanding nilai bahasa Inggris
- Walaupun nilai Fatoni di matematika (90) lebih tinggi dari mean, variabilitasnya juga lebih tinggi

**Menggunakan Function:**

```r
# Function untuk hitung CV
cv <- function(data) {
  return((sd(data) / mean(data)) * 100)
}

# Contoh penggunaan
data <- c(10, 12, 14, 16, 18, 20)
cv(data)
```

---

## Latihan dan Referensi

### Latihan Praktik

Untuk memperdalam pemahaman R, kamu bisa coba latihan-latihan berikut:

**1. R untuk Data Analisis:**
Lihat: [Latihan Bahasa R](../latihan/R-analisis.md)

**2. Latihan Dasar R:**
Lihat: [Latihan bahasa R](./latihan-bahasa/latihan-r.md)

**3. Catatan Tambahan:**
Lihat: [Catatan tambahan R](../latihan/note-r.md)

### Referensi Berguna

**Official Documentation:**
- [R Official Website](https://www.r-project.org/)
- [CRAN (Comprehensive R Archive Network)](https://cran.r-project.org/)
- [R Documentation](https://www.rdocumentation.org/)

**Tutorial dan Learning:**
- [R for Data Science (Free Book)](https://r4ds.had.co.nz/)
- [DataCamp R Tutorial](https://www.datacamp.com/courses/free-introduction-to-r)
- [Coursera R Programming](https://www.coursera.org/learn/r-programming)

**Specific Topics:**
- [Calculate Square Root in R](https://www.geeksforgeeks.org/calculate-square-root-of-a-number-in-r-language-sqrt-function/)
- [Matrix Operations in R](https://www.datamentor.io/r-programming/matrix/)
- [Data Visualization with R](https://r-graph-gallery.com/)

### Tips Belajar R

**1. Mulai dengan Basic:**
- Kuasai dulu tipe data dasar (vector, matrix, data frame)
- Pahami cara import/export data
- Latihan operasi dasar

**2. Practice dengan Real Data:**
- Download dataset dari Kaggle atau UCI Machine Learning Repository
- Coba analisis data sendiri
- Buat visualisasi yang menarik

**3. Gunakan RStudio:**
- RStudio adalah IDE terbaik untuk R
- Punya fitur autocomplete, syntax highlighting, dan debugging
- Download gratis di [rstudio.com](https://www.rstudio.com/)

**4. Eksplor Packages:**
- `ggplot2` untuk visualisasi advanced
- `dplyr` untuk data manipulation
- `tidyr` untuk data cleaning
- `caret` untuk machine learning

**5. Join Community:**
- [Stack Overflow R Tag](https://stackoverflow.com/questions/tagged/r)
- [R-bloggers](https://www.r-bloggers.com/)
- [RStudio Community](https://community.rstudio.com/)

### Cheat Sheets

**Data Types:**
```r
# Numeric
x <- 42
class(x)  # "numeric"

# Character
y <- "hello"
class(y)  # "character"

# Logical
z <- TRUE
class(z)  # "logical"

# Factor
f <- factor(c("low", "medium", "high"))
class(f)  # "factor"
```

**Useful Functions:**
```r
# Data exploration
head(data)      # First 6 rows
tail(data)      # Last 6 rows
str(data)       # Structure
summary(data)   # Summary statistics
dim(data)       # Dimensions
names(data)     # Column names

# Data cleaning
na.omit(data)   # Remove NA
is.na(data)     # Check NA
unique(data)    # Unique values
duplicated(data) # Check duplicates
```

