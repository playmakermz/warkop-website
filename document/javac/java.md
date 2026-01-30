# Panduan Belajar Bahasa Pemrograman Java

## Daftar Isi

1. [Pengenalan Java](#pengenalan-java)
2. [Instalasi Java](#instalasi-java)
   - [Instalasi di Ubuntu/Debian](#instalasi-di-ubuntudebian)
   - [Verifikasi Instalasi](#verifikasi-instalasi)
3. [Compile dan Run Program Java](#compile-dan-run-program-java)
   - [Cara Compile](#cara-compile)
   - [Cara Run](#cara-run)
   - [Troubleshooting](#troubleshooting)
4. [Aturan Penting Java](#aturan-penting-java)
5. [Metodologi Belajar](#metodologi-belajar)
6. [Struktur Dasar Program Java](#struktur-dasar-program-java)
   - [Penjelasan Public, Class, Static, Void](#penjelasan-public-class-static-void)
   - [Breakdown Code Dasar](#breakdown-code-dasar)
7. [Variabel dan Tipe Data](#variabel-dan-tipe-data)
   - [Deklarasi Variabel](#deklarasi-variabel)
   - [Tipe Data Primitif](#tipe-data-primitif)
8. [Array di Java](#array-di-java)
   - [Array Satu Dimensi](#array-satu-dimensi)
   - [Array Dua Dimensi (Matriks)](#array-dua-dimensi-matriks)
9. [Latihan dan Materi Lanjutan](#latihan-dan-materi-lanjutan)

---

## Pengenalan Java

Java adalah bahasa pemrograman yang sangat populer dan banyak digunakan di industri. Java terkenal dengan filosofi "Write Once, Run Anywhere" (WORA), yang artinya code Java bisa dijalankan di berbagai platform tanpa perlu modifikasi.

### Mengapa Belajar Java?

**Keunggulan Java:**
- **Platform Independent**: Code Java bisa jalan di Windows, Mac, Linux, dll
- **Object-Oriented**: Mendukung konsep OOP yang powerful
- **Robust dan Secure**: Built-in security features dan error handling
- **Large Community**: Komunitas besar, banyak library dan framework
- **Job Opportunities**: Banyak perusahaan besar pakai Java (Google, Amazon, Netflix, dll)

**Aplikasi Java:**
- Desktop applications (IntelliJ IDEA, Eclipse)
- Mobile apps (Android)
- Web applications (Spring, Jakarta EE)
- Enterprise systems
- Game development (Minecraft)

---

## Instalasi Java

### Instalasi di Ubuntu/Debian

Untuk install Java di Ubuntu atau Debian, gunakan command berikut di terminal:

```bash
# Update package list
sudo apt update

# Install JRE (Java Runtime Environment) dan JDK (Java Development Kit)
sudo apt install default-jre default-jdk
```

**Penjelasan:**
- **JRE (Java Runtime Environment)**: Diperlukan untuk menjalankan program Java
- **JDK (Java Development Kit)**: Diperlukan untuk develop (menulis dan compile) program Java. JDK sudah include JRE

### Verifikasi Instalasi

Setelah instalasi selesai, verifikasi dengan command berikut:

```bash
# Cek versi Java
java -version

# Cek versi Java compiler
javac -version
```

**Output yang diharapkan:**
```
java version "11.0.x" atau lebih baru
javac 11.0.x
```

Jika kedua command berhasil dan menampilkan versi, berarti Java sudah terinstall dengan baik.

**Referensi Instalasi:**
[How to Install Java on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04)

---

## Compile dan Run Program Java

Java adalah compiled language, yang artinya code harus di-compile dulu sebelum bisa dijalankan.

### Cara Compile

Compile adalah proses mengubah source code (.java) menjadi bytecode (.class) yang bisa dijalankan JVM.

```bash
javac namafile.java
```

**Contoh:**
```bash
javac start.java
```

Setelah compile berhasil, akan muncul file `start.class` di folder yang sama.

### Cara Run

Setelah di-compile, jalankan program dengan command:

```bash
java namafile
```

**PENTING**: Jangan include extension `.class` saat run!

**Contoh:**
```bash
java start
```

### Troubleshooting

**Error: "javac is not recognized"**
- Java belum terinstall atau belum ada di PATH
- Install ulang Java atau set PATH environment variable

**Error: "Could not find or load main class"**
- Nama class tidak sesuai dengan nama file
- Tidak ada method `main` di class
- Pastikan nama file sama dengan nama class

**Error: "Public class X must be defined in a file named X.java"**
- Nama file harus sama persis dengan nama public class
- Java case-sensitive!

**Referensi:**
[How to Compile and Run Java Program](https://www.javatpoint.com/how-to-compile-and-run-java-program)

---

## Aturan Penting Java

Ada beberapa aturan penting yang harus diikuti saat coding Java:

### 1. Semicolon Wajib

Setiap statement di Java harus diakhiri dengan semicolon (`;`).

```java
// Benar
int x = 5;
System.out.println("Hello");

// Salah - akan error
int x = 5
System.out.println("Hello")
```

### 2. Case Sensitive

Java sangat case-sensitive. Huruf besar dan kecil itu beda.

```java
int nilai = 10;    // variabel 'nilai'
int Nilai = 20;    // variabel 'Nilai' (beda dengan 'nilai')
int NILAI = 30;    // variabel 'NILAI' (beda lagi)
```

### 3. Nama File = Nama Public Class

Jika punya public class bernama `Start`, file harus bernama `Start.java` (persis sama).

```java
// File: Start.java
public class Start {
    // ...
}
```

### 4. Curly Braces Berpasangan

Setiap `{` harus punya pasangan `}`.

```java
public class Test {
    public static void main(String[] args) {
        if (true) {
            System.out.println("Hello");
        } // Tutup if
    } // Tutup main
} // Tutup class
```

### 5. Indentation (Opsional tapi Penting)

Meskipun tidak wajib, indentation membuat code lebih readable.

```java
// Bagus
public class Test {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}

// Buruk (tapi tetap jalan)
public class Test {
public static void main(String[] args) {
System.out.println("Hello");
}
}
```

---

## Metodologi Belajar

Tutorial ini menggunakan pendekatan pembelajaran bertahap:

### Tahapan Belajar

**1. Code Example**
Diberikan contoh code lengkap yang bisa langsung dicoba.

**2. Breakdown per Baris**
Setiap baris code dijelaskan satu per satu. Jika sudah dijelaskan di section sebelumnya, tidak akan diulangi lagi.

**3. Point Penting**
Highlight bagian-bagian code yang paling penting untuk dipahami.

**4. Latihan Praktik**
Di akhir, akan ada latihan untuk mengaplikasikan ilmu yang sudah dipelajari.

### Tips Belajar Efektif

- **Type, Jangan Copy-Paste**: Ketik ulang code untuk muscle memory
- **Eksperimen**: Coba modifikasi code dan lihat hasilnya
- **Debug Error**: Jangan takut error, ini bagian dari belajar
- **Latihan Rutin**: Coding adalah skill yang perlu latihan konsisten

---

## Struktur Dasar Program Java

Mari kita mulai dengan program Java paling sederhana.

### Penjelasan Public, Class, Static, Void

Sebelum masuk ke code, mari pahami keyword-keyword penting ini:

**public**: Access modifier yang artinya bisa diakses dari mana saja (class lain, package lain, dll).

**class**: Blueprint atau template untuk membuat object. Semua code Java harus ada di dalam class.

**static**: Artinya method ini milik class, bukan milik object. Method `main` harus static karena JVM perlu call method ini tanpa bikin object dulu.

**void**: Return type yang artinya method ini tidak mengembalikan nilai apapun.

**main**: Nama method yang special. Ini adalah entry point program Java. JVM akan mencari dan menjalankan method `main` pertama kali.

**String[] args**: Parameter untuk menerima command line arguments (input dari terminal saat run program).

### Program Hello World

```java
public class Start {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

**Cara compile dan run:**
```bash
javac Start.java
java Start
```

**Output:**
```
Hello World!
```

### Program dengan Variabel

```java
public class Start {
    public static void main(String[] args) {
        // Membuat variabel integer dengan nama 'nilai' dan memberinya value 1945
        int nilai = 1945;

        // Menampilkan nilai variabel ke terminal
        System.out.println("Nilai didalam variabel adalah " + nilai);
    }
}
```

**Cara compile dan run:**
```bash
javac Start.java
java Start
```

**Output:**
```
Nilai didalam variabel adalah 1945
```

### Breakdown Code Dasar

Mari kita breakdown setiap baris dari program di atas:

```java
public class Start {
```
**Penjelasan:**
- `public` = Access modifier, class ini bisa diakses dari mana saja
- `class` = Keyword untuk deklarasi class
- `Start` = Nama class (harus sama dengan nama file: Start.java)
- `{` = Curly brace pembuka untuk class

```java
    public static void main(String[] args) {
```
**Penjelasan:**
- `public` = Method ini bisa diakses dari luar
- `static` = Method ini bisa dipanggil tanpa bikin object
- `void` = Method ini tidak return value
- `main` = Nama method (entry point program)
- `String[] args` = Parameter untuk command line arguments
- `{` = Curly brace pembuka untuk method

```java
        int nilai = 1945;
```
**Penjelasan:**
- `int` = Tipe data integer (bilangan bulat)
- `nilai` = Nama variabel
- `=` = Assignment operator
- `1945` = Value yang di-assign ke variabel
- `;` = Semicolon untuk akhiri statement

```java
        System.out.println("Nilai didalam variabel adalah " + nilai);
```
**Penjelasan:**
- `System.out.println()` = Method untuk print ke console dengan newline
- `"Nilai didalam variabel adalah "` = String yang akan di-print
- `+` = Operator untuk concatenation (gabung string)
- `nilai` = Variabel yang valuenya akan di-print
- `;` = Semicolon untuk akhiri statement

```java
    }
```
Tutup curly brace untuk method `main`

```java
}
```
Tutup curly brace untuk class `Start`

### Point Penting

Bagian yang paling penting untuk dipahami dari code di atas:

```java
public class Start {
    public static void main(String[] args) {
        int nilai = 1945;  // Deklarasi variabel
        System.out.println("Nilai didalam variabel adalah " + nilai);  // Print variable
    }
}
```

**Konsep Penting:**
1. Setiap program Java harus punya minimal 1 class
2. Method `main` adalah entry point (titik mulai) program
3. Variabel harus punya tipe data (`int`, `String`, dll)
4. `System.out.println()` untuk print ke console

---

## Variabel dan Tipe Data

### Deklarasi Variabel

Variabel adalah container untuk menyimpan data. Di Java, setiap variabel harus punya tipe data.

**Sintaks:**
```java
tipeData namaVariabel = value;
```

**Contoh:**
```java
int umur = 25;
String nama = "Budi";
double harga = 99.99;
boolean isActive = true;
```

### Tipe Data Primitif

Java punya 8 tipe data primitif:

**1. byte**
```java
byte angka = 100;  // Range: -128 to 127
```

**2. short**
```java
short nilai = 1000;  // Range: -32,768 to 32,767
```

**3. int** (Paling sering dipakai)
```java
int jumlah = 100000;  // Range: -2^31 to 2^31-1
```

**4. long**
```java
long populasi = 7000000000L;  // Range: -2^63 to 2^63-1
// Tambah 'L' di akhir untuk long
```

**5. float**
```java
float harga = 19.99f;  // Decimal 32-bit
// Tambah 'f' di akhir untuk float
```

**6. double** (Paling sering untuk decimal)
```java
double pi = 3.14159;  // Decimal 64-bit
```

**7. boolean**
```java
boolean isTrue = true;   // true atau false
boolean isFalse = false;
```

**8. char**
```java
char huruf = 'A';  // Single character
// Pakai single quote ('), bukan double quote (")
```

### Tipe Data Reference

Selain primitif, ada juga reference type seperti String, Array, Object, dll.

**String:**
```java
String nama = "John Doe";
String alamat = "Jakarta";

// String concatenation
String fullInfo = nama + " tinggal di " + alamat;
```

### Naming Convention Variabel

**Aturan Penamaan:**
- Harus dimulai dengan huruf, underscore (_), atau dollar sign ($)
- Tidak boleh dimulai dengan angka
- Case-sensitive
- Tidak boleh pakai reserved keywords (int, class, public, dll)

**Best Practice:**
- Gunakan camelCase: `namaVariabel`, `jumlahSiswa`, `totalHarga`
- Nama harus deskriptif: `umur` lebih baik dari `u`
- Hindari singkatan yang tidak jelas

**Contoh:**
```java
// Good
int umurMahasiswa = 20;
String namaLengkap = "John Doe";
double totalHarga = 150000;

// Bad
int a = 20;  // Tidak deskriptif
String nm = "John";  // Singkatan tidak jelas
double 1harga = 150000;  // Dimulai dengan angka (ERROR!)
```

---

## Array di Java

Array adalah struktur data yang bisa menyimpan multiple values dengan tipe data yang sama.

### Array Satu Dimensi

Array 1 dimensi seperti list atau daftar yang berisi elemen-elemen dengan tipe data sama.

#### Deklarasi dan Inisialisasi

**Cara 1: Inisialisasi Langsung**
```java
int[] angka = {10, 20, 30, 40, 50};
String[] nama = {"Andi", "Budi", "Citra"};
```

**Cara 2: Deklarasi Dulu, Inisialisasi Belakangan**
```java
int[] nilai = new int[5];  // Array dengan 5 elemen
nilai[0] = 80;
nilai[1] = 85;
nilai[2] = 90;
nilai[3] = 75;
nilai[4] = 88;
```

#### Mengakses Element Array

Array di Java menggunakan zero-based indexing (index mulai dari 0).

```java
int[] angka = {10, 20, 30, 40, 50};

System.out.println(angka[0]);  // Output: 10
System.out.println(angka[2]);  // Output: 30
System.out.println(angka[4]);  // Output: 50
```

#### Program Lengkap dengan Array 1D

```java
public class Start {
    public static void main(String[] args) {
        // Membuat array dengan 3 elemen
        int[] arraySatu = {12, 10, 40};

        // Menampilkan array dalam format [12, 10, 40]
        System.out.print("Array: [");
        
        for (int i = 0; i < arraySatu.length; i++) {
            System.out.print(arraySatu[i]);
            
            // Tambah koma jika bukan elemen terakhir
            if (i < arraySatu.length - 1) {
                System.out.print(", ");
            }
        }
        
        System.out.println("]");
    }
}
```

**Output:**
```
Array: [12, 10, 40]
```

#### Breakdown Array 1D

Mari kita breakdown code di atas:

```java
int[] arraySatu = {12, 10, 40};
```
**Penjelasan:**
- `int[]` = Tipe data array of integers
- `arraySatu` = Nama variabel array
- `{12, 10, 40}` = Inisialisasi array dengan 3 elemen

```java
System.out.print("Array: [");
```
**Penjelasan:**
- `System.out.print()` = Print tanpa newline di akhir (beda dengan `println`)
- Print string `"Array: ["` sebagai pembuka

```java
for (int i = 0; i < arraySatu.length; i++) {
```
**Penjelasan:**
- `for` = Loop untuk iterasi
- `int i = 0` = Inisialisasi counter dari 0
- `i < arraySatu.length` = Kondisi loop (length adalah property untuk ukuran array)
- `i++` = Increment counter setiap iterasi

```java
System.out.print(arraySatu[i]);
```
**Penjelasan:**
- `arraySatu[i]` = Akses element array di index i
- Print element tanpa newline

```java
if (i < arraySatu.length - 1) {
    System.out.print(", ");
}
```
**Penjelasan:**
- Check apakah ini bukan elemen terakhir
- Jika bukan, print koma dan spasi sebagai separator
- `arraySatu.length - 1` adalah index terakhir

```java
System.out.println("]");
```
**Penjelasan:**
- Print kurung tutup `"]"`
- `println` akan tambah newline di akhir

#### Point Penting Array 1D

```java
// Inisialisasi array
int[] arraySatu = {12, 10, 40};

// Loop untuk akses setiap elemen
for (int i = 0; i < arraySatu.length; i++) {
    System.out.print(arraySatu[i]);
    
    // Separator kecuali untuk elemen terakhir
    if (i < arraySatu.length - 1) {
        System.out.print(", ");
    }
}
```

**Konsep Penting:**
1. Array menggunakan square brackets `[]`
2. Index dimulai dari 0
3. `.length` untuk dapat ukuran array
4. For loop adalah cara umum untuk iterasi array

### Array Dua Dimensi (Matriks)

Array 2D seperti tabel atau matriks yang punya baris dan kolom.

#### Deklarasi Array 2D

**Cara 1: Inisialisasi Langsung**
```java
int[][] matriks = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
```

**Cara 2: Deklarasi dengan Ukuran**
```java
int[][] matriks = new int[3][3];  // Matriks 3x3
matriks[0][0] = 1;
matriks[0][1] = 2;
// dst...
```

#### Program Lengkap Array 2D

```java
public class Start {
    public static void main(String[] args) {
        // Membuat array 2 dimensi (matriks 3x3)
        int[][] arrayDua = {
            {12, 10, 40},  // Baris pertama
            {13, 11, 41},  // Baris kedua
            {14, 12, 42}   // Baris ketiga
        };

        // Menampilkan matriks ke terminal
        for (int i = 0; i < 3; i++) {           // Loop untuk baris
            for (int j = 0; j < 3; j++) {       // Loop untuk kolom
                System.out.print(arrayDua[i][j] + " ");
            }
            System.out.println();  // Newline setelah setiap baris
        }
    }
}
```

**Output:**
```
12 10 40 
13 11 41 
14 12 42 
```

#### Breakdown Array 2D

```java
int[][] arrayDua = {
    {12, 10, 40},
    {13, 11, 41},
    {14, 12, 42}
};
```
**Penjelasan:**
- `int[][]` = Tipe data array 2 dimensi
- Setiap `{...}` adalah satu baris
- Ada 3 baris dan 3 kolom (matriks 3x3)

```java
for (int i = 0; i < 3; i++) {
```
**Penjelasan:**
- Loop luar untuk iterasi baris
- `i` adalah index baris (0, 1, 2)

```java
    for (int j = 0; j < 3; j++) {
```
**Penjelasan:**
- Loop dalam untuk iterasi kolom
- `j` adalah index kolom (0, 1, 2)
- Nested loop: untuk setiap baris, loop semua kolom

```java
        System.out.print(arrayDua[i][j] + " ");
```
**Penjelasan:**
- `arrayDua[i][j]` = Akses element di baris i, kolom j
- `+ " "` = Tambah spasi sebagai separator

```java
    }
    System.out.println();
```
**Penjelasan:**
- Setelah selesai satu baris (loop j selesai)
- Print newline untuk pindah ke baris baru

#### Visualisasi Array 2D

Array 2D bisa divisualisasikan seperti tabel:

```
       j=0  j=1  j=2
i=0  | 12 | 10 | 40 |
i=1  | 13 | 11 | 41 |
i=2  | 14 | 12 | 42 |
```

**Akses Element:**
- `arrayDua[0][0]` = 12 (baris 0, kolom 0)
- `arrayDua[0][2]` = 40 (baris 0, kolom 2)
- `arrayDua[2][1]` = 12 (baris 2, kolom 1)

#### Point Penting Array 2D

```java
// Inisialisasi array 2D
int[][] arrayDua = {
    {12, 10, 40},
    {13, 11, 41},
    {14, 12, 42}
};

// Nested loop untuk akses semua element
for (int i = 0; i < 3; i++) {        // Loop baris
    for (int j = 0; j < 3; j++) {    // Loop kolom
        System.out.print(arrayDua[i][j] + " ");
    }
    System.out.println();  // Newline per baris
}
```

**Konsep Penting:**
1. Array 2D pakai double brackets `[][]`
2. Format: `array[baris][kolom]`
3. Nested loop untuk iterasi (loop dalam loop)
4. Loop luar untuk baris, loop dalam untuk kolom

#### Array 2D dengan Size Dinamis

```java
// Membuat array 2D dengan ukuran dinamis
int baris = 4;
int kolom = 5;
int[][] matriks = new int[baris][kolom];

// Mengisi array dengan nilai
for (int i = 0; i < baris; i++) {
    for (int j = 0; j < kolom; j++) {
        matriks[i][j] = i * kolom + j;
    }
}

// Menampilkan array
for (int i = 0; i < baris; i++) {
    for (int j = 0; j < kolom; j++) {
        System.out.print(matriks[i][j] + "\t");  // Tab sebagai separator
    }
    System.out.println();
}
```

**Tips Array 2D:**
- Gunakan `.length` untuk dapat jumlah baris: `arrayDua.length`
- Gunakan `.length` pada baris untuk dapat jumlah kolom: `arrayDua[0].length`
- Array 2D di Java bisa punya ukuran kolom yang berbeda per baris (jagged array)

---

## Latihan dan Materi Lanjutan

### Latihan Praktik

Untuk memperdalam pemahaman Java, silakan kerjakan latihan berikut:

**Latihan Java:** [latihan-java.md](../latihan-bahasa/latihan-java.md)

Latihan ini akan membantu kamu mengaplikasikan konsep-konsep yang sudah dipelajari.

### Materi Lanjutan

Setelah menguasai dasar-dasar Java, kamu bisa lanjut ke topik yang lebih advanced:

**1. Fundamental Java**
[fundamental-java.md](./fundamental-java.md)

Topik yang dibahas:
- Object-Oriented Programming (OOP)
- Class dan Object
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

**2. Array Lanjutan**
[array-java.md](./array-java.md)

Topik yang dibahas:
- Array methods
- Array manipulation
- ArrayList dan Collections
- Sorting dan searching
- Multi-dimensional arrays

### Referensi Belajar Java

**Official Documentation:**
- [Oracle Java Documentation](https://docs.oracle.com/javase/tutorial/)
- [Java API Documentation](https://docs.oracle.com/en/java/javase/)

**Tutorial Online:**
- [W3Schools Java Tutorial](https://www.w3schools.com/java/)
- [JavaTpoint](https://www.javatpoint.com/java-tutorial)
- [GeeksforGeeks Java](https://www.geeksforgeeks.org/java/)

**Practice Platforms:**
- [HackerRank](https://www.hackerrank.com/domains/java)
- [LeetCode](https://leetcode.com/)
- [CodeWars](https://www.codewars.com/)

### Tips Lanjutan Belajar Java

**1. Install IDE**
Gunakan IDE untuk coding yang lebih nyaman:
- **IntelliJ IDEA** (Recommended, punya free version)
- **Eclipse** (Free, popular)
- **NetBeans** (Free)
- **VS Code** dengan Java Extension Pack

**2. Belajar Debugging**
- Gunakan breakpoint
- Step through code
- Watch variables
- Analyze stack trace

**3. Read Other People's Code**
- Lihat open source projects di GitHub
- Pelajari best practices
- Pahami design patterns

**4. Build Projects**
Buat project sendiri untuk latihan:
- Calculator
- To-Do List
- Student Management System
- Simple Game (Tic-Tac-Toe, Snake)
- Library Management System

**5. Learn Version Control**
- Git dan GitHub
- Commit message yang baik
- Branching strategy
- Collaboration dengan team

### Roadmap Belajar Java

**Level Beginner (1-2 bulan):**
- ✅ Syntax dasar dan struktur program
- ✅ Variabel dan tipe data
- ✅ Operator dan expressions
- ✅ Control flow (if, switch, loops)
- ✅ Array dan String
- Method dan functions

**Level Intermediate (2-3 bulan):**
- Object-Oriented Programming
- Exception handling
- File I/O
- Collections Framework
- Generics
- Lambda expressions

**Level Advanced (3+ bulan):**
- Multithreading
- Database connectivity (JDBC)
- Web development (Spring Framework)
- Design patterns
- Testing (JUnit)
- Build tools (Maven, Gradle)

---

