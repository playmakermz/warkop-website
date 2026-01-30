# Kumpulan latihan Javascript

Kerjakan latihan-latihan dibawah ini mengunakan bahasa pemrograman Javascript.

## Contoh pengerjaan latihan 

Latihan untuk menampilkan if condition, berdasarkan value yang ada. 

Tugas:
- Buat variabel bernama stokBuah yang berisi integer "10"
- Buat If statement yang dimana jika stokBuah lebih dari 15, tampilkan(print) "Buah masih banyak"
- lanjutan dari If statement, jika stokBuah kurang dari 15, maka tampilkan "Buah tersisa sedikit"

Output yang diharapkan:
```html
buah tersisa sedikit
```

Cara pengerjaan:
- Buka text editor
- Kerjakan tahapan yang ada dengan bahasa program javascript
- setelah program telah selesai ditulis
- jalankan program javascript
- pastikan Output dari terminal javascript, sesuai dengan "Output yang diharapkkan" dari tugas yang ada

Contoh code:
```r
let stokBuah = 10

if(stokBuah > 15){
    console.log("Buah masih banyak)
}
else if(stokBuah < 15){
    console.log("Buah tersisa sedikit)
} 
```

Ingat untuk pastikan hasil output dari terminal harus sesuai dengan "Output yang diharapkkan"

***
## Latihan Pertama 
***
Adalah latihan untuk melakukan akses data dari array dan juga melakukan modifikasi pada data yang ada.

Selesaikan setiap tahapan yang ada dibawah ini!

Tugas:

- Buat array bernama buah yang berisi "Apel", "Mangga", "Pisang", "Jeruk".

- Tampilkan array buah.

- Tampilkan elemen pertama dan ketiga.

- Ubah elemen kedua menjadi "Anggur".

- Tambahkan "Semangka" ke akhir array.

- Tampilkan array buah.

Output yang diharapkan:
```r
[ 'Apel', 'Mangga', 'Pisang', 'Jeruk' ]
Apel
Pisang
[ 'Apel', 'Anggur', 'Pisang', 'Jeruk', 'Semangka' ]
```

***
## Latihan ke 2
***
Tujuan: Melatih pemahaman array loop

Tugas:
- gunakan Loop array buah pada latihan pertama dan tampilkan sertiap elemen yang ada.
- Buat loop baru, gunakan `forEach` untuk menampilkan index elemen dan nilai elemen.

Output yang diharapkan:
```r
Indeks 0: Apel
Indeks 1: Mangga
Indeks 2: Pisang
Indeks 3: Jeruk
Indeks 0: Apel
Indeks 1: Mangga
Indeks 2: Pisang
Indeks 3: Jeruk

```

***
## Latihan ke 3
***

Tujuan: Melatihan pemahaman mengenai array Map dan array filter

Tugas:
- Buat array `angka` dengan nilai [1,3,5,7,9]
- Gunakan method `map()` untuk membuat array baru yang berisi setiap elemen dikali 3
- berdasarkan array baru, gunakan method `filter()` untuk membuat array baru yang hanya berisi elemen dengan nilai lebih besar dari 10


Output yang diharapkan:
```r
Hasil map:  [ 3, 9, 15, 21, 27 ]
Hasil filter:  [ 15, 21, 27 ]
```


***
## Latihan ke 4
***

Tujuan: Melatih pemahaman didalam menganalisa sebuah array

Tugas:
- Buat array dengan nama "buah" yang berisi "Apel", "Pisang", "Jeruk"
- Buat algoritma yang akan menganilisa array "buah" untuk mencari elemen dengan value "Pisang". Jika ada elemen "Pisang" tampilkan pada indeks keberapa elemen tersebut berada
- Buat algoritma yang akan menganilisa array "buah" untuk mencari elemen dengan value "Semangka". Tampilkan "Semangka tidak ada" jika element tersebut tidak ada pada array

Output yang diharapkan:
```r
Elemen dengan value pisang berada pada index ke : 1
Semangka tidak ada
```
