![finale](https://user-images.githubusercontent.com/60807663/153804659-c633bf08-733e-4463-afc0-6f87fe477d7f.png)

## Daftar Isi
1. [Ruby](#ruby)
2. [Untuk Apa Sih Memakai Ruby Language?](#untuk-apa-sih-memakai-ruby-language)
3. [Ruby Cheat Sheet](#ruby-cheat-sheet)
4. [Ruby Install Rails](#ruby-install-rails)
5. [Ruby Basic Syntax](#ruby-basic-syntax)
6. [Variabel](#variabel)
7. [Cara Melakukan Manipulasi String](#cara-melakukan-manipulasi-string)
8. [Menulis Variabel Constants](#menulis-variabel-constants)
9. [Control Flow](#control-flow)
10. [Unless](#unless)
11. [Case](#case)
12. [Loops](#loops)
13. [While](#while)
14. [Until](#until)
15. [Loop](#loop)
16. [Next pada Loop](#next-pada-loop)
17. [Arrays](#arrays)
18. [Functions](#functions)
19. [Latihan Ruby](#latihan-ruby)

# Ruby

Ruby adalah salah satu bahasa komputer yang bisa digunakan secara cross-platform. Oleh karena itu kamu tidak perlu khawatir dengan code yang dibuat, karena akan bisa dijalankan di semua platform.

Ruby pertama kali dirilis pada tahun 1995 oleh Yukihiro Matsumoto (Matz) dari Jepang. Ruby dirancang dengan filosofi untuk membuat programmer bahagia dan produktif. Bahasa ini fokus pada kesederhanaan dan produktivitas dengan syntax yang natural dan mudah dibaca.

## Untuk Apa Sih Memakai Ruby Language?

Ruby adalah salah satu bahasa program yang bisa digunakan untuk berbagai macam kebutuhan. Dengan kata lain ini bisa digunakan sebagai:

### Web Development

Ruby memiliki web development framework bernama Ruby on Rails. Rilis sejak tahun 2005.

Ruby on Rails membuat web development cepat dan mudah. Seorang developer bisa langsung membuat web application tanpa harus menyesuaikan setting (sebagai contoh setting localhost dan lainnya) karena sudah dipersiapkan dari sana. Dan juga disediakan pre-built code libraries yang dapat membantu mempercepat pengembangan code.

Beberapa website terkenal yang menggunakan Ruby on Rails:
- GitHub
- Shopify
- Airbnb
- Basecamp
- Hulu

### DevOps

Ruby juga digunakan pada DevOps (singkatan dari Software Development (Dev) dan IT Operations (Ops)). DevOps bertujuan untuk memperpendek system development life cycle dan menyediakan software yang dapat diandalkan setiap saat.

Tools DevOps yang menggunakan Ruby:
- Chef (automation tool)
- Puppet (configuration management)
- Vagrant (development environment)

### Automation

Ruby adalah salah satu bahasa program yang dapat diandalkan untuk automation. Developer bisa membuat script untuk melakukan sesuatu secara otomatis. Karena Ruby mudah untuk ditulis, script yang simple bisa dikerjakan dengan cepat.

### Web Scraping and Crawling

Ruby juga bisa digunakan untuk melakukan crawling pada halaman website. Mengambil data dari element tertentu dan mendownload halaman website secara cepat. Sebagai contoh, kamu bisa menggunakan Nokogiri untuk extract structured data dari HTML pada halaman website.

### Data Processing

Ruby language sangat cocok untuk melakukan processing data, cleaning, dan filtering. Ada beberapa fitur yang sudah tersedia dalam Ruby, seperti map, reduce, dan select. Fungsi ini sangat membantu untuk melakukan pemrosesan data.

## Ruby Cheat Sheet

Kamu bisa membayangkan Ruby sebagai laci yang digunakan untuk menyimpan sesuatu.

```ruby
myvariabel = 1
```

Terdapat banyak sekali tipe data di dalam Ruby:
- **Boolean** (true/false)
- **Integer** (bilangan bulat)
- **Float** (bilangan desimal)
- **String** (teks)
- **Symbol** (identifier yang immutable)
- **Array** (kumpulan data)
- **Hash** (pasangan key-value)

## Ruby Install Rails

```bash
sudo apt install ruby-full
sudo apt-get install libsqlite3-dev
sudo gem install sqlite3-ruby
gem list # Check sqlite3 dan sqlite3-ruby jika sudah terinstal

gem install rails
sudo rails new myapp 
cd myapp
bin/rails server # Buka http://localhost:3000
```

## Ruby Basic Syntax

### Print Something

Untuk menampilkan output ke terminal, kamu bisa menggunakan:

```ruby
puts 'Hello World!'  # Menampilkan teks dengan baris baru
print 'Hello'        # Menampilkan teks tanpa baris baru
p 'Hello'           # Menampilkan teks untuk debugging
```

# Variabel

Di dalam Ruby untuk melakukan deklarasi variabel tidak perlu membuat tipe secara spesifik (variabel constant yang tidak bisa diubah atau variabel normal yang bisa diubah sewaktu-waktu). Variabel Ruby bisa menyimpan semua tipe data (Boolean, float, integer, string dan lainnya).

Sebagai contoh:
```ruby
nama_variabel = 'Hello world'
```
atau
```ruby
namaVariabel = 'Hello world'
```

**Konvensi Penamaan Variabel di Ruby:**
- Gunakan snake_case untuk variabel lokal: `nama_variabel`
- Gunakan SCREAMING_SNAKE_CASE untuk konstanta: `NAMA_KONSTANTA`
- Gunakan camelCase untuk method names (opsional): `namaMethod`

Hampir semua fitur di dalam Ruby adalah object. Object variabel bisa diubah kapan saja.

Sebagai contoh:
```ruby
umur_ku = 89 
# Dua tahun kemudian
umur_ku = 91
# Hasil yang akan dikeluarkan adalah 91

# Atau bisa menggunakan cara seperti ini
umur_ku += 2
# Ini disebut sebagai Operators, hasil yang akan dikeluarkan adalah 89 + 2 
# Cara ini juga bisa digunakan pada string object
```

Di dalam variabel kita tidak perlu mengatakan tipe data apa yang sedang dipakai, cukup tulis data tersebut dan biarkan sistem yang akan mencari tahu.

Contoh tipe data:
```ruby
'ini adalah string'  # Tipe data string
383123              # Ini adalah tipe data integer 
23.42               # Ini adalah tipe data float 
true                # Ini adalah tipe data boolean
:symbol             # Ini adalah tipe data symbol
```

### Method pada String

```ruby
title = 'teks'
title.upcase     # Hasilkan TEKS secara sementara 
title.upcase!    # Hasilkan TEKS secara permanent, tersimpan di dalam memory
title.downcase   # Hasilkan teks secara sementara
title.downcase!  # Hasilkan teks secara permanent
title.capitalize # Huruf pertama kapital
title.length     # Menghitung panjang string
title.reverse    # Membalik string
```

**Perbedaan Method dengan dan tanpa `!` (bang):**
- Method tanpa `!`: Mengembalikan hasil baru tanpa mengubah variabel asli
- Method dengan `!`: Mengubah variabel asli secara permanent

## Cara Melakukan Manipulasi String

Metode ini dapat mempermudah penggabungan antara dua atau lebih variabel menjadi satu (String Interpolation).

```ruby
nama_makanan = 'nasi goreng'
jumlah_makanan = 3
hasil = "#{nama_makanan} beli #{jumlah_makanan}"
# Output: 'nasi goreng beli 3'
# Perlu diingat gunakan " bukan '
```

**Penting:** String interpolation `#{}` hanya bekerja dengan double quotes (`"`), tidak dengan single quotes (`'`).

Cara lain menggabungkan string:
```ruby
nama_depan = 'John'
nama_belakang = 'Doe'

# Menggunakan concatenation
nama_lengkap = nama_depan + ' ' + nama_belakang

# Menggunakan interpolation (lebih disarankan)
nama_lengkap = "#{nama_depan} #{nama_belakang}"
```

## Menulis Variabel Constants

Metode ini hanya menyerupai constant tidak sama persis. Di dalam constant variabel nilai tidak dapat diubah setelah sudah ditulis.

Di dalam Ruby kamu bisa menulis sebuah variabel yang akan memberikan notifikasi jika ada perubahan pada variabel yang dituju.

Contoh penulisan:
```ruby
TEST_CONST = 12
# Jika ada perubahan di variabel di atas maka akan ada notifikasi pada terminal
TEST_CONST = 14 
# Akan ada warning jika kita mengubah nilai di dalam variabel tersebut
# Warning: already initialized constant TEST_CONST
```

**Aturan penulisan konstanta:**
- Penulisan variabel harus penuh huruf besar
- Gunakan SCREAMING_SNAKE_CASE
- Meskipun Ruby memberi warning, nilai masih bisa diubah (berbeda dengan konstanta di bahasa lain)

## Control Flow

Pada penulisan sebuah instruksi terkadang diperlukan untuk menambahkan fungsi atau tindakan untuk mengontrol bagaimana sebuah instruksi tersebut dilakukan.

Sebagai contoh, mari kita buat sebuah perumpamaan:

Jika kita ingin pergi ke sekolah, di sana terdapat 2 cara untuk menuju ke sekolah:
1. Kita bisa menggunakan jalur paling dekat ke sekolah akan tetapi jalan raya tersebut banyak lubang
2. Kita bisa menggunakan jalur paling jauh ke sekolah akan tetapi jalan raya tersebut lebih lancar

Tentu ini adalah sebuah opsi, kedua jalan tersebut dapat menghasilkan sebuah hasil yang sama akan tetapi proses dilakukannya itu berbeda.

### Cara Melakukan Control Flow

Cara melakukannya adalah dengan menggunakan If Statement.

Sebagai contoh:
```ruby
umur_udin = 17

if umur_udin < 19 
    puts "Udin adalah anak SMA"
elsif umur_udin > 30 
    puts "Udin adalah seorang karyawan dari F.A.N.G"
else 
    puts "Udin adalah seorang mahasiswa"
end
```

Hasil yang akan dikeluarkan adalah "Udin adalah anak SMA", karena di situ umur Udin di bawah 19.

Di dalam If Statement akan dilakukan checking apakah data tersebut benar atau salah. Seperti contoh di atas, karena umur Udin kurang dari 19 maka hasil dari **if** itu benar dan akan dilakukan instruksi selanjutnya.

Bisa dikatakan jika sebuah persyaratan sudah terpenuhi maka instruksi selanjutnya akan dilakukan.

Dengan menggunakan If Statement kita bisa membuat program memiliki sebuah opsi persyaratan khusus sebelum menjalankan instruksi.

### Beberapa Symbol untuk Melakukan Perbandingan Nilai

```ruby
>   # Lebih besar dari 
<   # Kurang dari 
==  # Sama dengan 
>=  # Lebih besar atau sama dengan 
<=  # Lebih kecil atau sama dengan 
!=  # Tidak sama dengan
```

Di dalam If Statement kamu bisa menambahkan banyak sekali opsi. **elsif** untuk memberikan program opsi instruksi apa yang akan dilakukan selanjutnya.

### Cara Menulis If Statement dalam Satu Baris

**Metode 1: Inline If**
```ruby
IPK = 4
if IPK == 4 then puts 'Nilai yang memuaskan' else puts 'Ayo belajar lebih giat' end
```

**Metode 2: Ternary Expression**
```ruby
IPK = 4 
puts IPK == 4 ? 'Nilai bagus' : 'Coba lagi'
# Ini adalah Ternary Expression
```

Untuk format penulisannya seperti ini:
```
Kondisi_persyaratan ? true : false
```

1. **Kondisi persyaratan** adalah nilai yang akan diseleksi (di contoh pertama tadi adalah `IPK == 4`)
2. Symbol `?` adalah syntax untuk mengenali bahwa ini adalah Ternary Expression
3. Kolom `true` akan dijalankan jika persyaratan telah terpenuhi
4. Kolom `:` adalah bagian dari syntax jangan diubah
5. Kolom `false` akan dijalankan jika persyaratan tidak terpenuhi

Contohnya seperti ini:
```ruby
nilai = 2 + 3
hasil = nilai == 5 ? 'Jawaban benar' : 'Jawaban salah'
puts hasil  # Output: Jawaban benar
```

## Unless

Unless adalah cara lain untuk melakukan If Statement. Di dalam unless yang dipakai adalah nilai yang berisi 'false' atau bisa dikatakan nilai yang tidak memenuhi persyaratan.

**Perbedaan If dan Unless:**
- **If Statement:** Yang akan dipakai adalah nilai True (nilai yang sudah memenuhi persyaratan)
- **Unless Statement:** Yang akan dipakai adalah nilai False (nilai yang tidak memenuhi persyaratan)

```ruby
a = 10
unless a > 30
    puts "#{a} hasil dari false, karena 10 tidak lebih dari 30"
end
# Output: 10 hasil dari false, karena 10 tidak lebih dari 30
```

**Cara membaca Unless:**
"Unless a lebih dari 30" artinya "Jika a TIDAK lebih dari 30, jalankan kode ini"

Contoh perbandingan If vs Unless:
```ruby
umur = 15

# Menggunakan If
if umur < 18
    puts "Kamu masih di bawah umur"
end

# Menggunakan Unless (sama hasilnya)
unless umur >= 18
    puts "Kamu masih di bawah umur"
end
```

## Case

Case statement adalah alternatif untuk multiple if-elsif-else yang lebih rapi dan mudah dibaca.

```ruby
nilai = 10
case nilai  # Ini adalah parameter
when 1..9
    puts 'Nilai berada di jarak antara 1 sampai 9'
when 10 
    puts 'Nilai sama dengan 10'
else 
    puts 'Nilai tidak diketahui'
end
```

### Breakdown Code:

1. `nilai = 10` ini adalah variabel
2. `case nilai` "case" adalah syntax untuk menunjukkan bahwa ini adalah switch case, sedangkan nilai adalah variabel
3. `when 1..9` di sini adalah sebuah persyaratan apakah variabel 'nilai' berada di antara 1 sampai 9, jika benar maka instruksi selanjutnya akan dijalankan
4. `when 10` di sini adalah sebuah persyaratan apakah variabel 'nilai' sama dengan 10, jika benar maka instruksi akan dilanjutkan
5. `else` jika tidak ada opsi yang cocok maka akan dijalankan perintah di bawah ini
6. `end` ini adalah syntax yang wajib ditulis untuk mengakhiri switch case

### Cara Ruby Melakukan Analisa Perbandingan:

1. **Apakah nilai tersebut berada di dalam range?**
   ```ruby
   when 1..9  # Nilai antara 1 sampai 9
   ```

2. **Apakah nilai tersebut sama persis?**
   ```ruby
   when 'budi'  # Nilai sama dengan 'budi'
   ```

3. **Apakah nilai tersebut berbentuk tipe data tertentu?**
   ```ruby
   when String  # Apakah ini string?
   when Integer # Apakah ini integer?
   ```

### Case Tanpa Parameter

Kamu juga bisa menjalankan Ruby case tanpa mengisi parameter:

```ruby
nilai = 10
case 
when nilai < 10 
    puts 'Nilai kurang dari 10'
when nilai == 10 
    puts 'Nilai sama dengan 10'
when nilai > 10
    puts 'Nilai lebih dari 10'
end
```

Dengan menggunakan instruksi di atas maka akan dilakukan flow control yang cukup mirip dengan if statement. Jika persyaratan terpenuhi maka akan dijalankan.

Pada switch case di atas, tidak perlu mengisi nilai dari `case`. Dengan begitu cara pemakaiannya akan sama dengan if statement.

**Source:**
- https://stackoverflow.com/questions/948135/how-to-write-a-switch-statement-in-ruby?rq=1
- https://www.geeksforgeeks.org/ruby-case-statement/
- https://www.rubyguides.com/2019/10/ruby-ternary-operator/

## Loops

Loop adalah cara untuk menjalankan kode secara berulang-ulang sampai kondisi tertentu terpenuhi.

### For Loop

```ruby
for i in 2..100
    puts "Ini adalah nomor #{i}"
end
```

### Breakdown Code:

1. `for i in 2..100` untuk setiap angka di antara 2 sampai 100
2. Print 'ini adalah nomor #{variabel i}'
3. Akhiri loop

Di sini perintah akan diulang sebanyak 99 kali (dari 2 sampai 100).

### Each Method (Lebih Ruby Way)

```ruby
(1..5).each do |i|
    puts "Nomor: #{i}"
end

# Atau dengan bracket
(1..5).each { |i| puts "Nomor: #{i}" }
```

## While

While loop akan terus berjalan selama kondisi bernilai true.

```ruby
var_A = 0
while var_A < 100
    puts "Ini adalah loop ke #{var_A}"
    var_A += 1 
end 
```

### Breakdown:

1. `var_A = 0` ini adalah variabel
2. `while var_A < 100` selama nilai variabel berada di bawah 100, lakukan
3. `puts "ini adalah loop ke #{var_A}"` print string dengan nilai variabel
4. `var_A += 1` tambah 1 ke dalam variabel
5. `end` ini adalah syntax sebagai penutup while loop

Di dalam code di atas loop akan terus dilakukan hingga 100 kali. Setiap kali loop dilakukan, program akan melakukan dua instruksi yang sudah disiapkan.

**Penting:** Pastikan ada kondisi yang membuat loop berhenti, jika tidak akan terjadi infinite loop!

## Until

Until adalah kebalikan dari while. Loop akan berjalan sampai kondisi menjadi true.

```ruby
obj = 100

until obj < 1 
    puts "Ini adalah nomor ke #{obj}"
    obj -= 1 
end 
```

Metode ini kurang lebih sama seperti unless statement. Jika persyaratan tidak terpenuhi maka jalankan instruksi tersebut.

### Breakdown Code:

1. `obj = 100` adalah variabel
2. `until obj < 1` bisa kita ibaratkan sebagai "unless". Jika persyaratan tidak terpenuhi maka jalankan instruksi selanjutnya
3. `puts` digunakan untuk menampilkan nilai ke dalam terminal atau console
4. `end` adalah syntax untuk mengakhiri loop

**Perbandingan While vs Until:**
```ruby
# While: loop selama kondisi TRUE
counter = 0
while counter < 5
    puts counter
    counter += 1
end

# Until: loop sampai kondisi TRUE (selama kondisi FALSE)
counter = 0
until counter >= 5
    puts counter
    counter += 1
end
```

## Loop

Loop adalah cara paling basic untuk membuat loop tanpa kondisi. Kamu harus menggunakan `break` untuk menghentikannya.

```ruby
obj = 0

loop do 
    obj += 1 
    puts "Obj nilai ke #{obj}"

    if obj == 100 
        break 
    end 
end 

puts "Loop berakhir"
```

### Code Breakdown:

1. `obj` adalah variabel
2. `loop do` selama loop masih berjalan maka lakukan instruksi selanjutnya
3. `obj += 1` tambah 1 setiap kali loop
4. `if obj == 100` jika nilai obj sama dengan 100
5. `break` syntax ini hanya bisa digunakan di dalam loop statement untuk mengakhiri loop yang berjalan

**Kata Kunci Penting dalam Loop:**
- `break`: Menghentikan loop sepenuhnya
- `next`: Melompat ke iterasi berikutnya
- `redo`: Mengulang iterasi saat ini tanpa mengevaluasi kondisi lagi

## Next pada Loop

Next digunakan untuk melewati sisa kode dalam loop dan langsung melanjutkan ke iterasi berikutnya.

```ruby
abc = 10

for i in 1..10
    puts "Ini adalah nomor ke #{i}"
    
    if i == 5
        puts "========= Ini adalah angka 5"
        puts "Instruksi selanjutnya akan terlewati"
        # Next digunakan untuk membuat loop kembali ke instruksi pertama loop
        next
    end

    puts "Ini adalah bagian yang akan terlewati #{i}"
end
```

**Penjelasan:**
- Ketika `i == 5`, setelah mencetak pesan, `next` akan dijalankan
- Kode setelah `next` (`puts "Ini adalah bagian yang akan terlewati"`) tidak akan dijalankan untuk `i == 5`
- Loop langsung melanjutkan ke iterasi berikutnya (`i == 6`)

Contoh lain penggunaan `next`:
```ruby
# Hanya print angka genap
(1..10).each do |num|
    next if num.odd?  # Lewati jika angka ganjil
    puts num
end
# Output: 2, 4, 6, 8, 10
```

## Arrays

Array adalah kumpulan data yang tersimpan dalam satu variabel. Data dalam array memiliki index yang dimulai dari 0.

```ruby
nama_kelas = ['Kelas 1', 'Kelas 2', 'Kelas 3']

puts nama_kelas[0]   # Kelas 1
puts nama_kelas[1]   # Kelas 2
puts nama_kelas[2]   # Kelas 3 
puts nama_kelas[-1]  # Kelas 3 (index dari belakang)
puts nama_kelas[-3]  # Kelas 1 (index dari belakang)
puts nama_kelas.length # 3
```

**Index Negatif:**
- `-1` adalah elemen terakhir
- `-2` adalah elemen kedua dari belakang
- Dan seterusnya

### Opsi untuk Membuat Array

```ruby
# Cara 1: Array kosong
arr1 = []
arr2 = Array.new

# Cara 2: Array dengan isi
makanan = Array.new(4, 'nasi goreng')
# Akan ada 4 nasi goreng di list
# ["nasi goreng", "nasi goreng", "nasi goreng", "nasi goreng"]

# Cara 3: Array biasa
minuman = ['jeruk panas', 'Es coklat']
```

### Method untuk Manipulasi Array

```ruby
minuman = ['jeruk panas', 'Es coklat']

# Menambahkan item ke akhir array
minuman.push('Es kopi')       # ["jeruk panas", "Es coklat", "Es kopi"]
minuman << "Es gratis"        # ["jeruk panas", "Es coklat", "Es kopi", "Es gratis"]

# Menambahkan item ke awal array
minuman.unshift('Air putih')  

# Menghapus item terakhir
minuman.pop                   # Menghapus "Es gratis"

# Menghapus item pertama
minuman.shift                 # Menghapus "Air putih"

# Mengecek apakah array kosong
minuman.empty?                # false

# Mengecek apakah item ada dalam array
minuman.include?('Es kopi')   # true

# Mengurutkan array
angka = [5, 2, 8, 1, 9]
angka.sort                    # [1, 2, 5, 8, 9]

# Membalik array
angka.reverse                 # [9, 1, 8, 2, 5]
```

### Iterasi pada Array

```ruby
buah = ['apel', 'jeruk', 'mangga']

# Cara 1: Each
buah.each do |item|
    puts item
end

# Cara 2: Each dengan index
buah.each_with_index do |item, index|
    puts "#{index}: #{item}"
end

# Cara 3: Map (membuat array baru)
buah_kapital = buah.map { |item| item.upcase }
# ["APEL", "JERUK", "MANGGA"]
```

## Functions

Function adalah sebuah block code yang bisa dipanggil kapan saja. Istilahnya adalah DRY (Don't Repeat Yourself).

Di Ruby, function disebut sebagai **method**.

```ruby
def fungsi(argument)
    puts "Hallo, #{argument}"
end

fungsi('Budi')
# Output: Hallo, Budi
```

### Method dengan Return Value

```ruby
def tambah(a, b)
    return a + b
end

hasil = tambah(5, 3)
puts hasil  # Output: 8

# Atau tanpa keyword return (Ruby akan return baris terakhir)
def kali(a, b)
    a * b
end

hasil = kali(4, 5)
puts hasil  # Output: 20
```

### Method dengan Default Parameter

```ruby
def sapa(nama = "Teman")
    puts "Hallo, #{nama}!"
end

sapa          # Output: Hallo, Teman!
sapa("Budi")  # Output: Hallo, Budi!
```

### Method dengan Multiple Return Values

```ruby
def hitung(a, b)
    tambah = a + b
    kurang = a - b
    return tambah, kurang
end

hasil_tambah, hasil_kurang = hitung(10, 5)
puts hasil_tambah  # Output: 15
puts hasil_kurang  # Output: 5
```

### Method dengan Variable Arguments

```ruby
def jumlahkan(*angka)
    total = 0
    angka.each { |num| total += num }
    total
end

puts jumlahkan(1, 2, 3)        # Output: 6
puts jumlahkan(5, 10, 15, 20)  # Output: 50
```

## Hash (Dictionary)

Hash adalah struktur data yang menyimpan pasangan key-value. Mirip dengan object di JavaScript atau dictionary di Python.

```ruby
# Cara 1: Menggunakan rocket syntax
mahasiswa = {
    "nama" => "Budi",
    "umur" => 20,
    "jurusan" => "Informatika"
}

# Cara 2: Menggunakan symbol (lebih efisien)
mahasiswa = {
    nama: "Budi",
    umur: 20,
    jurusan: "Informatika"
}

# Mengakses value
puts mahasiswa[:nama]     # Output: Budi
puts mahasiswa[:umur]     # Output: 20

# Menambah key-value baru
mahasiswa[:ipk] = 3.8

# Mengecek apakah key ada
mahasiswa.has_key?(:nama)  # true

# Iterasi hash
mahasiswa.each do |key, value|
    puts "#{key}: #{value}"
end
```

## Blocks, Procs, dan Lambdas

Ruby memiliki konsep blocks yang sangat powerful.

### Blocks

```ruby
# Block dengan do...end
[1, 2, 3].each do |num|
    puts num * 2
end

# Block dengan curly braces (untuk satu baris)
[1, 2, 3].each { |num| puts num * 2 }

# Custom method yang menerima block
def salam
    puts "Sebelum block"
    yield
    puts "Setelah block"
end

salam { puts "Ini dari block!" }
```

## Tips Belajar Ruby

1. **Ruby adalah bahasa yang ekspresif:** Ada banyak cara untuk melakukan hal yang sama
2. **Ikuti konvensi Ruby:** Gunakan snake_case untuk variabel dan method
3. **Gunakan IRB untuk eksperimen:** Interactive Ruby Shell sangat berguna untuk testing
4. **Baca dokumentasi:** Ruby memiliki dokumentasi yang sangat lengkap di ruby-doc.org
5. **Praktik dengan project nyata:** Coba buat aplikasi sederhana untuk menguasai konsep

## Latihan Ruby

[Latihan Ruby](./latihan-bahasa/latihan-ruby.md)

## Task

### Devops Tool Chain
- https://en.wikipedia.org/wiki/DevOps_toolchain 
- https://en.wikipedia.org/wiki/DevOps 

## Perbedaan Ruby dengan Bahasa Lain

| Fitur | Ruby | Python | JavaScript |
|-------|------|--------|------------|
| Syntax | Ekspresif, fokus pada kebahagiaan programmer | Simpel, mudah dibaca | Fleksibel, berbasis prototype |
| Penggunaan Utama | Web development (Rails) | Data science, AI, web | Web development, frontend/backend |
| Performance | Sedang | Sedang | Cepat (dengan Node.js) |
| Community | Besar, fokus pada web | Sangat besar, beragam | Sangat besar, terutama web |

## Kesalahan Umum untuk Pemula

1. **Lupa menulis `end`:** Setiap block (if, while, def) harus ditutup dengan `end`
2. **Salah menggunakan `=` vs `==`:** `=` untuk assignment, `==` untuk comparison
3. **String interpolation dengan single quote:** Harus menggunakan double quote (`"`)
4. **Index array dimulai dari 0:** Bukan dari 1
5. **Mengubah array saat iterasi:** Bisa menyebabkan behavior yang tidak diharapkan

## Resource Belajar Tambahan

### Dokumentasi Resmi
- Ruby Documentation: https://ruby-doc.org/
- Ruby on Rails Guides: https://guides.rubyonrails.org/

### Tutorial Interaktif
- Codecademy Ruby Course
- Ruby Koans (belajar lewat testing)
- Exercism.io Ruby Track

### Buku Rekomendasi
- "The Well-Grounded Rubyist" by David A. Black
- "Eloquent Ruby" by Russ Olsen
- "Programming Ruby" (Pickaxe Book)

## Source

- https://stackoverflow.com/questions/948135/how-to-write-a-switch-statement-in-ruby?rq=1
- https://www.rubyguides.com/2015/10/ruby-case/
- https://github.com/training-mode/ruby
- https://github.com/rails/rails
- https://stackoverflow.com/questions/17350837/ruby-on-rails-add-gem-sqlite3-to-your-gemfile
- https://www.codecademy.com/resources/blog/should-i-learn-ruby/
- https://en.wikipedia.org/wiki/DevOps
- https://www.rubyguides.com/ruby-tutorial/
- https://www.ruby-lang.org/en/documentation/
