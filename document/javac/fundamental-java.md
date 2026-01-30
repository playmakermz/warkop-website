# Java Fundamental

Dokumen ini merangkum poin penting dan mendasar dalam bahasa pemrograman Java, mencakup variabel, tipe data, array, percabangan, dan perulangan.

## Daftar Isi

1. [Variabel](#variabel)
2. [String](#string)
3. [Integer](#integer)
4. [Float](#float)
5. [Boolean](#boolean)
6. [Array](#array)
7. [Ekspresi](#ekspresi)
8. [If Statement](#if-statement)
9. [Switch](#switch)
10. [Loop](#loop)
11. [Comment](#comment)
12. [Datetime](#datetime-current-time)

---

## Variabel

Variabel adalah konsep untuk menyimpan data ke dalam memory dengan menggunakan nama sebagai pengenal. Analoginya seperti menyimpan barang ke dalam laci di perpustakaan, dimana setiap laci memiliki nomor atau label tertentu.

Dalam Java, setiap variabel harus memiliki tipe data yang jelas. Berikut adalah contoh deklarasi berbagai tipe variabel di Java:

```java
// String: teks atau kumpulan karakter
String greeting = "Hello, World!";

// int: bilangan bulat
int age = 25;

// double: bilangan desimal
double price = 99.99;

// long: bilangan bulat yang lebih besar
long bigNumber = 1234567890123456789L;

// boolean: nilai benar atau salah
boolean isAvailable = true;

// char: karakter tunggal
char grade = 'A';

// Object: tipe data kompleks
String person = "Alice";
int personAge = 30;

// Array: kumpulan data dengan tipe yang sama
String[] colors = {"red", "green", "blue"};
```

### Mengubah Nilai Variabel

Setelah variabel dideklarasikan, kamu bisa mengubah nilainya kapan saja:

```java
int myNumber = 10; // Deklarasi awal dengan nilai 10
myNumber = 15;     // Mengubah nilai menjadi 15
System.out.println(myNumber); // Output: 15
```

---

## String

String adalah tipe data untuk menyimpan teks. Di Java, String ditulis dalam tanda petik ganda.

```java
public class Main {
  public static void main(String[] args) {
    String name = "John";
    name = "Bukan John"; // menimpa data sebelumnya
    System.out.println("Hallo " + name); // menggabungkan teks dengan variabel
    // Output: Hallo Bukan John
  }
}
```

**Catatan:** Operator `+` digunakan untuk menggabungkan (concatenate) string di Java.

---

## Integer

Integer adalah tipe data untuk menyimpan bilangan bulat (tanpa desimal). Di Java, tipe data integer yang umum digunakan adalah `int`.

```java
public class Main {
  public static void main(String[] args) {
    int myNum = 100000;
    System.out.println(myNum);
    // Output: 100000
  }
}
```

**Range nilai int:** sekitar -2 miliar hingga 2 miliar. Jika butuh angka yang lebih besar, gunakan `long`.

---

## Float

Float dan double adalah tipe data untuk menyimpan bilangan desimal. Double memiliki presisi lebih tinggi dibanding float.

```java
public class Main {
  public static void main(String[] args) {
    float myNum = 5.75f; // harus pakai 'f' di akhir untuk float
    double myDouble = 5.75; // double tidak perlu 'f'
    
    System.out.println(myNum);  
    System.out.println(myDouble);
  }
}
```

**Perbedaan:**
- `float`: presisi 6-7 digit desimal, ukuran 4 byte
- `double`: presisi 15-16 digit desimal, ukuran 8 byte (lebih direkomendasikan)

---

## Boolean

Boolean adalah tipe data yang hanya memiliki dua nilai: `true` (benar) atau `false` (salah). Sangat berguna untuk logika dan kondisi.

```java
public class Main {
  public static void main(String[] args) {
    boolean isJavaFun = true;
    boolean isFishTasty = false;
    
    System.out.println(isJavaFun);   // Output: true
    System.out.println(isFishTasty); // Output: false

    // Menggunakan boolean dalam kondisi
    System.out.println(isJavaFun == true); // Output: true
    
    // Contoh perbandingan
    int age = 20;
    boolean isAdult = age >= 18;
    System.out.println(isAdult); // Output: true
  }
}
```

---

## Array

Array adalah struktur data untuk menyimpan beberapa nilai dengan tipe data yang sama dalam satu variabel. Setiap elemen dalam array memiliki indeks, dimulai dari 0.

```java
public class Main {
  public static void main(String[] args) {
    // Membuat array dengan nilai awal
    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    
    // Mengakses elemen array (indeks dimulai dari 0)
    System.out.println(cars[0]); // Output: Volvo
    
    // Mengubah nilai elemen array
    cars[0] = "Opel";
    System.out.println(cars[0]); // Output: Opel

    // Menampilkan semua elemen array dengan for-each loop
    for (String i : cars) {
      System.out.println(i);
    }
    
    // Mengetahui panjang array
    System.out.println("Jumlah mobil: " + cars.length);
  }
}
```

**Cara lain membuat array:**
```java
// Membuat array dengan ukuran tertentu
int[] numbers = new int[5]; // array dengan 5 elemen, default value 0
numbers[0] = 10;
numbers[1] = 20;
```

---

## Ekspresi

Ekspresi adalah kombinasi dari variabel, operator, dan method yang menghasilkan sebuah nilai. Ekspresi merupakan bagian fundamental dalam pemrograman.

**Jenis ekspresi:**
- Perhitungan matematika: `5 + 3 * 2`
- Perbandingan: `x > 10`
- Pemanggilan method: `Math.sqrt(16)`
- Operasi logika: `isTrue && isFalse`

### Contoh Ekspresi Sederhana

```java
public class ContohEkspresi {
    public static void main(String[] args) {
        int angka = 10; // Deklarasi variabel
        int hasil = angka * 2 + 5; // Ekspresi matematika
        System.out.println("Hasil ekspresi: " + hasil); 
        // Output: Hasil ekspresi: 25
    }
}
```

**Penjelasan kode:**
- `public class ContohEkspresi` adalah nama kelas utama, file Java harus bernama ContohEkspresi.java
- `public static void main(String[] args)` adalah titik mulai eksekusi program
- `int hasil = angka * 2 + 5;` adalah ekspresi matematika (10 * 2 + 5 = 25)
- `System.out.println()` adalah method untuk menampilkan output

### Contoh Ekspresi Lainnya

```java
int hasil = 25;
int angka = 10;

// Ekspresi perbandingan (menghasilkan boolean)
boolean isGenap = (hasil % 2 == 0); // true, karena 25 % 2 = 1

// Ekspresi logika dengan operator AND
boolean isValid = (angka > 0 && hasil < 30); // true, kedua kondisi terpenuhi

// Ekspresi dengan method (akar kuadrat)
double akar = Math.sqrt(hasil); // 5.0
System.out.println("Akar kuadrat dari " + hasil + " adalah " + akar);
```

---

## If Statement

If statement digunakan untuk membuat keputusan berdasarkan kondisi tertentu. Program akan mengeksekusi blok kode tertentu hanya jika kondisi bernilai true.

```java
public class Main {
  public static void main(String[] args) {
    int time = 22;
    
    if (time < 10) {
      System.out.println("Good morning.");
    } else if (time < 18) {
      System.out.println("Good day.");
    } else {
      System.out.println("Good evening.");
    }
    // Output: Good evening.
  }
}
```

**Struktur if statement:**
- `if`: kondisi pertama yang dicek
- `else if`: kondisi alternatif jika kondisi pertama false
- `else`: dijalankan jika semua kondisi sebelumnya false

**Contoh lain:**
```java
int nilai = 85;

if (nilai >= 90) {
    System.out.println("Grade A");
} else if (nilai >= 80) {
    System.out.println("Grade B"); // Ini yang dijalankan
} else if (nilai >= 70) {
    System.out.println("Grade C");
} else {
    System.out.println("Grade D");
}
```

---

## Switch

Switch adalah alternatif dari if-else untuk mengecek satu variabel dengan banyak kemungkinan nilai. Lebih rapi dan mudah dibaca untuk kasus dengan banyak kondisi.

```java
public class Main {
  public static void main(String[] args) {
    int day = 4;
    
    switch (day) {
      case 1:
        System.out.println("Senin");
        break;
      case 2:
        System.out.println("Selasa");
        break;
      case 3:
        System.out.println("Rabu");
        break;
      case 4:
        System.out.println("Kamis");
        break;
      case 5:
        System.out.println("Jumat");
        break;
      case 6:
        System.out.println("Sabtu");
        break;
      case 7:
        System.out.println("Minggu");
        break;
      default:
        System.out.println("Hari tidak valid");
    }
    // Output: Kamis
  }
}
```

**Catatan penting:**
- `break` digunakan untuk keluar dari switch setelah case yang sesuai dieksekusi
- Tanpa `break`, program akan terus mengeksekusi case berikutnya (fall-through)
- `default` adalah pilihan jika tidak ada case yang cocok (opsional tapi direkomendasikan)

---

## Loop

Loop (perulangan) digunakan untuk menjalankan blok kode berulang kali selama kondisi tertentu terpenuhi.

### While Loop

While loop akan terus berjalan selama kondisi bernilai true.

```java
public class Main {
  public static void main(String[] args) {
    int i = 0;
    
    while (i < 5) {
      System.out.println(i);
      i++; // increment, menambah nilai i sebesar 1
    }
    // Output: 0 1 2 3 4
  }
}
```

### For Loop

For loop digunakan ketika kamu sudah tahu berapa kali perulangan akan dijalankan.

```java
public class Main {
  public static void main(String[] args) {
    // For loop standar
    for (int i = 0; i < 5; i++) {
      System.out.println(i);
    }
    // Output: 0 1 2 3 4

    // For-each loop untuk array
    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    for (String car : cars) {
      System.out.println(car);
    }
    // Output: Volvo BMW Ford Mazda (masing-masing di baris baru)
  }
}
```

**Struktur for loop:** `for (inisialisasi; kondisi; increment)`
- `int i = 0`: nilai awal
- `i < 5`: kondisi yang dicek sebelum setiap iterasi
- `i++`: yang dilakukan setelah setiap iterasi

### Break dalam Loop

`break` digunakan untuk menghentikan loop secara paksa.

```java
public class Main {
  public static void main(String[] args) {
    for (int i = 0; i < 10; i++) {
      if (i == 4) {
        break; // loop berhenti ketika i = 4
      }
      System.out.println(i);
    }
    // Output: 0 1 2 3
  }
}
```

### Continue dalam Loop

`continue` digunakan untuk melewati iterasi saat ini dan lanjut ke iterasi berikutnya.

```java
public class Main {
  public static void main(String[] args) {
    for (int i = 0; i < 10; i++) {
      if (i == 4) {
        continue; // skip ketika i = 4
      }
      System.out.println(i);
    }
    // Output: 0 1 2 3 5 6 7 8 9 (angka 4 tidak muncul)
  }
}
```

---

## Comment

Comment adalah catatan dalam kode yang tidak akan dieksekusi oleh program. Berguna untuk dokumentasi dan penjelasan.

```java
public class Main {
  public static void main(String[] args) {
    // Ini adalah single line comment
    // Digunakan untuk komentar satu baris

    /* 
       Ini adalah multi-line comment
       Kode dibawah akan menampilkan Hello World
       ke layar, dan ini sangat berguna untuk
       dokumentasi yang lebih panjang
    */
    
    System.out.println("Hello World");
    
    /**
     * Ini adalah documentation comment (Javadoc)
     * Biasanya digunakan untuk mendokumentasikan
     * class, method, dan variabel
     */
  }
}
```

**Jenis comment:**
- `//` untuk single line comment
- `/* */` untuk multi-line comment
- `/** */` untuk documentation comment (Javadoc)

---

## Datetime Current Time

Java menyediakan class `LocalDateTime` untuk bekerja dengan tanggal dan waktu.

```java
import java.time.LocalDateTime;  // import class LocalDateTime
import java.time.format.DateTimeFormatter; // untuk format custom

public class Main {
  public static void main(String[] args) {
    // Mendapatkan waktu sekarang
    LocalDateTime myObj = LocalDateTime.now();
    System.out.println(myObj);
    // Output: 2025-01-29T14:30:25.123456 (contoh)
    
    // Format waktu custom
    DateTimeFormatter myFormat = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
    String formattedDate = myObj.format(myFormat);
    System.out.println(formattedDate);
    // Output: 29-01-2025 14:30:25 (contoh)
  }
}
```

**Class lain untuk tanggal dan waktu:**
- `LocalDate`: hanya tanggal (tahun, bulan, hari)
- `LocalTime`: hanya waktu (jam, menit, detik)
- `LocalDateTime`: gabungan tanggal dan waktu
- `ZonedDateTime`: tanggal dan waktu dengan timezone

---

## Referensi

- [W3Schools Java Tutorial](https://www.w3schools.com/java/java_examples.asp) - Tutorial fundamental Java
- [Oracle Java Documentation](https://docs.oracle.com/en/java/) - Dokumentasi resmi Java
- [Java Programming for Beginners](https://www.geeksforgeeks.org/java/) - Tutorial Java untuk pemula
