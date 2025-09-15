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


## Referensi
- [Natural Language Processing](https://huggingface.co/learn/llm-course/chapter1/2?fw=pt)
- [Speech and Language Processing (Jurafsky & Martin)](https://web.stanford.edu/~jurafsky/slp3/)
- Natural Language Processing with Python (Bird, Klein, Loper)
- https://www.geeksforgeeks.org/nlp/subword-tokenization-in-nlp/
