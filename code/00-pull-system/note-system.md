# Teori dibalik ini

1. Memberikan kita jeda waktu untuk melakukan pull. Pull yang akan kita lakukan tidak akan ngawur, melainkan sesuai timing.
2. Memberikan chace kasar yang lebih tinggi untuk mendapatkan jackpot. Karena pull virtual ini, akan memberikan kita chace diluar dari game.
> Perempumaan nomor 2 adalah seperti ini: kita ingin mendapatkan dua dadu dengan angka 6. jika kita hanya melakukan 1 kali percobaan, maka chace kita adalah 1/36. jika kita melakukan 10 kali percobaan, maka chace kita adalah 10/36, lebih baik daripada 1/36.
3. intinya dengan simulasi ini, intinya "Strike when iron is hot".
4. jangan takut gagal di simulasi trial. Ambil yang menurutmu paling tinggi. kalau gagal bisa coba lagi nanti.

## Teori dasar ke dua

Bayangkan ini adalah lomba lempar dadu untuk mendapatkan angka 6. ada dua dadu: dadu pertama berbentuk lacip dan kotak sempurna, dadu kedua bentuknya lebih halus pada setiap sisinya.
simulasi kita ibaratkan sebagai dadu halus, sedangkan real adalah dadu lancip. tentu ada perbedaan pada permukaan dadu, yang memungkinkan mereka tidak berjalan sepenuhnya sama 100%.
Tetapi yang paling penting disini adalah sebuah 'act' untuk mencari hasil terdekat dengan jackpot pada dadu lancip. karena dasar perbandingan antara dadu lancip dan dadu halus adalah sama-sama 1/6.
ini adalah 'act' untuk mendekati.

## Teori dalam bentuk matematika

Jawabannya: Tono jauh lebih mungkin dapat “dua angka enam”.

Budi (1 percobaan melempar 2 dadu):
Peluang dua-enam = .

Tono (10 percobaan, masing-masing melempar 2 dadu):
Peluang gagal terus dalam 10 percobaan = .
Jadi peluang minimal sekali dapat dua-enam =


1-\left(\frac{35}{36}\right)^{10}\approx 1-0{,}7545=0{,}2455 \;=\; \mathbf{24{,}55\%}.

Intuisi sederhana: satu percobaan peluangnya kecil (≈2,78%). Dengan 10 percobaan independen, kesempatan “minimal sekali berhasil” naik jadi ≈24,6%. Per percobaan tetap sama sulitnya, tapi banyak percobaan meningkatkan peluang kumulatif.


## Mengenai waktu kapan pull

Pada teori probabilitas, kapan dilakukan pull tidak akan berpengaruh, karena semua total pull yang akan kita lakkukan dihitunga jadi satu.
Semisal kita melempar dua dadu pada hari senin, dan hari selasa, maka total percobaan yang kita lakukan adalah 2 kali.


###  Catatan Pull 

0. Mengubah Persen ke desimal: 0.50% / 100 = 0,0050

Cara penggunaan:
1. modif Probability dan variabel lainnya.
2. lakukan auto pull
3. lakukan manual pull berkali-kali, ikuti note disetiap game. (HSR, untuk setiap 250 pull simulasi == 1 realword)
4. lakukan real world pull

Cara Penggunaan V2:
1. Ubah Probabilitas ke desimal. Contoh: 0.50% jadi 0.50 / 100 = 0,0050
2. Modifikasi Probabilitas dan variabel
3. Auto pull
4. Manual pull pertama. Jika gagal, lakukan insert pull lalu Manual pull ( ulangi 1-4 kali. lalu reset simulasi )
5. Jangan tergoda dengan 10 pull Real World.



*Hati-hati terkadang ampas itu menyertai simulasi. Untuk HSR gunakan simulasi satu hari satu kali

### pendekatan 

## pendekatan 1

1. Lakukan simulasi sampai hit "Waktu Real world"
2. Real world pull
3. Nilai sembarang untuk insert simulasi pull
4. lakukan step 2-3 hingga 3 atau 4 kali


## Pendekatan 2

1. Lakukan simulasi sampai hit "waktu Real World"
2. Real world pull
3. Reset dan mulai tahapan 1-2 dari awal lagi.

# Informasi Fast Pull

Fast pull ini adalah simulasi pull yang dilakukan dalam satu kali perulangan. Semisal kita melakukan 100 pull dalam satu kali perulangan, maka kita tidak perlu melakukan 100 kali perulangan.

intinya pull dilakukan dalam bentuk batch, bukan satu per satu.
jadi atur batch size sesuai dengan kebutuhan.
semisal untuk AK batch size 100, untuk HSR batch size 600.

