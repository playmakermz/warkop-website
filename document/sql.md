# Pengenalan Database

Dengan adanya miliaran pengguna internet saat ini, sebuah sistem atau perangkat pengelola yang bisa mengatur, mendata, dan mengelompokkan data pengguna sangat dibutuhkan.

Peningkatan pembuatan dan penggunaan data meningkat sangat tajam. Untuk membuat suatu keputusan, banyak organisasi membutuhkan orang yang bisa mengelola data seperti business analysts, data engineer, dan lainnya.

SQL adalah bahasa program dan aplikasi pengelola data yang telah diandalkan oleh para developer dalam waktu yang lama. Meskipun SQL adalah teknologi lama, akan tetapi para developer secara terus menerus mengembangkannya.

## Daftar Isi
1. [Penjelasan Database](#penjelasan-database)
2. [Dataset](#dataset)
3. [Database Management System](#database-management-system-dbms)
4. [CRUD](#crud)
5. [Two Type of Database](#two-type-of-database)
6. [Relational Database](#relational-database)
7. [Non-Relational Databases](#non-relational-databases-nosql)
8. [Apa itu SQL?](#apa-itu-sql)
9. [SQL Process Flow](#sql-process-flow)
10. [Contoh Perintah pada SQL](#contoh-perintah-pada-sql)
11. [Database Queries](#database-queries)
12. [Type Primary Key](#type-primary-key)
13. [Natural Key Number](#natural-key-number)
14. [Surrogate Key](#surrogate-key)
15. [Candidate Key](#candidate-key)
16. [Alternate Key](#alternate-key)
17. [Foreign Key](#foreign-key)
18. [Composite Key](#composite-key)
19. [Wrap Up](#wrap-up)
20. [DDL - Data Definition Language](#ddl-data-definition-language)
21. [DML - Data Manipulation Language](#dml-data-manipulation-language)
22. [DCL - Data Control Language](#dcl-data-control-language)
23. [Field or Column](#field-or-column-kolom)
24. [Record or Row](#record-or-row-baris)
25. [SQL Constraint](#sql-constraint)
26. [Backup Database](#generate-backup-database)
27. [Restore Database](#restore-database)
28. [Operator Perbandingan](#operator-perbandingan)
29. [LIKE - Mengambil Data yang Mirip](#like)
30. [Baris NULL](#kolom-null)
31. [ORDER BY](#order-by)
32. [LIMIT](#limit)
33. [Wrap Up Rangkuman 2](#wrap-up-rangkuman)
34. [Latihan](#latihan-sql)

## Penjelasan Database

Secara umum, database adalah koleksi dari informasi yang terkait. Sebagai contoh: buku nomor telepon, daftar belanja, todo list, dan absensi kelas. Database bisa disimpan di mana saja, seperti:
- Di atas kertas
- Di dalam kepala
- Di dalam komputer
- File PowerPoint
- Catatan komen

Ada banyak sekali cara untuk mengatur database dan banyak tipe database yang didesain untuk tujuan tertentu.

Jika kamu sudah menggunakan Excel, kamu pasti terbiasa dengan tabel yang mirip seperti spreadsheet. Tabel memiliki baris (row) dan kolom (column). Database tabel harus diatur dengan kolom, dan setiap kolom harus memiliki nama yang unik (Primary Key).

**Kesimpulan:** Database adalah sebuah koleksi dari informasi yang terkait dan bisa disimpan di mana saja.

**Beberapa istilah pada tabel:**
- **Field** adalah nama kolom pada tabel, yang berbentuk horizontal
- **Record** adalah kelompok data pada satu baris yang memiliki hubungan

Contoh tabel, Field, dan Records:

nama murid | jurusan 
--- | --- 
Budi | IPA 
Ucup | IPA 
Ranti | IPS 
Rangga | Bahasa 

**Field** adalah "nama murid" dan "jurusan"

**Record** adalah "Budi" dan "IPA". Satu kelompok data yang berhubungan.

## Instalasi MySQL di Windows Subsystem for Linux (WSL)

Source: https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-database 

1. Buka terminal WSL (pada instruksi ini memakai Ubuntu)
2. Usahakan membiasakan diri dengan `sudo apt update`
3. Setelah berhasil update, install MySQL dengan `sudo apt install mysql-server`
4. Untuk memastikan versi dari SQL, gunakan `mysql --version`

Jika ingin membuat SQL server untuk produksi, lakukan secure installation dengan perintah `sudo mysql_secure_installation`

Biasanya di saat kita menghidupkan komputer, MySQL akan berada di status belum berjalan. Untuk membuat MySQL server bisa berjalan, gunakan `sudo /etc/init.d/mysql start`.

Cara untuk membuka MySQL melalui terminal: `sudo mysql`

**Penting! Jika kamu bertemu hal seperti ini saat secure installation:**

```
... Failed! Error: SET PASSWORD has no significance for user 'root'@'localhost' as the authentication method used doesn't store authentication data in the MySQL server. Please consider using ALTER USER instead if you want to change authentication parameters.
```

Ini adalah instruksi penanganan dari https://askubuntu.com/questions/1406395/mysql-root-password-setup-error :

1. Keluar dari pesan error tersebut
2. `sudo mysql` untuk masuk ke MySQL
3. `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password by 'my-secret-password';` lakukan alter user untuk merubah password
4. `exit;` untuk keluar dari MySQL
5. `sudo mysql_secure_installation` masuk kembali ke secure installation
6. `mysql -u <your username> -p`

## Cara Untuk Mengetahui USER dan Host yang Sudah Terdaftar pada MySQL

Sumber: http://mysql.phi-integration.com/administrasi-mysql/melihat-daftar-user 

1. Masuk ke dalam MySQL terlebih dahulu
2. Ketik `SELECT User, Host FROM mysql.user;`

## Cara Untuk Input Data ke dalam DATABASE

Langkah pertama untuk melakukan input data adalah dengan masuk ke dalam aplikasi MySQL terlebih dahulu. Setelah masuk ke dalam MySQL melalui terminal, akan muncul pesan seperti ini:

```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 13
Server version: 8.0.30-0ubuntu0.20.04.2 (Ubuntu)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

Dalam penggunaan command pada SQL, biasanya tidak case sensitive, jadi kamu bisa menggunakan huruf besar maupun kecil. Tetapi sangat dianjurkan menggunakan huruf besar untuk menandai bahwa itu adalah command SQL. Pada variabel seperti nama database dan tabel, SQL akan melakukan case sensitive. Jangan lupa untuk mengakhiri setiap perintah SQL dengan titik koma `;`

**Contoh Beberapa Tahapan yang Dilakukan:**

- Untuk mengetahui list database yang ada di dalam MySQL, ketik `SHOW DATABASES;`
- Untuk membuat database baru, ketik `CREATE DATABASE school;`
- Untuk memilih database, ketik `USE school;`
- Untuk membuat tabel baru di dalam database, ketik:
    ```sql
    CREATE TABLE student (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        name VARCHAR(200) NOT NULL, 
        major VARCHAR(150) NOT NULL,
        PRIMARY KEY (id)
    );
    ```
    Untuk lebih lengkapnya mengenai "Data Types" dan "Primary Key", bisa dilihat pada bagian bawah.
    
- Untuk melihat list tabel yang ada, ketik `SHOW TABLES;`
- Untuk melihat informasi kolom di dalam tabel, ketik `DESCRIBE student;`
- Untuk menambahkan records atau data ke dalam tabel, ketik:
    ```sql
    INSERT INTO student (name, major) VALUES 
        ('Budi', 'IPA'),
        ('Ucup', 'IPS'),
        ('Ranti', 'IPS'),
        ('Rangga', 'Bahasa');
    ```    
- Untuk mengambil records dari dalam tabel, ketik `SELECT * FROM student;`

Source: https://dev.mysql.com/doc/mysql-getting-started/en/

## Dataset

Cara mudah untuk menganalisa data adalah dengan menjalankannya secara side by side pada dataset!

Dataset adalah sekumpulan data yang terstruktur yang mempermudah manusia untuk membaca dan menganalisa data dalam jumlah yang banyak. Dataset biasanya berbentuk tabel yang terdiri dari baris dan kolom.

Dengan cara penggunaan baris dan kolom yang tepat, dataset akan mempermudah kita dalam melihat hubungan dari setiap data.

Misalkan dataset harga barang di bawah ini:

Nama Barang | Harga Barang | Barang Yang Terjual
--- | --- | ---
Kaos Kaki | 5000 | 20
Sepatu | 35000 | 25 
Sandal | 10000 | 10 
Tali Sepatu | 10000 | 5

Sekarang akan saya coba jelaskan perbedaan data, dataset, dan database.

Mari kita buat perumpamaan: data adalah lembar kertas pada buku. Dataset adalah kumpulan lembaran kertas, yaitu buku. Sedangkan database adalah lemari atau rak buku.

- **Data** adalah serpihan informasi
- **Dataset** adalah tempat di mana data dikumpulkan
- **Database** adalah wadah yang akan menyimpan kumpulan dataset

## SQL WHERE

```sql
SELECT column1, column2 
FROM nama_table 
WHERE column1 = 'requirement';
```

Klausa "WHERE" digunakan untuk melakukan filtering, hanya yang sesuai persyaratan yang akan diambil.

## SQL UPDATE Statement

```sql
UPDATE nama_table
SET column1 = value1, column2 = value2
WHERE condition;
```

Statement "UPDATE" digunakan untuk melakukan perubahan pada records yang telah ada.

## SQL DELETE Statement

```sql
DELETE FROM nama_table 
WHERE condition;
```

Statement "DELETE" digunakan untuk menghapus record yang telah ada.

## ALTER Table

```sql
ALTER TABLE nama_table 
    ADD COLUMN nama_column TEXT,
    DROP COLUMN nama,
    RENAME COLUMN nama TO nama_baru, 
    MODIFY nama VARCHAR(100) AFTER nama_column,
    MODIFY nama VARCHAR(100) FIRST;
```

Beberapa contoh statement untuk mengubah tabel.

## Menambahkan / Menghapus UNIQUE Constraint

```sql
ALTER TABLE nama_table 
    ADD CONSTRAINT column_unique UNIQUE (nama_column);
```

"ADD CONSTRAINT" ini adalah untuk menambahkan kata kunci, agar kita bisa dengan mudah menghapusnya nanti. "UNIQUE" akan memastikan bahwa semua value yang masuk berbeda dengan yang lain.

```sql
ALTER TABLE nama_table 
    DROP CONSTRAINT column_unique;
```

Perintah di atas untuk menghapus constraint unique.

## Menambahkan FOREIGN KEY

```sql
ALTER TABLE nama_column
    ADD CONSTRAINT fk_nama_column 
    FOREIGN KEY (nama_column) REFERENCES nama_column(id);
```

## Database Management System (DBMS)

DBMS adalah software khusus yang akan membantu pengguna mengelola database. DBMS membantu menambahkan, menghapus, dan mengubah data yang berada di database.

## CRUD

CRUD adalah singkatan dari Create, Read, Update, dan Delete. Ini adalah empat operasi dasar yang bisa dilakukan pada database.

## Two Type of Database

Ada dua tipe database utama:

### Relational Database (SQL)
Relational database mengatur data menjadi satu atau lebih tabel. Setiap tabel memiliki kolom dan baris. Kata kunci khusus mengidentifikasi setiap baris. Relational database adalah database yang berdasarkan data yang terhubung atau sudah ditentukan sebelumnya. Berbagai item disusun menjadi satu set tabel dengan kolom dan baris. Tabel digunakan untuk menyimpan informasi tentang objek yang akan dipresentasikan dalam database.

### Non-Relational (NoSQL / Tidak Hanya SQL)
Non-relational database menyimpan data dalam format yang lebih fleksibel seperti:
- Key-value pairs
- Document (JSON, XML)
- Graphs
- Flexible tables

## Relational Database

Contoh tabel mahasiswa:

ID | Name | Major
--- | --- | ---
1 | Jack | Biology
2 | Kate | Sociology
3 | Claire | English
4 | John | Chemistry

Contoh tabel user:

Username | Password | Email
--- | --- | ---
jsmith22 | wordpass | email1@example.com
catlover45 | apple223 | email2@example.com
gamerkid | pass123 | email3@example.com
giraffe | pass456 | email4@example.com

**Relational Database Management System (RDBMS)** membantu pengguna membuat dan mengelola relational database. Contohnya: MySQL, Oracle, PostgreSQL, MariaDB.

## Non-Relational Databases (NoSQL)

**Non-relational Database Management System (NRDBMS)** membantu pengguna membuat dan mengatur non-relational database. Contohnya: MongoDB, DynamoDB, Apache Cassandra.

**Implementation Specific:**
- Setiap non-relational database masuk kategori ini, tidak ada bahasa standar
- Kebanyakan NRDBMS akan menggunakan bahasa program mereka sendiri untuk menjalankan CRUD dan operasi administratif pada database

## Apa itu SQL?

SQL (Structured Query Language) adalah salah satu bahasa untuk membuat desain aturan di dalam relational database. Ini sudah ada sejak tahun 1970-an dan merupakan cara umum untuk mengakses data di dalam database. Fitur yang sering dipakai dalam SQL adalah membaca, memanipulasi, dan mengubah data. 

Beberapa alasan SQL bisa menjadi populer:

- Semantik dan mudah dipahami
- Bisa mengakses data yang besar secara langsung dari tempat penyimpanan
- Jika dibandingkan dengan spreadsheet tools, analisa data lebih mudah dilakukan dalam SQL karena mudah melakukan audit dan replikasi data
- SQL itu bagus sebagai database language untuk menyimpan data ke dalam database
- SQL adalah alat yang bagus untuk website seperti PHP, Python, Java, ASP dan lainnya untuk membuat website dinamis

Peringkat SQL dalam penggunaan di dunia data science tools berada di peringkat kedua menurut survei '2020 Data Science and Machine Learning Survey' dari Kaggle.

## SQL Process Flow

Saat kamu menjalankan SQL query, query tersebut akan pergi ke dalam SQL server. SQL server bekerja untuk mengelola database dan lainnya. SQL server memanggil database table dan mengembalikan hasilnya.

## Contoh Perintah pada SQL

Dalam penulisan SQL, pengguna tidak perlu memperhatikan besar atau kecilnya suatu huruf karena SQL tidak menggunakan case sensitive (kecuali untuk nama database, tabel, dan kolom).

Contoh perintah penting dalam SQL:
- `SELECT` untuk ekstrak data dari database
- `UPDATE` untuk memperbarui data dari database
- `DELETE` untuk hapus data dari database
- `INSERT INTO` untuk masukkan data baru ke database
- `CREATE DATABASE` untuk buat database baru
- `ALTER DATABASE` untuk ubah database
- `CREATE TABLE` untuk buat tabel baru
- `ALTER TABLE` untuk ubah tabel
- `DROP TABLE` untuk hapus tabel
- `CREATE INDEX` untuk buat index (kata kunci)
- `DROP INDEX` untuk hapus index

## Database Queries

Queries adalah permintaan yang dibuat oleh database management system untuk informasi spesifik.

Dengan semakin kompleks database tersebut, akan lebih sulit untuk mendapatkan sebuah informasi.

Secara mudahnya, queries adalah set instruksi pada database untuk mengambil atau memanipulasi data.

## Type Primary Key

Student ID | Name | Major
--- | --- | ---
1 | Jack | Biology
2 | Kate | Sociology
3 | Claire | English
4 | Jack | Biology
5 | Mike | Comp. Sci

Primary key itu penting dalam database tabel. Pastikan primary key adalah informasi yang pasti berbeda untuk setiap baris. Jika dengan contoh di atas maka primary key adalah 'Student ID', karena meskipun ada dua orang bernama "Jack", ID mereka tetap unik.

## Natural Key Number

Natural key number adalah kata kunci yang telah ada sebelumnya di dunia nyata. Sebagai contoh, nomor KTP adalah kata kunci yang telah ada di dunia nyata dan bisa digunakan sebagai natural key.

## Surrogate Key

Surrogate key adalah kata kunci yang tidak memiliki bentuk di dunia nyata. Biasanya berupa angka yang di-generate otomatis oleh sistem (seperti AUTO_INCREMENT).

## Candidate Key

Candidate key adalah kandidat kata kunci. Kita bisa sebut sebagai identitas yang bisa membedakan objek satu dengan yang lain. Sebagai contoh: jika kita ingin membedakan orang dengan menggunakan data pribadi, kita bisa menggunakan nomor KTP, atau menggunakan nomor handphone mereka, atau bisa menggunakan alamat email mereka. Setiap data tersebut bisa membedakan satu dengan yang lainnya. Ketiga data di atas bisa disebut sebagai candidate key yang akan dipakai sebagai primary key atau alternate key.

## Alternate Key

Alternate key bisa dikenal sebagai secondary key. Ini adalah identitas pembeda di dalam baris pada tabel yang bukan primary key tapi tetap unique.

## Foreign Key

Foreign key adalah atribut yang bisa kita simpan pada database tabel yang akan menghubungkan dengan database tabel lain.

Ini digunakan untuk menyimpan referensi primary key ke dalam baris database tabel lain.

**Tabel Employee:**

emp_id | name | branch_id | super_id
--- | --- | --- | ---
103 | Budi | 1 | 102
101 | Alva | 2 | 103
102 | Rangga | 3 | 101

**Tabel Branch:**

branch_id | branch_name | mgr_id
--- | --- | ---
3 | Bambang | 102
2 | Nasi Gorengeng | 101
1 | Soto | 103

Foreign key penting untuk menghubungkan atau mendefinisikan hubungan antar tabel. Dengan contoh di atas, kolom 'branch_id' adalah foreign key yang akan menghubungkan dengan database tabel bernama 'Branch'.

Di dalam contoh di atas, ini juga mendefinisikan siapa supervisor untuk setiap orang. Budi dengan employee ID '103' memiliki supervisor ID 102, yaitu 'Rangga'.

## Composite Key

Jika ada primary key yang terdiri dari 2 atau lebih kolom, biasa disebut sebagai composite key. Ini digunakan untuk membuat primary key tetap unik di antara banyak data yang memiliki kesamaan.

Sebagai contoh: untuk mengidentifikasi setiap murid dibutuhkan nama depan dan nama belakang. Akan sulit atau tidak mungkin bisa untuk membedakan murid jika hanya dari nama depan atau nama belakangnya saja.

Jika ada murid yang memiliki nama depan yang sama dengan murid lain, akan sulit untuk membedakannya. Dengan digunakannya composite key, kita bisa mengurangi kemungkinan salah membedakan orang.

Teknik tersebut sangat berguna untuk membedakan setiap data dengan data yang lain. Di dalam suatu sistem database tidak boleh ada kesamaan dari primary key. Setiap primary key itu harus unik dan berbeda dengan yang lain.

Tidak harus primary key saja yang bisa menggunakan composite key. Gabungan dari 2 atau lebih kolom bisa menjadi composite key juga.

## Wrap Up

Mari kita rangkum poin penting yang sudah dipelajari:

- Database adalah koleksi informasi
- Komputer bagus dalam menyimpan database
- DBMS membuat database lebih mudah diatur dan lebih aman
- DBMS memperbolehkan operasi CRUD
- Ada dua tipe database utama: relational dan non-relational

**RDBMS (Relational Database Management System) memiliki keuntungan:**

1. **Data Integrity** menyimpan data sekali dan menghindari duplikasi
2. **SQL Constraints** adalah aturan yang dipasang pada kolom tabel untuk menyimpan data dan menghindari pengguna menyimpan data yang tidak valid ke dalam kolom
3. **Better Security** menetapkan hak kepada pengguna individu. Menggunakan ini, pengguna bisa menyimpan data penting ke dalam tabel menggunakan username dan password
4. **Database Normalization** adalah proses untuk menyimpan database dengan efisien. Tidak perlu menyimpan data yang sama lebih dari satu kali
5. **Beberapa tipe relationships:**
   - **One to One Relationship:** Menggabungkan dua tabel
   - **One to Many Relationship:** Membuat foreign key dari parent table ke child table
   - **Many to Many Relationship:** Membuat relation table baru

**Structured Query Language (SQL):**
- Bahasa standar untuk berinteraksi dengan RDBMS
- Digunakan untuk menjalankan operasi CRUD
- Digunakan untuk menjelaskan tabel dan struktur
- SQL code biasanya digunakan dengan satu RDBMS dan tidak bisa langsung untuk yang lain (ada perbedaan syntax)

**Istilah Penting:**
- **Row** adalah baris yang melintang horizontal (kanan ke kiri)
- **Column** adalah baris melintang vertikal, dimulai dari atas ke bawah

## DDL (Data Definition Language)

DDL adalah kategori perintah SQL untuk mendefinisikan struktur database. Beberapa contoh:

- **CREATE:** Membuat tabel atau objek baru
- **ALTER:** Memodifikasi database objek seperti tabel
- **DROP:** Hapus seluruh tabel atau objek lain
- **USE:** Digunakan untuk memilih dan menggunakan objek

## DML (Data Manipulation Language)

DML adalah kategori perintah SQL untuk memanipulasi data dalam tabel. Beberapa contoh:

- **SELECT:** Mengambil satu atau lebih kolom. Sebagai contoh mengambil kolom dari tabel
- **INSERT:** Membuat atau memasukkan data record (baris) baru
- **UPDATE:** Mengubah objek pada database. Sebagai contoh digunakan untuk update tabel
- **DELETE:** Menghapus objek pada database

## DCL (Data Control Language)

DCL adalah kategori perintah SQL untuk mengontrol akses ke database. Beberapa contoh:

- **GRANT:** Memberikan hak istimewa kepada pengguna
- **REVOKE:** Mengambil kembali hak istimewa dari pengguna

## Field or Column (Kolom)

Field adalah kolom tabel yang didesain untuk mengelola informasi spesifik untuk record tabel (contoh: ID, name).

## Record or Row (Baris)

Record adalah garis horizontal pada tabel yang berisi satu set data lengkap.

## SQL Constraint

SQL constraint digunakan untuk memberikan aturan secara spesifik pada data dalam tabel. Ini untuk memastikan akurasi dan reliabilitas data dalam tabel.

### Contoh Beberapa Constraint:

- **NOT NULL:** Memastikan kolom tidak boleh kosong
- **UNIQUE:** Memastikan semua nilai dalam kolom berbeda
- **PRIMARY KEY:** Kombinasi NOT NULL dan UNIQUE
- **FOREIGN KEY:** Menghubungkan dua tabel

Contoh format:
```sql
CREATE TABLE nama_table (
    field_name tipe_data constraint
);
```

## Generate Backup Database

Tulis code ini pada terminal untuk menjalankan aplikasi mysqldump:
```bash
mysqldump -u root -p nama_database > nama_file_backup.sql
```

## Restore Database

1. Sebelum restore database, siapkan database kosong terlebih dahulu
2. `CREATE DATABASE nama_database;`
3. Pada terminal, jalankan perintah berikut ini:
   ```bash
   mysql -u root -p nama_database < nama_file_backup.sql
   ```

Cara di atas digunakan untuk backup dan restore database.
Source: https://phoenixnap.com/kb/how-to-backup-restore-a-mysql-database

## Untuk Melihat Isi Tabel

```sql
SELECT * FROM nama_table;
```

Untuk melihat seluruh list data dalam tabel, nilai ROW dan COLUMN.

Contoh output:

nama | harga 
--- | ---
Soto | 5000 
Rawon | 5000

## SQL Date Types

- `DATE` dengan format YYYY-MM-DD
- `DATETIME` dengan format YYYY-MM-DD HH:MM:SS
- `TIMESTAMP` untuk menyimpan waktu dengan timezone
- `YEAR` untuk menyimpan tahun dari 1901 ke 2155 dan 0000

## Data Integrity

Contoh data integrity pada database:
- **Entity Integrity:** Memastikan setiap baris memiliki primary key unik
- **Domain Integrity:** Memastikan data yang dimasukkan sesuai dengan tipe data kolom

## Contoh Pengambilan Data

```sql
SELECT nama_kolom FROM nama_table;
```

Digunakan untuk mengambil data dalam nama kolom yang dituju.

## Operator Perbandingan

```sql
SELECT * FROM purchases
WHERE price >= 10;
```

Operator perbandingan yang tersedia:
- `a < b` untuk mencari a lebih kecil dari b
- `a <= b` untuk mencari lebih kecil atau sama dengan b
- `a > b` untuk mencari a lebih besar dari b
- `a >= b` untuk lebih besar atau sama dengan b
- `a = b` untuk mencari yang sama persis dengan b
- `a != b` atau `a <> b` untuk mencari yang tidak sama dengan b

Contoh:
```sql
SELECT * FROM nama_database
WHERE nama_kolom <= 1000;
/* 1000 adalah data INT */
```

Ini digunakan untuk mengambil data INT di bawah atau sama dengan 1000.

## LIKE

LIKE digunakan untuk mengambil data yang mirip atau mengandung kata kunci tertentu.

```sql
SELECT * FROM nama_database 
WHERE nama_kolom LIKE '%kunci%';
```

Data yang akan diambil akan memiliki kemiripan atau kata kunci 'kunci'. Sama seperti `%` adalah wildcard yang digunakan untuk bypass atau melewati kata sebelumnya atau selanjutnya sesuai dengan penempatan wildcard.

Contoh:
- `name%` kata kunci yang dilewati adalah setelah dari 'name'
- `%name` kata kunci yang dilewati adalah sebelum dari 'name'
- `%name%` kata kunci yang dilewati adalah sebelum dan sesudah dari 'name'

## Kolom NULL

Record atau row yang tidak menyimpan data bisa disebut 'NULL'.

Kolom atau baris tidak menyimpan nilai apapun, maka kolom atau baris tersebut adalah NULL.

## Menampilkan Baris yang Berisi NULL

```sql
SELECT * FROM nama_database
WHERE nama_kolom IS NULL;
```

Untuk memilih baris yang berisi 'NULL' atau kosong.

```sql
SELECT * FROM nama_database
WHERE nama_kolom IS NOT NULL;
```

Untuk mengambil baris yang tidak 'NULL' atau kosong.

## AND

```sql
SELECT * FROM nama_database
WHERE nama_kolom = 'kata kunci'
AND nama_kolom2 = 'kata kunci ke 2';
```

AND digunakan untuk menambah kondisi. Penggunaannya seperti operator `&&` pada JavaScript (if statement). Saat menggunakan 'AND', tidak perlu menulis 'WHERE' di belakangnya.

## OR

```sql
SELECT * FROM nama_database
WHERE nama_kolom = 'kata kunci'
OR nama_kolom2 = 'kata kunci ke 2';
```

OR digunakan ketika salah satu kondisi terpenuhi, data akan diambil.

## ORDER BY

```sql
SELECT * FROM nama_database
WHERE nama_kolom = 'kata kunci'
ORDER BY nama_kolom DESC;
```

Jika tanpa 'WHERE':
```sql
SELECT * FROM nama_database
ORDER BY nama_kolom DESC;
```

ORDER BY digunakan untuk mengurutkan data pada kolom yang dipilih sesuai dengan method yang dipilih:
- **ASC** (menaik, dari bawah ke atas) contoh: [1,2,3,4,5,6,7,8]
- **DESC** (menurun, dari atas ke bawah) contoh: [8,7,6,5,4,3,2,1]

## LIMIT

LIMIT menentukan jumlah baris yang akan dikeluarkan sebagai output.

```sql
SELECT * FROM nama_database
WHERE nama_kolom = 'kata kunci'
LIMIT 5;
```

Perintah di atas akan membatasi output hanya 5 baris pertama.

## SQL Query

Pada akhir SQL statement atau SQL query, tulis semicolon (`;`) pada akhir statement.

Queries adalah set instruksi yang diberikan pada RDBMS mengenai informasi apa yang mau diambil.

## Wrap Up Rangkuman

Mari kita rangkum perintah SQL yang sudah dipelajari:

- `WHERE` digunakan untuk mencari kata kunci yang dituju
- `ORDER BY` digunakan untuk mengurutkan data
- `SELECT` digunakan untuk memilih atau mengambil kolom
- `FROM` digunakan untuk mengambil atau memilih tabel
- `USE` digunakan untuk mengambil atau memilih objek seperti database
- `CREATE` digunakan untuk membuat objek seperti database
- `LIKE` digunakan untuk mengambil data yang mirip
  - Format: `WHERE nama_kolom LIKE '%nama%'`
- `IS NULL` digunakan untuk mengambil data kolom yang memiliki nilai NULL atau kosong
  - Format: `WHERE nama_kolom IS NULL`
- `AND` digunakan untuk menambahkan kondisi pada query
  - Format: `WHERE nama_kolom = 'str' AND nama_kolom2 = 'str2'`
- `LIMIT` digunakan untuk membatasi data yang keluar (output)
  - Format: `WHERE nama_kolom = 'str' LIMIT 5`

## DROP Table

```sql
DROP TABLE table_name;
```

Digunakan untuk menghapus objek tabel yang dituju. Harus hati-hati dengan menggunakan statement tersebut. Sekali terhapus maka akan hilang selamanya.

## INSERT INTO Table

```sql
INSERT INTO nama_table (nama_kolom, nama_kolom2) 
VALUES ('value1', 'value2');
```

Pastikan urutan 'value' sudah sesuai dengan urutan kolom yang kita inginkan.

Jika tidak ditulis urutannya, maka akan diambil urutan yang sudah ada sebelumnya di dalam tabel.

## UPDATE Query

```sql
UPDATE nama_table 
SET nama_kolom = 'value baru' 
WHERE nama_kolom = 'value lama';
```

Atau:
```sql
UPDATE nama_table 
SET nama_kolom = 'value baru';
```

Jika menggunakan cara di atas tanpa WHERE maka semua data dalam 'nama_kolom' yang dipilih akan berubah semua.

'UPDATE' dan 'SET' dengan menggunakan statement ini bisa digunakan untuk mengubah record atau baris yang lama.

## DELETE Query

```sql
DELETE FROM nama_table
WHERE nama_kolom = 'value';
```

Statement di atas bisa digunakan untuk menghapus record atau baris yang dipilih.

## GROUP BY

```sql
SELECT nama_kolom, SUM(nilai_kolom) 
FROM nama_table 
GROUP BY nama_kolom;
```

`GROUP BY` adalah statement untuk mengatur data yang identik menjadi grup.

`SUM` adalah statement untuk menghitung hasil kolom numeric yang kita pilih.

Contoh:

**Sebelum GROUP BY:**

nama | pengeluaran
--- | ---
Budi | 5000
Budi | 10000

**Setelah GROUP BY:**

nama | SUM(pengeluaran) 
--- | ---
Budi | 15000

### Fungsi Agregat Lainnya:

- `SUM()` digunakan untuk menghitung total data dalam kolom yang dipilih
- `AVG()` digunakan untuk mencari nilai rata-rata pada kolom
- `COUNT()` digunakan untuk mendapatkan berapa banyak baris yang sesuai dengan kriteria
- `MAX()` digunakan untuk mendapatkan nilai tertinggi
- `MIN()` digunakan untuk mendapatkan nilai terendah

Contoh `COUNT()`:
```sql
SELECT nama, COUNT(harga)
FROM nama_table 
WHERE harga <= 10000;
```

Total baris yang akan dicari adalah yang harus di bawah dan sama dengan 10000.

## DISTINCT

`DISTINCT` adalah kata kunci yang digunakan untuk mengeliminasi records atau baris yang memiliki value duplikat.

```sql
SELECT DISTINCT nama_kolom
FROM nama_table 
ORDER BY nama_kolom;
```

Perintah di atas digunakan untuk mengeliminasi records atau baris yang memiliki value duplikat dan diurutkan. `ORDER BY` jika tidak ada method yang diisi maka akan menggunakan `ASC` secara default.

## Tipe Data

Sebagai contoh dalam Excel atau aplikasi penyimpanan data spreadsheet lainnya, kita bisa menentukan pada kolom tertentu harus kita isi dengan data berbentuk angka atau huruf. Akan tetapi penggunaan kolom tersebut bisa saja berubah-ubah.

Dalam SQL, jika kolom tersebut dibuat untuk tipe data number, maka seterusnya akan begitu. Kita bisa memilih tipe data apa untuk kolom yang kita buat sesuai dengan kebutuhan.

### Contoh Tipe Data pada SQL:

### Data Integer

- `TINYINT` tipe data ini akan mengambil nilai dari (-128 sampai 127)
- `SMALLINT` tipe data ini akan mengambil nilai dari (-32768 sampai 32767)
- `MEDIUMINT` tipe data ini akan mengambil nilai dari (-8388608 sampai 8388607)
- `INT` tipe data ini akan mengambil nilai dari (-2147483648 sampai 2147483647)
- `BIGINT` tipe data ini akan mengambil nilai dari (-9223372036854775808 sampai 9223372036854775807)

### Data Float

`FLOAT` adalah tipe data angka yang memiliki bagian desimal di akhir angka atau memiliki tanda 'titik' yang menandakan bilangan desimal. Contoh: 0.9 atau 3.14

Tipe data float cocok digunakan untuk variabel yang berisi angka pecahan seperti hasil pembagian dan lainnya.

### DECIMAL

Tipe data number khusus yang ditentukan jumlah precision dan scalenya.

Sebagai contoh:
- `DECIMAL(5,2)` bisa menghasilkan output seperti ini '999.99'
- `DECIMAL(3,1)` output '99.9'
- `DECIMAL(3)` output '999'

### CHAR and VARCHAR

Adalah tipe data untuk menyimpan bentuk 'string' seperti kata, angka, dan bentuk karakter spesial.

- `CHAR(size)` ini adalah fixed length string. Jika disimpan di sini 10, maka akan ada 10 karakter yang tersimpan (ditambahkan spasi jika kurang).
  - Input: `CHAR(7)` dengan value 'namaku'
  - Output: 'namaku ' (dengan spasi tambahan)

- `VARCHAR(size)` ini adalah variable length string yang bisa otomatis menyesuaikan data yang disimpan.
  - Input: `VARCHAR(7)` dengan value 'namaku'
  - Output: 'namaku' (tanpa spasi tambahan)

### Date and Time Data Type

Tipe data ini digunakan untuk menyimpan data berformat waktu. Tanggal, bulan, tahun, dan jam.

- `DATE` data yang disimpan berformat 'YYYY-MM-DD'
- `DATETIME` data yang disimpan berformat 'YYYY-MM-DD HH:MM:SS'
- `TIMESTAMP` mirip dengan DATETIME tapi dengan timezone
- `YEAR` data yang disimpan mulai dari 1901 ke 2155 dan 0000

### ENUM

Adalah tipe data string yang bisa kita tentukan pilihannya atau opsinya.

```sql
ENUM('opsi1', 'opsi2')
```

Contoh:
```sql
ENUM('pria', 'wanita')
```

Dalam statement di atas, data yang diperbolehkan masuk adalah data 'pria' atau 'wanita'. Selain itu akan ditolak oleh SQL.

## Mengubah Tabel

```sql
ALTER TABLE nama_table 
    ADD COLUMN nama_kolom TEXT,
    DROP COLUMN nama_kolom,
    RENAME COLUMN kolom_lama TO nama_baru,
    MODIFY nama_kolom VARCHAR(100) AFTER nama_kolom,
    MODIFY nama_kolom TEXT FIRST;
```

**Break down kata kunci:**
- `ALTER TABLE` digunakan untuk memilih tabel mana yang akan diubah
- `ADD COLUMN` digunakan untuk menambahkan kolom pada tabel
- `DROP COLUMN` digunakan untuk menghapus kolom
- `RENAME COLUMN` digunakan untuk mengubah nama kolom
- `MODIFY, AFTER, FIRST` digunakan untuk memindahkan urutan kolom

## Update Table

```sql
UPDATE nama_table 
SET nama_kolom = 'nilai_baru',
    nama_kolom2 = 'nilai_baru2'
WHERE nama_kolom = 'string';
```

Query di atas digunakan untuk mengubah data dalam kolom secara spesifik. Jika tidak menggunakan 'WHERE' maka keseluruhan data akan diubah.

## Rename Table

```sql
ALTER TABLE nama_table 
RENAME TO nama_table_baru;
```

## JOIN

```sql
SELECT * FROM nama_table1
JOIN nama_table2 
ON nama_table1.kolom_value = nama_table2.kolom_value;
```

Dengan query di atas kita bisa menghubungkan dua tabel dan menempatkannya bersandingan atau bersebelahan dengan statement 'ON' dan '='. Tabel akan bersebelahan jika value mereka sama.

### Jenis JOIN:

- **INNER JOIN:** Mengembalikan baris yang memiliki kecocokan di kedua tabel
- **LEFT JOIN:** Mengembalikan semua baris dari tabel kiri dan yang cocok dari tabel kanan
- **RIGHT JOIN:** Mengembalikan semua baris dari tabel kanan dan yang cocok dari tabel kiri
- **FULL OUTER JOIN:** Mengembalikan semua baris dari kedua tabel

## SHOW CREATE TABLE

```sql
SHOW CREATE TABLE nama_table;
```

Perintah ini akan menunjukkan secara penuh detail mengenai query SQL yang masuk dalam pembuatan tabel.

## DESCRIBE

```sql
DESCRIBE nama_table;
```

Akan menunjukkan field, type dan lainnya yaitu informasi dasar pada tabel tersebut.

## Note Kecil

Contoh data modeling adalah relational databases. Data modeling adalah proses membuat struktur database yang efisien dan terorganisir.

## Latihan SQL

Panduan latihan:
[Latihan SQL](../document/latihan-bahasa/latihan-sql.md)

## Tips Belajar SQL

1. **Praktik Langsung:** Cara terbaik belajar SQL adalah dengan praktek langsung membuat query
2. **Mulai dari Sederhana:** Mulai dari query SELECT sederhana, lalu tingkatkan kompleksitasnya
3. **Pahami Konsep JOIN:** JOIN adalah salah satu konsep paling penting dalam SQL
4. **Gunakan EXPLAIN:** Gunakan EXPLAIN untuk memahami bagaimana query kamu dijalankan
5. **Backup Selalu:** Selalu backup database sebelum melakukan operasi DELETE atau UPDATE yang besar

## Common Mistakes dan Cara Menghindarinya

1. **Lupa WHERE pada UPDATE/DELETE:** Bisa menyebabkan semua data berubah atau terhapus
2. **Tidak Menggunakan Primary Key:** Membuat data sulit diidentifikasi
3. **SQL Injection:** Selalu validasi input dari user
4. **Tidak Melakukan Normalisasi:** Data menjadi redundan dan sulit maintain

## Pranala Menarik

Berikut beberapa sumber belajar tambahan yang bisa kamu eksplorasi:

- https://dev.mysql.com/doc/refman/8.0/en/alter-table.html
- https://stevenpcurtis.medium.com/what-is-a-floating-point-number-6991f2f85a28
- https://www.duniailkom.com/mengenal-tipe-data-float-dan-cara-penulisan-float-dalam-php/
- https://www.youtube.com/watch?v=xYBclb-sYQ4
- https://en.wikipedia.org/wiki/Composite_key
- https://www.kelasexcel.id/2014/09/pengertian-row-column-cell-dan-range-excel.html
- https://www.youtube.com/watch?v=HXV3zeQKqGY&t=1504s
- https://www.w3schools.com/sql/sql_syntax.asp
- https://mode.com/sql-tutorial/introduction-to-sql/
- https://www.analyticsvidhya.com/blog/2020/07/8-sql-techniques-data-analysis-analytics-data-science/
- https://www.studytonight.com/dbms/introduction-to-sql.php
- https://www.sqlshack.com/introduction-to-sql/
- https://way2tutorial.com/sql/sql-introduction.php
- https://aws.amazon.com/id/relational-database/
- http://www.agiledata.org/essays/keys.html
- https://www.w3schools.com/sql/sql_examples.asp
- https://www.codepolitan.com/membuat-database-dan-tabel-di-mysql-5884222be38fa
- https://www.tutorialspoint.com/sql/sql-rdbms-concepts.htm
- https://www.tutorialspoint.com/sqlite/sqlite_python.htm
