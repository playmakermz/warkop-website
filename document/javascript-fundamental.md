# Konsep Fundamental JavaScript

## Daftar Isi
- [Node.js](#nodejs)
- [NPM](#npm)
- [API](#api)
- [Variabel](#variabel)
- [Data Type](#data-type)
- [Operator](#operator)
- [Expression](#expression)
- [Comment](#comment)
- [If Statement](#if-statement)
- [Loop](#loop)
- [Array](#array)
- [Function](#function)
- [Object](#object)
- [Template Literal](#template-literal-string-interpolation)
- [Export dan Import](#export-dan-import)

## Node.js

Node.js adalah runtime environment JavaScript yang bersifat open source dan cross platform, memungkinkan kita menjalankan JavaScript di sisi server (backend). Dibangun pada tahun 2009 oleh Ryan Dahl, Node.js sekarang sangat populer di kalangan developer karena arsitektur dan kemudahan penggunaannya dalam pengembangan aplikasi.

### Kelebihan Node.js

**1. Non-blocking & Asynchronous**

Salah satu kelebihan utama Node.js adalah kemampuannya menangani banyak permintaan secara bersamaan tanpa harus menunggu satu permintaan selesai terlebih dahulu. Ini sangat berguna untuk aplikasi yang bekerja secara real time dengan banyak user, seperti:
- Aplikasi chat atau messaging
- Online game multiplayer
- Live streaming
- Social media feeds

**Analogi:** Bayangkan kamu di resto cepat saji. Node.js seperti kasir yang bisa menerima pesanan dari banyak customer sekaligus dan mengerjakan pesanan sambil menerima pesanan baru, bukan harus menunggu satu pesanan selesai baru terima pesanan berikutnya.

**2. NPM (Node Package Manager)**

Node.js memiliki package manager bernama NPM, yang merupakan salah satu repository open source terbesar di dunia dengan lebih dari satu juta package yang bisa kita gunakan. Ini menghemat waktu development karena kita tidak perlu membuat semuanya dari nol.

**3. Perfect untuk API Development**

Node.js sangat populer untuk membangun API (Application Programming Interface) karena kemampuannya menangani permintaan dan respons dalam format JSON dengan efisien. JSON adalah format standar untuk pertukaran data antar aplikasi, membuat Node.js ideal untuk integrasi dengan berbagai service dan aplikasi lain.

**Contoh Penggunaan Node.js:**

```javascript
// Server sederhana dengan Node.js
const http = require('http')

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' })
    res.end('Hello from Node.js!')
})

server.listen(3000, () => {
    console.log('Server running on port 3000')
})
```

### Kapan Pakai Node.js?

**Bagus untuk:**
- Real-time applications (chat, gaming, collaboration tools)
- RESTful APIs
- Microservices
- Streaming applications
- Single Page Applications (SPA)

**Kurang cocok untuk:**
- CPU intensive tasks (heavy computation)
- Applications yang butuh banyak processing matematika kompleks

## NPM

NPM (Node Package Manager) adalah tool untuk mengelola package dan dependencies dalam project Node.js. Setiap kali kamu install Node.js, NPM sudah terinstall otomatis.

### Apa itu Package?

Package adalah kumpulan kode JavaScript yang dibuat oleh developer lain dan bisa kita pakai langsung dalam project kita. Bayangkan seperti "bahan masakan siap pakai" yang tinggal kita olah.

### Command NPM Penting

**1. Inisialisasi Project:**

```bash
npm init
```

Membuat file `package.json` yang berisi informasi project dan dependencies.

**2. Install Package:**

```bash
npm install express
# atau singkatnya
npm i express
```

Install package dan simpan di `node_modules`.

**3. Install sebagai Dev Dependency:**

```bash
npm install --save-dev nodemon
# atau
npm i -D nodemon
```

Package yang hanya dipakai saat development, tidak di production.

**4. Install Global:**

```bash
npm install -g typescript
```

Install package secara global, bisa dipakai di semua project.

**5. Uninstall Package:**

```bash
npm uninstall express
```

**6. Update Package:**

```bash
npm update
```

### File package.json

File ini adalah "manifest" dari project kita:

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "Project saya",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "dependencies": {
    "express": "^4.18.0"
  },
  "devDependencies": {
    "nodemon": "^2.0.15"
  }
}
```

**Scripts:** Command custom yang bisa kamu jalankan dengan `npm run <script-name>`

**Dependencies:** Package yang dibutuhkan saat production

**DevDependencies:** Package yang hanya dibutuhkan saat development

### Versioning di NPM

NPM menggunakan Semantic Versioning (SemVer):

```
^4.18.2
│ │  │
│ │  └── Patch (bug fixes)
│ └───── Minor (new features, backward compatible)
└────── Major (breaking changes)
```

- `^4.18.2`: Install versi 4.x.x terbaru (update minor & patch)
- `~4.18.2`: Install versi 4.18.x terbaru (update patch saja)
- `4.18.2`: Install versi spesifik ini saja

## API

API (Application Programming Interface) adalah set protokol dan tools yang memungkinkan dua atau lebih software berkomunikasi dan bekerja sama.

### Analogi Sederhana

Bayangkan kamu di restoran:
- **Kamu (Client):** Mau pesan makanan
- **Menu (API Documentation):** Daftar makanan yang bisa dipesan
- **Pelayan (API):** Menerima pesananmu dan kasih ke dapur
- **Dapur (Server):** Masak makanan
- **Pelayan (API):** Bawa makanan ke mejamu

Kamu tidak perlu tau cara masak atau ke dapur langsung. Cukup pesan lewat pelayan (API).

### Jenis-jenis API

**1. Web APIs (REST APIs)**

API yang menggunakan protokol HTTP untuk berkomunikasi. Ini yang paling umum dipakai.

**Contoh:**
- Google Maps API: Untuk tampilkan peta dan lokasi
- Twitter API: Untuk posting tweet atau ambil data tweet
- Weather API: Untuk ambil data cuaca
- Payment Gateway API: Untuk proses pembayaran

**Contoh Request:**

```javascript
// Fetch data dari API
fetch('https://api.example.com/users')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error))
```

**2. Operating System API**

API yang menghubungkan aplikasi dengan operating system untuk mengakses resource komputer.

**Contoh:**
- File System API: Untuk baca/tulis file
- Camera API: Untuk akses kamera
- Geolocation API: Untuk ambil lokasi device

**3. Library/Framework API**

API yang disediakan oleh library atau framework untuk menggunakan fitur-fiturnya.

**Contoh:**

**React API:**
```javascript
import React from 'react'

// Menggunakan React API
function MyComponent() {
    const [count, setCount] = React.useState(0)
    
    return (
        <button onClick={() => setCount(count + 1)}>
            Clicked {count} times
        </button>
    )
}
```

### HTTP Methods dalam Web API

- **GET:** Ambil data
- **POST:** Kirim/buat data baru
- **PUT/PATCH:** Update data
- **DELETE:** Hapus data

### Status Code HTTP

- **200:** OK (sukses)
- **201:** Created (data berhasil dibuat)
- **400:** Bad Request (request salah)
- **401:** Unauthorized (tidak ada akses)
- **404:** Not Found (data tidak ditemukan)
- **500:** Internal Server Error (error di server)

## Variabel

Variabel adalah "wadah" untuk menyimpan data yang bisa dipakai dan diubah dalam program.

### Kenapa JavaScript Dinamis?

JavaScript adalah bahasa pemrograman yang dinamis (dynamically typed), artinya variabel bisa menyimpan berbagai tipe data tanpa perlu deklarasi tipe secara eksplisit. Ini membuat JavaScript fleksibel, tapi kita harus hati-hati agar tidak salah tipe data.

```javascript
let x = 5       // x adalah number
x = "hello"     // sekarang x adalah string (ini valid!)
x = true        // sekarang x adalah boolean (juga valid!)
```

### Cara Deklarasi Variabel

Ada 3 cara deklarasi variabel di JavaScript: `var`, `let`, dan `const`.

**1. var (Cara Lama)**

```javascript
var nama = "Budi"
var umur = 25
```

**Karakteristik var:**
- Function scoped (bisa diakses di seluruh function)
- Bisa di-redeclare
- Bisa diubah nilainya
- Hoisting (dibawa ke atas)

**2. let (Modern, ES6+)**

```javascript
let nama = "Andi"
let umur = 30
```

**Karakteristik let:**
- Block scoped (hanya bisa diakses dalam block `{}`)
- Tidak bisa di-redeclare dalam scope yang sama
- Bisa diubah nilainya

**3. const (Constant, ES6+)**

```javascript
const PI = 3.14159
const nama = "Citra"
```

**Karakteristik const:**
- Block scoped
- Tidak bisa di-redeclare
- Tidak bisa diubah nilainya (untuk primitive)
- Harus langsung diberi nilai saat deklarasi

### Perbedaan Scope: var vs let

**Function Scope (var):**

```javascript
function testVar() {
    if (true) {
        var x = 10
    }
    console.log(x)  // 10 (bisa diakses, meski di luar block if)
}
```

**Block Scope (let):**

```javascript
function testLet() {
    if (true) {
        let y = 20
    }
    console.log(y)  // Error! y tidak bisa diakses di luar block
}
```

**Contoh Masalah dengan var:**

```javascript
for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 1000)
}
// Output: 3 3 3 (bukan 0 1 2!)

// Dengan let (benar):
for (let i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 1000)
}
// Output: 0 1 2
```

### Const dengan Object dan Array

`const` mencegah reassignment, tapi tidak mencegah mutasi isi object/array:

```javascript
// Ini ERROR
const x = 5
x = 10  // Error!

// Ini OK
const arr = [1, 2, 3]
arr.push(4)        // OK! Array jadi [1, 2, 3, 4]
arr[0] = 100       // OK! Array jadi [100, 2, 3, 4]
// arr = [5, 6]    // Error! Tidak bisa reassign

const obj = { name: "Budi" }
obj.name = "Andi"  // OK! Ubah property
obj.age = 25       // OK! Tambah property
// obj = {}        // Error! Tidak bisa reassign
```

### Best Practice

1. **Default pakai `const`** untuk variabel yang tidak akan berubah
2. **Pakai `let`** jika nilai variabel akan berubah
3. **Hindari `var`** di code modern
4. **Penamaan variabel:**
   - Gunakan camelCase: `firstName`, `totalPrice`
   - Nama deskriptif: `userName` lebih baik dari `x`
   - Hindari keyword reserved: `class`, `function`, dll

```javascript
// Good
const MAX_USERS = 100
let currentUser = "Budi"
let isLoggedIn = false

// Bad
const x = 100
let a = "Budi"
let b = false
```

## Data Type

JavaScript mendukung berbagai tipe data yang terbagi menjadi dua kategori: **Primitive** dan **Reference**.

### Primitive Data Types

**1. String**

Tipe data untuk teks, diapit dengan tanda kutip (single, double, atau backtick).

```javascript
let name1 = "Budi"      // Double quotes
let name2 = 'Andi'      // Single quotes
let name3 = `Citra`     // Backticks (template literal)

let greeting = "Hello, " + name1  // Concatenation
let greet2 = `Hello, ${name1}`    // Template literal
```

**2. Number**

Tipe data untuk angka (integer atau float).

```javascript
let age = 25            // Integer
let price = 19.99       // Float
let negative = -10      // Negative number
let infinity = Infinity // Infinity
let notNumber = NaN     // Not a Number

console.log(10 / 0)     // Infinity
console.log("abc" / 2)  // NaN
```

**3. Boolean**

Tipe data untuk nilai true atau false.

```javascript
let isActive = true
let isAdmin = false

let x = 5
let y = 10
console.log(x > y)      // false
console.log(x < y)      // true
```

**4. Null**

Representasi nilai kosong yang sengaja di-set.

```javascript
let user = null  // Sengaja dikosongkan
console.log(user)  // null
```

**5. Undefined**

Variabel yang sudah dideklarasi tapi belum diberi nilai.

```javascript
let score
console.log(score)  // undefined

function test() {
    // Tidak ada return
}
console.log(test())  // undefined
```

**Perbedaan Null vs Undefined:**

```javascript
let a = null       // Sengaja dikosongkan
let b             // Lupa kasih nilai

console.log(typeof a)  // "object" (quirk JavaScript)
console.log(typeof b)  // "undefined"

console.log(a == b)    // true (nilai sama)
console.log(a === b)   // false (tipe berbeda)
```

**6. Symbol (ES6)**

Tipe data untuk membuat identifier yang unik.

```javascript
let id1 = Symbol('id')
let id2 = Symbol('id')

console.log(id1 === id2)  // false (setiap Symbol unik)
```

**7. BigInt (ES2020)**

Untuk angka yang sangat besar (lebih dari 2^53 - 1).

```javascript
let bigNumber = 1234567890123456789012345678901234567890n
let anotherBig = BigInt("9007199254740991")

console.log(bigNumber + anotherBig)
```

### Reference Data Types

**1. Object**

Koleksi key-value pairs.

```javascript
let person = {
    name: "Budi",
    age: 25,
    isStudent: true,
    address: {
        city: "Jakarta",
        country: "Indonesia"
    }
}

console.log(person.name)          // Budi
console.log(person.address.city)  // Jakarta
```

**2. Array**

Koleksi data dalam bentuk list.

```javascript
let fruits = ["apel", "jeruk", "mangga"]
let numbers = [1, 2, 3, 4, 5]
let mixed = [1, "hello", true, { name: "Budi" }]

console.log(fruits[0])      // apel
console.log(numbers.length) // 5
```

**3. Function**

Function juga adalah object di JavaScript.

```javascript
function greet(name) {
    return `Hello, ${name}!`
}

console.log(typeof greet)  // "function"
```

### Mengecek Tipe Data

**Pakai typeof:**

```javascript
console.log(typeof "hello")      // "string"
console.log(typeof 42)           // "number"
console.log(typeof true)         // "boolean"
console.log(typeof undefined)    // "undefined"
console.log(typeof null)         // "object" (ini bug JavaScript!)
console.log(typeof {})           // "object"
console.log(typeof [])           // "object" (array juga object!)
console.log(typeof function(){}) // "function"
```

**Cek Array:**

```javascript
let arr = [1, 2, 3]

console.log(Array.isArray(arr))      // true
console.log(arr instanceof Array)    // true
console.log(typeof arr)              // "object" (kurang spesifik)
```

**Cek Null:**

```javascript
let x = null

if (x === null) {
    console.log("x adalah null")
}
```

### Type Conversion (Konversi Tipe)

**1. String ke Number:**

```javascript
let str = "123"

let num1 = Number(str)        // 123
let num2 = parseInt(str)      // 123
let num3 = parseFloat("12.5") // 12.5
let num4 = +str               // 123 (unary plus)

console.log(Number("abc"))    // NaN
```

**2. Number ke String:**

```javascript
let num = 123

let str1 = String(num)        // "123"
let str2 = num.toString()     // "123"
let str3 = num + ""           // "123"
```

**3. Boolean Conversion:**

```javascript
// Falsy values (jadi false):
Boolean(0)           // false
Boolean("")          // false
Boolean(null)        // false
Boolean(undefined)   // false
Boolean(NaN)         // false

// Semua lainnya truthy (jadi true):
Boolean(1)           // true
Boolean("hello")     // true
Boolean([])          // true
Boolean({})          // true
```

### Contoh Lengkap:

```javascript
// Deklarasi berbagai tipe data
let myString = 'Hello, world!'        // String
let myNumber = 42                     // Number
let myBoolean = true                  // Boolean
let myNull = null                     // Null
let myUndefined                       // Undefined
let myObject = { name: 'John', age: 30 }  // Object
let myArray = [1, 2, 3, 4, 5]        // Array
let mySymbol = Symbol('foo')         // Symbol

// Cek tipe data
console.log(typeof myString)     // "string"
console.log(typeof myNumber)     // "number"
console.log(typeof myBoolean)    // "boolean"
console.log(typeof myNull)       // "object"
console.log(typeof myUndefined)  // "undefined"
console.log(typeof myObject)     // "object"
console.log(typeof myArray)      // "object"
console.log(typeof mySymbol)     // "symbol"

// Cek khusus array
console.log(Array.isArray(myArray))  // true
```

## Operator

Operator adalah simbol yang digunakan untuk melakukan operasi pada data atau variabel.

### 1. Arithmetic Operators (Operator Aritmatika)

Untuk operasi matematika dasar:

```javascript
let a = 10
let b = 3

console.log(a + b)  // 13 (Addition/penjumlahan)
console.log(a - b)  // 7  (Subtraction/pengurangan)
console.log(a * b)  // 30 (Multiplication/perkalian)
console.log(a / b)  // 3.333... (Division/pembagian)
console.log(a % b)  // 1  (Modulus/sisa bagi)
console.log(a ** b) // 1000 (Exponentiation/pangkat, ES2016)

// Increment dan Decrement
let x = 5
console.log(x++)    // 5 (post-increment, pakai dulu baru tambah)
console.log(x)      // 6

let y = 5
console.log(++y)    // 6 (pre-increment, tambah dulu baru pakai)
console.log(y)      // 6
```

**Contoh Modulus (%):**

```javascript
// Cek angka genap atau ganjil
let num = 10
if (num % 2 === 0) {
    console.log("Genap")
} else {
    console.log("Ganjil")
}

// Mendapatkan digit terakhir
let number = 12345
console.log(number % 10)  // 5
```

### 2. Assignment Operators (Operator Penugasan)

```javascript
let x = 10          // Assignment dasar

x += 5              // x = x + 5 → 15
x -= 3              // x = x - 3 → 12
x *= 2              // x = x * 2 → 24
x /= 4              // x = x / 4 → 6
x %= 4              // x = x % 4 → 2
x **= 3             // x = x ** 3 → 8
```

### 3. Comparison Operators (Operator Perbandingan)

Mengembalikan nilai boolean (true/false):

```javascript
let a = 5
let b = 10
let c = "5"

// Equal (==) - Cek nilai saja, tidak cek tipe
console.log(a == c)      // true (5 == "5")

// Strict Equal (===) - Cek nilai DAN tipe
console.log(a === c)     // false (number !== string)

// Not Equal (!=)
console.log(a != b)      // true

// Strict Not Equal (!==)
console.log(a !== c)     // true (tipe berbeda)

// Greater than (>)
console.log(b > a)       // true

// Less than (<)
console.log(a < b)       // true

// Greater than or equal (>=)
console.log(a >= 5)      // true

// Less than or equal (<=)
console.log(a <= 5)      // true
```

**Kapan Pakai == vs ===:**

```javascript
// Gunakan === (strict equality) untuk keamanan
5 === 5         // true
5 === "5"       // false

// == bisa menyebabkan bug
5 == "5"        // true (JavaScript convert tipe otomatis)
0 == false      // true
"" == false     // true
null == undefined  // true

// Best practice: SELALU pakai ===
```

### 4. Logical Operators (Operator Logika)

Untuk menggabungkan atau memodifikasi kondisi boolean:

**AND (&&):** Semua kondisi harus true

```javascript
let age = 25
let hasLicense = true

// Boleh nyetir kalau umur >= 17 DAN punya SIM
if (age >= 17 && hasLicense) {
    console.log("Boleh nyetir")
} else {
    console.log("Tidak boleh nyetir")
}

// Short-circuit: kalau kondisi pertama false, kondisi kedua tidak dicek
console.log(false && console.log("Ini tidak akan tampil"))
```

**OR (||):** Minimal satu kondisi true

```javascript
let isWeekend = true
let isHoliday = false

// Libur kalau weekend ATAU hari libur
if (isWeekend || isHoliday) {
    console.log("Libur!")
} else {
    console.log("Kerja")
}

// Short-circuit: kalau kondisi pertama true, kondisi kedua tidak dicek
console.log(true || console.log("Ini tidak akan tampil"))
```

**NOT (!):** Membalik nilai boolean

```javascript
let isRaining = false

if (!isRaining) {
    console.log("Tidak hujan, bisa jalan-jalan")
}

// Double NOT untuk convert ke boolean
console.log(!!1)        // true
console.log(!!"hello")  // true
console.log(!!0)        // false
console.log(!!"")       // false
```

**Contoh Kombinasi:**

```javascript
let age = 20
let hasID = true
let hasTicket = true

// Boleh masuk kalau (umur >= 18 DAN punya ID) ATAU punya ticket VIP
if ((age >= 18 && hasID) || hasTicket) {
    console.log("Boleh masuk")
}
```

### 5. String Operators

```javascript
// Concatenation dengan +
let firstName = "Budi"
let lastName = "Santoso"
let fullName = firstName + " " + lastName  // "Budi Santoso"

// Concatenation dengan +=
let message = "Hello"
message += " World"  // "Hello World"

// Dengan angka jadi string
let result = "Score: " + 100  // "Score: 100"
```

### 6. Ternary Operator (Conditional)

Shorthand untuk if-else sederhana:

```javascript
// Sintaks: condition ? valueIfTrue : valueIfFalse

let age = 18
let status = age >= 18 ? "Dewasa" : "Anak-anak"
console.log(status)  // "Dewasa"

// Nested ternary (hati-hati, bisa sulit dibaca)
let score = 85
let grade = score >= 90 ? "A" : 
            score >= 80 ? "B" : 
            score >= 70 ? "C" : "D"
console.log(grade)  // "B"
```

### 7. Nullish Coalescing (??) - ES2020

Mengembalikan operand kanan jika operand kiri adalah `null` atau `undefined`:

```javascript
let user1 = null
let user2 = "Budi"

console.log(user1 ?? "Guest")  // "Guest"
console.log(user2 ?? "Guest")  // "Budi"

// Berbeda dengan || yang cek falsy value
let count = 0
console.log(count || 10)   // 10 (0 adalah falsy)
console.log(count ?? 10)   // 0 (0 bukan null/undefined)
```

### 8. Optional Chaining (?.) - ES2020

Mengakses property yang mungkin null/undefined dengan aman:

```javascript
let user = {
    name: "Budi",
    address: {
        city: "Jakarta"
    }
}

// Tanpa optional chaining
console.log(user.address.city)        // "Jakarta"
// console.log(user.contact.phone)    // Error!

// Dengan optional chaining
console.log(user.contact?.phone)      // undefined (tidak error)
console.log(user.address?.city)       // "Jakarta"
```

### Operator Precedence (Urutan Operasi)

```javascript
let result = 5 + 3 * 2      // 11 (bukan 16)
// Perkalian lebih dulu daripada penjumlahan

let result2 = (5 + 3) * 2   // 16
// Pakai kurung untuk ubah precedence
```

**Urutan dari tertinggi:**
1. `()` - Parentheses
2. `**` - Exponentiation
3. `*`, `/`, `%` - Multiplication, Division, Modulus
4. `+`, `-` - Addition, Subtraction
5. `<`, `>`, `<=`, `>=` - Comparison
6. `==`, `===`, `!=`, `!==` - Equality
7. `&&` - Logical AND
8. `||` - Logical OR
9. `=`, `+=`, `-=`, etc. - Assignment

## Expression

Expression adalah kombinasi dari nilai, variabel, dan operator yang menghasilkan nilai baru.

### Jenis Expression

**1. Arithmetic Expression:**

```javascript
let x = 5
let y = 10

let sum = x + y           // 15
let product = (x * y) - x // 45
let complex = (x + y) * 2 / (x - 2)  // 10
```

**2. String Expression:**

```javascript
let firstName = "Budi"
let lastName = "Santoso"
let fullName = firstName + " " + lastName  // "Budi Santoso"
```

**3. Logical Expression:**

```javascript
let age = 20
let hasLicense = true

let canDrive = age >= 17 && hasLicense  // true
```

**4. Assignment Expression:**

```javascript
let x = 10  // Expression yang menghasilkan 10
let y = (x = 5)  // y jadi 5, x juga jadi 5
```

**5. Function Call Expression:**

```javascript
function add(a, b) {
    return a + b
}

let result = add(5, 3)  // 8
```

**6. Object/Array Expression:**

```javascript
let person = { name: "Budi", age: 25 }  // Object expression
let numbers = [1, 2, 3, 4, 5]           // Array expression
```

### Statement vs Expression

**Expression:** Menghasilkan nilai
**Statement:** Melakukan aksi

```javascript
// Expression (menghasilkan nilai)
5 + 3                // 8
"hello" + " world"   // "hello world"
x > 5                // true atau false

// Statement (melakukan aksi)
let x = 5            // Deklarasi variabel
if (x > 5) { }       // Control flow
for (let i = 0; i < 5; i++) { }  // Loop
```

**Expression bisa jadi statement, tapi statement tidak bisa jadi expression:**

```javascript
// Expression sebagai statement
5 + 3  // Valid, tapi hasilnya tidak dipakai

// Statement tidak bisa jadi expression
let x = (if (true) { 5 })  // Error! if statement tidak return value
```

## Comment

Comment adalah catatan dalam kode yang tidak dijalankan oleh program. Berguna untuk menjelaskan kode atau temporary disable code.

### Single Line Comment

Pakai `//` untuk comment satu baris:

```javascript
// Ini adalah comment, tidak akan dijalankan
let name = "Budi"  // Comment bisa juga di akhir baris

// let age = 25  // Code ini di-comment (tidak jalan)
```

### Multi Line Comment

Pakai `/* */` untuk comment beberapa baris:

```javascript
/*
Ini adalah comment
yang lebih dari satu baris.
Bisa banyak baris.
*/

let x = 10

/*
function oldFunction() {
    // Code lama yang tidak dipakai lagi
    console.log("old")
}
*/
```

### JSDoc Comment

Format khusus untuk dokumentasi function:

```javascript
/**
 * Menghitung luas persegi panjang
 * @param {number} panjang - Panjang persegi panjang
 * @param {number} lebar - Lebar persegi panjang
 * @returns {number} Luas persegi panjang
 */
function hitungLuas(panjang, lebar) {
    return panjang * lebar
}
```

### Best Practices untuk Comment

**1. Comment Menjelaskan "Kenapa", Bukan "Apa":**

```javascript
// Bad - Terlalu obvious
let price = 100  // Set price ke 100

// Good - Menjelaskan alasan
let price = 100  // Harga promo untuk member baru
```

**2. Hindari Comment Berlebihan:**

```javascript
// Bad - Code sudah jelas
let total = price + tax  // Tambahkan price dan tax

// Good - Comment hanya kalau perlu
let total = price + tax  // Total sudah include PPn 11%
```

**3. Update Comment Saat Update Code:**

```javascript
// Bad - Comment tidak match dengan code
let discount = 0.2  // Diskon 10%

// Good
let discount = 0.2  // Diskon 20%
```

**4. TODO Comment:**

```javascript
// TODO: Tambah validasi email
function registerUser(email) {
    // ...
}

// FIXME: Bug saat user input angka negatif
function calculate(number) {
    // ...
}
```

**5. Gunakan Comment untuk Disable Code Temporary:**

```javascript
function test() {
    console.log("Production code")
    
    // console.log("Debug info")  // Disable saat production
    // console.log(userData)
}
```

## If Statement

If statement adalah struktur kontrol untuk membuat keputusan dalam program berdasarkan kondisi tertentu.

### Format Dasar

```javascript
if (condition) {
    // Code yang dijalankan kalau condition true
}
```

**Cara Kerja:**
1. JavaScript cek apakah `condition` bernilai true
2. Kalau true, jalankan code dalam block `{}`
3. Kalau false, skip block tersebut

**Contoh:**

```javascript
let age = 18

if (age >= 18) {
    console.log("Kamu sudah dewasa")
}
// Output: Kamu sudah dewasa
```

### If...Else

Untuk handle kondisi false:

```javascript
if (condition) {
    // Code kalau true
} else {
    // Code kalau false
}
```

**Contoh:**

```javascript
let temperature = 25

if (temperature > 30) {
    console.log("Cuaca panas")
} else {
    console.log("Cuaca sejuk")
}
// Output: Cuaca sejuk
```

### If...Else If...Else

Untuk multiple conditions:

```javascript
if (condition1) {
    // Code kalau condition1 true
} else if (condition2) {
    // Code kalau condition2 true
} else if (condition3) {
    // Code kalau condition3 true
} else {
    // Code kalau semua condition false
}
```

**Contoh:**

```javascript
let score = 85

if (score >= 90) {
    console.log("Grade A")
} else if (score >= 80) {
    console.log("Grade B")
} else if (score >= 70) {
    console.log("Grade C")
} else if (score >= 60) {
    console.log("Grade D")
} else {
    console.log("Grade E")
}
// Output: Grade B
```

### Nested If (If Bersarang)

If statement di dalam if statement:

```javascript
let age = 20
let hasLicense = true

if (age >= 17) {
    if (hasLicense) {
        console.log("Boleh nyetir")
    } else {
        console.log("Umur cukup tapi tidak punya SIM")
    }
} else {
    console.log("Umur belum cukup")
}
```

### Logical Operators dalam If

**AND (&&):** Semua kondisi harus true

```javascript
let age = 25
let hasID = true

if (age >= 18 && hasID) {
    console.log("Boleh masuk klub")
}
```

**OR (||):** Minimal satu kondisi true

```javascript
let day = "Sabtu"
let isHoliday = false

if (day === "Sabtu" || day === "Minggu" || isHoliday) {
    console.log("Hari libur!")
}
```

**NOT (!):** Membalik kondisi

```javascript
let isRaining = false

if (!isRaining) {
    console.log("Tidak hujan, bisa jalan-jalan")
}
```

**Kombinasi:**

```javascript
let age = 25
let hasTicket = true
let hasID = true

// Boleh masuk kalau (umur >= 18 DAN punya ID) ATAU punya ticket
if ((age >= 18 && hasID) || hasTicket) {
    console.log("Boleh masuk")
}
```

### Truthy dan Falsy Values

JavaScript punya nilai yang dianggap true atau false dalam kondisi:

**Falsy values (dianggap false):**
- `false`
- `0`
- `""` (empty string)
- `null`
- `undefined`
- `NaN`

**Semua nilai lain adalah truthy (dianggap true):**
- `true`
- Angka selain 0: `1`, `-1`, `3.14`
- String tidak kosong: `"hello"`, `"0"`, `" "`
- Array: `[]`, `[1, 2]`
- Object: `{}`, `{ name: "Budi" }`

**Contoh:**

```javascript
let name = ""

if (name) {
    console.log("Ada nama")
} else {
    console.log("Nama kosong")
}
// Output: Nama kosong

let items = []

if (items.length) {
    console.log("Ada items")
} else {
    console.log("Array kosong")
}
// Output: Array kosong
```

### Switch Statement (Alternatif If...Else)

Untuk banyak kondisi dengan nilai spesifik:

```javascript
let day = "Senin"

switch (day) {
    case "Senin":
        console.log("Awal minggu")
        break
    case "Jumat":
        console.log("Menjelang weekend")
        break
    case "Sabtu":
    case "Minggu":
        console.log("Weekend!")
        break
    default:
        console.log("Hari biasa")
}
```

### Ternary Operator (Shorthand)

Untuk if-else sederhana:

```javascript
let age = 20
let status = age >= 18 ? "Dewasa" : "Anak-anak"

// Sama dengan:
let status2
if (age >= 18) {
    status2 = "Dewasa"
} else {
    status2 = "Anak-anak"
}
```

### Contoh Real World

**1. Validasi Form:**

```javascript
function validateForm(username, password) {
    if (!username) {
        console.log("Username tidak boleh kosong")
        return false
    }
    
    if (username.length < 3) {
        console.log("Username minimal 3 karakter")
        return false
    }
    
    if (!password) {
        console.log("Password tidak boleh kosong")
        return false
    }
    
    if (password.length < 6) {
        console.log("Password minimal 6 karakter")
        return false
    }
    
    return true
}
```

**2. Grade Calculator:**

```javascript
function getGrade(score) {
    if (score < 0 || score > 100) {
        return "Nilai tidak valid"
    } else if (score >= 90) {
        return "A"
    } else if (score >= 80) {
        return "B"
    } else if (score >= 70) {
        return "C"
    } else if (score >= 60) {
        return "D"
    } else {
        return "E"
    }
}

console.log(getGrade(85))  // B
```

**3. Access Control:**

```javascript
function checkAccess(user) {
    if (!user) {
        return "User tidak login"
    }
    
    if (user.role === "admin") {
        return "Full access"
    } else if (user.role === "editor") {
        return "Edit access"
    } else if (user.role === "viewer") {
        return "Read only"
    } else {
        return "No access"
    }
}
```

## Loop

Loop adalah struktur kontrol untuk mengulang eksekusi kode beberapa kali. Sangat berguna untuk mengolah array, melakukan iterasi, atau menjalankan kode sampai kondisi tertentu terpenuhi.

### 1. For Loop

Loop yang paling umum digunakan, cocok kalau kamu tau berapa kali mau loop.

**Sintaks:**

```javascript
for (initialization; condition; increment) {
    // Code yang diulang
}
```

**Bagian-bagian:**
- **Initialization:** Nilai awal (dijalankan sekali di awal)
- **Condition:** Syarat untuk terus loop (dicek setiap iterasi)
- **Increment:** Update counter setiap iterasi

**Contoh Dasar:**

```javascript
for (let i = 1; i <= 5; i++) {
    console.log(i)
}
// Output: 1 2 3 4 5
```

**Cara Kerja:**
1. `let i = 1` → Set i = 1
2. Cek `i <= 5` → true, jalankan code
3. `i++` → i jadi 2
4. Cek `i <= 5` → true, jalankan code
5. Ulangi sampai kondisi false

**Loop Array:**

```javascript
let fruits = ["apel", "jeruk", "mangga"]

for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i])
}
// Output: apel jeruk mangga
```

**Loop Mundur:**

```javascript
for (let i = 5; i >= 1; i--) {
    console.log(i)
}
// Output: 5 4 3 2 1
```

**Loop dengan Step Tertentu:**

```javascript
// Loop genap
for (let i = 0; i <= 10; i += 2) {
    console.log(i)
}
// Output: 0 2 4 6 8 10
```

### 2. While Loop

Loop yang terus berjalan selama kondisi masih true. Cocok kalau tidak tau pasti berapa kali mau loop.

**Sintaks:**

```javascript
while (condition) {
    // Code yang diulang
}
```

**Contoh:**

```javascript
let i = 1

while (i <= 5) {
    console.log(i)
    i++
}
// Output: 1 2 3 4 5
```

**Contoh Real World:**

```javascript
// Loop sampai user input benar
let password = ""

while (password !== "rahasia") {
    password = prompt("Masukkan password:")
}
console.log("Login berhasil!")
```

**Infinite Loop (Hati-hati!):**

```javascript
// INI BAHAYA - Loop tidak akan berhenti!
let x = 1
while (x > 0) {
    console.log(x)
    x++  // x terus bertambah, selalu > 0
}

// Pastikan ada kondisi untuk berhenti
let y = 1
while (y <= 5) {  // Ada batas
    console.log(y)
    y++
}
```

### 3. Do...While Loop

Mirip while, tapi code dijalankan minimal sekali (cek kondisi di akhir).

**Sintaks:**

```javascript
do {
    // Code yang diulang (minimal jalan 1x)
} while (condition)
```

**Contoh:**

```javascript
let i = 1

do {
    console.log(i)
    i++
} while (i <= 5)
// Output: 1 2 3 4 5
```

**Perbedaan While vs Do-While:**

```javascript
// While: Tidak jalan kalau kondisi false dari awal
let x = 10
while (x < 5) {
    console.log(x)  // Tidak jalan sama sekali
}

// Do-While: Jalan minimal 1x walaupun kondisi false
let y = 10
do {
    console.log(y)  // Jalan 1x → Output: 10
} while (y < 5)
```

### 4. For...Of Loop (ES6)

Loop untuk iterasi array dan iterable objects. Lebih simple dari for biasa.

**Sintaks:**

```javascript
for (let element of array) {
    // Code
}
```

**Contoh:**

```javascript
let fruits = ["apel", "jeruk", "mangga"]

for (let fruit of fruits) {
    console.log(fruit)
}
// Output: apel jeruk mangga
```

**Dengan String:**

```javascript
let name = "Budi"

for (let char of name) {
    console.log(char)
}
// Output: B u d i
```

### 5. For...In Loop

Loop untuk iterasi properties object atau index array.

**Untuk Object:**

```javascript
let person = {
    name: "Budi",
    age: 25,
    city: "Jakarta"
}

for (let key in person) {
    console.log(key + ": " + person[key])
}
// Output:
// name: Budi
// age: 25
// city: Jakarta
```

**Untuk Array (Dapat Index):**

```javascript
let fruits = ["apel", "jeruk", "mangga"]

for (let index in fruits) {
    console.log(index + ": " + fruits[index])
}
// Output:
// 0: apel
// 1: jeruk
// 2: mangga
```

### Break dan Continue

**Break:** Keluar dari loop sepenuhnya

```javascript
for (let i = 1; i <= 10; i++) {
    if (i === 5) {
        break  // Stop loop saat i = 5
    }
    console.log(i)
}
// Output: 1 2 3 4
```

**Continue:** Skip iterasi current, lanjut ke iterasi berikutnya

```javascript
for (let i = 1; i <= 5; i++) {
    if (i === 3) {
        continue  // Skip saat i = 3
    }
    console.log(i)
}
// Output: 1 2 4 5
```

### Nested Loop (Loop Bersarang)

Loop di dalam loop:

```javascript
// Tabel perkalian
for (let i = 1; i <= 3; i++) {
    for (let j = 1; j <= 3; j++) {
        console.log(`${i} x ${j} = ${i * j}`)
    }
}
// Output:
// 1 x 1 = 1
// 1 x 2 = 2
// 1 x 3 = 3
// 2 x 1 = 2
// ...
```

**Pattern:**

```javascript
// Buat pattern segitiga
for (let i = 1; i <= 5; i++) {
    let row = ""
    for (let j = 1; j <= i; j++) {
        row += "*"
    }
    console.log(row)
}
// Output:
// *
// **
// ***
// ****
// *****
```

### Kapan Pakai Loop Mana?

| Loop Type | Kapan Pakai |
|-----------|-------------|
| **for** | Tau berapa kali mau loop, iterasi array dengan index |
| **while** | Tidak tau berapa kali, loop sampai kondisi terpenuhi |
| **do-while** | Sama dengan while, tapi code harus jalan minimal 1x |
| **for...of** | Iterasi array/string, butuh nilai element |
| **for...in** | Iterasi properties object atau index array |

### Contoh Real World

**1. Sum Array:**

```javascript
let numbers = [1, 2, 3, 4, 5]
let sum = 0

for (let num of numbers) {
    sum += num
}
console.log(sum)  // 15
```

**2. Find Max Value:**

```javascript
let numbers = [5, 12, 8, 130, 44]
let max = numbers[0]

for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
        max = numbers[i]
    }
}
console.log(max)  // 130
```

**3. Filter Array:**

```javascript
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let evenNumbers = []

for (let num of numbers) {
    if (num % 2 === 0) {
        evenNumbers.push(num)
    }
}
console.log(evenNumbers)  // [2, 4, 6, 8, 10]
```

**4. Count Occurrences:**

```javascript
let fruits = ["apel", "jeruk", "apel", "mangga", "apel"]
let count = 0

for (let fruit of fruits) {
    if (fruit === "apel") {
        count++
    }
}
console.log(`Apel ada ${count} buah`)  // Apel ada 3 buah
```

## Array

Array adalah struktur data untuk menyimpan banyak nilai dalam satu variabel. Nilai disimpan dalam urutan tertentu dan bisa diakses dengan index (dimulai dari 0).

### Membuat Array

```javascript
// Array literal (cara umum)
let fruits = ["apel", "jeruk", "mangga"]
let numbers = [1, 2, 3, 4, 5]
let mixed = [1, "hello", true, { name: "Budi" }]

// Array constructor
let arr1 = new Array(3)        // Array dengan 3 slot kosong
let arr2 = new Array(1, 2, 3)  // [1, 2, 3]

// Array kosong
let empty = []
```

### Mengakses Element

```javascript
let fruits = ["apel", "jeruk", "mangga", "pisang"]

console.log(fruits[0])   // apel (index pertama)
console.log(fruits[2])   // mangga
console.log(fruits[3])   // pisang

// Akses element terakhir
console.log(fruits[fruits.length - 1])  // pisang
console.log(fruits.at(-1))  // pisang (ES2022)
```

### Mengubah Element

```javascript
let fruits = ["apel", "jeruk", "mangga"]

fruits[1] = "anggur"  // Ubah "jeruk" jadi "anggur"
console.log(fruits)   // ["apel", "anggur", "mangga"]
```

### Array Methods

**1. Push (Tambah di Akhir):**

```javascript
let fruits = ["apel", "jeruk"]
fruits.push("mangga")
console.log(fruits)  // ["apel", "jeruk", "mangga"]
```

**2. Pop (Hapus dari Akhir):**

```javascript
let fruits = ["apel", "jeruk", "mangga"]
let removed = fruits.pop()
console.log(fruits)   // ["apel", "jeruk"]
console.log(removed)  // "mangga"
```

**3. Unshift (Tambah di Awal):**

```javascript
let fruits = ["jeruk", "mangga"]
fruits.unshift("apel")
console.log(fruits)  // ["apel", "jeruk", "mangga"]
```

**4. Shift (Hapus dari Awal):**

```javascript
let fruits = ["apel", "jeruk", "mangga"]
let removed = fruits.shift()
console.log(fruits)   // ["jeruk", "mangga"]
console.log(removed)  // "apel"
```

### Loop Array

```javascript
let fruits = ["apel", "jeruk", "mangga"]

// For loop
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i])
}

// For...of
for (let fruit of fruits) {
    console.log(fruit)
}

// ForEach
fruits.forEach(fruit => {
    console.log(fruit)
})
```

### Array Methods Lanjutan

Lihat file [javascript-array.md](javascript-array.md) untuk penjelasan lengkap tentang:
- map()
- filter()
- find()
- reduce()
- dan method array lainnya

## Function

Function adalah blok kode yang bisa dipanggil berkali-kali. Membantu membuat kode lebih terorganisir dan reusable.

### Function Declaration

```javascript
function greet(name) {
    console.log("Hello, " + name)
}

greet("Budi")  // Hello, Budi
```

### Function Expression

```javascript
const greet = function(name) {
    console.log("Hello, " + name)
}

greet("Andi")  // Hello, Andi
```

### Arrow Function (ES6)

```javascript
// Bentuk lengkap
const greet = (name) => {
    console.log("Hello, " + name)
}

// Bentuk singkat (single parameter, single statement)
const greet2 = name => console.log("Hello, " + name)

// Multiple parameters
const add = (a, b) => a + b

greet("Citra")      // Hello, Citra
console.log(add(5, 3))  // 8
```

### Parameters dan Return

```javascript
// Dengan parameter
function tambah(a, b) {
    return a + b
}

let hasil = tambah(5, 3)
console.log(hasil)  // 8

// Default parameter
function salam(nama = "Tamu") {
    console.log("Halo, " + nama)
}

salam()         // Halo, Tamu
salam("Budi")   // Halo, Budi
```

### Function Scope

```javascript
let globalVar = "global"

function test() {
    let localVar = "local"
    console.log(globalVar)  // Bisa akses global
    console.log(localVar)   // Bisa akses local
}

test()
// console.log(localVar)  // Error! Tidak bisa akses local dari luar
```

### Contoh Praktis

```javascript
// Validasi email
function isValidEmail(email) {
    return email.includes("@") && email.includes(".")
}

console.log(isValidEmail("budi@email.com"))  // true
console.log(isValidEmail("budigmail.com"))   // false

// Calculate discount
function calculatePrice(price, discount = 0) {
    return price - (price * discount / 100)
}

console.log(calculatePrice(100000, 10))  // 90000
console.log(calculatePrice(100000))      // 100000
```

## Object

Object adalah struktur data yang menyimpan data dalam bentuk key-value pairs.

### Membuat Object

```javascript
// Object literal
let person = {
    name: "Budi",
    age: 25,
    city: "Jakarta",
    isStudent: true
}

// Nested object
let user = {
    name: "Andi",
    address: {
        street: "Jl. Merdeka",
        city: "Bandung",
        zipCode: 40111
    }
}
```

### Mengakses Property

```javascript
let person = {
    name: "Budi",
    age: 25
}

// Dot notation
console.log(person.name)  // Budi

// Bracket notation
console.log(person["age"])  // 25

// Nested
let user = {
    address: { city: "Jakarta" }
}
console.log(user.address.city)  // Jakarta
```

### Mengubah dan Menambah Property

```javascript
let person = {
    name: "Budi",
    age: 25
}

// Ubah property
person.age = 26
person["name"] = "Budi Santoso"

// Tambah property baru
person.city = "Jakarta"
person.isActive = true

console.log(person)
// { name: "Budi Santoso", age: 26, city: "Jakarta", isActive: true }
```

### Method dalam Object

```javascript
let calculator = {
    add: function(a, b) {
        return a + b
    },
    subtract: function(a, b) {
        return a - b
    }
}

console.log(calculator.add(5, 3))       // 8
console.log(calculator.subtract(10, 4)) // 6

// ES6 shorthand
let calc2 = {
    add(a, b) {
        return a + b
    }
}
```

### This Keyword

```javascript
let person = {
    name: "Budi",
    age: 25,
    greet: function() {
        console.log("Halo, nama saya " + this.name)
    }
}

person.greet()  // Halo, nama saya Budi
```

### Loop Object

```javascript
let person = {
    name: "Budi",
    age: 25,
    city: "Jakarta"
}

// For...in
for (let key in person) {
    console.log(key + ": " + person[key])
}
// Output:
// name: Budi
// age: 25
// city: Jakarta

// Object.keys()
let keys = Object.keys(person)
console.log(keys)  // ["name", "age", "city"]

// Object.values()
let values = Object.values(person)
console.log(values)  // ["Budi", 25, "Jakarta"]

// Object.entries()
let entries = Object.entries(person)
console.log(entries)
// [["name", "Budi"], ["age", 25], ["city", "Jakarta"]]
```

## Template Literal (String Interpolation)

Template literal adalah cara modern untuk membuat string yang bisa include variabel dan expression dengan mudah. Menggunakan backtick (\`) bukan tanda kutip biasa.

### Sintaks Dasar

```javascript
let name = "Budi"
let age = 25

// Cara lama (concatenation)
let message1 = "Nama saya " + name + " dan umur saya " + age + " tahun"

// Cara baru (template literal)
let message2 = `Nama saya ${name} dan umur saya ${age} tahun`

console.log(message2)  // Nama saya Budi dan umur saya 25 tahun
```

### Expression dalam Template Literal

```javascript
let a = 10
let b = 20

console.log(`${a} + ${b} = ${a + b}`)  // 10 + 20 = 30
console.log(`${a} x ${b} = ${a * b}`)  // 10 x 20 = 200

// Function call
function greet(name) {
    return `Hello, ${name}!`
}

console.log(`${greet("Budi")}`)  // Hello, Budi!
```

### Multi-line String

```javascript
// Cara lama (pakai \n)
let text1 = "Baris 1\nBaris 2\nBaris 3"

// Cara baru (langsung enter)
let text2 = `Baris 1
Baris 2
Baris 3`

console.log(text2)
// Output:
// Baris 1
// Baris 2
// Baris 3
```

### Nested Template Literal

```javascript
let name = "Budi"
let scores = [80, 90, 85]

let message = `Nilai ${name}:
${scores.map(score => `- ${score}`).join('\n')}`

console.log(message)
// Output:
// Nilai Budi:
// - 80
// - 90
// - 85
```

### Contoh Praktis

**1. HTML Template:**

```javascript
let user = {
    name: "Budi",
    email: "budi@email.com",
    role: "Admin"
}

let html = `
    <div class="user-card">
        <h2>${user.name}</h2>
        <p>Email: ${user.email}</p>
        <p>Role: ${user.role}</p>
    </div>
`

console.log(html)
```

**2. SQL Query:**

```javascript
let tableName = "users"
let userId = 123

let query = `
    SELECT * FROM ${tableName}
    WHERE id = ${userId}
`

console.log(query)
```

**3. Dynamic URL:**

```javascript
let baseUrl = "https://api.example.com"
let userId = 42

let url = `${baseUrl}/users/${userId}/posts`
console.log(url)  // https://api.example.com/users/42/posts
```

**4. Report Generator:**

```javascript
let product = {
    name: "Laptop",
    price: 10000000,
    stock: 5
}

let tax = 0.11
let total = product.price + (product.price * tax)

let report = `
Produk: ${product.name}
Harga: Rp ${product.price.toLocaleString()}
Pajak (11%): Rp ${(product.price * tax).toLocaleString()}
Total: Rp ${total.toLocaleString()}
Stok: ${product.stock} unit
`

console.log(report)
```

### Tagged Template Literals (Advanced)

```javascript
function highlight(strings, ...values) {
    return strings.reduce((result, str, i) => {
        return result + str + (values[i] ? `<mark>${values[i]}</mark>` : '')
    }, '')
}

let name = "Budi"
let age = 25

let html = highlight`Nama saya ${name} dan umur ${age}`
console.log(html)
// Nama saya <mark>Budi</mark> dan umur <mark>25</mark>
```

**Referensi:**
- https://stackoverflow.com/questions/3304014/how-to-interpolate-variables-in-strings-in-javascript-without-concatenation
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals

## Export dan Import

Export dan import adalah cara untuk membagi kode JavaScript ke beberapa file (modular programming). Ini membuat kode lebih terorganisir dan mudah di-maintain.

### Kenapa Pakai Modules?

**Tanpa Modules:**
```javascript
// Semua kode dalam satu file (messy!)
// file: app.js (1000+ baris)
function add(a, b) { return a + b }
function subtract(a, b) { return a - b }
function validateUser(user) { ... }
function connectDB() { ... }
// ... banyak code lainnya
```

**Dengan Modules:**
```javascript
// file: math.js
export function add(a, b) { return a + b }
export function subtract(a, b) { return a - b }

// file: validation.js
export function validateUser(user) { ... }

// file: database.js
export function connectDB() { ... }

// file: app.js (clean!)
import { add, subtract } from './math.js'
import { validateUser } from './validation.js'
import { connectDB } from './database.js'
```

### ES6 Modules (Modern)

#### Named Export

Mengexport beberapa hal dari satu file:

```javascript
// file: utils.js

// Export individual
export function add(a, b) {
    return a + b
}

export function subtract(a, b) {
    return a - b
}

export const PI = 3.14159

// Atau export di akhir
function multiply(a, b) {
    return a * b
}

function divide(a, b) {
    return a / b
}

export { multiply, divide }
```

**Import Named Exports:**

```javascript
// file: app.js

// Import specific
import { add, subtract } from './utils.js'

console.log(add(5, 3))       // 8
console.log(subtract(10, 4)) // 6

// Import dengan alias
import { add as tambah, subtract as kurang } from './utils.js'

console.log(tambah(5, 3))  // 8

// Import semua
import * as utils from './utils.js'

console.log(utils.add(5, 3))      // 8
console.log(utils.multiply(4, 2)) // 8
```

#### Default Export

Mengexport satu hal utama dari file:

```javascript
// file: User.js

export default class User {
    constructor(name, email) {
        this.name = name
        this.email = email
    }
    
    greet() {
        return `Hello, ${this.name}`
    }
}
```

**Import Default Export:**

```javascript
// file: app.js

// Bisa kasih nama apa saja (tidak harus User)
import User from './User.js'
import Customer from './User.js'  // Sama aja

let user = new User("Budi", "budi@email.com")
console.log(user.greet())  // Hello, Budi
```

#### Mixed Export (Default + Named)

```javascript
// file: config.js

const API_URL = "https://api.example.com"
const API_KEY = "secret123"

export default API_URL  // Default export

export { API_KEY }      // Named export

// Atau
export const TIMEOUT = 5000
```

**Import Mixed:**

```javascript
// file: app.js

import API_URL, { API_KEY, TIMEOUT } from './config.js'

console.log(API_URL)   // https://api.example.com
console.log(API_KEY)   // secret123
console.log(TIMEOUT)   // 5000
```

### CommonJS (Node.js Style)

Format lama yang masih dipakai di Node.js:

#### Module.exports

```javascript
// file: math.js

function add(a, b) {
    return a + b
}

function subtract(a, b) {
    return a - b
}

// Export object
module.exports = {
    add,
    subtract
}

// Atau export default
module.exports = add
```

**Require:**

```javascript
// file: app.js

const math = require('./math.js')

console.log(math.add(5, 3))      // 8
console.log(math.subtract(10, 4)) // 6

// Destructuring
const { add, subtract } = require('./math.js')

console.log(add(5, 3))  // 8
```

### Contoh Struktur Project

```
project/
├── index.html
├── js/
│   ├── app.js          (main file)
│   ├── utils/
│   │   ├── math.js
│   │   └── validation.js
│   ├── components/
│   │   ├── User.js
│   │   └── Product.js
│   └── config/
│       └── api.js
```

**math.js:**

```javascript
export function add(a, b) {
    return a + b
}

export function subtract(a, b) {
    return a - b
}
```

**User.js:**

```javascript
export default class User {
    constructor(name, email) {
        this.name = name
        this.email = email
    }
    
    getInfo() {
        return `${this.name} (${this.email})`
    }
}
```

**api.js:**

```javascript
export const API_URL = "https://api.example.com"
export const API_KEY = "secret123"

export default API_URL
```

**app.js:**

```javascript
import { add, subtract } from './utils/math.js'
import User from './components/User.js'
import API_URL, { API_KEY } from './config/api.js'

console.log(add(5, 3))  // 8

let user = new User("Budi", "budi@email.com")
console.log(user.getInfo())  // Budi (budi@email.com)

console.log(API_URL)  // https://api.example.com
```

### Pakai di HTML

```html
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body>
    <!-- PENTING: tambahkan type="module" -->
    <script type="module" src="js/app.js"></script>
</body>
</html>
```

### Dynamic Import (ES2020)

Import module secara conditional atau on-demand:

```javascript
// Import saat dibutuhkan
button.addEventListener('click', async () => {
    const { add } = await import('./math.js')
    console.log(add(5, 3))
})

// Conditional import
if (condition) {
    const module = await import('./module-a.js')
} else {
    const module = await import('./module-b.js')
}
```

### Re-export

Export ulang dari module lain:

```javascript
// file: index.js (barrel export)

export { add, subtract } from './math.js'
export { default as User } from './User.js'
export * from './validation.js'
```

Sekarang bisa import dari satu file:

```javascript
import { add, User, validateEmail } from './index.js'
```

### Best Practices

**1. Satu File Satu Tanggung Jawab:**

```javascript
// Good
// math.js - hanya math functions
// user.js - hanya User class
// api.js - hanya API config

// Bad
// utils.js - campur math, user, api, dll
```

**2. Gunakan Default Export untuk Hal Utama:**

```javascript
// User.js
export default class User { ... }  // Default export untuk class

// config.js
export default API_URL  // Default export untuk config utama
export { API_KEY, TIMEOUT }  // Named untuk yang lain
```

**3. Konsisten dengan Naming:**

```javascript
// File: User.js → Export: User (PascalCase untuk class)
// File: math.js → Export: add, subtract (camelCase untuk function)
// File: api.js → Export: API_URL (UPPER_CASE untuk constant)
```

**4. Avoid Circular Dependencies:**

```javascript
// Bad - Circular dependency
// a.js imports b.js
// b.js imports a.js

// Good - Refactor to c.js
// a.js imports c.js
// b.js imports c.js
```

***

## Referensi
- https://www.golinuxcloud.com/javascript-if-not/
- https://www.w3schools.com/js/js_comparisons.asp
- https://developer.mozilla.org/en-US/docs/Web/JavaScript
- https://javascript.info
- https://nodejs.org/docs
- https://www.freecodecamp.org
