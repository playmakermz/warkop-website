# JavaScript Array

## Daftar Isi
- [Pengenalan Array](#pengenalan-array)
- [Dasar-Dasar Array](#dasar-dasar-array)
- [Method Dasar Array](#method-dasar-array)
  - [Push](#push)
  - [Pop](#pop)
  - [Shift](#shift)
  - [Unshift](#unshift)
  - [Splice](#splice)
  - [Concat](#concat)
  - [Slice](#slice)
  - [Join](#join)
  - [Reverse](#reverse)
  - [Sort](#sort)
- [Array of Objects](#array-of-objects)
- [Method Array Lanjutan](#method-array-lanjutan)
  - [Map](#map)
  - [Filter](#filter)
  - [ForEach](#foreach)
  - [Find](#find)
  - [FindIndex](#findindex)
  - [Reduce](#reduce)
  - [Some](#some)
  - [Every](#every)
  - [Includes](#includes)

## Pengenalan Array

Array di JavaScript adalah object spesial yang bisa menyimpan banyak nilai sekaligus. Nilai yang disimpan bisa bermacam macam tipe data, termasuk:
- Number
- String
- Boolean
- Object
- Function
- Bahkan array lain (nested array)

**Kenapa Pakai Array?**

Bayangkan kamu punya 100 nama siswa. Daripada bikin 100 variabel berbeda, lebih praktis simpan semuanya dalam satu array!

**Contoh Array:**

```javascript
const myArray = [1, 2, 3, 4, 5]
const fruits = ["apel", "jeruk", "mangga"]
const mixed = [1, "hello", true, { name: "Budi" }]
```

**Karakteristik Array:**
- Dimulai dari index 0 (bukan 1)
- Panjangnya dinamis (bisa bertambah atau berkurang)
- Bisa menyimpan berbagai tipe data sekaligus

## Dasar-Dasar Array

### Membuat Array

Ada beberapa cara untuk membuat array:

**1. Array Literal (Paling Umum):**

```javascript
const numbers = [1, 2, 3, 4, 5]
const names = ["Budi", "Andi", "Citra"]
const empty = []  // Array kosong
```

**2. Pakai Constructor:**

```javascript
const arr1 = new Array(5)       // Array dengan 5 slot kosong
const arr2 = new Array(1, 2, 3) // Array [1, 2, 3]
```

**3. Array.of() (ES6):**

```javascript
const arr = Array.of(1, 2, 3)  // [1, 2, 3]
```

**4. Array.from() (ES6):**

```javascript
const str = "hello"
const chars = Array.from(str)  // ['h', 'e', 'l', 'l', 'o']
```

### Mengakses Element Array

Array menggunakan index yang dimulai dari 0:

```javascript
const fruits = ["apel", "jeruk", "mangga", "pisang"]

console.log(fruits[0])   // apel (index pertama)
console.log(fruits[1])   // jeruk
console.log(fruits[2])   // mangga
console.log(fruits[3])   // pisang
console.log(fruits[4])   // undefined (tidak ada)
```

**Mengakses Element Terakhir:**

```javascript
const lastFruit = fruits[fruits.length - 1]  // pisang
// atau pakai at() (ES2022)
const lastFruit2 = fruits.at(-1)  // pisang
```

### Mengubah Element Array

Kamu bisa mengubah nilai element dengan mengakses indexnya:

```javascript
const myArray = [1, 2, 3, 4, 5]

myArray[2] = 10  // Ubah index 2 dari 3 jadi 10
console.log(myArray)  // [1, 2, 10, 4, 5]

myArray[0] = 100  // Ubah index 0
console.log(myArray)  // [100, 2, 10, 4, 5]
```

### Length Property

Property `length` menunjukkan jumlah element dalam array:

```javascript
const fruits = ["apel", "jeruk", "mangga"]
console.log(fruits.length)  // 3

// Bisa diubah untuk memotong array
fruits.length = 2
console.log(fruits)  // ["apel", "jeruk"]

// Set length lebih besar akan menambah slot kosong
fruits.length = 5
console.log(fruits)  // ["apel", "jeruk", empty x 3]
```

## Method Dasar Array

Array punya banyak method bawaan untuk memanipulasi data. Mari kita pelajari satu per satu.

### Push

Method `push()` menambahkan element baru ke **akhir** array dan mengembalikan panjang array yang baru.

```javascript
const fruits = ["apel", "jeruk"]

fruits.push("mangga")
console.log(fruits)  // ["apel", "jeruk", "mangga"]

// Bisa tambah beberapa sekaligus
fruits.push("pisang", "anggur")
console.log(fruits)  // ["apel", "jeruk", "mangga", "pisang", "anggur"]

// Return nilai adalah panjang array baru
const newLength = fruits.push("melon")
console.log(newLength)  // 6
```

**Kapan Pakai:**
- Menambah item ke shopping cart
- Menambah data baru ke list
- Building array secara dinamis

### Pop

Method `pop()` menghapus element **terakhir** dari array dan mengembalikan element yang dihapus.

```javascript
const fruits = ["apel", "jeruk", "mangga", "pisang"]

const removed = fruits.pop()
console.log(removed)  // "pisang"
console.log(fruits)   // ["apel", "jeruk", "mangga"]

// Pop lagi
fruits.pop()
console.log(fruits)  // ["apel", "jeruk"]
```

**Push dan Pop = Stack (LIFO):**

```javascript
const stack = []

stack.push(1)    // [1]
stack.push(2)    // [1, 2]
stack.push(3)    // [1, 2, 3]

stack.pop()      // 3, array jadi [1, 2]
stack.pop()      // 2, array jadi [1]
```

### Shift

Method `shift()` menghapus element **pertama** dari array dan mengembalikan element yang dihapus. Semua element lain akan bergeser ke index yang lebih rendah.

```javascript
const fruits = ["apel", "jeruk", "mangga", "pisang"]

const removed = fruits.shift()
console.log(removed)  // "apel"
console.log(fruits)   // ["jeruk", "mangga", "pisang"]

fruits.shift()
console.log(fruits)  // ["mangga", "pisang"]
```

**Catatan:** `shift()` lebih lambat dari `pop()` karena harus menggeser semua element.

### Unshift

Method `unshift()` menambahkan element baru ke **awal** array dan mengembalikan panjang array yang baru.

```javascript
const fruits = ["mangga", "pisang"]

fruits.unshift("apel")
console.log(fruits)  // ["apel", "mangga", "pisang"]

// Bisa tambah beberapa sekaligus
fruits.unshift("melon", "anggur")
console.log(fruits)  // ["melon", "anggur", "apel", "mangga", "pisang"]
```

**Unshift dan Shift = Queue (FIFO):**

```javascript
const queue = []

queue.push(1)      // [1]
queue.push(2)      // [1, 2]
queue.push(3)      // [1, 2, 3]

queue.shift()      // 1, array jadi [2, 3]
queue.shift()      // 2, array jadi [3]
```

### Splice

Method `splice()` bisa menambah, menghapus, atau mengganti element di posisi manapun dalam array. Ini adalah method yang paling fleksibel tapi agak kompleks.

**Sintaks:**
```javascript
array.splice(start, deleteCount, item1, item2, ...)
```

**Parameter:**
- `start`: Index mulai mengubah array
- `deleteCount`: Jumlah element yang mau dihapus
- `item1, item2, ...`: Element baru yang mau ditambahkan

**1. Menghapus Element:**

```javascript
const fruits = ["apel", "jeruk", "mangga", "pisang", "anggur"]

// Hapus 2 element mulai dari index 1
fruits.splice(1, 2)
console.log(fruits)  // ["apel", "pisang", "anggur"]
```

**2. Menambah Element:**

```javascript
const fruits = ["apel", "mangga"]

// Tambah element di index 1, hapus 0 element
fruits.splice(1, 0, "jeruk", "pisang")
console.log(fruits)  // ["apel", "jeruk", "pisang", "mangga"]
```

**3. Mengganti Element:**

```javascript
const fruits = ["apel", "jeruk", "mangga"]

// Mulai dari index 1, hapus 1 element, tambah 2 element baru
fruits.splice(1, 1, "pisang", "anggur")
console.log(fruits)  // ["apel", "pisang", "anggur", "mangga"]
```

**4. Menghapus Semua Element Setelah Index Tertentu:**

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7]

// Hapus semua element mulai dari index 3
numbers.splice(3)
console.log(numbers)  // [1, 2, 3]
```

**Return Value:**

`splice()` mengembalikan array berisi element yang dihapus:

```javascript
const fruits = ["apel", "jeruk", "mangga", "pisang"]
const removed = fruits.splice(1, 2)

console.log(removed)  // ["jeruk", "mangga"]
console.log(fruits)   // ["apel", "pisang"]
```

### Concat

Method `concat()` menggabungkan dua atau lebih array menjadi array baru tanpa mengubah array asli.

```javascript
const arr1 = [1, 2, 3]
const arr2 = [4, 5, 6]
const arr3 = [7, 8, 9]

const combined = arr1.concat(arr2)
console.log(combined)  // [1, 2, 3, 4, 5, 6]

// Gabung beberapa array sekaligus
const allCombined = arr1.concat(arr2, arr3)
console.log(allCombined)  // [1, 2, 3, 4, 5, 6, 7, 8, 9]

// Array asli tidak berubah
console.log(arr1)  // [1, 2, 3]
```

**Concat dengan Nilai Tunggal:**

```javascript
const fruits = ["apel", "jeruk"]
const moreFruits = fruits.concat("mangga", "pisang")

console.log(moreFruits)  // ["apel", "jeruk", "mangga", "pisang"]
```

**Alternatif Modern (Spread Operator):**

```javascript
const arr1 = [1, 2, 3]
const arr2 = [4, 5, 6]

const combined = [...arr1, ...arr2]
console.log(combined)  // [1, 2, 3, 4, 5, 6]
```

### Slice

Method `slice()` mengambil potongan array dan mengembalikan array baru tanpa mengubah array asli.

**Sintaks:**
```javascript
array.slice(start, end)
```

**Parameter:**
- `start`: Index mulai (inclusive)
- `end`: Index akhir (exclusive, tidak termasuk)

**Contoh:**

```javascript
const fruits = ["apel", "jeruk", "mangga", "pisang", "anggur"]

// Ambil dari index 1 sampai 3 (tidak termasuk 3)
const sliced1 = fruits.slice(1, 3)
console.log(sliced1)  // ["jeruk", "mangga"]

// Ambil dari index 2 sampai akhir
const sliced2 = fruits.slice(2)
console.log(sliced2)  // ["mangga", "pisang", "anggur"]

// Ambil 2 element terakhir
const sliced3 = fruits.slice(-2)
console.log(sliced3)  // ["pisang", "anggur"]

// Array asli tidak berubah
console.log(fruits)  // ["apel", "jeruk", "mangga", "pisang", "anggur"]
```

**Copy Array:**

```javascript
const original = [1, 2, 3, 4, 5]
const copy = original.slice()

console.log(copy)  // [1, 2, 3, 4, 5]
console.log(copy === original)  // false (array berbeda)
```

**Perbedaan Slice vs Splice:**

| Aspek | Slice | Splice |
|-------|-------|--------|
| Mengubah array asli | Tidak | Ya |
| Return | Array baru | Array element yang dihapus |
| Fungsi | Salin sebagian array | Ubah array (hapus/tambah) |

### Join

Method `join()` menggabungkan semua element array menjadi satu string dengan separator yang ditentukan.

```javascript
const fruits = ["apel", "jeruk", "mangga"]

// Default separator adalah koma
const str1 = fruits.join()
console.log(str1)  // "apel,jeruk,mangga"

// Pakai separator custom
const str2 = fruits.join(" - ")
console.log(str2)  // "apel - jeruk - mangga"

const str3 = fruits.join(" dan ")
console.log(str3)  // "apel dan jeruk dan mangga"

// Tanpa separator
const str4 = fruits.join("")
console.log(str4)  // "apeljerukmangga"
```

**Contoh Praktis:**

```javascript
const path = ["home", "user", "documents", "file.txt"]
const fullPath = path.join("/")
console.log(fullPath)  // "home/user/documents/file.txt"

const words = ["Halo", "dunia", "JavaScript"]
const sentence = words.join(" ")
console.log(sentence)  // "Halo dunia JavaScript"
```

**Dengan Array Number:**

```javascript
const numbers = [1, 2, 3, 4, 5]
const result = numbers.join(" + ")
console.log(result)  // "1 + 2 + 3 + 4 + 5"
```

### Reverse

Method `reverse()` membalik urutan element dalam array. **Perhatian:** Method ini mengubah array asli!

```javascript
const numbers = [1, 2, 3, 4, 5]

numbers.reverse()
console.log(numbers)  // [5, 4, 3, 2, 1]

const fruits = ["apel", "jeruk", "mangga"]
fruits.reverse()
console.log(fruits)  // ["mangga", "jeruk", "apel"]
```

**Kalau Tidak Mau Ubah Array Asli:**

```javascript
const original = [1, 2, 3, 4, 5]

// Cara 1: Pakai slice dulu
const reversed1 = original.slice().reverse()
console.log(reversed1)  // [5, 4, 3, 2, 1]
console.log(original)   // [1, 2, 3, 4, 5] (tidak berubah)

// Cara 2: Pakai spread operator
const reversed2 = [...original].reverse()
console.log(reversed2)  // [5, 4, 3, 2, 1]
console.log(original)   // [1, 2, 3, 4, 5] (tidak berubah)
```

### Sort

Method `sort()` mengurutkan element array. **Perhatian:** Method ini mengubah array asli!

**Sort String (Alphabetically):**

```javascript
const fruits = ["pisang", "apel", "mangga", "jeruk"]

fruits.sort()
console.log(fruits)  // ["apel", "jeruk", "mangga", "pisang"]
```

**Sort Number (HARUS pakai compare function!):**

```javascript
const numbers = [40, 100, 1, 5, 25, 10]

// SALAH: Tanpa compare function (akan sort sebagai string)
numbers.sort()
console.log(numbers)  // [1, 10, 100, 25, 40, 5] ❌

// BENAR: Dengan compare function
const numbers2 = [40, 100, 1, 5, 25, 10]

// Ascending (kecil ke besar)
numbers2.sort((a, b) => a - b)
console.log(numbers2)  // [1, 5, 10, 25, 40, 100] ✓

// Descending (besar ke kecil)
numbers2.sort((a, b) => b - a)
console.log(numbers2)  // [100, 40, 25, 10, 5, 1] ✓
```

**Cara Kerja Compare Function:**

```javascript
function compareNumbers(a, b) {
    // Kalau return negatif, a sebelum b
    // Kalau return positif, b sebelum a
    // Kalau return 0, tidak ada perubahan
    return a - b
}

const numbers = [3, 1, 4, 1, 5]
numbers.sort(compareNumbers)
console.log(numbers)  // [1, 1, 3, 4, 5]
```

**Sort Array of Objects:**

```javascript
const students = [
    { name: "Budi", score: 85 },
    { name: "Andi", score: 92 },
    { name: "Citra", score: 78 }
]

// Sort by score (ascending)
students.sort((a, b) => a.score - b.score)
console.log(students)
// [
//   { name: "Citra", score: 78 },
//   { name: "Budi", score: 85 },
//   { name: "Andi", score: 92 }
// ]

// Sort by name (alphabetically)
students.sort((a, b) => a.name.localeCompare(b.name))
console.log(students)
// [
//   { name: "Andi", score: 92 },
//   { name: "Budi", score: 85 },
//   { name: "Citra", score: 78 }
// ]
```

**Sort Tanpa Ubah Array Asli:**

```javascript
const original = [3, 1, 4, 1, 5]

const sorted = [...original].sort((a, b) => a - b)
console.log(sorted)    // [1, 1, 3, 4, 5]
console.log(original)  // [3, 1, 4, 1, 5] (tidak berubah)
```

## Array of Objects

Array of objects adalah salah satu struktur data paling umum di JavaScript. Ini adalah array yang setiap elementnya berupa object.

### Apa itu Array of Objects?

Array of objects adalah cara menyimpan data relational dalam satu variabel, di mana setiap element adalah object yang punya property dan value.

**Contoh:**

```javascript
let students = [
    { name: 'Alice', age: 20, major: 'Computer Science' },
    { name: 'Bob', age: 22, major: 'Mathematics' },
    { name: 'Charlie', age: 21, major: 'Chemistry' }
]
```

**Struktur:**
- `{ }` adalah object
- `name` adalah property
- `'Alice'` adalah value

### Mengakses Data

**1. Mengakses Property Specific Object:**

```javascript
// Dot notation
console.log(students[0].name)   // Alice
console.log(students[1].age)    // 22
console.log(students[2].major)  // Chemistry

// Bracket notation
console.log(students[0]['name'])  // Alice
console.log(students[1]['age'])   // 22
```

**Kapan Pakai Bracket Notation:**
- Property punya spasi atau karakter khusus
- Property name disimpan dalam variabel

```javascript
let data = [
    { 'user name': 'Budi', 'user-id': 123 }
]

console.log(data[0]['user name'])  // Budi (harus pakai bracket)

let prop = 'user-id'
console.log(data[0][prop])  // 123 (property dari variabel)
```

**2. Loop Semua Data:**

```javascript
// Pakai forEach
students.forEach(function(student) {
    console.log(student.name + ' is ' + student.age + ' years old.')
})

// Atau pakai for...of
for (let student of students) {
    console.log(`${student.name} studies ${student.major}`)
}

// Atau pakai for loop biasa
for (let i = 0; i < students.length; i++) {
    console.log(students[i].name)
}
```

### Mengubah Data

**1. Ubah Property Specific Object:**

```javascript
students[0].name = 'Budi'
console.log(students[0].name)  // Budi

students[1].age = 23
console.log(students[1].age)  // 23
```

**2. Tambah Property Baru:**

```javascript
students[0].grade = 'A'
console.log(students[0])
// { name: 'Budi', age: 20, major: 'Computer Science', grade: 'A' }
```

**3. Hapus Property:**

```javascript
delete students[0].major
console.log(students[0])
// { name: 'Budi', age: 20, grade: 'A' }
```

### Menambah Object Baru ke Array

```javascript
let newStudent = { name: 'Diana', age: 19, major: 'Physics' }
students.push(newStudent)

// Atau langsung
students.push({ name: 'Eva', age: 20, major: 'Biology' })
```

### Mencari Object dalam Array

```javascript
// Cari student bernama Bob
const bob = students.find(student => student.name === 'Bob')
console.log(bob)  // { name: 'Bob', age: 22, major: 'Mathematics' }

// Cari index student bernama Charlie
const charlieIndex = students.findIndex(student => student.name === 'Charlie')
console.log(charlieIndex)  // 2
```

### Filter Berdasarkan Kondisi

```javascript
// Students yang umurnya >= 21
const olderStudents = students.filter(student => student.age >= 21)
console.log(olderStudents)

// Students dengan major tertentu
const csStudents = students.filter(student => student.major === 'Computer Science')
console.log(csStudents)
```

### Bentuk Sederhana (Object Literal)

Kadang kamu cuma butuh satu object tanpa array:

```javascript
let dataDiri = { nama: 'budi', hobby: 'memasak', umur: 25 }

// Akses property
console.log(dataDiri.nama)   // budi
console.log(dataDiri.hobby)  // memasak
console.log(dataDiri.umur)   // 25

// Ubah property
dataDiri.hobby = 'membaca'
console.log(dataDiri.hobby)  // membaca
```

### Contoh Real World

**1. Daftar Produk:**

```javascript
const products = [
    { id: 1, name: 'Laptop', price: 10000000, stock: 5 },
    { id: 2, name: 'Mouse', price: 50000, stock: 20 },
    { id: 3, name: 'Keyboard', price: 200000, stock: 15 }
]

// Total nilai stock
const totalValue = products.reduce((sum, product) => {
    return sum + (product.price * product.stock)
}, 0)
console.log(totalValue)  // 54000000
```

**2. User Management:**

```javascript
const users = [
    { id: 1, username: 'budi', email: 'budi@email.com', active: true },
    { id: 2, username: 'andi', email: 'andi@email.com', active: false },
    { id: 3, username: 'citra', email: 'citra@email.com', active: true }
]

// Ambil semua user yang aktif
const activeUsers = users.filter(user => user.active)

// Ambil semua email
const emails = users.map(user => user.email)
console.log(emails)  // ['budi@email.com', 'andi@email.com', 'citra@email.com']
```

## Method Array Lanjutan

Method-method ini sangat powerful untuk manipulasi data array.

### Map

Method `map()` membuat array baru dengan hasil dari memanggil function pada setiap element array asli.

**Konsep:**
- Tidak mengubah array asli
- Return array baru dengan panjang yang sama
- Setiap element diproses oleh callback function

**Sintaks:**
```javascript
array.map(function(element, index, array) {
    return newValue
})
```

**Contoh Dasar:**

```javascript
const numbers = [1, 2, 3, 4, 5]

// Kalikan setiap element dengan 2
const doubled = numbers.map(function(number) {
    return number * 2
})

console.log(doubled)   // [2, 4, 6, 8, 10]
console.log(numbers)   // [1, 2, 3, 4, 5] (tidak berubah)
```

**Dengan Arrow Function (Lebih Singkat):**

```javascript
const numbers = [1, 2, 3, 4, 5]

const squared = numbers.map(number => number ** 2)
console.log(squared)  // [1, 4, 9, 16, 25]
```

**Map pada Array of Objects:**

```javascript
const persons = [
    { name: 'Alice', age: 23 },
    { name: 'Bob', age: 37 },
    { name: 'Charlie', age: 19 }
]

// Ambil semua nama
const names = persons.map(person => person.name)
console.log(names)  // ['Alice', 'Bob', 'Charlie']

// Transform object
const personInfo = persons.map(person => {
    return {
        fullName: person.name,
        isAdult: person.age >= 18,
        category: person.age >= 30 ? 'Senior' : 'Junior'
    }
})

console.log(personInfo)
// [
//   { fullName: 'Alice', isAdult: true, category: 'Junior' },
//   { fullName: 'Bob', isAdult: true, category: 'Senior' },
//   { fullName: 'Charlie', isAdult: true, category: 'Junior' }
// ]
```

**Dengan Index:**

```javascript
const fruits = ['apel', 'jeruk', 'mangga']

const indexedFruits = fruits.map((fruit, index) => {
    return `${index + 1}. ${fruit}`
})

console.log(indexedFruits)
// ['1. apel', '2. jeruk', '3. mangga']
```

**Contoh Praktis:**

```javascript
const prices = [10000, 20000, 30000]

// Tambah pajak 10%
const pricesWithTax = prices.map(price => price * 1.1)
console.log(pricesWithTax)  // [11000, 22000, 33000]

// Format ke currency
const formattedPrices = prices.map(price => {
    return `Rp ${price.toLocaleString()}`
})
console.log(formattedPrices)
// ['Rp 10.000', 'Rp 20.000', 'Rp 30.000']
```

### Filter

Method `filter()` membuat array baru berisi semua element yang lolos test dari callback function.

**Konsep:**
- Tidak mengubah array asli
- Return array baru (bisa lebih pendek, sama panjang, atau kosong)
- Hanya element yang return `true` yang masuk array baru

**Sintaks:**
```javascript
array.filter(function(element, index, array) {
    return condition  // true atau false
})
```

**Contoh Dasar:**

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Ambil hanya angka genap
const evenNumbers = numbers.filter(function(number) {
    return number % 2 === 0
})

console.log(evenNumbers)  // [2, 4, 6, 8, 10]
```

**Dengan Arrow Function:**

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Angka lebih dari 5
const bigNumbers = numbers.filter(num => num > 5)
console.log(bigNumbers)  // [6, 7, 8, 9, 10]
```

**Filter Array of Objects:**

```javascript
const arrayUmur = [20, 18, 17, 16, 21, 23]

// Yang punya KTP (umur >= 18)
const pemilikKTP = arrayUmur.filter(function(umur) {
    return umur >= 18
})

console.log(pemilikKTP)  // [20, 18, 21, 23]
```

**Contoh dengan Array of Objects:**

```javascript
const students = [
    { name: 'Alice', grade: 85, status: 'active' },
    { name: 'Bob', grade: 72, status: 'inactive' },
    { name: 'Charlie', grade: 90, status: 'active' },
    { name: 'Diana', grade: 65, status: 'active' }
]

// Students dengan grade >= 80
const topStudents = students.filter(student => student.grade >= 80)
console.log(topStudents)
// [
//   { name: 'Alice', grade: 85, status: 'active' },
//   { name: 'Charlie', grade: 90, status: 'active' }
// ]

// Students yang aktif
const activeStudents = students.filter(student => student.status === 'active')
console.log(activeStudents.length)  // 3
```

**Multiple Conditions:**

```javascript
const products = [
    { name: 'Laptop', price: 10000000, inStock: true },
    { name: 'Mouse', price: 50000, inStock: false },
    { name: 'Keyboard', price: 200000, inStock: true },
    { name: 'Monitor', price: 2000000, inStock: true }
]

// Produk yang tersedia dan harga < 3000000
const affordable = products.filter(product => {
    return product.inStock && product.price < 3000000
})

console.log(affordable)
// [
//   { name: 'Keyboard', price: 200000, inStock: true },
//   { name: 'Monitor', price: 2000000, inStock: true }
// ]
```

**Filter String:**

```javascript
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction']

// Kata dengan panjang > 6
const longWords = words.filter(word => word.length > 6)
console.log(longWords)  // ['exuberant', 'destruction']

// Kata yang mengandung huruf 'e'
const wordsWithE = words.filter(word => word.includes('e'))
console.log(wordsWithE)  // ['elite', 'exuberant', 'destruction']
```

### ForEach

Method `forEach()` menjalankan function pada setiap element array. Berbeda dengan `map()`, `forEach()` tidak return array baru.

**Sintaks:**
```javascript
array.forEach(function(element, index, array) {
    // Code yang dijalankan untuk setiap element
})
```

**Contoh Dasar:**

```javascript
const fruits = ['apel', 'jeruk', 'mangga']

fruits.forEach(function(fruit) {
    console.log(fruit)
})
// Output:
// apel
// jeruk
// mangga
```

**Dengan Arrow Function:**

```javascript
const numbers = [1, 2, 3, 4, 5]

numbers.forEach(num => console.log(num * 2))
// Output: 2 4 6 8 10
```

**Dengan Index:**

```javascript
const fruits = ['apel', 'jeruk', 'mangga']

fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`)
})
// Output:
// 0: apel
// 1: jeruk
// 2: mangga
```

**ForEach pada Array of Objects:**

```javascript
const students = [
    { name: 'Alice', score: 85 },
    { name: 'Bob', score: 92 },
    { name: 'Charlie', score: 78 }
]

students.forEach(student => {
    console.log(`${student.name} mendapat nilai ${student.score}`)
})
// Output:
// Alice mendapat nilai 85
// Bob mendapat nilai 92
// Charlie mendapat nilai 78
```

**Modifikasi Element (Hati-hati!):**

```javascript
const numbers = [1, 2, 3, 4, 5]

// Ini TIDAK mengubah array
numbers.forEach(num => {
    num = num * 2  // Tidak mengubah array asli
})
console.log(numbers)  // [1, 2, 3, 4, 5]

// Kalau mau ubah, akses lewat index
numbers.forEach((num, index, arr) => {
    arr[index] = num * 2
})
console.log(numbers)  // [2, 4, 6, 8, 10]
```

**ForEach vs Map:**

```javascript
const numbers = [1, 2, 3, 4, 5]

// forEach: tidak return apa-apa
const result1 = numbers.forEach(num => num * 2)
console.log(result1)  // undefined

// map: return array baru
const result2 = numbers.map(num => num * 2)
console.log(result2)  // [2, 4, 6, 8, 10]
```

**Kapan Pakai ForEach:**
- Kalau cuma mau loop dan lakukan sesuatu (print, update database, dll)
- Tidak butuh return value
- Side effects (seperti update DOM, console.log, dll)

**Kapan Pakai Map:**
- Mau transform array jadi array baru
- Butuh return value
- Functional programming style

### Find

Method `find()` mencari dan mengembalikan element **pertama** yang memenuhi kondisi. Kalau tidak ketemu, return `undefined`.

**Sintaks:**
```javascript
array.find(function(element, index, array) {
    return condition
})
```

**Contoh Dasar:**

```javascript
const numbers = [1, 5, 10, 15, 20]

const found = numbers.find(num => num > 10)
console.log(found)  // 15 (element pertama yang > 10)
```

**Kalau Tidak Ketemu:**

```javascript
const numbers = [1, 2, 3, 4, 5]

const found = numbers.find(num => num > 10)
console.log(found)  // undefined
```

**Find pada Array of Objects:**

```javascript
const users = [
    { id: 1, name: 'Budi', age: 25 },
    { id: 2, name: 'Andi', age: 30 },
    { id: 3, name: 'Citra', age: 27 }
]

// Cari user dengan id 2
const user = users.find(u => u.id === 2)
console.log(user)  // { id: 2, name: 'Andi', age: 30 }

// Cari user dengan name 'Citra'
const citra = users.find(u => u.name === 'Citra')
console.log(citra)  // { id: 3, name: 'Citra', age: 27 }
```

**Contoh Praktis:**

```javascript
const products = [
    { id: 101, name: 'Laptop', price: 10000000 },
    { id: 102, name: 'Mouse', price: 50000 },
    { id: 103, name: 'Keyboard', price: 200000 }
]

// Cari product berdasarkan ID
function getProductById(id) {
    return products.find(product => product.id === id)
}

console.log(getProductById(102))
// { id: 102, name: 'Mouse', price: 50000 }

console.log(getProductById(999))  // undefined
```

### FindIndex

Method `findIndex()` mirip dengan `find()`, tapi mengembalikan **index** element pertama yang memenuhi kondisi. Kalau tidak ketemu, return `-1`.

**Sintaks:**
```javascript
array.findIndex(function(element, index, array) {
    return condition
})
```

**Contoh:**

```javascript
const numbers = [1, 5, 10, 15, 20]

const index = numbers.findIndex(num => num > 10)
console.log(index)  // 3 (index element 15)

// Kalau tidak ketemu
const notFound = numbers.findIndex(num => num > 100)
console.log(notFound)  // -1
```

**FindIndex pada Array of Objects:**

```javascript
const students = [
    { id: 1, name: 'Alice', grade: 85 },
    { id: 2, name: 'Bob', grade: 92 },
    { id: 3, name: 'Charlie', grade: 78 }
]

// Cari index student dengan grade >= 90
const topStudentIndex = students.findIndex(s => s.grade >= 90)
console.log(topStudentIndex)  // 1

// Gunakan index untuk update
if (topStudentIndex !== -1) {
    students[topStudentIndex].grade = 95
    console.log(students[topStudentIndex])
    // { id: 2, name: 'Bob', grade: 95 }
}
```

**Contoh: Hapus Element Berdasarkan Kondisi:**

```javascript
const todos = [
    { id: 1, task: 'Belajar JS', done: false },
    { id: 2, task: 'Buat project', done: true },
    { id: 3, task: 'Deploy', done: false }
]

// Hapus todo dengan id 2
const indexToDelete = todos.findIndex(todo => todo.id === 2)
if (indexToDelete !== -1) {
    todos.splice(indexToDelete, 1)
}

console.log(todos)
// [
//   { id: 1, task: 'Belajar JS', done: false },
//   { id: 3, task: 'Deploy', done: false }
// ]
```

### Reduce

Method `reduce()` mengeksekusi reducer function pada setiap element dan menghasilkan satu nilai akhir. Sangat powerful untuk aggregation (menjumlahkan, menggabungkan, dll).

**Sintaks:**
```javascript
array.reduce(function(accumulator, currentValue, index, array) {
    return newAccumulator
}, initialValue)
```

**Parameter:**
- `accumulator`: Nilai yang terakumulasi dari iterasi sebelumnya
- `currentValue`: Element yang sedang diproses
- `initialValue`: Nilai awal accumulator (opsional)

**Contoh: Sum Array:**

```javascript
const numbers = [1, 2, 3, 4, 5]

const sum = numbers.reduce((acc, num) => {
    return acc + num
}, 0)  // 0 adalah initial value

console.log(sum)  // 15
```

**Cara Kerja Reduce:**

```javascript
// Iterasi 1: acc = 0,  num = 1  → return 0 + 1 = 1
// Iterasi 2: acc = 1,  num = 2  → return 1 + 2 = 3
// Iterasi 3: acc = 3,  num = 3  → return 3 + 3 = 6
// Iterasi 4: acc = 6,  num = 4  → return 6 + 4 = 10
// Iterasi 5: acc = 10, num = 5  → return 10 + 5 = 15
```

**Contoh: Product Array:**

```javascript
const numbers = [2, 3, 4, 5]

const product = numbers.reduce((acc, num) => acc * num, 1)
console.log(product)  // 120 (2 * 3 * 4 * 5)
```

**Contoh: Find Max Value:**

```javascript
const numbers = [5, 12, 8, 130, 44]

const max = numbers.reduce((acc, num) => {
    return num > acc ? num : acc
}, numbers[0])

console.log(max)  // 130
```

**Reduce pada Array of Objects:**

```javascript
const products = [
    { name: 'Laptop', price: 10000000 },
    { name: 'Mouse', price: 50000 },
    { name: 'Keyboard', price: 200000 }
]

// Total harga
const totalPrice = products.reduce((total, product) => {
    return total + product.price
}, 0)

console.log(totalPrice)  // 10250000
```

**Counting Occurrences:**

```javascript
const fruits = ['apel', 'jeruk', 'apel', 'mangga', 'jeruk', 'apel']

const count = fruits.reduce((acc, fruit) => {
    acc[fruit] = (acc[fruit] || 0) + 1
    return acc
}, {})

console.log(count)
// { apel: 3, jeruk: 2, mangga: 1 }
```

**Grouping:**

```javascript
const students = [
    { name: 'Alice', grade: 'A' },
    { name: 'Bob', grade: 'B' },
    { name: 'Charlie', grade: 'A' },
    { name: 'Diana', grade: 'C' },
    { name: 'Eva', grade: 'B' }
]

const grouped = students.reduce((acc, student) => {
    const grade = student.grade
    if (!acc[grade]) {
        acc[grade] = []
    }
    acc[grade].push(student.name)
    return acc
}, {})

console.log(grouped)
// {
//   A: ['Alice', 'Charlie'],
//   B: ['Bob', 'Eva'],
//   C: ['Diana']
// }
```

**Flattening Array:**

```javascript
const nested = [[1, 2], [3, 4], [5, 6]]

const flattened = nested.reduce((acc, arr) => {
    return acc.concat(arr)
}, [])

console.log(flattened)  // [1, 2, 3, 4, 5, 6]
```

### Some

Method `some()` mengecek apakah **minimal satu** element memenuhi kondisi. Return `true` atau `false`.

**Sintaks:**
```javascript
array.some(function(element, index, array) {
    return condition
})
```

**Contoh:**

```javascript
const numbers = [1, 2, 3, 4, 5]

// Apakah ada angka genap?
const hasEven = numbers.some(num => num % 2 === 0)
console.log(hasEven)  // true

// Apakah ada angka > 10?
const hasLarge = numbers.some(num => num > 10)
console.log(hasLarge)  // false
```

**Some pada Array of Objects:**

```javascript
const students = [
    { name: 'Alice', grade: 85 },
    { name: 'Bob', grade: 92 },
    { name: 'Charlie', grade: 78 }
]

// Apakah ada student dengan grade >= 90?
const hasTopStudent = students.some(s => s.grade >= 90)
console.log(hasTopStudent)  // true

// Apakah ada student bernama Diana?
const hasDiana = students.some(s => s.name === 'Diana')
console.log(hasDiana)  // false
```

**Contoh Praktis:**

```javascript
const permissions = ['read', 'write', 'delete']

// Apakah user punya akses delete?
const canDelete = permissions.some(p => p === 'delete')
console.log(canDelete)  // true

// Validasi form
const formFields = [
    { name: 'username', value: 'budi' },
    { name: 'email', value: '' },
    { name: 'password', value: '123456' }
]

// Apakah ada field kosong?
const hasEmptyField = formFields.some(field => field.value === '')
console.log(hasEmptyField)  // true
```

### Every

Method `every()` mengecek apakah **semua** element memenuhi kondisi. Return `true` atau `false`.

**Sintaks:**
```javascript
array.every(function(element, index, array) {
    return condition
})
```

**Contoh:**

```javascript
const numbers = [2, 4, 6, 8, 10]

// Apakah semua angka genap?
const allEven = numbers.every(num => num % 2 === 0)
console.log(allEven)  // true

// Apakah semua angka > 5?
const allLarge = numbers.every(num => num > 5)
console.log(allLarge)  // false (ada 2 dan 4)
```

**Every pada Array of Objects:**

```javascript
const students = [
    { name: 'Alice', grade: 85, passed: true },
    { name: 'Bob', grade: 92, passed: true },
    { name: 'Charlie', grade: 78, passed: true }
]

// Apakah semua student lulus?
const allPassed = students.every(s => s.passed)
console.log(allPassed)  // true

// Apakah semua grade >= 80?
const allHighGrade = students.every(s => s.grade >= 80)
console.log(allHighGrade)  // false
```

**Perbedaan Some vs Every:**

```javascript
const numbers = [1, 2, 3, 4, 5]

// some: minimal satu yang true
console.log(numbers.some(n => n > 3))   // true (ada 4 dan 5)

// every: semua harus true
console.log(numbers.every(n => n > 3))  // false (1,2,3 tidak > 3)
```

**Contoh Praktis:**

```javascript
// Validasi semua field sudah diisi
const formData = [
    { field: 'username', value: 'budi' },
    { field: 'email', value: 'budi@email.com' },
    { field: 'password', value: '123456' }
]

const allFilled = formData.every(data => data.value !== '')
console.log(allFilled)  // true

// Check permissions
const userPermissions = ['read', 'write', 'delete']
const requiredPermissions = ['read', 'write']

const hasAllPermissions = requiredPermissions.every(perm => 
    userPermissions.includes(perm)
)
console.log(hasAllPermissions)  // true
```

### Includes

Method `includes()` mengecek apakah array mengandung element tertentu. Return `true` atau `false`.

**Sintaks:**
```javascript
array.includes(searchElement, fromIndex)
```

**Contoh:**

```javascript
const fruits = ['apel', 'jeruk', 'mangga', 'pisang']

console.log(fruits.includes('jeruk'))   // true
console.log(fruits.includes('durian'))  // false

// Case sensitive untuk string
console.log(fruits.includes('Apel'))    // false (huruf besar)
```

**Dengan FromIndex:**

```javascript
const numbers = [1, 2, 3, 4, 5, 3, 2, 1]

console.log(numbers.includes(3))     // true
console.log(numbers.includes(3, 4))  // true (mulai cari dari index 4)
console.log(numbers.includes(3, 6))  // false (tidak ada 3 setelah index 6)
```

**Includes vs IndexOf:**

```javascript
const arr = [1, 2, 3, NaN, 5]

// includes bisa detect NaN
console.log(arr.includes(NaN))   // true

// indexOf tidak bisa detect NaN
console.log(arr.indexOf(NaN))    // -1
```

**Contoh Praktis:**

```javascript
// Check user role
const userRoles = ['admin', 'editor', 'viewer']

if (userRoles.includes('admin')) {
    console.log('User is admin')
}

// Filter tags
const availableTags = ['javascript', 'python', 'java', 'ruby']
const searchTag = 'python'

if (availableTags.includes(searchTag)) {
    console.log(`Tag ${searchTag} ditemukan`)
}

// Validasi input
const allowedColors = ['red', 'green', 'blue', 'yellow']
const userColor = 'purple'

if (!allowedColors.includes(userColor)) {
    console.log('Warna tidak valid')
}
```

## Chaining Array Methods

Kamu bisa menggabungkan beberapa array method untuk operasi yang kompleks:

```javascript
const students = [
    { name: 'Alice', grade: 85, active: true },
    { name: 'Bob', grade: 72, active: false },
    { name: 'Charlie', grade: 90, active: true },
    { name: 'Diana', grade: 65, active: true },
    { name: 'Eva', grade: 88, active: true }
]

// Ambil nama student yang aktif dengan grade >= 80
const topActiveStudents = students
    .filter(s => s.active)              // Filter yang aktif
    .filter(s => s.grade >= 80)         // Filter grade >= 80
    .map(s => s.name)                   // Ambil nama aja
    .sort()                             // Sort alphabetically

console.log(topActiveStudents)  // ['Alice', 'Charlie', 'Eva']
```

**Contoh Lain:**

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

const result = numbers
    .filter(n => n % 2 === 0)     // Ambil angka genap: [2,4,6,8,10]
    .map(n => n * 2)               // Kalikan 2: [4,8,12,16,20]
    .reduce((sum, n) => sum + n, 0) // Jumlahkan: 60

console.log(result)  // 60
```

## Tips dan Best Practices

**1. Pilih Method yang Tepat:**

```javascript
// Kalau mau transform → pakai map()
const doubled = numbers.map(n => n * 2)

// Kalau mau filter → pakai filter()
const evens = numbers.filter(n => n % 2 === 0)

// Kalau mau cari satu → pakai find()
const found = numbers.find(n => n > 5)

// Kalau mau loop tanpa return → pakai forEach()
numbers.forEach(n => console.log(n))
```

**2. Hindari Mutasi Array Asli:**

```javascript
// Bad (mengubah array asli)
const arr1 = [1, 2, 3]
arr1.push(4)

// Good (buat array baru)
const arr1 = [1, 2, 3]
const arr2 = [...arr1, 4]
```

**3. Pakai Arrow Function untuk Callback Singkat:**

```javascript
// Panjang
const doubled = numbers.map(function(n) {
    return n * 2
})

// Singkat
const doubled = numbers.map(n => n * 2)
```

**4. Check Array Kosong:**

```javascript
const arr = []

if (arr.length === 0) {
    console.log('Array kosong')
}

// Atau
if (!arr.length) {
    console.log('Array kosong')
}
```

**5. Shallow Copy vs Deep Copy:**

```javascript
// Shallow copy (reference object masih sama)
const arr1 = [{ name: 'Budi' }]
const arr2 = [...arr1]
arr2[0].name = 'Andi'
console.log(arr1[0].name)  // 'Andi' (ikut berubah!)

// Deep copy (benar-benar terpisah)
const arr3 = JSON.parse(JSON.stringify(arr1))
arr3[0].name = 'Citra'
console.log(arr1[0].name)  // 'Andi' (tidak berubah)
```

***

## Referensi
- https://www.freecodecamp.org/news/javascript-array-of-objects-tutorial-how-to-create-update-and-loop-through-objects-using-js-array-methods/
- https://www.w3schools.com/jsref/jsref_filter.asp
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
- https://javascript.info/array
- https://javascript.info/array-methods
