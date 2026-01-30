# JavaScript Class

## Daftar Isi
- [Class](#class)
- [Method](#method)
- [Function](#function)
- [Return](#return)
- [Parameter dan Argument](#parameter-dan-argument)
- [Private dan Public Properties](#private-dan-public-properties)
- [Instance (Blueprint)](#instance-blueprint)
- [Object](#object)
- [Constructor](#constructor)
- [This](#this)
- [New](#new)
- [Super](#super)
- [Empat Konsep Utama OOP](#empat-konsep-utama-oop)
- [OOP dan Garbage Collection](#oop-dan-garbage-collection)

## Class

Secara sederhana, class di JavaScript adalah blueprint (cetak biru) untuk membuat object yang memiliki kemiripan pada properties dan behavior. Dengan class, kita bisa membuat properties dan method yang dapat dibagikan dengan instance class lainnya.

**Analogi Sederhana:**

Bayangkan class seperti cetakan kue atau cetakan es krim. Dengan cetakan ini, kita bisa membuat banyak kue dengan rasa yang berbeda beda, tapi bentuknya tetap sama. Cetakan adalah class, kue yang dihasilkan adalah instance.

**Keuntungan Class:**

Dengan class, kita bisa mengatur project code yang besar dengan lebih efisien. Code menjadi lebih:
- Terorganisir dengan baik
- Mudah di-maintain
- Reusable (bisa dipakai ulang)
- Lebih mudah dipahami

**Contoh Class Sederhana:**

```javascript
class Mobil {
    constructor(merk, warna) {
        this.merk = merk
        this.warna = warna
    }
    
    jalan() {
        console.log(`${this.merk} berwarna ${this.warna} sedang jalan`)
    }
}

// Membuat instance dari class Mobil
let mobil1 = new Mobil("Toyota", "Merah")
let mobil2 = new Mobil("Honda", "Biru")

mobil1.jalan()  // Toyota berwarna Merah sedang jalan
mobil2.jalan()  // Honda berwarna Biru sedang jalan
```

## Method

Method di JavaScript adalah function yang berada di dalam object atau class. Method memiliki kemampuan untuk mengakses method lain atau properties yang ada di dalam object tersebut.

**Perbedaan Function vs Method:**

- **Function:** Bisa dipanggil secara langsung dari mana saja
- **Method:** Harus dipanggil melalui object atau instance

**Contoh Method:**

```javascript
const person = {
    name: "John",
    age: 30,
    greet: function() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`)
    }
};

person.greet()  // Memanggil method melalui object person
// Output: Hello, my name is John and I am 30 years old.
```

**Method dalam Class:**

```javascript
class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
    
    // Method di dalam class
    greet() {
        console.log(`Halo, nama saya ${this.name}`)
    }
    
    // Method bisa memanggil method lain
    introduce() {
        this.greet()
        console.log(`Umur saya ${this.age} tahun`)
    }
}

let person = new Person("Budi", 25)
person.introduce()
// Output:
// Halo, nama saya Budi
// Umur saya 25 tahun
```

## Function

Function adalah blok kode yang bisa dipanggil berkali kali. Function yang berada di dalam class atau object disebut sebagai method.

Ada beberapa cara untuk menulis function di JavaScript:

### 1. Function Declaration

Cara paling umum untuk membuat function:

```javascript
function tambah(x, y) {
    return x + y
}

console.log(tambah(5, 3))  // 8
```

**Karakteristik:**
- Mengalami hoisting (bisa dipanggil sebelum dideklarasi)
- Punya nama function sendiri

### 2. Function Expression

Function yang disimpan dalam variabel:

```javascript
const tambah = function(x, y) {
    return x + y
}

console.log(tambah(5, 3))  // 8
```

**Karakteristik:**
- Tidak mengalami hoisting
- Bisa anonymous (tanpa nama)

### 3. Arrow Function

Cara singkat menulis function (ES6):

```javascript
const tambah = (x, y) => x + y

console.log(tambah(5, 3))  // 8
```

**Karakteristik:**
- Sintaks lebih singkat
- Tidak punya `this` sendiri
- Tidak bisa dipakai sebagai constructor

### 4. Constructor Function

Function yang digunakan untuk membuat object:

```javascript
function Person(nama, umur) {
    this.nama = nama
    this.umur = umur
    
    this.perkenalan = function() {
        console.log(`Nama: ${this.nama}, Umur: ${this.umur}`)
    }
}

const budi = new Person("Budi", 25)
budi.perkenalan()  // Nama: Budi, Umur: 25
```

**Karakteristik:**
- Digunakan dengan kata kunci `new`
- Membuat object baru setiap kali dipanggil

## Return

Return adalah perintah untuk mengembalikan nilai dari function. Setelah return dijalankan, kode di bawahnya tidak akan dieksekusi.

**Contoh Dasar:**

```javascript
function addNumbers(a, b) {
    return a + b
}

const result = addNumbers(5, 3)
console.log(result)  // 8
```

**Return Menghentikan Eksekusi:**

```javascript
function cekUmur(umur) {
    if (umur < 17) {
        return "Belum cukup umur"
        console.log("ini tidak akan dijalankan")  // Tidak akan jalan
    }
    return "Sudah cukup umur"
}

console.log(cekUmur(15))  // Belum cukup umur
```

**Function Tanpa Return:**

```javascript
function sapaan(nama) {
    console.log("Halo " + nama)
    // Tidak ada return
}

let hasil = sapaan("Budi")  // Halo Budi
console.log(hasil)           // undefined (karena tidak ada return)
```

**Tips:** Kalau function tidak punya return, hasilnya adalah `undefined`.

## Parameter dan Argument

Ini adalah dua konsep yang berbeda tapi saling berhubungan.

### Parameter

Parameter adalah variabel yang kita tulis di dalam kurung saat membuat function. Ini seperti "placeholder" untuk nilai yang akan diterima nanti.

### Argument

Argument adalah nilai asli yang kita kirim ke function saat memanggilnya.

**Contoh:**

```javascript
function greet(name) {  // 'name' adalah parameter
    console.log(`Hello, ${name}!`)
}

greet("John")  // "John" adalah argument
// Output: Hello, John!
```

**Analogi Sederhana:**
- Parameter = kotak kosong yang siap diisi
- Argument = barang yang kita masukkan ke kotak

**Multiple Parameters:**

```javascript
function buatProfil(nama, umur, kota) {  // 3 parameter
    console.log(`${nama}, ${umur} tahun, tinggal di ${kota}`)
}

buatProfil("Budi", 25, "Jakarta")  // 3 argument
// Output: Budi, 25 tahun, tinggal di Jakarta
```

**Default Parameter:**

```javascript
function salam(nama = "Tamu") {  // Parameter dengan nilai default
    console.log(`Halo ${nama}`)
}

salam()         // Halo Tamu (pakai default)
salam("Andi")   // Halo Andi (pakai argument)
```

## Private dan Public Properties

Secara default, semua properties dari object bersifat public, artinya bisa diakses dan dimodifikasi dari luar object. Tapi kita juga bisa membuat properties yang private (hanya bisa diakses dari dalam).

### Public Properties

Properties yang bisa diakses dari mana saja:

```javascript
class Person {
    constructor(nama, umur) {
        this.nama = nama    // Public property
        this.umur = umur    // Public property
    }
}

let budi = new Person("Budi", 25)
console.log(budi.nama)      // Bisa diakses dari luar
budi.umur = 26              // Bisa diubah dari luar
```

### Private Properties (Cara Lama dengan Closure)

Membuat private properties menggunakan closure dalam constructor function:

```javascript
function Person(age) {
    let myName = 'budi'  // Private property (pakai let di dalam function)

    this.getAge = function() {
        return age  // Public method untuk akses private property
    }

    this.getName = function() {
        return myName  // Public method untuk akses private property
    }
}

let person = new Person(25)
console.log(person.getName())  // budi (akses lewat method)
// console.log(person.myName)  // undefined (tidak bisa akses langsung)
```

**Cara Kerja:**
1. Variabel dideklarasi dengan `let` atau `const` di dalam function
2. Variabel tersebut hanya bisa diakses dari dalam function
3. Gunakan method untuk mengakses atau mengubah nilai private property

### Private Fields (ES2022)

Cara modern dengan tanda `#` di depan property:

```javascript
class BankAccount {
    #saldo = 0  // Private field (pakai #)
    
    constructor(saldoAwal) {
        this.#saldo = saldoAwal
    }
    
    deposit(jumlah) {
        this.#saldo += jumlah
    }
    
    getSaldo() {
        return this.#saldo
    }
}

let akun = new BankAccount(1000)
akun.deposit(500)
console.log(akun.getSaldo())  // 1500
// console.log(akun.#saldo)   // Error! Private field tidak bisa diakses
```

**Keuntungan Private Properties:**
- Melindungi data sensitif
- Kontrol akses yang lebih baik
- Mencegah perubahan yang tidak diinginkan dari luar

## Instance (Blueprint)

Dalam Object Oriented Programming (OOP), ada konsep blueprint dan instance yang penting untuk dipahami.

### Apa itu Blueprint?

Blueprint adalah cetak biru atau desain awal untuk membuat sesuatu. Di JavaScript, **class adalah blueprint**.

**Analogi:**
- Blueprint = Desain rumah di kertas
- Instance = Rumah yang dibangun berdasarkan desain

### Apa itu Instance?

Instance adalah object yang dibuat dari class. Satu class bisa menghasilkan banyak instance dengan karakteristik yang berbeda.

**Contoh:**

```javascript
// Class = Blueprint
class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
    
    greet() {
        console.log(`Halo, nama saya ${this.name}`)
    }
}

// Instance = Hasil dari blueprint
const person1 = new Person('John', 30)  // Instance 1
const person2 = new Person('Jane', 25)  // Instance 2

// Setiap instance punya data sendiri
console.log(person1.name)  // John
console.log(person2.name)  // Jane
```

### Perbedaan Class dan Instance

| Aspek | Class | Instance |
|-------|-------|----------|
| Definisi | Blueprint/template | Object yang dibuat dari class |
| Jumlah | Satu | Bisa banyak |
| Fungsi | Mendefinisikan struktur | Menyimpan data aktual |
| Keyword | `class` | `new` |

**Analogi Lain:**

Bayangkan di atas meja ada 5 apel (instance). Setiap apel punya ukuran dan warna yang berbeda beda, tapi semuanya tetap apel (dari blueprint yang sama).

```javascript
class Apel {
    constructor(ukuran, warna) {
        this.ukuran = ukuran
        this.warna = warna
    }
}

let apel1 = new Apel("besar", "merah")    // Instance 1
let apel2 = new Apel("kecil", "hijau")    // Instance 2
let apel3 = new Apel("sedang", "kuning")  // Instance 3
// Semua adalah apel, tapi dengan karakteristik berbeda
```

## Object

Object adalah salah satu konsep terpenting di JavaScript. Hampir semua yang kita gunakan di JavaScript adalah object.

### Apa itu Object?

Object adalah koleksi data dan fungsi yang berhubungan, biasanya dalam bentuk pasangan key-value (seperti property dan value di CSS).

**Yang Bukan Object (Primitive Types):**
Ada 6 tipe data primitif di JavaScript:
1. null
2. undefined
3. strings
4. numbers
5. boolean
6. symbols

Selain itu, semuanya adalah object!

### Struktur Object

```javascript
let person = {
    // Property (data)
    nama: "Budi",
    umur: 25,
    
    // Method (fungsi)
    salam: function() {
        console.log("Halo!")
    }
}
```

**Kelebihan Object:**
- **Encapsulation:** Data dan fungsi digabung jadi satu
- **Inheritance:** Bisa mewarisi properties dari object lain
- **Representation:** Bisa merepresentasikan hal yang kompleks dengan terstruktur

### 5 Cara Membuat Object

#### 1. Object Literal Syntax

Cara paling sederhana dan umum:

```javascript
const person = {
    name: "John",
    age: 30,
    address: {
        street: "123 Main St",
        city: "New York",
        state: "NY"
    },
    sayHello: function() {
        console.log(`Hello, my name is ${this.name}!`)
    }
}

// Mengakses properties
console.log(person.name)              // John
console.log(person.address.city)      // New York
person.sayHello()                     // Hello, my name is John!
```

**Kapan Pakai:**
- Untuk object yang cuma dibuat sekali
- Struktur sederhana
- Tidak butuh banyak instance

#### 2. Constructor Function Syntax

Untuk membuat banyak object dengan struktur sama:

```javascript
function Person(firstName, lastName, age) {
    this.firstName = firstName
    this.lastName = lastName
    this.age = age
    
    this.greet = function() {
        console.log(`Hello, my name is ${this.firstName} ${this.lastName}`)
    }
}

let john = new Person("John", "Doe", 30)
let jane = new Person("Jane", "Smith", 25)

john.greet()  // Hello, my name is John Doe
jane.greet()  // Hello, my name is Jane Smith
```

**Kapan Pakai:**
- Butuh banyak object dengan struktur sama
- Sebelum ES6 (cara lama)

#### 3. ES6 Class Syntax

Cara modern dan lebih clean:

```javascript
class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }

    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`)
    }
}

const john = new Person('John', 30)
john.greet()  // Hello, my name is John and I am 30 years old.
```

**Kapan Pakai:**
- Project modern (ES6+)
- Butuh inheritance
- Code lebih terorganisir

#### 4. Object.create() Method

Membuat object dengan prototype tertentu:

```javascript
// Buat object template
const person = {
    greeting: 'Hello!',
    sayHello() {
        console.log(this.greeting)
    }
}

// Buat object baru berdasarkan template
const john = Object.create(person)
john.name = 'John'

john.sayHello()  // Hello!
console.log(john.name)  // John
```

**Kapan Pakai:**
- Butuh kontrol lebih atas prototype
- Inheritance tanpa class

#### 5. Factory Function Pattern

Function yang return object baru:

```javascript
function createPerson(name, age) {
    return {
        name: name,
        age: age,
        greet: function() {
            console.log('Hello, my name is ' + this.name)
        }
    }
}

let person1 = createPerson('John', 30)
let person2 = createPerson('Jane', 25)

person1.greet()  // Hello, my name is John
person2.greet()  // Hello, my name is Jane
```

**Kapan Pakai:**
- Tidak mau pakai `new` keyword
- Butuh logic tambahan saat membuat object
- Enkapsulasi yang lebih fleksibel

## Constructor

Constructor adalah method khusus yang otomatis dipanggil saat membuat instance baru dari class. Ini seperti function yang jalan otomatis untuk setup awal object.

### Karakteristik Constructor

1. Namanya selalu `constructor` (di ES6 class)
2. Dipanggil otomatis saat pakai keyword `new`
3. Digunakan untuk inisialisasi properties
4. Hanya ada satu constructor per class

### Constructor di ES6 Class

```javascript
class Person {
    constructor(name, age) {  // Constructor
        this.name = name      // Inisialisasi property
        this.age = age
        console.log("Instance baru dibuat!")
    }

    sayHello() {
        console.log(`Hello, my name is ${this.name}`)
    }
}

const john = new Person('John', 30)
// Output: Instance baru dibuat!
john.sayHello()  // Hello, my name is John
```

### Constructor Function (Cara Lama)

Sebelum ES6, kita pakai function biasa sebagai constructor:

```javascript
function Person(name, age) {
    this.name = name
    this.age = age
    this.sayHello = function() {
        console.log('Hello, my name is ' + this.name)
    }
}

const john = new Person('John', 30)
john.sayHello()  // Hello, my name is John
```

### Fungsi Constructor

**1. Inisialisasi Properties:**

```javascript
class Car {
    constructor(merk, tahun) {
        this.merk = merk
        this.tahun = tahun
        this.km = 0           // Property default
        this.kondisi = "baru"  // Property default
    }
}

let mobil = new Car("Toyota", 2023)
console.log(mobil.km)       // 0
console.log(mobil.kondisi)  // baru
```

**2. Validasi Input:**

```javascript
class Person {
    constructor(name, age) {
        if (age < 0) {
            throw new Error("Umur tidak boleh negatif!")
        }
        this.name = name
        this.age = age
    }
}

// let person = new Person("Budi", -5)  // Error!
let person2 = new Person("Andi", 25)    // OK
```

**3. Setup Awal:**

```javascript
class Game {
    constructor(playerName) {
        this.playerName = playerName
        this.score = 0
        this.level = 1
        this.isPlaying = false
        console.log(`Game dimulai! Selamat datang ${playerName}`)
    }
}

let game = new Game("Budi")
// Output: Game dimulai! Selamat datang Budi
```

### Constructor dengan Default Values

```javascript
class Product {
    constructor(name, price = 0, stock = 0) {
        this.name = name
        this.price = price
        this.stock = stock
    }
}

let product1 = new Product("Laptop")
let product2 = new Product("Mouse", 50000, 10)

console.log(product1.price)  // 0 (default)
console.log(product2.price)  // 50000
```

**Catatan Penting:**
Constructor memastikan setiap instance yang dibuat punya property dan nilai awal yang konsisten sesuai blueprint class.

## This

`this` adalah keyword khusus di JavaScript yang merujuk pada object yang sedang aktif atau context dari kode yang sedang dijalankan.

### This di Class

Di dalam class, `this` merujuk pada instance dari class tersebut:

```javascript
class Person {
    constructor(name) {
        this.name = name  // this = instance yang dibuat
    }

    sayHello() {
        console.log(`Hello, my name is ${this.name}`)
        // this.name mengakses property dari instance
    }
    
    introduce() {
        this.sayHello()  // this.sayHello() memanggil method lain
    }
}

const person = new Person('John')
person.sayHello()     // Hello, my name is John
person.introduce()    // Hello, my name is John
```

### Kenapa Pakai This?

**1. Mengakses Property dari Instance:**

```javascript
class Calculator {
    constructor() {
        this.result = 0  // Property instance
    }
    
    add(num) {
        this.result += num  // Akses property pakai this
        return this
    }
    
    getResult() {
        return this.result
    }
}

let calc = new Calculator()
calc.add(5).add(3)
console.log(calc.getResult())  // 8
```

**2. Memanggil Method Lain:**

```javascript
class User {
    constructor(username) {
        this.username = username
    }
    
    greet() {
        console.log(`Halo ${this.username}`)
    }
    
    welcome() {
        this.greet()  // Memanggil method greet
        console.log("Selamat datang di aplikasi kami!")
    }
}

let user = new User("Budi")
user.welcome()
// Output:
// Halo Budi
// Selamat datang di aplikasi kami!
```

**3. Method Chaining:**

```javascript
class Builder {
    constructor() {
        this.config = {}
    }
    
    setName(name) {
        this.config.name = name
        return this  // Return this untuk chaining
    }
    
    setAge(age) {
        this.config.age = age
        return this
    }
    
    build() {
        return this.config
    }
}

let result = new Builder()
    .setName("Budi")
    .setAge(25)
    .build()

console.log(result)  // { name: "Budi", age: 25 }
```

### This di Object Literal

```javascript
const person = {
    name: "John",
    age: 30,
    greet: function() {
        console.log(`Nama saya ${this.name}`)  // this = object person
    }
}

person.greet()  // Nama saya John
```

### Contoh Sederhana

```javascript
class Mobil {
    constructor(merk, warna) {
        this.merk = merk      // Simpan ke property instance
        this.warna = warna
    }
    
    info() {
        // Akses property dari instance yang sama
        console.log(`Mobil ${this.merk} berwarna ${this.warna}`)
    }
}

let mobil1 = new Mobil("Toyota", "Merah")
let mobil2 = new Mobil("Honda", "Biru")

mobil1.info()  // Mobil Toyota berwarna Merah
mobil2.info()  // Mobil Honda berwarna Biru
// this di mobil1.info() merujuk ke mobil1
// this di mobil2.info() merujuk ke mobil2
```

**Catatan Penting:**
- `this` di class merujuk ke instance yang memanggil method
- Tanpa `this`, kita tidak bisa akses properties atau methods dari instance
- `this` memungkinkan setiap instance punya data sendiri

## New

Keyword `new` digunakan untuk membuat instance baru dari class atau constructor function. Saat pakai `new`, JavaScript akan membuat object baru dan menjalankan constructor.

### Apa yang Terjadi Saat Pakai New?

1. Object kosong baru dibuat
2. Property `this` di constructor merujuk ke object baru
3. Constructor dijalankan untuk setup object
4. Object baru dikembalikan

### Contoh dengan Constructor Function

```javascript
function Person(name, age) {
    this.name = name
    this.age = age
}

const john = new Person('John', 30)
console.log(john.name)  // John
console.log(john.age)   // 30
```

**Tanpa `new` (Salah!):**

```javascript
const jane = Person('Jane', 25)  // Lupa pakai new
console.log(jane)  // undefined
// Properties tidak tersimpan karena tidak ada object baru yang dibuat
```

### Contoh dengan ES6 Class

```javascript
class Car {
    constructor(make, model, year) {
        this.make = make
        this.model = model
        this.year = year
    }

    getDetails() {
        return `${this.make} ${this.model} (${this.year})`
    }
}

const myCar = new Car('Honda', 'Civic', 2021)
console.log(myCar.getDetails())  // Honda Civic (2021)
```

### New dan This Bekerja Sama

Keyword `new` bekerja dengan `this`. Tanpa `this` untuk property, `new` tidak akan berfungsi dengan baik.

```javascript
class BankAccount {
    constructor(accountNumber, balance) {
        this.accountNumber = accountNumber  // Pakai this
        this.balance = balance              // Pakai this
    }
    
    deposit(amount) {
        this.balance += amount
    }
}

let account1 = new BankAccount("001", 1000)
let account2 = new BankAccount("002", 5000)

console.log(account1.balance)  // 1000
console.log(account2.balance)  // 5000
// Setiap instance punya data terpisah
```

### Membuat Banyak Instance

Dengan `new`, kita bisa buat banyak object dengan karakteristik serupa:

```javascript
class Student {
    constructor(name, grade) {
        this.name = name
        this.grade = grade
    }
    
    study() {
        console.log(`${this.name} sedang belajar`)
    }
}

// Membuat banyak student
let student1 = new Student("Budi", "A")
let student2 = new Student("Andi", "B")
let student3 = new Student("Citra", "A")

student1.study()  // Budi sedang belajar
student2.study()  // Andi sedang belajar
student3.study()  // Citra sedang belajar
```

### Analogi

Bayangkan `new` seperti tombol "print" pada printer:
- Class/Constructor = desain dokumen
- `new` = tombol print
- Instance = dokumen yang dicetak

Setiap kali tekan `new`, kita dapat salinan baru yang independen.

## Super

`super` adalah keyword untuk mengakses dan memanggil method dari parent class di dalam child class. Ini penting saat menggunakan inheritance.

### Fungsi Super

**1. Memanggil Constructor Parent:**

```javascript
class Animal {
    constructor(name) {
        this.name = name
    }

    speak() {
        console.log(`${this.name} bersuara`)
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name)  // Panggil constructor Animal
        this.breed = breed  // Tambah property baru
    }

    speak() {
        console.log(`${this.name} menggonggong`)
    }
}

const dog = new Dog('Buddy', 'Golden Retriever')
dog.speak()  // Buddy menggonggong
```

**Tanpa super akan error:**

```javascript
class Cat extends Animal {
    constructor(name, color) {
        // super(name)  // Kalau ini dihapus, akan error!
        this.color = color
    }
}

// Error: Must call super constructor before accessing 'this'
```

### 2. Memanggil Method Parent

`super` juga bisa dipakai untuk memanggil method dari parent class:

```javascript
class Animal {
    constructor(name) {
        this.name = name
    }

    speak() {
        console.log(`${this.name} makes a noise.`)
    }
}

class Dog extends Animal {
    constructor(name) {
        super(name)
    }

    speak() {
        super.speak()  // Panggil method speak dari parent
        console.log(`${this.name} barks.`)
    }
}

const dog = new Dog('Rufus')
dog.speak()
// Output:
// Rufus makes a noise.
// Rufus barks.
```

### Contoh Lebih Kompleks

```javascript
class Vehicle {
    constructor(brand, speed) {
        this.brand = brand
        this.speed = speed
    }
    
    info() {
        console.log(`Brand: ${this.brand}, Max Speed: ${this.speed} km/h`)
    }
    
    move() {
        console.log(`${this.brand} bergerak`)
    }
}

class Car extends Vehicle {
    constructor(brand, speed, doors) {
        super(brand, speed)  // Panggil constructor Vehicle
        this.doors = doors
    }
    
    info() {
        super.info()  // Panggil method info dari Vehicle
        console.log(`Jumlah pintu: ${this.doors}`)
    }
    
    move() {
        super.move()  // Panggil method move dari Vehicle
        console.log(`Mobil berjalan di jalan raya`)
    }
}

let car = new Car("Toyota", 180, 4)
car.info()
// Output:
// Brand: Toyota, Max Speed: 180 km/h
// Jumlah pintu: 4

car.move()
// Output:
// Toyota bergerak
// Mobil berjalan di jalan raya
```

### Contoh Praktis

```javascript
class Animal {
    constructor(name) {
        this.name = name
    }

    speak() {
        console.log(`${this.name} bersuara`)
    }
}

class Dog extends Animal {
    constructor(name, makanan) {
        super(name)  // WAJIB! Kalau dihapus akan error
        this.makanan = makanan
    }

    speak() {
        console.log(`${this.name} menggonggong`)
    }
    
    makan() {
        console.log(`${this.name} makan ${this.makanan}`)
    }
}

const dog = new Dog('Buddy', 'dogfood')
dog.speak()  // Buddy menggonggong
dog.makan()  // Buddy makan dogfood
```

### Aturan Penting Super

1. **Di constructor child class, super() HARUS dipanggil sebelum menggunakan `this`**

```javascript
class Child extends Parent {
    constructor(a, b) {
        this.b = b  // ERROR! Super harus dipanggil dulu
        super(a)
    }
}

// Yang benar:
class Child extends Parent {
    constructor(a, b) {
        super(a)    // Panggil super dulu
        this.b = b  // Baru bisa pakai this
    }
}
```

2. **Super hanya bisa dipakai di child class yang extends parent**

```javascript
class NormalClass {
    constructor() {
        super()  // ERROR! Tidak ada parent class
    }
}
```

**Catatan:**
Super memungkinkan child class untuk memanfaatkan functionality dari parent class sambil menambah atau mengubah behavior sendiri.

## Empat Konsep Utama OOP

Object Oriented Programming (OOP) memiliki 4 pilar utama yang penting untuk dipahami:

### 1. Encapsulation (Enkapsulasi)

Enkapsulasi adalah konsep menyembunyikan detail implementasi dan hanya menampilkan fungsionalitas yang diperlukan.

**Tujuan:**
- Melindungi data dari akses langsung
- Membuat kode lebih aman
- Memberikan informasi ke developer lain bahwa kode tertentu tidak boleh diubah sembarangan

**Contoh dengan Private Fields:**

```javascript
class BankAccount {
    #balance = 0  // Private field (encapsulation)
    
    constructor(initialBalance) {
        this.#balance = initialBalance
    }
    
    // Public method untuk akses private data
    deposit(amount) {
        if (amount > 0) {
            this.#balance += amount
        }
    }
    
    withdraw(amount) {
        if (amount > 0 && amount <= this.#balance) {
            this.#balance -= amount
            return true
        }
        return false
    }
    
    getBalance() {
        return this.#balance
    }
}

let account = new BankAccount(1000)
account.deposit(500)
console.log(account.getBalance())  // 1500
// account.#balance = 0  // Error! Tidak bisa akses langsung
```

**Keuntungan:**
- Data terlindungi dari perubahan yang tidak diinginkan
- Kontrol penuh atas bagaimana data diakses atau diubah
- Lebih mudah maintain dan debug

### 2. Inheritance (Pewarisan)

Inheritance adalah proses membuat class baru yang mewarisi karakteristik dari class parent.

**Tujuan:**
- Code reusability (menghindari duplikasi kode)
- Membuat hierarki class yang terorganisir
- Mempermudah maintenance

**Contoh:**

```javascript
// Parent class
class Vehicle {
    constructor(brand, speed) {
        this.brand = brand
        this.speed = speed
    }
    
    move() {
        console.log(`${this.brand} bergerak dengan kecepatan ${this.speed} km/h`)
    }
}

// Child class mewarisi dari Vehicle
class Car extends Vehicle {
    constructor(brand, speed, doors) {
        super(brand, speed)  // Warisi properties dari parent
        this.doors = doors
    }
    
    honk() {
        console.log("Tin tin!")
    }
}

class Motorcycle extends Vehicle {
    constructor(brand, speed, type) {
        super(brand, speed)
        this.type = type
    }
    
    wheelie() {
        console.log("Motor melakukan wheelie!")
    }
}

let car = new Car("Toyota", 120, 4)
let motor = new Motorcycle("Honda", 100, "sport")

car.move()      // Toyota bergerak dengan kecepatan 120 km/h
car.honk()      // Tin tin!

motor.move()    // Honda bergerak dengan kecepatan 100 km/h
motor.wheelie() // Motor melakukan wheelie!
```

**Keuntungan:**
- Tidak perlu tulis ulang kode yang sama
- Child class otomatis punya semua property dan method dari parent
- Mudah extend functionality

### 3. Polymorphism (Polimorfisme)

Polymorphism adalah kemampuan object yang berbeda untuk merespon method yang sama dengan cara berbeda. Ini adalah bentuk lanjutan dari inheritance, di mana child class mengubah (override) method dari parent.

**Tujuan:**
- Flexibility dalam implementasi
- Satu interface, banyak implementasi
- Code lebih dynamic

**Contoh:**

```javascript
class Animal {
    sound() {
        console.log('Hewan ini bersuara')
    }
    
    move() {
        console.log('Hewan ini bergerak')
    }
}

class Dog extends Animal {
    sound() {  // Override method sound
        console.log('Guk guk!')
    }
    
    move() {
        console.log('Anjing berlari dengan 4 kaki')
    }
}

class Cat extends Animal {
    sound() {  // Override method sound
        console.log('Meow!')
    }
    
    move() {
        console.log('Kucing melompat dengan lincah')
    }
}

class Bird extends Animal {
    sound() {  // Override method sound
        console.log('Cicit cicit!')
    }
    
    move() {
        console.log('Burung terbang di udara')
    }
}

// Polymorphism in action
const animals = [
    new Animal(),
    new Dog(),
    new Cat(),
    new Bird()
]

animals.forEach(animal => {
    animal.sound()
    animal.move()
    console.log('---')
})

// Output:
// Hewan ini bersuara
// Hewan ini bergerak
// ---
// Guk guk!
// Anjing berlari dengan 4 kaki
// ---
// Meow!
// Kucing melompat dengan lincah
// ---
// Cicit cicit!
// Burung terbang di udara
```

**Keuntungan:**
- Satu method bisa punya banyak behavior
- Flexible dan extensible
- Mudah tambah tipe baru tanpa ubah kode existing

### 4. Abstraction (Abstraksi)

Abstraction adalah konsep menyembunyikan detail kompleks dan hanya menampilkan fitur penting. Fokus ke "apa yang dilakukan" bukan "bagaimana caranya".

**Tujuan:**
- Simplifikasi kompleksitas
- Fokus ke interface, bukan implementasi
- Mudah digunakan tanpa perlu tau detail internal

**Contoh:**

```javascript
class Animal {
    constructor(name, sound) {
        if (this.constructor === Animal) {
            throw new Error("Abstract class tidak bisa di-instantiate langsung!")
        }
        this.name = name
        this.sound = sound
    }
    
    // Abstract method (harus di-implement di child class)
    makeSound() {
        throw new Error("Method makeSound() harus di-implement!")
    }
    
    // Concrete method
    eat() {
        console.log(`${this.name} sedang makan`)
    }
}

class Dog extends Animal {
    constructor(name) {
        super(name, "Guk guk")
    }
    
    // Implement abstract method
    makeSound() {
        console.log(`${this.name} bersuara: ${this.sound}`)
    }
}

class Cat extends Animal {
    constructor(name) {
        super(name, "Meow")
    }
    
    // Implement abstract method
    makeSound() {
        console.log(`${this.name} bersuara: ${this.sound}`)
    }
}

// const animal = new Animal("Generic", "Sound")  // Error!
const dog = new Dog("Buddy")
const cat = new Cat("Whiskers")

dog.makeSound()  // Buddy bersuara: Guk guk
dog.eat()        // Buddy sedang makan

cat.makeSound()  // Whiskers bersuara: Meow
cat.eat()        // Whiskers sedang makan
```

**Contoh dengan Parameter:**

```javascript
class Shape {
    constructor(color) {
        this.color = color
    }
    
    // Abstract method
    calculateArea() {
        throw new Error("Method calculateArea() harus di-implement!")
    }
    
    describe() {
        console.log(`Ini adalah bentuk berwarna ${this.color}`)
    }
}

class Circle extends Shape {
    constructor(color, radius) {
        super(color)
        this.radius = radius
    }
    
    calculateArea() {
        return Math.PI * this.radius * this.radius
    }
}

class Rectangle extends Shape {
    constructor(color, width, height) {
        super(color)
        this.width = width
        this.height = height
    }
    
    calculateArea() {
        return this.width * this.height
    }
}

let circle = new Circle("merah", 5)
let rectangle = new Rectangle("biru", 4, 6)

circle.describe()  // Ini adalah bentuk berwarna merah
console.log("Luas lingkaran:", circle.calculateArea())  // 78.54

rectangle.describe()  // Ini adalah bentuk berwarna biru
console.log("Luas persegi panjang:", rectangle.calculateArea())  // 24
```

**Keuntungan:**
- Menyembunyikan kompleksitas
- User cukup tau cara pakai, tidak perlu tau detail implementasi
- Lebih flexible untuk perubahan internal

### Ringkasan 4 Pilar OOP

| Konsep | Tujuan | Analogi |
|--------|--------|---------|
| **Encapsulation** | Sembunyikan data internal | Mobil: kamu cuma perlu tau cara nyetir, tidak perlu tau cara mesin bekerja |
| **Inheritance** | Warisi properties dari parent | Anak mewarisi sifat dari orang tua |
| **Polymorphism** | Satu interface, banyak bentuk | Tombol "play": bisa untuk musik, video, atau game |
| **Abstraction** | Fokus ke fitur penting | Remote TV: cuma ada tombol penting, detail internal tersembunyi |

## OOP dan Garbage Collection

OOP dan garbage collection adalah dua konsep yang berbeda, tapi sama sama penting dalam pemrograman.

### Apa itu Garbage Collection?

Garbage collection adalah proses otomatis untuk membersihkan memory yang tidak terpakai lagi. JavaScript punya garbage collector bawaan yang bekerja di background.

**Fungsi:**
- Membersihkan object yang tidak lagi digunakan
- Membebaskan memory yang tidak terpakai
- Mencegah memory leak

### Bagaimana Garbage Collection Bekerja?

```javascript
function createObjects() {
    let obj1 = { name: "Object 1" }  // Object dibuat
    let obj2 = { name: "Object 2" }
    
    // Function selesai, obj1 dan obj2 tidak bisa diakses lagi
    // Garbage collector akan membersihkan memory mereka
}

createObjects()  // Setelah function selesai, memory dibersihkan
```

### Contoh dengan Class

```javascript
class Player {
    constructor(name) {
        this.name = name
        console.log(`${name} bergabung`)
    }
}

function gameSession() {
    let player1 = new Player("Budi")    // Instance dibuat
    let player2 = new Player("Andi")
    
    // Lakukan sesuatu dengan player
    console.log(`${player1.name} vs ${player2.name}`)
    
    // Function selesai
    // player1 dan player2 tidak ada yang reference lagi
    // Garbage collector akan membersihkan memory mereka
}

gameSession()
// Setelah function selesai, instance Player dibersihkan dari memory
```

### Kapan Object Dibersihkan?

Object akan dibersihkan kalau:
1. Tidak ada reference ke object tersebut
2. Keluar dari scope
3. Reference di-set jadi null

**Contoh:**

```javascript
let user = { name: "Budi" }  // Object dibuat dan ada reference

user = null  // Reference dihapus, object siap dibersihkan

// Garbage collector akan membersihkan object { name: "Budi" }
```

### Memory Leak (Kebocoran Memory)

Memory leak terjadi kalau object tidak pernah dibersihkan walaupun sudah tidak dipakai:

```javascript
// Bad practice: Global array terus bertambah
let globalArray = []

function addData() {
    for (let i = 0; i < 1000; i++) {
        globalArray.push({ data: new Array(1000) })
    }
}

addData()
addData()
addData()
// globalArray terus membesar, memory tidak pernah dibersihkan!
```

### Best Practices

**1. Hindari Global Variables:**

```javascript
// Bad
let globalUser = { name: "Budi" }

// Good
function processUser() {
    let localUser = { name: "Budi" }
    // localUser akan dibersihkan setelah function selesai
}
```

**2. Clear References:**

```javascript
let users = [
    { name: "Budi" },
    { name: "Andi" }
]

// Setelah selesai dipakai
users = null  // atau users = []
```

**3. Remove Event Listeners:**

```javascript
class Component {
    constructor() {
        this.handleClick = this.handleClick.bind(this)
        document.addEventListener('click', this.handleClick)
    }
    
    destroy() {
        // Penting! Remove listener saat component dihapus
        document.removeEventListener('click', this.handleClick)
    }
    
    handleClick() {
        console.log('clicked')
    }
}
```

### Perbedaan OOP dan Garbage Collection

| Aspek | OOP | Garbage Collection |
|-------|-----|-------------------|
| Definisi | Paradigma pemrograman | Sistem manajemen memory |
| Tujuan | Struktur dan organisasi kode | Bersihkan memory yang tidak terpakai |
| Kontrol | Developer | Otomatis (JavaScript engine) |
| Fokus | Bagaimana kode ditulis | Bagaimana memory dikelola |

**Catatan Penting:**
Meskipun JavaScript punya garbage collector otomatis, kita tetap harus menulis kode dengan bijak untuk menghindari memory leak dan memastikan aplikasi berjalan efisien.

***

## Referensi
- ChatGPT
- freeCodeCamp
- https://en.wikipedia.org/wiki/Name-value_pair
- https://javascript.info/class
- https://eloquentjavascript.net/06_object.html
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript
- https://stackoverflow.com/questions/2885385/what-is-the-difference-between-an-instance-and-an-object
- https://towardsdatascience.com/everything-about-javascript-object-part-1-854025d71fea
