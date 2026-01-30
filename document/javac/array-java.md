# Array di Java

Array adalah kumpulan data yang tersusun secara terorganisir dan dapat kita kelola untuk melakukan berbagai operasi, termasuk perhitungan. Array sangat berguna ketika kita perlu mengelola banyak data dengan tipe yang sama.

## Daftar Isi

1. [Karakteristik Array](#karakteristik-array)
2. [Integer Array](#integer-array)
3. [Array dengan Inisialisasi Langsung](#array-dengan-inisialisasi-langsung)
4. [Cara Deklarasi Array](#cara-deklarasi-array)
5. [Panjang Array](#panjang-array)
6. [Loop dengan For-Each](#loop-dengan-for-each)
7. [Array Multidimensi](#array-multidimensi)
8. [Operasi Umum pada Array](#operasi-umum-pada-array)
9. [Tips dan Peringatan](#tips-dan-peringatan)

---

## Karakteristik Array

Sebelum menggunakan array, penting untuk memahami karakteristiknya:

**Index Based**  
Semua elemen yang dimasukkan ke dalam array akan terhitung mulai dari nol (0). Jadi array dengan 5 elemen memiliki index dari 0 sampai 4.

**Tipe Data Harus Seragam**  
Semua elemen dalam satu array harus memiliki tipe data yang sama. Misalnya, array integer hanya bisa menampung integer, tidak bisa dicampur dengan string atau boolean.

**Ukuran Tetap**  
Setelah array dideklarasikan dengan ukuran tertentu, ukurannya tidak bisa diubah lagi. Jika butuh lebih banyak ruang, harus membuat array baru.

---

## Integer Array

Contoh membuat array untuk menyimpan angka (integer):

```java
public class ContohArray {
    public static void main(String[] args) {
        // Deklarasi array
        int[] angka;
        
        // Inisialisasi array dengan ukuran 5
        angka = new int[5];
        
        // Mengisi nilai ke array
        angka[0] = 10;
        angka[1] = 20;
        angka[2] = 30;
        angka[3] = 40;
        angka[4] = 50;
        
        // Mengakses elemen array
        System.out.println("Elemen ke-2: " + angka[1]);
        // Output: Elemen ke-2: 20
        
        // Loop melalui array
        for (int i = 0; i < angka.length; i++) {
            System.out.println("Indeks " + i + ": " + angka[i]);
        }
        /* Output:
           Indeks 0: 10
           Indeks 1: 20
           Indeks 2: 30
           Indeks 3: 40
           Indeks 4: 50
        */
    }
}
```

### Penjelasan Kode:

| Code | Penjelasan |
|------|------------|
| `int[] angka;` | Mendeklarasikan variabel array dengan tipe integer. Ini memberitahu Java bahwa `angka` adalah array yang akan menampung data integer |
| `angka = new int[5];` | Menginisialisasi array dengan ukuran 5 elemen. Array ini sekarang bisa menampung 5 angka dengan index 0 sampai 4 |
| `angka[0] = 10;` | Memasukkan nilai 10 ke dalam array pada index 0 (elemen pertama) |
| `System.out.println("Elemen ke-2: " + angka[1]);` | Menampilkan elemen pada index 1 (elemen kedua). Ingat, index dimulai dari 0! |
| `for (int i = 0; i < angka.length; i++)` | Loop yang mengiterasi semua elemen array. `angka.length` memberikan jumlah total elemen dalam array |

**Catatan Penting:**  
Saat array dibuat dengan `new int[5]`, semua elemen otomatis diisi dengan nilai default 0 untuk integer. Untuk boolean akan diisi false, untuk String akan diisi null.

---

## Array dengan Inisialisasi Langsung

Cara lebih praktis untuk membuat array adalah dengan langsung memberikan nilai saat deklarasi:

```java
public class ContohArray2 {
    public static void main(String[] args) {
        // Deklarasi dan inisialisasi langsung
        String[] names = {"Alice", "Bob", "Charlie"};
        
        // Mengakses elemen
        System.out.println("Nama pertama: " + names[0]);
        // Output: Nama pertama: Alice
        
        // Mengubah nilai elemen
        names[1] = "Bobby";
        System.out.println("Nama kedua: " + names[1]);
        // Output: Nama kedua: Bobby
        
        // Menampilkan semua nama
        System.out.println("\nDaftar semua nama:");
        for (int i = 0; i < names.length; i++) {
            System.out.println((i + 1) + ". " + names[i]);
        }
        /* Output:
           Daftar semua nama:
           1. Alice
           2. Bobby
           3. Charlie
        */
    }
}
```

### Penjelasan Kode:

| Code | Penjelasan |
|------|------------|
| `String[] names = {"Alice", "Bob", "Charlie"};` | Cara singkat untuk deklarasi dan inisialisasi array sekaligus. Java otomatis menghitung ukuran array berdasarkan jumlah elemen yang diberikan (dalam hal ini 3) |
| `names[1] = "Bobby";` | Mengubah atau menimpa nilai pada index 1. Nilai "Bob" diganti menjadi "Bobby" |

**Keuntungan cara ini:**  
Lebih cepat dan praktis jika sudah tahu data apa saja yang akan disimpan di array.

---

## Cara Deklarasi Array

Ada beberapa cara untuk mendeklarasikan array di Java:

```java
public class CaraDeklarasiArray {
    public static void main(String[] args) {
        // Cara 1: Deklarasi terpisah dari inisialisasi
        int[] numbers1;
        numbers1 = new int[3];
        numbers1[0] = 1;
        numbers1[1] = 2;
        numbers1[2] = 3;
        
        // Cara 2: Deklarasi dan inisialisasi ukuran sekaligus
        int[] numbers2 = new int[3];
        numbers2[0] = 10;
        numbers2[1] = 20;
        numbers2[2] = 30;
        
        // Cara 3: Deklarasi dan inisialisasi nilai langsung
        int[] numbers3 = {100, 200, 300};
        
        // Cara 4: Dengan kata kunci new dan nilai langsung
        int[] numbers4 = new int[]{1000, 2000, 3000};
        
        // Semua cara di atas valid dan menghasilkan array yang siap digunakan
        System.out.println("Array 1, elemen pertama: " + numbers1[0]);
        System.out.println("Array 2, elemen pertama: " + numbers2[0]);
        System.out.println("Array 3, elemen pertama: " + numbers3[0]);
        System.out.println("Array 4, elemen pertama: " + numbers4[0]);
    }
}
```

**Pilih cara yang paling sesuai:**
- Gunakan cara 1 atau 2 jika ukuran sudah diketahui tapi nilai akan diisi kemudian
- Gunakan cara 3 atau 4 jika nilai sudah diketahui sejak awal

---

## Panjang Array

Untuk mengetahui berapa banyak elemen dalam array, gunakan properti `.length`:

```java
public class PanjangArray {
    public static void main(String[] args) {
        int[] angka = {10, 20, 30, 40, 50};
        
        // Mendapatkan panjang array
        int panjang = angka.length;
        System.out.println("Jumlah elemen dalam array: " + panjang);
        // Output: Jumlah elemen dalam array: 5
        
        // Berguna untuk loop agar tidak keluar dari batas array
        System.out.println("Elemen terakhir: " + angka[panjang - 1]);
        // Output: Elemen terakhir: 50
        
        // Contoh praktis: menghitung total
        int total = 0;
        for (int i = 0; i < angka.length; i++) {
            total += angka[i];
        }
        System.out.println("Total semua elemen: " + total);
        // Output: Total semua elemen: 150
    }
}
```

**Catatan:**  
`length` adalah properti (bukan method), jadi tidak pakai tanda kurung `()`. Berbeda dengan String yang pakai `length()`.

---

## Loop dengan For-Each

For-each loop (enhanced for loop) adalah cara yang lebih simpel untuk mengiterasi semua elemen array tanpa perlu index:

```java
public class ForEachLoop {
    public static void main(String[] args) {
        int[] angka = {10, 20, 30, 40, 50};
        
        // Loop biasa dengan index
        System.out.println("Dengan loop biasa:");
        for (int i = 0; i < angka.length; i++) {
            System.out.println(angka[i]);
        }
        
        // For-each loop (lebih simple)
        System.out.println("\nDengan for-each:");
        for (int nilai : angka) {
            System.out.println(nilai);
        }
        /* Output keduanya sama:
           10
           20
           30
           40
           50
        */
        
        // Contoh dengan String array
        String[] buah = {"Apel", "Jeruk", "Mangga"};
        System.out.println("\nDaftar buah:");
        for (String nama : buah) {
            System.out.println("- " + nama);
        }
        /* Output:
           Daftar buah:
           - Apel
           - Jeruk
           - Mangga
        */
    }
}
```

**Kapan pakai for-each?**
- Ketika hanya perlu membaca nilai dari array
- Ketika tidak butuh index
- Lebih mudah dibaca dan tidak ada resiko salah index

**Kapan pakai loop biasa?**
- Ketika perlu memodifikasi nilai array
- Ketika butuh index untuk keperluan tertentu
- Ketika perlu loop dengan step tertentu (misal kelipatan 2)

---

## Array Multidimensi

Array multidimensi adalah array yang berisi array lain. Yang paling umum adalah array 2 dimensi (seperti tabel atau matrix).

```java
public class ArrayMultidimensi {
    public static void main(String[] args) {
        // Array 2 dimensi (seperti tabel)
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        // Mengakses elemen (baris, kolom)
        System.out.println("Elemen baris 0, kolom 1: " + matrix[0][1]);
        // Output: Elemen baris 0, kolom 1: 2
        
        System.out.println("Elemen baris 2, kolom 2: " + matrix[2][2]);
        // Output: Elemen baris 2, kolom 2: 9
        
        // Loop melalui array 2D
        System.out.println("\nMatrix lengkap:");
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println(); // Pindah baris
        }
        /* Output:
           Matrix lengkap:
           1 2 3
           4 5 6
           7 8 9
        */
        
        // Contoh praktis: tabel nilai siswa
        String[] nama = {"Ali", "Budi", "Citra"};
        int[][] nilai = {
            {80, 85, 90},  // nilai Ali (Matematika, Fisika, Kimia)
            {75, 80, 85},  // nilai Budi
            {90, 95, 88}   // nilai Citra
        };
        
        String[] mataPelajaran = {"Matematika", "Fisika", "Kimia"};
        
        System.out.println("\nTabel Nilai Siswa:");
        for (int i = 0; i < nama.length; i++) {
            System.out.println("\n" + nama[i] + ":");
            for (int j = 0; j < mataPelajaran.length; j++) {
                System.out.println("  " + mataPelajaran[j] + ": " + nilai[i][j]);
            }
        }
    }
}
```

**Cara berpikir array 2D:**
- Index pertama `[i]` adalah baris (row)
- Index kedua `[j]` adalah kolom (column)
- `matrix[2][1]` berarti baris ke-2, kolom ke-1

**Cara deklarasi lain untuk array 2D:**
```java
// Dengan ukuran tertentu
int[][] matrix1 = new int[3][3]; // 3 baris, 3 kolom

// Ukuran baris tetap, kolom bisa berbeda
int[][] matrix2 = new int[3][];
matrix2[0] = new int[2]; // baris 0 punya 2 kolom
matrix2[1] = new int[4]; // baris 1 punya 4 kolom
matrix2[2] = new int[3]; // baris 2 punya 3 kolom
```

---

## Operasi Umum pada Array

Berikut adalah operasi yang sering dilakukan pada array:

```java
public class OperasiArray {
    public static void main(String[] args) {
        int[] angka = {45, 12, 78, 34, 90, 23};
        
        // 1. Mencari nilai maksimum
        int max = angka[0];
        for (int nilai : angka) {
            if (nilai > max) {
                max = nilai;
            }
        }
        System.out.println("Nilai maksimum: " + max);
        // Output: Nilai maksimum: 90
        
        // 2. Mencari nilai minimum
        int min = angka[0];
        for (int nilai : angka) {
            if (nilai < min) {
                min = nilai;
            }
        }
        System.out.println("Nilai minimum: " + min);
        // Output: Nilai minimum: 12
        
        // 3. Menghitung rata-rata
        int total = 0;
        for (int nilai : angka) {
            total += nilai;
        }
        double rata = (double) total / angka.length;
        System.out.println("Rata-rata: " + rata);
        // Output: Rata-rata: 47.0
        
        // 4. Mencari elemen tertentu
        int cari = 78;
        boolean ditemukan = false;
        int indexDitemukan = -1;
        
        for (int i = 0; i < angka.length; i++) {
            if (angka[i] == cari) {
                ditemukan = true;
                indexDitemukan = i;
                break;
            }
        }
        
        if (ditemukan) {
            System.out.println("Angka " + cari + " ditemukan di index " + indexDitemukan);
        } else {
            System.out.println("Angka " + cari + " tidak ditemukan");
        }
        // Output: Angka 78 ditemukan di index 2
        
        // 5. Menghitung jumlah elemen tertentu
        int[] nilai = {80, 90, 75, 90, 85, 90};
        int cariNilai = 90;
        int jumlah = 0;
        
        for (int n : nilai) {
            if (n == cariNilai) {
                jumlah++;
            }
        }
        System.out.println("Nilai " + cariNilai + " muncul sebanyak " + jumlah + " kali");
        // Output: Nilai 90 muncul sebanyak 3 kali
    }
}
```

---

## Tips dan Peringatan

### ArrayIndexOutOfBoundsException

Ini adalah error yang paling sering terjadi saat bekerja dengan array. Terjadi ketika mencoba mengakses index yang tidak ada:

```java
public class ArrayError {
    public static void main(String[] args) {
        int[] angka = {10, 20, 30}; // array dengan 3 elemen (index 0, 1, 2)
        
        // INI AKAN ERROR!
        // System.out.println(angka[3]); // Error: index 3 tidak ada
        // System.out.println(angka[-1]); // Error: index negatif tidak valid
        
        // Cara aman: selalu cek dulu
        int index = 3;
        if (index >= 0 && index < angka.length) {
            System.out.println(angka[index]);
        } else {
            System.out.println("Index tidak valid");
        }
        // Output: Index tidak valid
    }
}
```

### Tips Praktis

**1. Gunakan konstanta untuk ukuran array**
```java
final int UKURAN = 10;
int[] data = new int[UKURAN];
```

**2. Inisialisasi array dengan nilai tertentu**
```java
int[] angka = new int[5];
for (int i = 0; i < angka.length; i++) {
    angka[i] = 100; // Semua elemen diisi 100
}
```

**3. Copy array dengan benar**
```java
int[] asli = {1, 2, 3};
int[] copy = asli; // INI SALAH! Hanya copy referensi

// Cara yang benar:
int[] copyBenar = new int[asli.length];
for (int i = 0; i < asli.length; i++) {
    copyBenar[i] = asli[i];
}

// Atau pakai method built-in:
int[] copyMudah = Arrays.copyOf(asli, asli.length);
```

**4. Membandingkan array**
```java
int[] array1 = {1, 2, 3};
int[] array2 = {1, 2, 3};

// INI SALAH!
// System.out.println(array1 == array2); // false, karena membandingkan referensi

// Cara yang benar:
boolean sama = Arrays.equals(array1, array2);
System.out.println(sama); // true
```

**5. Print array dengan mudah**
```java
import java.util.Arrays;

int[] angka = {1, 2, 3, 4, 5};
System.out.println(Arrays.toString(angka));
// Output: [1, 2, 3, 4, 5]
```

### Batasan Array

- Ukuran array tidak bisa diubah setelah dibuat
- Semua elemen harus tipe data yang sama
- Tidak ada method bawaan untuk menambah atau menghapus elemen
- Jika butuh ukuran dinamis, pertimbangkan menggunakan ArrayList (akan dipelajari di materi Collection)

---

## Kesimpulan

Array adalah struktur data fundamental di Java yang memungkinkan kita menyimpan banyak data dengan tipe yang sama. Meskipun memiliki keterbatasan (ukuran tetap), array sangat efisien dan berguna untuk banyak kasus. Poin penting yang perlu diingat:

- Index array dimulai dari 0
- Ukuran array tetap setelah dibuat
- Gunakan `.length` untuk mendapatkan jumlah elemen
- Hati-hati dengan ArrayIndexOutOfBoundsException
- For-each loop lebih mudah untuk iterasi sederhana
- Array multidimensi berguna untuk data tabular

Latihan rutin dengan array akan membuat kamu lebih mahir dalam memanipulasi data!
