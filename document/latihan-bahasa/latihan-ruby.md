# Latihan ruby

## Contoh latihan 

Tugas: buat program Ruby dengan fungsi Konversi menit ke detik, data harus berasal dari input terminal

Contoh input:
```r
1
2
```

contoh output:
```r
60
120
```

Cara pengerjaan:
- Buat algoritma pemecahan masalah
- coba masukan integer sesuai dengan contoh input
- pastikan nilai jika nilai input dan output sama dengan contoh

contoh code
```ruby
print "Masukkan menit: "
menit = gets.chomp.to_i  # Konversi ke integer

print menit * 60
```

## Latihan 1

adalah latihan untuk kemampuan dasar algoritma

Tugas: 
- Konversi jam ke detik
- data harus data harus berasal dari input terminal

contoh input:
```ruby
1
2
```

contoh output:
```ruby
3600
7200
```

## Latihan 2

Adalah latihan melakukan analisa data sederhana

Tugas:
- Buat variabel untuk menyimpan array `[1,3,4,6,3,6,1,2]`
- Buat algoritma yang dimana berfungsi untuk menentukan setiap angka itu adalah genap atau ganjil

contoh input:
```r
[1,3,4,6,3,6,1,2]
```

contoh output:
```r
ganjil
ganjil
genap
genap
ganjil
ganjil
genap
```

## Latihan 3

Latihan dasar penggunaan array

Tugas:
- Cetak angka dari 1-100 dengan menggunakan fungsi `while`

contoh input: Tidak ada input terminal

output:
```r
1
2
3
4
...
```

## latihan 4

Analisi data array 

Tugas:
- Cari elemen terbesar kedua dalam array [10,2,4,5,7]

Contoh input: Tidak ada input terminal

output: 
```r
7
```

## latihan 5

Modifikasi data array 

Tugas:
- Gunakan method `map`
- melakukan perubahan array string menjadi kapital
- data array adalah `["apple", "banana"]`

Contoh input: tidak ada input terminal 

contoh output: 
```r
["APPLE", "BANANA"]
```

## Referensi
- https://ruby-doc.org/docs/Tutorial/part_02/user_input.html [Input data ruby ke terminal]