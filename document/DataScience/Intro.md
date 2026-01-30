# Pengenalan Data Science

Di era digital ini, kita menyaksikan ledakan volume data yang luar biasa besar di internet. Data ini begitu masif sehingga mustahil untuk diolah dengan cara-cara lama. Dari sinilah lahir sebuah terobosan yang dulu dikenal sebagai *data mining* dan kini lebih populer dengan sebutan **Data Science**.

***

## Apa Itu Data Science dan Mengapa Penting?

Secara sederhana, Data Science adalah disiplin ilmu yang bertugas untuk **mengumpulkan**, **menganalisis**, dan pada akhirnya **menentukan prospek bisnis** dari data yang ada. Tanpa adanya Data Science, triliunan data yang tersimpan hanyalah tumpukan "sampah digital" yang tidak memiliki nilai dan hanya akan membebani perangkat penyimpanan.

Saat ini, data sering kali dinilai lebih berharga daripada minyak bumi atau emas. Alasannya, dari data kita bisa mendapatkan informasi mendalam yang bisa digunakan untuk pengambilan keputusan di berbagai bidang, mulai dari ekonomi hingga pasar saham.

### Hubungan dengan Kecerdasan Buatan (AI) & Machine Learning

Data Science sering disandingkan dengan **Kecerdasan Buatan (AI)** dan **Machine Learning**.

* **Kecerdasan Buatan (AI)** adalah sebuah set latihan yang bertujuan agar mesin atau komputer memiliki kemampuan kognitif seperti manusia.
* **Machine Learning** adalah metode pelatihan bagi komputer agar mampu mengklasifikasikan informasi berdasarkan pengalaman dari data yang telah diberikan.

Persamaan mendasar antara ketiganya adalah ketergantungan pada *training data*. *Training data* merupakan kumpulan data yang sengaja disiapkan untuk melatih AI atau Machine Learning agar dapat menjalankan tugas atau protokol yang kita inginkan. Karena itu, bisa disimpulkan bahwa AI dan Machine Learning adalah cabang dari Data Science yang berlandaskan pada data.

***

## Proses dalam Data Science

Dalam praktiknya, terdapat beberapa proses utama yang perlu dilakukan dalam sebuah proyek Data Science:

1.  **Memahami Permasalahan**: Tahap awal untuk mengidentifikasi tujuan dan masalah yang ingin dipecahkan.
2.  **Persiapan dan Penyesuaian Sampel Data**: Mengumpulkan dan mempersiapkan data yang relevan.
3.  **Pembangunan Model**: Membuat model analisis berdasarkan data yang telah disiapkan.
4.  **Aplikasi dan Evaluasi Model**: Menerapkan model pada dataset untuk melihat hasil atau *output* yang dihasilkan.
5.  **Penyebaran dan Pemeliharaan Model**: Mengimplementasikan model ke dalam sistem yang berjalan dan terus memeliharanya.

***

## Konsep-Konsep Kunci

### Model Data

Dalam Data Science, **model** diartikan sebagai representasi hubungan antar variabel dalam sebuah kumpulan data. Setiap variabel saling terikat dan melengkapi satu sama lain.

Contoh sederhananya adalah **model Nomor Induk Mahasiswa (NIM)**. Model ini terdiri dari beberapa variabel yang saling berhubungan, seperti:

* Nama Mahasiswa
* Nomor Mahasiswa
* Tanggal Pendaftaran
* Jurusan
* Fakultas

### Bahasa Alami (Natural Language)

Bahasa alami adalah bentuk data yang **tidak terstruktur**. Untuk menganalisisnya, diperlukan keahlian khusus dari pakar bahasa. Analisisnya berfokus pada pola penggunaan bahasa, analisis sentimen, dan berbagai bentuk analisa lain yang berbasis bahasa.

### Data Pre-processing

