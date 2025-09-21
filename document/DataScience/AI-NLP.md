# NLP ( Natural Language Processing )

Natural Language Processing (NLP) merupakan bidang pembelajaran untuk Machine agar mereka bisa memahami kosakata manusia. Dengan NLP Machine akan dapat memahami konteks dari kata, tidak didasarkan dari kata yang individu.

NLP disini juga diterapkan pada bidang seperti: pengenalan suara dan Computer vision.

Contoh paling sederhana mengenai NLP:

- Melakukan analisa kata didalam kalimat:
  Semisal "Game ini seru sekali!" analisa akan dilakukan untuk menentukan apakan ini sentimen posisitif atau tidak.

- menerjemahkan teks
- meringkas teks
- dan lain-lain yang berhubungan dengan pengelolahan teks

## 1. Pondasi dari Prosesing bahasa

## 1.1 kata dan tokens

NLP disini tidak sesederhana suatu bentuk 'kata' mereka lebih kompleks dari itu. 

- Tantangan: Pada suatu bahasa, definisi dari setiap kata yang ada tidak memiliki batas dan perekembangan bahasa tidak ada batasnya. dengan kata lain, pada tata bahasa akan selalu ditemukan kata yang tidak dikenali
- Ukuran klasifikasi kecil (Subwords). Machine saatg ini masih kesulitan untuk melakukan anilasi kata ataupun kalimat yang kompleks, oleh karena itu mereka memecahnya menjadi bagian-bagian kecil yang dikenal sebagai Subwords.
- Algoritma Tokenization:
  - Proses pemecahan kalimat menjadi bagian-bagian kecil itu disebut sebagai Token. contoh kata "lower" akan dipecah menjadi "low" dan "er"
  - Aturan berdasarkan Tokenization: aturan inti digunakan untuk memecah kata ( koma, tanda baca, dll ) dan melebarkan kata singkatan (dll ke dan lain-lain )
  - Byte-pair Encoding (BPE): adalah algoritma untuk tokenisasi. BPE akan mengelolah huruf atau subword menjadi token yang lebih panjang untuk diproses machine.
  - Wordpiece algorithm: adalah variasi dari BPE yang berpendekatan berdasarkan "bagianmana yang lebih meningkatkan kemungkinan pada tokenisasi language model"
 
- Corpora( Koleksi teks): NLP bergantung terhadarp corpora untuk pelatihan dan evaluasi. Corpora disini digunakan untuk pelatihan didasarkan "Representasi dari bahasa, genre, dan grup sosial" yang sesuai pelatihan. Pengunaan dari Datasheets dan kartu model.

## 1.2 Unicode dan encoding

- Unicode: "Merupakan system yang menjadi representasi huruf didalam berbagai macam script menulis yang ada diseluruh dunia"
- UTF-8: adalah bentuk metode encoding untuk represetnasi dari unicode point di file text.

## 1.3 Regular Expressions

"Bentuk notasi algebra untuk string dari set huruf" Disini Regex digunakan untuk melakukan pemilhan, pencarian, dan manipulasi text string, Proses yang krusial untuk pre-tokenization di algoritma BPE. 

## 1.4 Minimum Edit Distance

Secara definisi ini bisa diartikan "nilai minimum untuk edit operasi ( +, -, /) butuh transformasi satu string ke string yang lain." Tujuannny adalah memperbaiki adannya typo pada text yang dianalisa.

# 2. Language Model

## 2.1. N-gram Language Models

- Definisi: N-grams mungkin adalah bentuk paling sederhana daari suatu model bahasa. mereka disini menempatkan probability ke urutan dari kata atau token dan prediksi kata/token selanjutnya berdasarkan perhitungan Asumsi Markov.
- Probability Estimation: Probability biasannya dilakukan estimasi mengunakan "Maximum Likehooh Estimation (MLE)" dengan menghitung munculnya n-gram pada pelatihan corpus.
- Smoothing: Penyelesaian masalah jika n-grams tidak ditemukan pada data latihan dengan cara alokasi ulang probability mass.
- Evaluasi:
  - Perplexity: metrix standart yang digunakan untuk perhitungan n-gram models.

## 2.2 Neural Language Models (Beyond N-grams)

- Limit dari N-grams: N-grams disini tumbuh dan berkembang dengan tujuan meningkatkan order dan inability untuk menciptakan(Generalize) kata yang tidak diketahui.
- Neural Appropach: Neural Language Model didasarkan dari kata ke suatu ruang dimana dipertemukan dengan konteks yang mirip atau menyerupai. Disini akan membutuhkan ukuran energi yang cukup banyak untuk dilatih.
- Feedforward Neural Language models: Mengambil representasi dari kata sebelumnya menjadi input dan output dari probability distribusi dari kata selanjutnya.
- Transformer-based Large Language Models (LLMs): adalah program AI complex yang dapat memahami dan membuat bahasa manusia. Mereka dissini memilki "perhatian khusus" untuk menghubungkan kata melalui teks panjang dan "mengingat" puluhan ribu kata disaat bersamaan. ini membuat mereka sangat bagus uintuk membuat text baru berdasarkan apa yang kamu tanyakan, potensi ini sangat bisa melebarkan kemampuan dari komputer dalam mengelolah bahasa.

## 3 The Big Change: Large Language Model (LLMs)

- Akhir-akhir ini, banyak sekali macam AI model yang kita kenal sebagai LLM seperti GPT dan Grok datang dan mengubah perkembangan dari NLP. 