jangan terlalu besar ukuran batch size, karena akan membuat simulasi kurang detail. semisal nilai jackpot adalah 5000, dengan setiap batch loop adalah 1000, maka simulasi akan kurang detail.

# PGR 
```
[ PGR  ] 


#Game Name
game_name = "PGR"
# Kemungkinan beruntung!
a_probability = 0.0050
# Berapa banyak minimum percobaan
a_percobaan = 2_300
# Batch  size terkecil mau berapa
a_batchSize = 200
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 20


>>>>>>>>>>>>>>>>>> PGR Cosu

#Game Name
game_name = "PGR Cosu"
# Kemungkinan beruntung!
a_probability = 0.049
# Berapa banyak minimum percobaan
a_percobaan = 240
# Batch  size terkecil mau berapa
a_batchSize = 5
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 1

# 2 kali sukses. pity 80/100


```

# Arknight 
```
[Arknight]

> Laporan pull Ak (2% atau 0.0020):
tertinggi adalah :     10742
lakukan percobaan di : 8000

Jackpot tertinggi: 10742


>>>>>>>>>>>>> Informasi Variabel yang akan digunakan

#Game Name
game_name = "Arknights"
# Kemungkinan beruntung!
a_probability = 0.0020
# Berapa banyak minimum percobaan
a_percobaan = 4_000
# Batch  size terkecil mau berapa
a_batchSize = 300
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 10


>>>>>>>>>>>>>> Informasi jackpot didapatkan

Jackpot Real pull didapatakan saat: 5, 50, 65, 131, 132, 150+

dengan 10 kali Simulasi percobaan gagal

>>>>>>>>>>>>>> Pengalaman gacha 15 / 10 / 2025 <<<<<<<<<<<<<<<<<<<


#Game Name
game_name = "Arknights"
# Kemungkinan beruntung!
# 0.8 untuk Light Cone
# a_probability = 0.0008
a_probability = 0.0020
# Berapa banyak minimum percobaan
a_percobaan = 6_000
# Batch  size terkecil mau berapa
a_batchSize = 300
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 10
# Ini untuk memilih meotde pull
# NO : Normal speed
# MP : Multiprocess
pull_method = 'NO'

--------------- jackpot 1 -----------------
pull baru: 460

total : 9810

Tambahan: 13 ( real pull. Urutan : 1, simulasi, 1, simulasi, 10, 1 ( jackpot ) )

--------------- jackpot 2 -----------

pull baru: 410

total: 9800

tambahan : 3 real ( 1, simulai, 1 )

------------- jackpot 3 --------------

pull baru: 510

total: 9870

tambahan : 8 ( 1, simulasi, 7 )


============================== > Theory < ===========================

adalah untuk pastikan dapatkan nilai simulasi paling tinggi, minimal 9800. lalu lanjutkan dengan pull asli tanpa mempedulikan simulasi, jalankan terus pull asli tersebut tanpa simulai hingga jackpot.
```