Pada kondisi nyata, *big data* cenderung bersifat *noise* (mengandung gangguan), *missing* (ada bagian yang hilang), dan inkonsisten. Faktor-faktor seperti kurangnya akurasi dan kelengkapan data dapat membuatnya tidak bisa diandalkan.

Untuk meningkatkan kualitas data, dilakukanlah proses yang disebut **data pre-processing**. Ini adalah tahap persiapan data sebelum masuk ke proses *data mining*. Beberapa tahapan yang umum dilakukan antara lain:

* **Data Cleaning**: Menghapus data yang tidak konsisten atau tidak relevan.
* **Data Integration**: Menggabungkan data dari berbagai sumber.
* **Data Reduction**: Mengurangi volume data tanpa menghilangkan informasi penting.
* **Data Transformation**: Mengubah format data agar sesuai untuk proses analisis.

***

## Mengenal Statistik dalam Data Science

Statistik memegang peranan vital dalam Data Science dan secara umum terbagi menjadi dua, yaitu statistik deskriptif dan inferensial.

### Statistik Deskriptif

Statistik deskriptif adalah metode eksplorasi data yang bertujuan untuk memberikan **gambaran atau informasi ringkas** mengenai suatu kumpulan data (dataset). Dengan metode ini, dataset yang sangat besar dapat disajikan dalam bentuk yang lebih sederhana namun tetap menggambarkan informasi intinya.

Contoh penerapannya adalah menghitung rata-rata pendapatan tahunan karyawan atau rentang tinggi badan siswa di satu kelas.

Terdapat tiga fokus utama dalam statistik deskriptif:

1.  **Ukuran Pemusatan Data**: Menggunakan metode seperti **Mean** (rata-rata), **Median** (nilai tengah), dan **Mode** (nilai yang paling sering muncul). Untuk mencari median, data harus diurutkan dari terkecil hingga terbesar.
2.  **Ukuran Penyebaran Data**: Menggunakan metrik seperti **Range** (selisih nilai maksimum dan minimum), **Variance**, dan **Standard Deviation**. Varian dan standar deviasi diukur berdasarkan selisih antara setiap nilai data dengan nilai mean-nya.
3.  **Bentuk Distribusi Data**: Menggunakan teknik seperti **Symmetry**, **Skewness**, dan **Kurtosis** untuk memahami bentuk sebaran data.

Analisis deskriptif bisa dilakukan secara **univariat** (menganalisis satu atribut) atau **multivariat** (menganalisis hubungan antara dua atribut atau lebih). Contoh analisis multivariat adalah mencari **korelasi**, misalnya untuk memahami hubungan antara cuaca dengan penjualan minuman dingin.

### Statistik Inferensial

Statistik inferensial adalah teknik yang digunakan untuk **menarik kesimpulan mengenai suatu populasi** besar berdasarkan data sampel yang lebih kecil. Teknik ini sangat berguna ketika sumber daya untuk meneliti keseluruhan populasi terbatas. Oleh karena itu, peneliti dapat mengambil sampel dari beberapa individu untuk dianalisis, lalu hasilnya digeneralisasi untuk populasi yang lebih besar.

Beberapa konsep dasar yang digunakan dalam statistik inferensial adalah teori probabilitas serta variabel random diskrit dan kontinu.

Pengantar Ilmu Data: Dari Probabilitas hingga Pembelajaran Mesin
Ilmu data adalah bidang yang menggunakan berbagai teori dan teknik untuk mengekstrak wawasan dari data. Panduan ini akan membahas konsep-konsep fundamental yang menjadi dasar dalam analisis dan pemodelan data.

Pengantar Ilmu Data: Dari Probabilitas hingga Pembelajaran Mesin
Ilmu data adalah bidang yang menggunakan berbagai teori dan teknik untuk mengekstrak wawasan dari data. Panduan ini akan membahas konsep-konsep fundamental yang menjadi dasar dalam analisis dan pemodelan data.