- Ini adalah bentuk kecerdasan buatan sekala masive, yang telah 'membaca' teks dengan jumlah besar( triliunan "parameters" atau bit dari suatu pengetahuan )

- Nilai jualnya adalah memiliki kemampuan superpower untuk memahami dan membuat ulang teks manusia, memahami suatu pola, dan bentuk pengelolahan lain didalam suatu teks bahasa.

## 4. Large Language Models (LLMs) and Advanced Training 

### 4.1 Apa itu LLMs?

Large Language Models adalah bentukan dari sistem AI yang bisa memahami dan mebuat teks selayaknya manusia. Kita bayangkan sebagai system yang berjalan sendiri dengan pengalaman telah membaca miliaran buku dan website untuk memahami bahasa manusia. 

### 4.2 Bagaimana LLM bekerja?
- Decoder only models: berfungsi untuk membuat teks satu persatu, dan memprediksi apa yang harus selanjutnya. selayaknya manusia berbicara, setelah kita berpikir, tahap selanjutnya adalah memilih kata.
- Encoder Decoder models: sederhannya ini adalah bagian translate anatar bahasa manusia. indonesia inggris dan sebaliknya.
- Encoder only models: fokusnya adalah untuk memahami teks bukan untuk membuat ulang. Ini sangat berfungsi sebagai mesin analisa teks manusia, mengambil makna atau emosi yang ada didalam teks.

### 4.3 Bagaimana LLMs belajara
- Pretraining: AI akan membaca dengan sejumlah besar teks dari internet dan belajar memprediksii kata selanjutnya didalam kalimat. Selayaknya bayi yang belajar komunikasi dari orang tuanya.
- Insstruction Training: AI belajar untuk mengikutii instruksi seperti "Coba jawab pertanyaan" atau "buatkan kesimpulan." Latihan sederhana seperti ini akan didampingi dengan contoh jawaban yang benar.
- Alignment Training: AI akan belajar etika yang memastikan responnya sesuai dengan manusia. semisal AI milik Elon akan belajar etika berdasarkan sudut pandang Elon.

### 4.4 The Technology Behind LLMs

- Attention Mechanism: Ini adalah teknologi yang akan membantu LLMs memahami suatu konteks. disaat pemrosesan kata, AI akan menganalisa seluruh kata didalam kalimat untuk memahmi setiap kata yang dipakai.
- How Attention Works: Setiap kata akan memiliki tiga bentuk representasi: Query( Apa yang harus dicari ), Key (Apa yang direpresentasikan ), dan Nilai (Informasi apa yang terkandung)
- Challenges with LLMs: Halusinasi, terkadang hasil proses LLMs terdengar meyakinkan tetapi sebenarnya itu salah. Bias, dikarenakan bacaan AI berasal dari internet yang ada informasi subjektif itu dapat mempengaruhi AI. Hak cipta, tergantung dengan penciptannya, mereka bisa saja mengunakan sumber tidak resmi untuk belajar.

## 5. Understanding Speech Processing

### 5.1 Basic Speech Sounds
- What is Speech Processing: Pemrosesan bicara adalah bagaimana suatu komputer memamhami bagaimana bahasa manusia dan mengubahnya lagi menjadi bahasa suara. Selayaknya komputer mendenngarkan dan berbicara kepada kita dengan normal.
- How We Make Speech Sounds:
  - Phones, adalah bangunan sederhana dari bahasa. Contohnya  adalah "ah," "bee," atau "guh." Peneliti menggunakan aplhabet khusus untuk menentukan dan membuat suara yang natural  
  - Prosody, Ini adalah bentuk melody dari suara, bagaimana suara kita yang nada tinggi ke rendah, menjadi semakin kencang atau halus, dan bagaimana kata itu disatikuan. Memberikan ciri khas antara kata pasive, tanya, dan perintah.
- How computer "See" speech:
  - Sound Waves : Disaat kita sebagai manusia berbicara, kita menciptakan vibrasi diatas angin.
  - Sound note (Spectograms) : Time, Pitch, Volume
  - MFCC Features: adalah nilai ukur spesial yang berfokus sebagai bagaian dari suara, tujuan adalah untuk memahami bagaimana seseorang berbicara, atau menyerupai bagaimana telinga kita memproses suara.

### 5.2 Speech Recognition ( Understanding Speech )
Bagaimana Komputer belajar memahami cara bicara?
- Encode: Mendengarkan secara seksama bagaimana cara bicara dan membuat pemahaman internal
- Decoder: mengubah pemahaman tersebut menjadi data tulis

Self-Supervised Learning: Computer akan belajar berdasarkan banyaknya audio suara tanpa ada kata kunci script yang menjadi panduan untuk menebak apa yang dikatakan, selayaknya bayi yang berusaha belajar cara bicara dari keluarga.

CTC ( Connectionist Temporal Classification ): 

# Glossary (Glosarium)

- Large Language Model(LLM): secara
- "Transformer based"  :
- Natural Language Processing :
- vastly broadened the scope :
- Tokens : Unit kecil didalam Language model yang menjalankan proses, menjadikan mereka keseluruhan kata, ini adalah bagian dari kata (subwords), atau bahakan satuan huruf.




## Referensi
- [Natural Language Processing](https://huggingface.co/learn/llm-course/chapter1/2?fw=pt)
- [Speech and Language Processing (Jurafsky & Martin)](https://web.stanford.edu/~jurafsky/slp3/)
- Natural Language Processing with Python (Bird, Klein, Loper)
- https://www.geeksforgeeks.org/nlp/subword-tokenization-in-nlp/