# HSR 
```
 [ HSR ] 
> Laporan pull HSR (0.6% atau 0.0006):
Streak tertinggi adalah :    34_487 | gunakan 20_000 - 21_000
Modus Jackpot adalah 3986

Ini adalah Testing Ground untuk HSR. dimana probabilitas milik mereka adalah 0.6%.

0.006 adalah angka desimal.
kita bisa ketahui bentuk persen dengan cara.

Untuk mendapatkan character 5 Star : 0.006 x 100
gunakan 24_300 untuk mengatur jarak jackpot

Untuk mendapatkan character 4 Star : 5.100 / 100 = 0.051
gunakan 18_000 untuk mengatur jarak jackpot



Record Pull HSR 19/08/2025:
Total pull: 233461
Total jackpot: 112

>>>>>>>       Pengalaman Gacha beruntung 03/09/2025 <<<<<<<<

jackpot di HSR tgl 02/09/2025 dan 03/09/2025. Jadi trick simulasi gacha ini hanya gunakan satu kali sehari saja.

disini melakukan satu kali pull setiap ... simulasi pull:

252
252
252
252
252
252
126
357

Nilai pull baru: 13515
Total pull: 343888

>>>>>>>       Pengalaman Gacha beruntung 15/09/2025 <<<<<<<<

pull saber.

disini hanya melakukan 1 kali pull real, tanpa ada pull simulasi tambahan(Manual)

Nilai pull baru: 11490
Total pull: 33052

>>>>>>> Pengalaman 25-09-2025

Pull saber, tapi rate off.

 ============  Game Name : System 02 - HSR Scharacter Time: 06:19:25 =============

 Ini nilai percobaan : 700 , Nilai pull baru: 11500 , Total pull: 11995
 Ini nilai percobaan : 300 , Nilai pull baru: 12200 , Total pull: 12695
 Ini nilai percobaan : 200 , Nilai pull baru: 12500 , Total pull: 12995
 Ini nilai percobaan : 200 , Nilai pull baru: 12700 , Total pull: 13195
 Ini nilai percobaan : 200 , Nilai pull baru: 12900 , Total pull: 13395 ------------- ( setelah 200 selesai. 1 real dan jackpot!)
 Ini nilai percobaan : 1000 , Nilai pull baru: 13100 , Total pull: 13595
 ------> Kegagalan pada simulasi ke: 13141 , pull baru: 13141 , Total pull: 13637

 biasakan dimulai dari 700 dan 200-300 untuk setiap simulasi. jika gagal maka coba lagi selanjutnya. disetiap sela 700, 300,200,200,200 adalah 1 real world pull

>>>>>>>>>>>>>>>>>>>>>>>>> Variabel yang digunaka hsr <<<<<<<<<<<<<<<<<<<<<<<

# Kemungkinan beruntung!
# 0.8 untuk Light Cone
# a_probability = 0.0008
a_probability = 0.0006
# Berapa banyak minimum percobaan
a_percobaan = 20_000
# Batch  size terkecil mau berapa
a_batchSize = 1000
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 10



.......................... ini juga hsr

#Game Name
game_name = "System 02 - HSR Scharacter"
# Kemungkinan beruntung!
# 0.8 untuk Light Cone
# a_probability = 0.0008
a_probability = 0.0006
# Berapa banyak minimum percobaan
a_percobaan = 20_000
# Batch  size terkecil mau berapa
a_batchSize = 1000
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 60


....................... ini hsr

#Game Name
game_name = "System 02 - HSR Scharacter"
# Kemungkinan beruntung!
# 0.8 untuk Light Cone
# a_probability = 0.0008
a_probability = 0.0006
# Berapa banyak minimum percobaan
a_percobaan = 22_000
# Batch  size terkecil mau berapa
a_batchSize = 1000
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 10
# Ini untuk memilih meotde pull
# NO : Normal speed
# MP : Multiprocess
pull_method = 'NO'



# =========================================== pendekatan 24-09-2025 ===================================

Tujuan adalah gacha Evernight dengan pengeluaran paling sedikit ( 14 pull total untuk evernight ).
Disini dilakukan dua pendekatan sekaligus

# ============================ Pendekatan 24/11/2025 =========

 ============  Game Name : System 02 - HSR Scharacter Time: 18:15:45 ============= 

 ------> Kegagalan pada simulasi ke: 1646 , pull baru: 1646 , Total pull: 32847
 ------> Kegagalan pada simulasi ke: 1948 , pull baru: 1948 , Total pull: 33150
 ------> Kegagalan pada simulasi ke: 3210 , pull baru: 3210 , Total pull: 34413
 ------> Kegagalan pada simulasi ke: 3454 , pull baru: 3454 , Total pull: 34658
 ------> Kegagalan pada simulasi ke: 3855 , pull baru: 3855 , Total pull: 35060
 ------> Kegagalan pada simulasi ke: 7340 , pull baru: 7340 , Total pull: 38546
 ------> Kegagalan pada simulasi ke: 8377 , pull baru: 8377 , Total pull: 39584
 ------> Kegagalan pada simulasi ke: 9086 , pull baru: 9086 , Total pull: 40294
 ------> Kegagalan pada simulasi ke: 9106 , pull baru: 9106 , Total pull: 40315
 ------> Kegagalan pada simulasi ke: 12594 , pull baru: 12594 , Total pull: 43804
```

## pendekatan 1
- Simulasi sampai selesai
- lakukan pull 1 real
- Ulangi pendekatan 1 sebanyak 5 kali


## Pendekatan 2

1. Simulasi sampai selesai
2. 1 real pull akun utama
3. lanjutkan simulasi sebelumnya dengan 'manual insert'
4. 10-11 real pull akun cadangan
5. 1. real pull akun utama
6. jika masih belum, lanjutkan simulasi lagi
7. 1 real pull akun utama
8. jika masih belum, maka ulangi lagi nomor 6 dan 7

## Laporan praktik yang dilakukan pd 24-09-2025

1. Simulasi sampai selesai
2. 1 real pull akun utama
3. lanjutkan simulasi sebelumnya dengan 'manual insert' (700 simulasi)
4. 10-11 real pull akun cadangan
5. 1. real pull akun utama
6. jika masih belum, lanjutkan simulasi lagi ( 300 simulasi )
7. 1 real pull akun utama
8. lanjutkan lagi simulasi ( 300 simulasi )
9. 1 real pull akun utama. Jackpot!

Laporan pull simulasi:
pull Baru: 12810
Total: 13226