## 🎲 Fondasi: Teori Probabilitas
Untuk membangun model dari sampel populasi, kita memerlukan pendekatan teori probabilitas. Probabilitas adalah angka yang menunjukkan tingkat atau derajat ketidakpastian suatu fenomena. Ada tiga teori utama dalam probabilitas:

Teori Laplace: Teori ini menyatakan bahwa semua kejadian memiliki peluang yang sama untuk terjadi. Contohnya, saat melempar dadu, probabilitas untuk mendapatkan angka ganjil (1, 3, atau 5) adalah 1/2, karena ada tiga angka ganjil dari total enam kemungkinan sisi dadu.

Teori Frequentist: Menurut teori ini, probabilitas suatu kejadian bergantung pada seberapa sering kejadian itu terjadi dalam sejumlah besar percobaan. Semakin banyak percobaan pelemparan dadu yang dilakukan, semakin tinggi kemungkinan kita akan mendapatkan angka ganjil.

Teori Bayesian (Subjektif): Dalam teori ini, peneliti menentukan nilai kemungkinan berdasarkan informasi yang telah mereka miliki sebelumnya, yang disebut sebagai "a priori".

## 📊 Statistik Inferensial: Sampling & Uji Hipotesis
Dalam statistik inferensial, kita membuat asumsi tentang populasi berdasarkan sampel acak yang kita ambil. Sampel ini adalah perwakilan terbatas dari populasi yang lebih besar.

Penentuan Sampel
Ada tiga metode dasar untuk menentukan sampel:

Berdasarkan populasi yang jumlahnya telah diketahui.

Berdasarkan populasi yang jumlahnya tidak diketahui.

Berdasarkan jumlah sampel bertingkat.

Distribusi Probabilitas
Distribusi probabilitas adalah cara umum yang digunakan untuk menentukan pola yang ada di dalam suatu data.

Uji Hipotesis
Uji hipotesis adalah kesimpulan sementara yang kebenarannya harus dibuktikan melalui penelitian. Ini berfungsi sebagai titik awal untuk mengonfirmasi pernyataan dari sampel yang telah dikumpulkan.

Hipotesis Nol (H 
0
​
 ): Ini adalah pernyataan negatif yang dianggap benar sampai terbukti salah. Dalam analogi persidangan, ini sama dengan "praduga tak bersalah," di mana seseorang dianggap tidak bersalah kecuali terbukti sebaliknya.

Hipotesis Alternatif (H 
1
​
 ): Ini adalah pernyataan positif yang dianggap salah kecuali terbukti benar. Dalam analogi yang sama, ini adalah pernyataan bahwa seseorang telah melakukan kejahatan.

Terdapat dua tipe uji hipotesis:

Uji Langsung (Directional): Hipotesis yang arahnya jelas, di mana peneliti dapat melakukan uji satu arah (uji kanan atau uji kiri).

Uji Tidak Langsung (Non-directional): Hipotesis yang tidak memiliki arah tertentu. Biasanya, hipotesis ini menggunakan frasa "sama dengan" pada H 
0
​
 .

## 📝 Memahami Data
Kualitas dan bentuk data sangat memengaruhi hasil analisis.

Kualitas dan Keterbatasan Data
Data berkualitas rendah dapat mempersulit proses prediksi. Beberapa masalah kualitas data yang umum termasuk:

Noise dan outlier (nilai ekstrem).

Nilai yang hilang atau salah.

Duplikasi data.

Beberapa komponen utama yang menjadi indikator data berkualitas baik adalah:

Akurasi: Baik secara posisi, waktu, maupun atribut.

Kelengkapan dan Konsistensi.

Reliabilitas dan Representatif.

Bentuk Dasar Data
Data memiliki dua bentuk dasar yang menjelaskan identitasnya:

Data Diskrit: Diperoleh dari hasil perhitungan dan tidak memiliki satuan unit, contohnya jumlah penduduk.

