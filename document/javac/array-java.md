# Array 

Array adalah sebuah kumpulan data yang dapat kita kelola dan gunakan untuk melakukan perhitungan.

Kriteria array adalah:
- Index based: yang berarti bahwa semua elemen yang dimasukan kedalam array akan terhitung mulai dari nol
- Tipe data harus seragam
- Ukuran nilai yang dapat ditampung array akan sesuai dengan deklarasi yang kita buat

## Integer array 
```
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
        
        // Loop melalui array
        for (int i = 0; i < angka.length; i++) {
            System.out.println("Indeks " + i + ": " + angka[i]);
        }
    }
}
```

Breakdown:
- int[] angka; - 
- angka = new int[5] - adalah menentukan ukuran array
- angka[0] = 10; - adalah menun

  Code  | Penjelasan
  --- | ---
  int[] angka; | untuk memberikan kriteria bahwa array tersebut bertipe int
  angka = new int[5] | adalah menentukan ukuran array
  angka[0] = 10; | adalah memasukan nilai 10 kedalam index array ke 0
  System.out.println("Elemen ke-2: " + angka[1]); | adalah untuk menampilkan dan melakukan akses terhadap elemen pada indeks ke "1"
  for (int i = 0; i < angka.length; i++) { ... } | adalah loop yang mengakses elemen, dan menampilkan


## Array dengan inisialisasi langsung 
```
public class ContohArray2 {
    public static void main(String[] args) {
        // Deklarasi + inisialisasi langsung
        String[] names = {"Alice", "Bob", "Charlie"};
        
        // Mengakses elemen
        System.out.println("Nama pertama: " + names[0]);
        
        // Mengubah nilai elemen
        names[1] = "Bobby";
        System.out.println("Nama kedua: " + names[1]);
    }
}
```

Breakdown:
code | Penjelasan
--- | ---
String[] names = {"Alice", "Bob", "Charlie"}; | Deklarasi dan inisialisasi 
names[1] = "Bobby"; | Menimpa nilai pada index ke 1 menjadi "Bobby"

========================================== Note tambahan untuk array =========================

## Mencari panjan array 
```
int panjang = angka.length;
```

## Loop dengan for-each ( Menampilkan setiap item pada array angka )
```
for (int nilai : angka) {
  System.out.println(niali) 
}
```

## Array multidimensi:
```
int[][] matrix = {{1, 2}, {3, 4}};
```
  
