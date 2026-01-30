# Javascript 

## Daftar Isi
- [Comment](#01)
- [Variabel](#02)
- [If Statement](#03)
- [Menambahkan Variabel ke Template String](#04)
- [Loops dan Iteration](#05)
- [Do While](#06)
- [While Statement](#07)
- [Labeled Statement](#08)
- [Convert String ke Number](#09)
- [Function](#10)
- [Parameters](#11)
- [Return Value](#12)
- [Get the Last Element in Array](#13)
- [Function Expression](#14)
- [Arrow Function](#15)
- [Callback Function](#16)
- [Rest Parameters](#17)
- [Object Notation](#18)
- [Class Syntax](#19)
- [What is a Class](#20)
- [Class Expression](#21)
- [Getters / Setters](#22)
- [Computed Names](#23)
- [Class Fields](#24)
- [Class Inheritance](#25)
- [Inheritance](#26)
- [Encapsulation Programming](#27)
- [For Each](#28)
- [Array Find](#29)
- [Filter](#30)
- [Map](#31)
- [Exports dan Require](#32)
- [Module Exports](#33)

## Pengenalan JavaScript

File format untuk JavaScript adalah `.js`

Untuk menjalankan JavaScript, kamu bisa menggunakan:
1. Console di web browser (tekan F12 atau klik kanan > Inspect)
2. Terminal Linux dengan menggunakan aplikasi Node.js (ketik `node namafile.js`)

### Tentang ECMAScript dan JavaScript

ECMAScript adalah standar yang mendefinisikan aturan bahasa JavaScript. Sedangkan JavaScript sendiri adalah implementasi dari standar ECMAScript tersebut. Jadi bisa dibilang ECMAScript adalah "buku aturan" sementara JavaScript adalah "praktiknya".

JavaScript engines (mesin JavaScript) biasanya ada di web browser, seperti:
- V8 di Chrome
- SpiderMonkey di Firefox  
- Chakra di Edge

Setiap engine ini seperti modul bahasa untuk aplikasinya, yang memungkinkan browser mendukung JavaScript.

Sumber: https://www.freecodecamp.org/news/whats-the-difference-between-javascript-and-ecmascript-cba48c73a2b5/

## Paradigma Programming 

Ada beberapa paradigma pemrograman yang berbeda, masing-masing punya ciri khas dan cara pandang tersendiri dalam menyelesaikan masalah. Berikut beberapa paradigma yang umum:

**Paradigma Pemrograman Prosedural**  
Pendekatan yang fokus pada urutan instruksi yang dilakukan terhadap data. Contohnya seperti kamu ngasih perintah step by step ke komputer.

**Paradigma Pemrograman Fungsional**  
Pendekatan yang lebih fokus pada fungsi, atau bagaimana data dimanipulasi dan diproses dalam program. Seperti resep masakan yang bisa dipake berkali-kali.

**Paradigma Pemrograman Berorientasi Objek (OOP)**  
Pendekatan yang mengorganisir program dalam bentuk objek yang terdiri dari data dan metode untuk memanipulasi data tersebut. Mirip seperti bikin blueprint mobil yang bisa diproduksi berkali-kali.

## Comment
### 01 

Komentar itu catatan yang kamu tulis di dalam kode tapi tidak dijalankan oleh program. Berguna banget buat ngingetin diri sendiri atau kasih tau orang lain tentang kode yang kamu tulis.

Penulisan komentar di JavaScript:

```javascript
// Ini komentar satu baris, cukup pake dua garis miring

/*
Ini komentar yang bisa beberapa baris,
kamu bisa tulis banyak baris di sini,
berguna buat penjelasan yang panjang
*/ 
```

## Variabel 
### 02 

Variabel adalah tempat untuk menyimpan data. Bayangkan seperti kotak yang bisa kamu kasih label dan isi dengan sesuatu.

Beberapa cara deklarasi variabel:

```javascript
var_a = 10          // cara lama, sekarang jarang dipake
let var_b = 10      // cara modern, nilai bisa diubah
const var_c = 10    // nilai tetap, tidak bisa diubah
```

Kamu juga bisa deklarasi beberapa variabel sekaligus:

```javascript
let user = "Budi",
    umur = 25 
```

**Aturan Penting:**

Tidak boleh deklarasi variabel yang sama dua kali dalam satu scope (ruang lingkup):

```javascript
let user = "budi"
let user = "bambang"  // Error! Variabel user sudah ada

// Akan muncul SyntaxError
```

Dalam penamaan variabel, tidak boleh ada angka di paling depan:

```javascript
let 01halo = "text"  // Error! Tidak boleh dimulai dengan angka

// Yang benar:
let halo01 = "text"  // Ini boleh
```

**Tips Penamaan Variabel:**
- Gunakan nama yang deskriptif: `namaUser` lebih baik dari `x`
- Pakai camelCase untuk nama yang terdiri dari beberapa kata: `namaDepan`, `umurUser`
- Hindari kata-kata reserved JavaScript seperti `class`, `function`, dll

Referensi: https://javascript.info/variables

## If Statement 
### 03 

Dengan if statement, kamu bisa bikin instruksi yang hanya dijalankan kalau persyaratan tertentu terpenuhi. Seperti "kalau hujan, bawa payung".

**Bentuk Dasar:**

```javascript
let year = 2022
if (year == 2022) console.log("tahun 2022")
// Output: tahun 2022 
```

Atau dengan blok kode (lebih umum):

```javascript
let year = 2022 
if (year == 2022) {
    console.log("tahun 2022")
}
// Output: tahun 2022 
```

**Dengan Else If dan Else:**

```javascript
let var_a = 10 

if (var_a == 10) {
    console.log('10')
} else if (var_a > 10) {
    console.log('lebih dari 10')
} else {
    console.log('kurang dari 10')
}
```

### Inline If Statement (Conditional Operator / Ternary)

Kalau kamu mau bikin if statement yang singkat, bisa pake operator ternary:

```javascript
let var_a = 2022
let year = (var_a == 2022) ? "sekarang tahun 2022" : "sekarang bukan 2022"

// Format: kondisi ? nilai_jika_true : nilai_jika_false
// Output: "sekarang tahun 2022"
```

Contoh dengan beberapa kondisi:

```javascript
let age = 18;

let message = (age < 3) ? 'Hi, baby!' :
  (age < 18) ? 'Hello!' :
  (age < 100) ? 'Greetings!' :
  'What an unusual age!';

console.log(message)
// Output: Greetings!
```

Sumber: https://javascript.info/ifelse

## Menambahkan Variabel ke Dalam String (Template Literal)
### 04

Template literal memungkinkan kamu memasukkan variabel langsung ke dalam string dengan mudah. Gunakan backtick (`) bukan tanda kutip biasa.

```javascript
let budi = "nama siswa"
let var_a = `halo ${budi}`
console.log(var_a)  // Output: halo nama siswa
```

Kelebihan template literal:
- Bisa pakai enter untuk baris baru tanpa perlu `\n`
- Bisa masukin variabel atau expresi dengan `${}`
- Lebih mudah dibaca

```javascript
let nama = "Andi"
let umur = 20
let pesan = `Nama saya ${nama}, umur saya ${umur} tahun.
Saya masih kuliah.`
// Bisa langsung enter tanpa masalah
```

Referensi case statement: https://www.freecodecamp.org/news/javascript-switch-case-js-switch-statement-example/

## Loops dan Iteration 
### 05

Loop bisa membuat instruksi yang berulang. Berguna banget kalau kamu mau melakukan sesuatu berkali-kali tanpa nulis kode yang sama berulang kali.

**For Loop:**

```javascript
for (let langkah = 0; langkah < 5; langkah++) {
    console.log('berjalan satu langkah')
}
// Output: "berjalan satu langkah" sebanyak 5 kali
```

### Struktur For Loop

```javascript
for ([initialExpression]; [conditionExpression]; [incrementExpression])
  statement
```

Cara kerjanya:
1. `initialExpression` biasanya sebagai loop counter (penghitung loop), dijalankan sekali di awal
2. `conditionExpression` adalah syarat dalam if statement (kalau memenuhi syarat maka dijalankan)
3. `statement` adalah blok kode yang dijalankan `{...}`
4. Setelah statement dijalankan, dilakukan increment pada counter
5. Kembali cek condition, kalau masih true lanjut lagi

Contoh lebih detail:

```javascript
for (let i = 0; i < 3; i++) {
    console.log(`Loop ke ${i}`)
}
// Output:
// Loop ke 0
// Loop ke 1
// Loop ke 2
```

## Do While
### 06

Do while adalah loop yang pasti dijalankan minimal satu kali, baru kemudian dicek kondisinya.

```javascript
do {
    statement
} while (condition);
```

Kalau condition bernilai `true`, statement akan terus dijalankan.

Contoh:

```javascript
let i = 0;
do {
  i += 1;
  console.log(i);
} while (i < 5);

// Output: 1, 2, 3, 4, 5
```

Perbedaan dengan while biasa:
- `do while` pasti jalan minimal 1x, baru cek kondisi
- `while` biasa cek kondisi dulu, baru jalan

## While Statement 
### 07 

While loop terus berjalan selama kondisinya masih true.

```javascript
while (condition) {
    statement
}
```

Contoh sederhana:

```javascript
let n = 0;
let x = 0;
while (n < 3) {
  n++;
  x += n;
}
// n akan jadi 3, x akan jadi 6 (1+2+3)
```

Contoh dengan kondisi yang lebih kompleks:

```javascript
let main = true
let value = 0
while (main) {
  value += 1
  if (value == 5) {
    console.log('end')
    main = false
  }
}
// Loop berhenti saat value mencapai 5
```

**Hati-hati:** Pastikan kondisinya bisa jadi false, kalau tidak loop akan jalan terus (infinite loop)!

## Labeled Statement 
### 08

Dengan labeled statement, kamu bisa menutup loop yang lebih spesifik, terutama kalau ada nested loop (loop dalam loop).

Tidak harus pakai `break`, kamu juga bisa gunakan `continue` untuk restart loop dari awal lagi.

Contoh:

```javascript
let x = 0;
let z = 0;
labelCancelLoops: while (true) {
  console.log('Outer loops: ' + x);
  x += 1;
  z = 1;
  while (true) {
    console.log('Inner loops: ' + z);
    z += 1;
    if (z === 10 && x === 10) {
      break labelCancelLoops;  // Keluar dari kedua loop sekaligus
    } else if (z === 10) {
      break;  // Hanya keluar dari inner loop
    }
  }
}
```

**Kapan Pakai:**
- Saat ada nested loop yang dalam
- Kamu mau keluar dari semua loop sekaligus, bukan cuma loop terdekat

## For In 

For in digunakan untuk loop melalui index dari array atau properti dari object.

```javascript
let makanan = ['nasi', 'tahu', 'tempe']

for (let i in makanan) {
  console.log(i)
}

// Output: 0 1 2 (index dari array)
```

Contoh dengan object:

```javascript
let person = {nama: "Budi", umur: 25, kota: "Surabaya"}

for (let key in person) {
  console.log(key + ": " + person[key])
}
// Output:
// nama: Budi
// umur: 25
// kota: Surabaya
```

## For Of 

For of digunakan untuk loop melalui nilai (value) dari array.

```javascript
let makanan = ['nasi', 'tahu', 'tempe']

for (let i of makanan) {
  console.log(i)
}

// Output: nasi tahu tempe (nilai dari array)
```

**Perbedaan For In vs For Of:**
- `for in` → dapat index/key
- `for of` → dapat value

Sumber: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration?retiredLocale=id

## Convert String ke Number 
### 09 

Ada beberapa cara untuk mengubah string menjadi number:

**1. parseInt()**

Mengubah string jadi integer (bilangan bulat):

```javascript
let myString = '140'
parseInt(myString)  // 140 

let a = 34.22
parseInt(a)  // 34 (desimal dihilangkan)
```

**2. Number()**

Mengubah string jadi number (bisa desimal):

```javascript
Number("10");          // 10 
Number(" 10  ");       // 10 (spasi diabaikan)
Number("10.33");       // 10.33 (tetap ada desimalnya)
```

**3. parseFloat()**

Khusus untuk mengubah string ke bilangan desimal:

```javascript
parseFloat("10.33");   // 10.33
parseFloat("10");      // 10
```

**4. Operator + (Plus)**

Cara singkat dengan operator:

```javascript
let str = "123"
let num = +str  // 123 (tipe number)
```

Sumber: https://dev.to/sanchithasr/7-ways-to-convert-a-string-to-number-in-javascript-4l

## Function | ES5
### 10

Function adalah blok kode yang bisa dipanggil berkali-kali. Bayangkan seperti resep masakan, sekali tulis bisa dipake kapan aja.

```javascript
function namaFungsi() {
    console.log('halo')
}
```

Cara memanggilnya:

```javascript
namaFungsi()  // Output: halo
```

Dengan menggunakan function, kamu bisa pakai blok kode tersebut kapan saja tanpa nulis ulang.

### Local Variable

Variabel yang dideklarasi dalam function hanya bisa diakses dari dalam function tersebut:

```javascript
function myFunction() {
    let var_a = "hello"  // Hanya bisa diakses di dalam function ini
}

console.log(var_a)  // Error! var_a tidak bisa diakses di luar
```

### Catatan Tambahan Function

**ES5 vs ES6:**
- Expression function dan function biasa sudah ada dari versi ES5
- Arrow function baru ada di ES6

**Hoisting di Node.js:**
Pada Node.js, function declaration mengalami hoisting. Artinya kamu bisa panggil function sebelum ditulis:

```javascript
myFunction()  // Ini tetap jalan

function myFunction() {
    console.log("halo")
}
```

**Catatan:** Hoisting hanya berlaku untuk function declaration, tidak untuk function expression atau arrow function.

Referensi: https://medium.com/@zac_heisey/es5-vs-es6-functions-cb51536002ee

## Parameters
### 11

Parameter adalah nilai yang bisa kamu kirim ke dalam function.

```javascript
function myFunction(nama) {
    console.log(nama)
}

myFunction("Budi")  // Output: Budi
```

### Parameter Default

Kamu bisa kasih nilai default kalau parameter tidak diisi:

```javascript
function myFunction(nama = "budi") {
    console.log(nama)
}

myFunction()        // Output: budi (pakai default)
myFunction("Andi")  // Output: Andi (pakai yang dikirim)
```

### Multiple Parameters

Bisa terima beberapa parameter sekaligus:

```javascript
function perkenalan(nama, umur, kota) {
    console.log(`Nama: ${nama}, Umur: ${umur}, Kota: ${kota}`)
}

perkenalan("Budi", 25, "Jakarta")
// Output: Nama: Budi, Umur: 25, Kota: Jakarta
```

## Return Value 
### 12

Return digunakan untuk mengembalikan nilai dari function. Setelah return, kode di bawahnya tidak akan dijalankan.

```javascript
function tambah(a, b) {
    return a + b
}

let hasil = tambah(5, 3)  // hasil = 8
```

Contoh tanpa return:

```javascript
function sapaan(nama) {
    console.log("Halo " + nama)
    // Tidak ada return, function tidak mengembalikan nilai
}

let x = sapaan("Budi")  // x = undefined
```

### Return di Tengah Function

Return juga bisa dipakai untuk menghentikan function:

```javascript
function cekUmur(umur) {
    if (umur < 18) {
        return "Belum cukup umur"  // Function berhenti di sini
    }
    return "Sudah cukup umur"
}
```

## Get the Last Element in Array
### 13

Ada beberapa cara untuk mengambil element terakhir dari array:

**1. Pakai Length:**

```javascript
let fruits = ["apel", "jeruk", "mangga"]
let lastFruit = fruits[fruits.length - 1]  // "mangga"
```

**2. Pakai Slice:**

```javascript
let fruits = ["apel", "jeruk", "mangga"]
let lastFruit = fruits.slice(-1)[0]  // "mangga"
```

**3. Pakai Pop (tapi ini menghapus element):**

```javascript
let fruits = ["apel", "jeruk", "mangga"]
let lastFruit = fruits.pop()  // "mangga"
// Tapi fruits sekarang jadi ["apel", "jeruk"]
```

**4. Pakai At (ES2022):**

```javascript
let fruits = ["apel", "jeruk", "mangga"]
let lastFruit = fruits.at(-1)  // "mangga"
```

## Function Expression
### 14

Function expression adalah cara lain untuk membuat function, dengan menyimpannya ke dalam variabel.

```javascript
let sapaan = function(nama) {
    return "Halo " + nama
}

console.log(sapaan("Budi"))  // Output: Halo Budi
```

**Perbedaan dengan Function Declaration:**

```javascript
// Function Declaration (ada hoisting)
greet()  // Bisa dipanggil sebelum ditulis
function greet() {
    console.log("Halo")
}

// Function Expression (tidak ada hoisting)
greet()  // Error! Tidak bisa dipanggil sebelum dideklarasi
let greet = function() {
    console.log("Halo")
}
```

## Arrow Function
### 15

Arrow function adalah cara singkat untuk menulis function (ES6). Pakai tanda panah `=>`.

**Bentuk Lengkap:**

```javascript
let tambah = (a, b) => {
    return a + b
}
```

**Bentuk Singkat (kalau cuma satu statement):**

```javascript
let tambah = (a, b) => a + b
```

**Kalau Cuma Satu Parameter:**

```javascript
let kuadrat = x => x * x
// Bisa tanpa kurung untuk satu parameter
```

**Tanpa Parameter:**

```javascript
let sapaan = () => console.log("Halo")
```

### Perbedaan Arrow Function dengan Function Biasa:

1. Sintaks lebih singkat
2. Tidak punya `this` sendiri (pakai `this` dari luar)
3. Tidak bisa dipakai sebagai constructor
4. Tidak punya `arguments` object

Contoh perbedaan `this`:

```javascript
// Function biasa
let obj1 = {
    nama: "Budi",
    sapaan: function() {
        console.log("Halo " + this.nama)  // this merujuk ke obj1
    }
}

// Arrow function
let obj2 = {
    nama: "Andi",
    sapaan: () => {
        console.log("Halo " + this.nama)  // this tidak merujuk ke obj2
    }
}
```

## Callback Function
### 16

Callback adalah function yang dikirim sebagai parameter ke function lain, untuk dijalankan nanti.

**Contoh Sederhana:**

```javascript
function salam(nama) {
    console.log("Halo " + nama)
}

function prosesInput(callback) {
    let nama = "Budi"
    callback(nama)  // Memanggil function salam
}

prosesInput(salam)  // Output: Halo Budi
```

**Contoh dengan Anonymous Function:**

```javascript
function prosesInput(callback) {
    let nama = "Budi"
    callback(nama)
}

prosesInput(function(nama) {
    console.log("Halo " + nama)
})
```

**Contoh Nyata (Array Methods):**

```javascript
let numbers = [1, 2, 3, 4, 5]

// map pakai callback function
let doubled = numbers.map(function(num) {
    return num * 2
})
// [2, 4, 6, 8, 10]

// Atau pakai arrow function
let doubled2 = numbers.map(num => num * 2)
```

### Kapan Pakai Callback:

- Operasi asynchronous (fetch data, timer)
- Event handling (klik button, submit form)
- Array methods (map, filter, forEach)

## Rest Parameters
### 17

Rest parameters memungkinkan function menerima jumlah parameter yang tidak terbatas sebagai array. Pakai tiga titik `...`.

**Sintaks:**

```javascript
function namaFunction(...namaParameter) {
    // namaParameter adalah array
}
```

**Contoh:**

```javascript
function tambahSemua(...numbers) {
    let total = 0
    for (let num of numbers) {
        total += num
    }
    return total
}

console.log(tambahSemua(1, 2, 3))        // 6
console.log(tambahSemua(1, 2, 3, 4, 5))  // 15
```

**Dengan Arrow Function:**

```javascript
let fun = (...arg) => {
    arg.map((i) => console.log(i))
}

fun(1, 2, 3, 4, 5, 6, 7)
// Output: 1 2 3 4 5 6 7
```

**Rest Parameter dengan Parameter Biasa:**

```javascript
function perkenalan(nama, umur, ...hobi) {
    console.log(`Nama: ${nama}`)
    console.log(`Umur: ${umur}`)
    console.log(`Hobi: ${hobi.join(", ")}`)
}

perkenalan("Budi", 20, "Membaca", "Gaming", "Coding")
// Nama: Budi
// Umur: 20
// Hobi: Membaca, Gaming, Coding
```

**Catatan:** Rest parameter harus selalu di posisi terakhir!

## Object Notation
### 18

Object adalah kumpulan data dan function yang tersimpan dalam pasangan key-value.

**Membuat Object:**

```javascript
let person = {
    nama: "Budi",
    umur: 25,
    kota: "Jakarta",
    salam: function() {
        console.log("Halo dari " + this.nama)
    }
}
```

**Mengakses Property:**

```javascript
console.log(person.nama)      // Budi
console.log(person["umur"])   // 25
person.salam()                // Halo dari Budi
```

**Menambah Property:**

```javascript
person.pekerjaan = "Developer"
person["email"] = "budi@email.com"
```

**Mengubah Property:**

```javascript
person.umur = 26
person["kota"] = "Surabaya"
```

**Menghapus Property:**

```javascript
delete person.pekerjaan
```

**Object Method Shorthand (ES6):**

```javascript
let person = {
    nama: "Budi",
    salam() {  // Tidak perlu tulis function
        console.log("Halo")
    }
}
```

**Property Shorthand:**

```javascript
let nama = "Budi"
let umur = 25

// Cara lama
let person1 = {
    nama: nama,
    umur: umur
}

// Cara baru (ES6)
let person2 = { nama, umur }  // Sama hasilnya
```

## Class Syntax
### 19

Class adalah template untuk membuat object. Sintaks class diperkenalkan di ES6 untuk membuat OOP lebih mudah di JavaScript.

**Sintaks Dasar:**

```javascript
class Person {
    constructor(nama, umur) {
        this.nama = nama
        this.umur = umur
    }
    
    salam() {
        console.log(`Halo, nama saya ${this.nama}`)
    }
}
```

**Membuat Instance:**

```javascript
let budi = new Person("Budi", 25)
let andi = new Person("Andi", 30)

budi.salam()  // Halo, nama saya Budi
andi.salam()  // Halo, nama saya Andi
```

**Constructor:**
- Method khusus yang otomatis dipanggil saat membuat instance baru
- Digunakan untuk inisialisasi property

**Method:**
- Function yang ada di dalam class
- Bisa dipanggil oleh semua instance

## What is a Class
### 20

Class adalah blueprint (cetak biru) untuk membuat object. Seperti desain rumah yang bisa dipakai untuk membangun banyak rumah yang mirip.

**Konsep Dasar:**

```javascript
// Class = Blueprint
class Mobil {
    constructor(merk, warna) {
        this.merk = merk
        this.warna = warna
    }
    
    jalan() {
        console.log(`${this.merk} berwarna ${this.warna} sedang jalan`)
    }
}

// Instance = Hasil dari blueprint
let mobil1 = new Mobil("Toyota", "Merah")
let mobil2 = new Mobil("Honda", "Biru")

mobil1.jalan()  // Toyota berwarna Merah sedang jalan
mobil2.jalan()  // Honda berwarna Biru sedang jalan
```

**Kenapa Pakai Class:**

1. Organisasi kode lebih baik
2. Bisa buat banyak object dengan property dan method yang sama
3. Mendukung inheritance (pewarisan)
4. Code lebih mudah di-maintain

**Analogi:**
- Class = Cetakan kue
- Instance = Kue yang dihasilkan dari cetakan
- Property = Karakteristik kue (rasa, ukuran)
- Method = Apa yang bisa dilakukan dengan kue (dimakan, dihias)

## Class Expression
### 21

Selain class declaration, kamu juga bisa buat class dengan class expression (disimpan dalam variabel).

**Named Class Expression:**

```javascript
let Person = class Orang {
    constructor(nama) {
        this.nama = nama
    }
    
    salam() {
        console.log(`Halo ${this.nama}`)
    }
}

let budi = new Person("Budi")
budi.salam()  // Halo Budi
```

**Anonymous Class Expression:**

```javascript
let Person = class {
    constructor(nama) {
        this.nama = nama
    }
    
    salam() {
        console.log(`Halo ${this.nama}`)
    }
}

let budi = new Person("Budi")
```

**Perbedaan dengan Class Declaration:**

1. Class expression tidak mengalami hoisting (seperti function expression)
2. Bisa disimpan dalam variabel, dikirim sebagai parameter, atau dikembalikan dari function

## Getters / Setters
### 22

Getter dan Setter adalah method khusus untuk mengakses dan mengubah property dengan kontrol lebih.

**Getter:** Method untuk mendapatkan nilai property
**Setter:** Method untuk mengatur nilai property

**Contoh Dasar:**

```javascript
class Person {
    constructor(namaDepan, namaBelakang) {
        this._namaDepan = namaDepan
        this._namaBelakang = namaBelakang
    }
    
    // Getter
    get namaLengkap() {
        return `${this._namaDepan} ${this._namaBelakang}`
    }
    
    // Setter
    set namaLengkap(nama) {
        let parts = nama.split(" ")
        this._namaDepan = parts[0]
        this._namaBelakang = parts[1]
    }
}

let person = new Person("Budi", "Santoso")
console.log(person.namaLengkap)  // Budi Santoso (pakai getter)

person.namaLengkap = "Andi Wijaya"  // Pakai setter
console.log(person._namaDepan)      // Andi
```

**Contoh dengan Validasi:**

```javascript
class BudiFamily {
    constructor(namaDepan, namaBelakang) {
        this._firstName = namaDepan
        this._lastName = namaBelakang
    }

    get firstName() {
        console.log('Getter dipanggil dengan ' + this._firstName)
        return this._firstName
    }

    set firstName(parameter) {
        console.log('Setter dipanggil dengan ' + parameter)
        if (parameter != "budi") {
            throw new Error('First Name harus budi!')
        }
        this._firstName = parameter
    }
}

let anakBudi = new BudiFamily("budi", 'toni')
console.log(anakBudi.firstName)  // Mengakses getter
// anakBudi.firstName = 'wahyu'  // Error dari setter
```

**Contoh Lain dengan Validasi di Getter:**

```javascript
class BudiFamily {
    constructor(namaDepan, namaBelakang) {
        this._firstName = namaDepan
        this._lastName = namaBelakang
    }

    get firstName() {
        if (this._firstName != 'budi') {
            throw new Error('Parameter default harus Budi!')
        }
        return this._firstName
    }

    set firstName(parameter) {
        if (parameter != "budi") {
            throw new Error('Nilai yang diubah juga harus budi!')
        }
        this._firstName = parameter
    }
}

let anakBudi = new BudiFamily("budi", 'toni')
console.log(anakBudi.firstName)  // Ini akan mengakses getter
console.log(anakBudi._firstName) // Ini mengakses property langsung

// anakBudi.firstName = "wahyu"  // Error dari setter
// let anakOmBudi = new BudiFamily('rangga', 'wahyu')  // Error dari getter
```

**Catatan Penting:**

- Getter bekerja saat instance dibuat dan saat property diakses. Mereka melakukan pengecekan pada argument yang dimasukkan
- Setter bekerja saat instance sudah terbuat dan ada perubahan property
- Getter bekerja seperti function tapi dipanggil seperti property (tanpa tanda kurung)
- Getter tidak boleh punya parameter
- Setter harus punya tepat satu parameter

**Cara Kerja Get dan Set:**

1. Saat instance dibuat, constructor mengisi property
2. Kalau ada getter, property bisa diakses seperti variabel biasa
3. Kalau ada setter, property bisa diubah dengan validasi
4. Setter dijalankan dulu, lalu hasilnya disimpan dan bisa diakses lewat getter

## Computed Names
### 23

Computed property names memungkinkan kamu menggunakan expresi sebagai nama property.

**Contoh Dasar:**

```javascript
let propName = "nama"

let person = {
    [propName]: "Budi",  // Sama dengan nama: "Budi"
    ["umur"]: 25
}

console.log(person.nama)  // Budi
```

**Dengan Expresi:**

```javascript
let prefix = "user"
let id = 123

let obj = {
    [prefix + id]: "Budi",        // user123: "Budi"
    [prefix + "_name"]: "Data"    // user_name: "Data"
}

console.log(obj.user123)      // Budi
console.log(obj.user_name)    // Data
```

**Di Dalam Class:**

```javascript
let methodName = "salam"

class Person {
    constructor(nama) {
        this.nama = nama
    }
    
    [methodName]() {
        console.log(`Halo ${this.nama}`)
    }
}

let person = new Person("Budi")
person.salam()  // Halo Budi
```

## Class Fields
### 24

Class fields adalah cara modern untuk deklarasi property langsung di dalam class body (tanpa constructor).

**Sintaks Dasar:**

```javascript
class Person {
    // Public field
    nama = "Default"
    umur = 0
    
    // Method
    salam() {
        console.log(`Halo ${this.nama}`)
    }
}

let person = new Person()
console.log(person.nama)  // Default
```

**Dengan Constructor:**

```javascript
class Person {
    nama = "Default"  // Nilai default
    
    constructor(nama) {
        if (nama) {
            this.nama = nama  // Override nilai default
        }
    }
}

let person1 = new Person()        // nama: "Default"
let person2 = new Person("Budi")  // nama: "Budi"
```

**Private Fields (ES2022):**

Private field pakai tanda `#` di depan nama:

```javascript
class BankAccount {
    #saldo = 0  // Private field
    
    deposit(jumlah) {
        this.#saldo += jumlah
    }
    
    getSaldo() {
        return this.#saldo
    }
}

let akun = new BankAccount()
akun.deposit(1000)
console.log(akun.getSaldo())  // 1000
// console.log(akun.#saldo)   // Error! Private field tidak bisa diakses dari luar
```

**Keuntungan Class Fields:**

1. Lebih clean dan mudah dibaca
2. Bisa langsung kasih nilai default
3. Support private fields untuk encapsulation

## Class Inheritance
### 25

Inheritance (pewarisan) memungkinkan class baru mewarisi property dan method dari class yang sudah ada.

**Sintaks Dasar dengan `extends`:**

```javascript
class Animal {
    constructor(nama) {
        this.nama = nama
    }
    
    suara() {
        console.log(`${this.nama} bersuara`)
    }
}

class Kucing extends Animal {
    suara() {
        console.log(`${this.nama} mengeong: Meow!`)
    }
}

let kucing = new Kucing("Tom")
kucing.suara()  // Tom mengeong: Meow!
```

**Menggunakan `super`:**

`super` digunakan untuk memanggil constructor atau method dari parent class:

```javascript
class Animal {
    constructor(nama, umur) {
        this.nama = nama
        this.umur = umur
    }
    
    info() {
        console.log(`Nama: ${this.nama}, Umur: ${this.umur}`)
    }
}

class Anjing extends Animal {
    constructor(nama, umur, ras) {
        super(nama, umur)  // Panggil constructor parent
        this.ras = ras
    }
    
    info() {
        super.info()  // Panggil method parent
        console.log(`Ras: ${this.ras}`)
    }
}

let anjing = new Anjing("Buddy", 3, "Golden Retriever")
anjing.info()
// Nama: Buddy, Umur: 3
// Ras: Golden Retriever
```

**Method Overriding:**

Child class bisa override (menimpa) method dari parent:

```javascript
class Bentuk {
    luas() {
        return 0
    }
}

class Persegi extends Bentuk {
    constructor(sisi) {
        super()
        this.sisi = sisi
    }
    
    luas() {  // Override method luas
        return this.sisi * this.sisi
    }
}

let persegi = new Persegi(5)
console.log(persegi.luas())  // 25
```

## Inheritance
### 26

Inheritance (pewarisan) adalah salah satu pilar OOP yang memungkinkan class mewarisi karakteristik dari class lain.

**Konsep:**
- **Parent Class / Super Class:** Class yang diwariskan
- **Child Class / Sub Class:** Class yang mewarisi

**Keuntungan Inheritance:**

1. **Code Reusability:** Tidak perlu tulis ulang kode yang sama
2. **Hierarki:** Bisa buat struktur class yang terorganisir
3. **Polymorphism:** Child class bisa punya behavior berbeda

**Contoh Nyata:**

```javascript
// Parent Class
class Kendaraan {
    constructor(merk, tahun) {
        this.merk = merk
        this.tahun = tahun
    }
    
    info() {
        return `${this.merk} tahun ${this.tahun}`
    }
    
    jalan() {
        console.log("Kendaraan berjalan")
    }
}

// Child Class 1
class Mobil extends Kendaraan {
    constructor(merk, tahun, pintu) {
        super(merk, tahun)
        this.pintu = pintu
    }
    
    jalan() {
        console.log(`Mobil ${this.merk} berjalan di jalan raya`)
    }
}

// Child Class 2
class Motor extends Kendaraan {
    constructor(merk, tahun, cc) {
        super(merk, tahun)
        this.cc = cc
    }
    
    jalan() {
        console.log(`Motor ${this.merk} berjalan di jalan`)
    }
}

let mobil = new Mobil("Toyota", 2020, 4)
let motor = new Motor("Honda", 2021, 150)

mobil.jalan()  // Mobil Toyota berjalan di jalan raya
motor.jalan()  // Motor Honda berjalan di jalan
```

## Encapsulation Programming
### 27

Encapsulation adalah konsep untuk menyembunyikan detail implementasi dan hanya menampilkan fungsionalitas yang diperlukan.

**Tujuan Encapsulation:**

1. Melindungi data dari akses langsung
2. Kontrol akses ke property dan method
3. Membuat kode lebih aman dan maintainable

**Cara Implementasi:**

**1. Pakai Konvensi (underscore):**

```javascript
class BankAccount {
    constructor(saldo) {
        this._saldo = saldo  // Konvensi: underscore = internal property
    }
    
    deposit(jumlah) {
        if (jumlah > 0) {
            this._saldo += jumlah
        }
    }
    
    getSaldo() {
        return this._saldo
    }
}

let akun = new BankAccount(1000)
akun.deposit(500)
console.log(akun.getSaldo())  // 1500
// akun._saldo = 0  // Tidak disarankan! Tapi masih bisa
```

**2. Pakai Private Fields (ES2022):**

```javascript
class BankAccount {
    #saldo  // Private field
    
    constructor(saldo) {
        this.#saldo = saldo
    }
    
    deposit(jumlah) {
        if (jumlah > 0) {
            this.#saldo += jumlah
        }
    }
    
    withdraw(jumlah) {
        if (jumlah > 0 && jumlah <= this.#saldo) {
            this.#saldo -= jumlah
            return true
        }
        return false
    }
    
    getSaldo() {
        return this.#saldo
    }
}

let akun = new BankAccount(1000)
akun.deposit(500)
console.log(akun.getSaldo())  // 1500
// console.log(akun.#saldo)   // Error! Tidak bisa diakses dari luar
```

**3. Pakai Getter/Setter:**

```javascript
class Person {
    #umur
    
    constructor(umur) {
        this.#umur = umur
    }
    
    get umur() {
        return this.#umur
    }
    
    set umur(nilai) {
        if (nilai > 0 && nilai < 150) {
            this.#umur = nilai
        } else {
            console.log("Umur tidak valid")
        }
    }
}

let person = new Person(25)
console.log(person.umur)  // 25
person.umur = 26          // OK
person.umur = 200         // Umur tidak valid
```

## For Each
### 28

forEach adalah method array untuk melakukan loop pada setiap element. Lebih simple dari for loop biasa.

**Sintaks:**

```javascript
array.forEach(function(element, index, array) {
    // code
})
```

**Contoh Dasar:**

```javascript
let buah = ["apel", "jeruk", "mangga"]

buah.forEach(function(item) {
    console.log(item)
})
// Output: apel jeruk mangga
```

**Dengan Arrow Function:**

```javascript
let numbers = [1, 2, 3, 4, 5]

numbers.forEach(num => console.log(num * 2))
// Output: 2 4 6 8 10
```

**Dengan Index:**

```javascript
let buah = ["apel", "jeruk", "mangga"]

buah.forEach((item, index) => {
    console.log(`${index}: ${item}`)
})
// Output:
// 0: apel
// 1: jeruk
// 2: mangga
```

**Perbedaan forEach vs for:**

```javascript
// For Loop
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i])
    // Bisa pakai break, continue
}

// forEach
arr.forEach(item => {
    console.log(item)
    // Tidak bisa pakai break, continue
})
```

**Catatan:** forEach tidak bisa dihentikan di tengah jalan (tidak bisa pakai break).

## Array Find
### 29

Method `find()` mencari element pertama yang memenuhi kondisi dan mengembalikan element tersebut.

**Sintaks:**

```javascript
array.find(function(element, index, array) {
    // return true jika element memenuhi kondisi
})
```

**Contoh Dasar:**

```javascript
let numbers = [1, 5, 10, 15, 20]

let result = numbers.find(num => num > 10)
console.log(result)  // 15 (element pertama yang > 10)
```

**Mencari Object dalam Array:**

```javascript
let users = [
    { id: 1, nama: "Budi" },
    { id: 2, nama: "Andi" },
    { id: 3, nama: "Citra" }
]

let user = users.find(u => u.id === 2)
console.log(user)  // { id: 2, nama: "Andi" }
```

**Kalau Tidak Ketemu:**

```javascript
let numbers = [1, 2, 3, 4, 5]

let result = numbers.find(num => num > 10)
console.log(result)  // undefined (tidak ada yang memenuhi)
```

**find() vs filter():**

```javascript
let numbers = [1, 5, 10, 15, 20]

// find: return element pertama yang cocok
let found = numbers.find(num => num > 10)  // 15

// filter: return array semua element yang cocok
let filtered = numbers.filter(num => num > 10)  // [15, 20]
```

## Filter
### 30

Method `filter()` membuat array baru berisi semua element yang memenuhi kondisi.

**Sintaks:**

```javascript
array.filter(function(element, index, array) {
    // return true untuk element yang mau disimpan
})
```

**Contoh Dasar:**

```javascript
let numbers = [1, 2, 3, 4, 5, 6]

let evenNumbers = numbers.filter(num => num % 2 === 0)
console.log(evenNumbers)  // [2, 4, 6]
```

**Filter Object:**

```javascript
let products = [
    { nama: "Laptop", harga: 10000000 },
    { nama: "Mouse", harga: 50000 },
    { nama: "Keyboard", harga: 200000 }
]

let murah = products.filter(p => p.harga < 1000000)
console.log(murah)
// [{ nama: "Mouse", harga: 50000 }, { nama: "Keyboard", harga: 200000 }]
```

**Multiple Conditions:**

```javascript
let users = [
    { nama: "Budi", umur: 17, aktif: true },
    { nama: "Andi", umur: 25, aktif: true },
    { nama: "Citra", umur: 30, aktif: false }
]

let result = users.filter(u => u.umur >= 18 && u.aktif)
console.log(result)  // [{ nama: "Andi", umur: 25, aktif: true }]
```

**Filter String:**

```javascript
let names = ["Budi", "Andi", "Bambang", "Citra"]

let withB = names.filter(name => name.startsWith("B"))
console.log(withB)  // ["Budi", "Bambang"]
```

## Map
### 31

Method `map()` membuat array baru dengan hasil dari function yang dipanggil pada setiap element.

**Sintaks:**

```javascript
array.map(function(element, index, array) {
    // return nilai baru untuk element
})
```

**Contoh Dasar:**

```javascript
let numbers = [1, 2, 3, 4, 5]

let doubled = numbers.map(num => num * 2)
console.log(doubled)  // [2, 4, 6, 8, 10]
```

**Map Object Property:**

```javascript
let users = [
    { nama: "Budi", umur: 25 },
    { nama: "Andi", umur: 30 },
    { nama: "Citra", umur: 27 }
]

let names = users.map(user => user.nama)
console.log(names)  // ["Budi", "Andi", "Citra"]
```

**Transform Object:**

```javascript
let products = [
    { nama: "Laptop", harga: 10000 },
    { nama: "Mouse", harga: 50 }
]

let withTax = products.map(p => {
    return {
        nama: p.nama,
        hargaAsli: p.harga,
        hargaPajak: p.harga * 1.1
    }
})
```

**Chaining Methods:**

```javascript
let numbers = [1, 2, 3, 4, 5, 6]

let result = numbers
    .filter(num => num % 2 === 0)  // [2, 4, 6]
    .map(num => num * 2)            // [4, 8, 12]

console.log(result)  // [4, 8, 12]
```

**map() vs forEach():**

```javascript
// map: membuat array baru
let doubled = numbers.map(num => num * 2)

// forEach: tidak return apa-apa (cuma untuk side effect)
numbers.forEach(num => console.log(num * 2))
```

## Exports dan Require
### 32

Exports dan require digunakan untuk membagi kode ke beberapa file (modular).

**Sintaks CommonJS (Node.js):**

**File: math.js**

```javascript
function tambah(a, b) {
    return a + b
}

function kurang(a, b) {
    return a - b
}

// Export function
module.exports = {
    tambah,
    kurang
}
```

**File: main.js**

```javascript
// Import module
const math = require('./math.js')

console.log(math.tambah(5, 3))   // 8
console.log(math.kurang(10, 4))  // 6
```

**Export Individual:**

```javascript
// File: utils.js
function greet(nama) {
    return `Halo ${nama}`
}

module.exports.greet = greet

// Atau langsung
exports.greet = function(nama) {
    return `Halo ${nama}`
}
```

**Import Individual:**

```javascript
const { greet } = require('./utils.js')
console.log(greet("Budi"))  // Halo Budi
```

## Module Exports
### 33

Module exports adalah cara untuk mengexport sesuatu dari file.

**Export Default:**

```javascript
// File: person.js
class Person {
    constructor(nama) {
        this.nama = nama
    }
}

module.exports = Person  // Export class
```

**Import:**

```javascript
// File: main.js
const Person = require('./person.js')

let budi = new Person("Budi")
```

**Export Multiple:**

```javascript
// File: helpers.js
const PI = 3.14159

function luasLingkaran(r) {
    return PI * r * r
}

function kelilingLingkaran(r) {
    return 2 * PI * r
}

module.exports = {
    PI,
    luasLingkaran,
    kelilingLingkaran
}
```

**Import Multiple:**

```javascript
const { PI, luasLingkaran } = require('./helpers.js')

console.log(luasLingkaran(5))  // 78.53975
```

**ES6 Modules (Modern):**

```javascript
// Export
export function tambah(a, b) {
    return a + b
}

export const PI = 3.14

// Import
import { tambah, PI } from './math.js'
```

**Catatan:** ES6 modules pakai `import/export`, sedangkan CommonJS pakai `require/module.exports`.

## Undefined vs Null

Undefined dan null keduanya merepresentasikan "kosong", tapi punya arti yang berbeda.

```javascript
let a
typeof a  // "undefined"

let c = undefined  // Tidak disarankan dalam komunitas
// Referensi: https://www.geeksforgeeks.org/undefined-vs-null-in-javascript/

let b = null
typeof b  // "object" (ini quirk JavaScript)

null == undefined   // true (nilai konsepnya sama)
null === undefined  // false (tipe nilai mereka berbeda)
```

**Perbedaan:**

**Undefined:**
- Bentuk kosong sepenuhnya
- Terjadi saat deklarasi variabel tapi tidak diberi nilai
- Secara otomatis diberikan JavaScript

```javascript
let nama
console.log(nama)  // undefined

function test() {
    // Tidak ada return
}
console.log(test())  // undefined
```

**Null:**
- Nilai yang bisa kita masukkan ke variabel
- Merepresentasikan "sengaja dikosongkan"
- Kita yang secara eksplisit set nilainya

```javascript
let user = null  // Sengaja diisi null (belum ada user)

// Nanti bisa diisi
user = { nama: "Budi" }
```

**Kapan Pakai:**
- Pakai `undefined` untuk variabel yang belum diinisialisasi
- Pakai `null` untuk sengaja mengosongkan nilai

Referensi: https://www.geeksforgeeks.org/undefined-vs-null-in-javascript/

## Get dan Setter 

Getter dan Setter adalah cara untuk mengontrol akses ke property class.

**Contoh Pertama:**

```javascript
class BudiFamily {
    constructor(namaDepan, namaBelakang) {
        this._firstName = namaDepan
        this._lastName = namaBelakang
    }

    get firstName() {
        console.log('Getter dipanggil dengan ' + this._firstName)
        return this._firstName
    }

    set firstName(parameter) {
        console.log('Setter dipanggil dengan ' + parameter)
        if (parameter != "budi") {
            throw new Error('First Name harus budi!')
        }
        this._firstName = parameter
    }
}

let anakBudi = new BudiFamily("budi", 'toni')
console.log(anakBudi.firstName)  // Mengakses getter
console.log(anakBudi._firstName) // Mengakses property langsung
console.log(anakBudi.lastName)   // Undefined (tidak ada getter)
// anakBudi.firstName = 'wahyu'  // Error dari setter
```

**Contoh Kedua dengan Validasi:**

```javascript
class BudiFamily {
    constructor(namaDepan, namaBelakang) {
        this._firstName = namaDepan
        this._lastName = namaBelakang
    }

    get firstName() {
        if (this._firstName != 'budi') {
            throw new Error('Parameter default harus Budi!')
        }
        return this._firstName
    }

    set firstName(parameter) {
        if (parameter != "budi") {
            throw new Error('Nilai yang diubah juga harus budi!')
        }
        this._firstName = parameter
    }
}

let anakBudi = new BudiFamily("budi", 'toni')

console.log(anakBudi.firstName)  // Mengakses getter
console.log(anakBudi._firstName) // Mengakses property langsung

// anakBudi.firstName = "wahyu"  // Error dari setter

// let anakOmBudi = new BudiFamily('rangga', 'wahyu')
// Error dari getter saat mencoba akses firstName
```

**Cerita di Balik Kode:**

Pada kode di atas bercerita tentang keluarga Budi. Semua keturunan harus memiliki nama depan "budi".

**Breakdown:**

- **Getter** bekerja saat awal kita membuat instance dan saat property diakses. Mereka melakukan pengecekan pada argument yang dimasukkan.

- **Setter** bekerja saat instance sudah terbuat dan ada perubahan property. Mereka hanya aktif kalau melakukan perubahan pada property yang ada.

- Pola pengerjaan setelah instance dibuat dan dilakukan perubahan: argument pertama akan diolah di setter, kemudian dikirim ke getter untuk menyimpan data, dan menampilkan data kalau dipanggil.

- Getter bekerja seperti function tapi dipanggil seperti property. Oleh karena itu tidak ada `()` pada akhir pemanggilan.

- Di dalam getter tidak boleh ada parameter.

## Destructuring Array Parameter

Tujuannya adalah menggunakan nilai dari array atau object sebagai parameter function.

**Destructuring Object:**

```javascript
function math({a, b}) {
    console.log({a})
    return a + b 
}

console.log(math({a: 1, b: 2}))  // 3
```

Breakdown:
- Parameter dibuat dengan `{}`
- Menambahkan value dengan `math({a: 1, b: 2})`

**Destructuring Array:**

```javascript
// Array dengan setiap item memiliki relasi
let buahDetail = ['Apel', 'Manis']

// Function dibuat untuk mengambil buahDetail
// Dengan konsep parameter destructuring
function dapDetail([nama, rasa]) {
    console.log(`Nama buah: ${nama}, rasanya ${rasa}`)
}

dapDetail(buahDetail)
// Output: Nama buah: Apel, rasanya Manis
```

**Destructuring Object dengan Alias:**

```javascript
let buah = {
    name: 'Apel',
    id: 1211,
    size: 'kecil'
}

// Parameter pakai alias, merujuk pada property object
function getDetails({name: nama, size: ukuran}) {
    console.log(`Nama buah ${nama} ukuran ${ukuran}`)
}

getDetails(buah)
// Output: Nama buah Apel ukuran kecil
```

**Destructuring Nested Object:**

```javascript
let buah = {
    name: 'Apel',
    id: 1211,
    size: 'kecil',
    address: {
        city: 'Malang',
        code: 123
    }
}

// Memasukkan object ke dalam destructured
// untuk mengakses address.city
function getDetails({ name, size, address: {city} }) {
    let abc = `Nama buah ${name}, ukuran ${size}, dari kota: ${city}`
    console.log(abc)
}

getDetails(buah)
// Output: Nama buah Apel, ukuran kecil, dari kota: Malang
```

## Rest Parameter 

Rest parameter dengan tiga titik `...args` atau `...parameters`.

```javascript
function fun(...arg) {
    arg.map((i) => console.log(i))
}

fun(1, 2, 3, 4, 5, 6, 7)
// Output: 1 2 3 4 5 6 7 (satu per satu)
```

**Kegunaan:**
- Menerima jumlah parameter yang tidak terbatas
- Parameter dijadikan array
- Harus selalu di posisi terakhir parameter

## preventDefault()

preventDefault() digunakan untuk mencegah behavior default dari sebuah event.

Referensi: https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_event_preventdefault

Kalau pakai di form, tool ini bisa memastikan tag `form` tidak melakukan refresh halaman saat submit.

**Contoh:**

```javascript
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault()  // Cegah refresh halaman
    
    // Proses data form di sini
    console.log("Form disubmit tanpa refresh")
})
```

Referensi: https://www.geeksforgeeks.org/parameter-destructuring/

## Melakukan Perubahan pada Property Object di Dalam Array

Cara melakukan perubahan pada property object yang ada di dalam array.

```javascript
let employees_data = [
    {
        employee_id: 1,
        employee_group: 'Alpha',
        employee_name: "Aman",
    },
    {
        employee_id: 2,
        employee_group: 'Alpha',
        employee_name: "Bhargava",
    },
    {
        employee_id: 3,
        employee_group: 'Delta',
        employee_name: "Chaitanya",
    },
];

let new_updated_data = employees_data.map((employee) => {
    if (employee.employee_id === 2) {
        return {
            ...employee,
            employee_name: "Anthony",  // Ubah nama
        };
    }
    return employee;  // Kembalikan tanpa perubahan
});

console.log("Updated Data: ");
console.log(new_updated_data);
```

**Penjelasan:**
- Pakai `map()` untuk loop array
- Cek kondisi dengan `if`
- Pakai spread operator `...employee` untuk copy semua property
- Override property yang mau diubah

Referensi: https://www.geeksforgeeks.org/how-to-modify-an-objects-property-in-an-array-of-objects-in-javascript/

## Switch Case 

Switch case adalah alternatif dari if else untuk cek nilai yang spesifik.

```javascript
let abc = 3

function Print(item) {
    console.log(item)
}

// Pakai If Statement
if (abc === 3) {
    Print(3)
}
else if (abc === 4) {
    Print(abc)
}
else {
    Print(abc)
}

// Pakai Switch Case
switch(abc) {
    case 1:
        Print('hi ' + abc)
        break
    case 2:
        Print('hi ' + abc)
        break
    case 3:
        Print('hi ' + abc)
        break
    default:
        Print('de' + abc)
}
```

**Perbedaan:**

- `if` statement mencari nilai true atau false (kondisi)
- `switch` mencari nilai yang sama persis (equality)

**Kapan Pakai Switch:**
- Kalau ada banyak kemungkinan nilai yang spesifik
- Lebih clean daripada banyak if else

**Catatan:** Jangan lupa `break`, kalau tidak case berikutnya juga akan dijalankan!

Referensi: https://medium.com/@michellekwong2/switch-vs-if-else-1d458e7b0711

***
## Mencari Nilai Bilangan Prima 
***

Bilangan prima adalah bilangan yang hanya bisa dibagi oleh 1 dan dirinya sendiri.

```javascript
function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;  // Jika bilangan prima, return true
}

let myArray = [1, 2, 3, 4, 5, 6, 7]

let hasilPrima = myArray.filter((item) => {
    return isPrime(item)
})

console.log(hasilPrima);  // Output: [2, 3, 5, 7]
```

**Logika:**

1. Kalau nilai kurang dari atau sama dengan 1, bukan prima
2. Loop dari 2 sampai akar kuadrat dari number
3. Kalau ketemu pembagi, berarti bukan prima
4. Kalau tidak ketemu pembagi, berarti prima

**Kenapa Pakai Math.sqrt():**
Karena kalau ada pembagi lebih besar dari akar kuadrat, pasti ada pasangan pembagi yang lebih kecil. Jadi cukup cek sampai akar kuadratnya aja.

Referensi: https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-number-to-determine-if-the-number-is

## Mencari Bilangan Genap 

Bilangan genap adalah bilangan yang habis dibagi 2.

```javascript
function isEven(num) {
    if ((num % 2) === 0) {
        return true
    }
    else {
        return false
    }
}

let myArray = [1, 2, 3, 4, 5, 6, 7, 8]

let bilanganGenap = myArray.filter((item) => {
    return isEven(item)
})

console.log(myArray)
console.log(bilanganGenap);  // Output: [2, 4, 6, 8]
```

**Versi Singkat:**

```javascript
function isEven(num) {
    return num % 2 === 0
}

// Atau langsung di filter
let bilanganGenap = myArray.filter(num => num % 2 === 0)
```

**Logika:**
- Gunakan operator modulo `%`
- Kalau `num % 2 === 0`, berarti genap
- Kalau `num % 2 !== 0`, berarti ganjil

## Array Sort 

Method `sort()` digunakan untuk mengurutkan array.

**Sort Angka (Ascending):**

```javascript
const points = [40, 100, 1, 5, 25, 10];

let urut = points.sort((a, b) => {
    return a - b
})

console.log(urut)
// Output: [1, 5, 10, 25, 40, 100]
```

**Cara Kerja:**

- Parameter `a` adalah element pertama yang dibandingkan
- Parameter `b` adalah element kedua yang dibandingkan
- Kalau `a - b` hasilnya negatif, `a` ditaruh sebelum `b`
- Kalau `a - b` hasilnya positif, `b` ditaruh sebelum `a`
- Kalau hasilnya 0, posisi tidak berubah

**Sort Descending (Terbalik):**

```javascript
const points = [40, 100, 1, 5, 25, 10];

let urut = points.sort((a, b) => {
    return b - a
})

console.log(urut)
// Output: [100, 40, 25, 10, 5, 1]
```

**Sort String (Alphabetically):**

```javascript
let fruits = ["Banana", "Orange", "Apple", "Mango"]

fruits.sort()
console.log(fruits)
// Output: ["Apple", "Banana", "Mango", "Orange"]
```

**Catatan Penting:**
- `sort()` mengubah array asli (mutasi)
- Untuk angka, harus pakai compare function `(a, b) => a - b`
- Tanpa compare function, angka diurutkan sebagai string

Referensi: https://www.w3schools.com/js/js_array_sort.asp

***
## Additional Note 
- [JavaScript Class](../document/javascript-class.md)
- [JavaScript Array](../document/javascript-array.md)
- [JavaScript Fundamental](../document/javascript-fundamental.md)
- [JavaScript Synchronous](../document/project-react/async.md)
- [AJAX](../document/ajax.md)

## Latihan JavaScript
- [Latihan JavaScript](../document/latihan-bahasa/latihan-js.md)

***
## Referensi:
- Internet is Hard 
- freeCodeCamp 
- Mozilla MDN
- ChatGPT
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get (getter dan setter)
- https://javascript.info
- https://www.w3schools.com