Data Kontinu: Diperoleh dari hasil pengukuran dan memiliki satuan, seperti suhu (Celcius) atau berat (kilogram).

Jenis Analisis Data
Terdapat beberapa jenis analisis berdasarkan waktunya:

Analisis Historis: Menjelaskan data dari masa lalu.

Analisis Deskriptif: Menjelaskan data dari masa lalu dan masa kini.

Analisis Prediktif: Menjelaskan kejadian yang mungkin terjadi di masa depan.

## 🤖 Model Prediktif dan Algoritma
Model prediktif digunakan untuk membuat prediksi tentang masa depan berdasarkan data historis.

Regresi
Regresi adalah model yang digunakan untuk memahami hubungan antara variabel bebas (indikator) dan variabel terikat.

Regresi Linear Sederhana: Menganalisis hubungan antara satu variabel bebas dan satu variabel terikat.

Regresi Linear Berganda (Multiple): Menganalisis hubungan variabel yang jumlahnya lebih dari dua.


Dilisensikan oleh Google
Pohon Keputusan (Decision Tree)
Ketika hubungan antar variabel tidak linear, algoritma pohon keputusan dapat digunakan. Algoritma ini membagi dataset menjadi bagian-bagian yang lebih kecil untuk membuat model prediksi. Beberapa terminologi penting dalam pohon keputusan meliputi Root Node, Splitting, Decision Node, dan Pruning.

## 🧠 Klasifikasi dan Pembelajaran Mesin
Klasifikasi adalah proses penting untuk mengkategorikan data ke dalam kelas atau label yang telah ditentukan.

Proses Klasifikasi
Proses ini biasanya melibatkan pembagian data menggunakan prinsip Pareto (80/20), di mana 80% data digunakan untuk pelatihan (training) model dan 20% sisanya digunakan untuk pengujian (testing) model. Tujuannya adalah membuat model yang dapat melakukan klasifikasi otomatis pada data uji.

Bentuk-Bentuk Pembelajaran Mesin
Supervised Learning (Pembelajaran Terbimbing)
Komputer belajar dari data yang sudah diberi label. Contohnya, komputer dilatih dengan ribuan gambar berlabel "kucing" dan "anjing" untuk mengenali polanya. Setelah itu, komputer diuji dengan gambar baru tanpa label untuk melihat apakah ia bisa mengklasifikasikannya dengan benar. Penerapan di dunia nyata adalah algoritma rekomendasi YouTube, yang menyarankan konten serupa berdasarkan riwayat tontonan pengguna.

Unsupervised Learning (Pembelajaran Tak Terbimbing)
Komputer mengklasifikasikan data yang tidak memiliki label. Peneliti tidak memiliki ekspektasi output tertentu; sebaliknya, komputer secara mandiri mengidentifikasi pola atau ciri khas dalam data tersebut. Fokus utamanya adalah pada data input, sementara output sepenuhnya ditentukan oleh mesin.

Semi-Supervised Learning
Ini adalah gabungan dari supervised dan unsupervised learning, di mana sebagian data memiliki label dan sebagian lagi tidak.

Reinforcement Learning (RL)
Ini adalah pendekatan pembelajaran mesin yang didasarkan pada data real-time, berbeda dengan model lain yang menggunakan data historis. Algoritma RL berfokus pada analisis pola data real-time dan belajar melalui sistem reward (jika melakukan fungsi yang benar) dan punishment (jika melakukan fungsi yang salah). Contohnya adalah optimasi iklan berdasarkan Click-Through Rate (CTR), di mana iklan yang mendapat banyak interaksi akan lebih sering ditampilkan untuk efektivitas dana.



## Bab lanjutan
- [Natural Language Processing](./AI-NLP.md)
- [LLM secara gratis](./FreeLLM.md)



## Referensi
- Pengantar Data Science, bumi aksara, 2022
