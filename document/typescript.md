# Panduan Belajar TypeScript

## Daftar Isi

1. [Pengenalan TypeScript](#pengenalan-typescript)
   - [Apa itu TypeScript?](#apa-itu-typescript)
   - [Keuntungan Menggunakan TypeScript](#keuntungan-menggunakan-typescript)
2. [Instalasi dan Setup](#instalasi-dan-setup)
   - [Install TypeScript](#install-typescript)
   - [Menjalankan File TypeScript](#menjalankan-file-typescript)
   - [Troubleshooting](#troubleshooting)
3. [Dasar-Dasar TypeScript](#dasar-dasar-typescript)
   - [Tipe Data Primitif](#tipe-data-primitif)
   - [Union Type](#union-type)
   - [Object Type](#object-type)
   - [Literal Type](#literal-type)
4. [Percabangan dan Kondisi](#percabangan-dan-kondisi)
5. [Array di TypeScript](#array-di-typescript)
   - [Array Biasa](#array-biasa)
   - [Tuple](#tuple)
   - [Readonly Array](#readonly-array)
6. [Loop dan Perulangan](#loop-dan-perulangan)
7. [Function di TypeScript](#function-di-typescript)
   - [Function Biasa](#function-biasa)
   - [Arrow Function](#arrow-function)
   - [Optional Parameter](#optional-parameter)
   - [Function Overloading](#function-overloading)
8. [Class dan OOP](#class-dan-oop)
   - [Membuat Class](#membuat-class)
   - [Inheritance (Pewarisan)](#inheritance-pewarisan)
   - [Access Modifier](#access-modifier)
9. [Referensi dan Resources](#referensi-dan-resources)

---

## Pengenalan TypeScript

### Apa itu TypeScript?

TypeScript adalah superset dari JavaScript yang menambahkan sistem tipe data statis. Bayangkan JavaScript yang bisa lebih "ketat" dalam mengatur tipe data. Dengan TypeScript, kita bisa mendefinisikan tipe data untuk variabel, function, dan parameter.

Di era modern, aplikasi web jadi semakin kompleks. Code yang kita tulis juga makin banyak, dan ini bisa bikin bug makin susah dilacak. TypeScript hadir untuk mengatasi masalah ini dengan sistem tipe data yang ketat.

### Keuntungan Menggunakan TypeScript

**1. Mencegah Bug Lebih Awal**

TypeScript bisa nangkep error tipe data saat kita lagi nulis code, bukan pas aplikasi sudah running. Jadi bug bisa diperbaiki lebih cepat dan menghemat waktu debugging.

**Contoh Masalah di JavaScript:**
```javascript
// JavaScript biasa - tidak ada error sampai code dijalankan
function add(a, b) {
  return a + b;
}

add(5, "10"); // Hasil: "510" (bukan 15!)
```

**Solusi dengan TypeScript:**
```typescript
// TypeScript - error langsung terdeteksi saat coding
function add(a: number, b: number): number {
  return a + b;
}

add(5, "10"); // Error: Argument tipe 'string' tidak bisa assign ke parameter tipe 'number'
```

**2. Code Lebih Mudah Dipahami**

Dengan tipe data yang jelas, developer lain (atau kamu sendiri nanti) bisa lebih mudah ngerti maksud dari code. Ini sangat membantu saat kerja dalam tim atau saat buka code lama.

**3. Refactoring Lebih Aman**

Saat kamu ubah code (refactor), TypeScript memastikan perubahan tersebut tidak menyebabkan bug di bagian lain. Sistem tipe data akan warning kalau ada yang tidak compatible.

**4. Developer Experience Lebih Baik**

TypeScript menyediakan fitur autocompletion dan IntelliSense yang sangat membantu. IDE bisa kasih saran code yang tepat, jadi coding jadi lebih cepat dan efisien.

**5. Dokumentasi Built-in**

Tipe data TypeScript berfungsi sebagai dokumentasi inline. Kamu tidak perlu baca dokumentasi terpisah untuk tau parameter apa yang dibutuhkan suatu function.

### Contoh Perbandingan JavaScript vs TypeScript

**JavaScript:**
```javascript
// Tidak jelas apa yang diharapkan dan apa yang dikembalikan
function greet(name) {
  return "Hello, " + name;
}

greet(123); // Tidak ada error, tapi hasilnya aneh
```

**TypeScript:**
```typescript
// Jelas: menerima string, mengembalikan string
function greet(name: string): string {
  return "Hello, " + name;
}

greet(123); // Error: tipe number tidak bisa digunakan sebagai string
```

---

## Instalasi dan Setup

### Install TypeScript

Untuk mulai menggunakan TypeScript, kita perlu install beberapa package. Ikuti langkah berikut:

**1. Install ts-node Secara Global**

```bash
npm install -g ts-node
```

`ts-node` adalah tool yang memungkinkan kita menjalankan file TypeScript langsung tanpa harus compile dulu ke JavaScript.

**2. Install TypeScript (Opsional tapi Direkomendasikan)**

```bash
npm install -g typescript
```

Package ini memberikan akses ke TypeScript compiler (`tsc`) yang berguna untuk compile TypeScript ke JavaScript.

### Menjalankan File TypeScript

Setelah install ts-node, kamu bisa langsung jalankan file TypeScript:

```bash
ts-node namafile.ts
```

**Contoh:**
```bash
# Membuat file hello.ts
echo 'console.log("Hello TypeScript!");' > hello.ts

# Menjalankan file
ts-node hello.ts
```

### Troubleshooting

**Problem: Error "ERR_UNKNOWN_FILE_EXTENSION"**

Jika kamu mendapat error ini, kemungkinan besar file `package.json` kamu menggunakan `"type": "module"`. Solusinya ada 2:

**Solusi 1: Hapus/Ubah type di package.json**
```json
{
  "name": "my-project",
  // Hapus atau ubah baris ini:
  // "type": "module"
}
```

**Solusi 2: Gunakan ESM loader**
```bash
ts-node --esm namafile.ts
```

**Problem: Module not found**

Jika ada error module not found, pastikan kamu sudah install dependencies yang diperlukan:
```bash
npm install
```

### Referensi Instalasi

Untuk informasi lebih detail tentang instalasi, bisa cek link berikut:
- [Cara Execute TypeScript File](https://www.geeksforgeeks.org/how-to-execute-typescript-file-using-command-line/)
- [Running TypeScript with ts-node](https://www.digitalocean.com/community/tutorials/typescript-running-typescript-ts-node)
- [Troubleshooting ERR_UNKNOWN_FILE_EXTENSION](https://stackoverflow.com/questions/62096269/cant-run-my-node-js-typescript-project-typeerror-err-unknown-file-extension)

---

## Dasar-Dasar TypeScript

TypeScript menambahkan sistem tipe data ke JavaScript. Mari kita pelajari tipe data dasar yang tersedia.

### Tipe Data Primitif

Tipe data primitif adalah tipe data dasar yang paling sering digunakan.

```typescript
// String - untuk teks
let name: string = "Udin";
let greeting: string = 'Hello World';

// Number - untuk angka (integer dan desimal)
let age: number = 10;
let price: number = 99.99;
let negative: number = -5;

// Boolean - untuk nilai true/false
let isReady: boolean = true;
let isLoggedIn: boolean = false;

// Null - nilai kosong yang explicit
let empty: null = null;

// Undefined - nilai yang belum didefinisikan
let notDefined: undefined = undefined;
```

**Penjelasan:**
- **String**: Tipe data untuk teks, bisa pakai petik tunggal atau ganda
- **Number**: Semua angka di TypeScript adalah number, tidak ada perbedaan integer dan float
- **Boolean**: Hanya bisa bernilai `true` atau `false`
- **Null**: Nilai kosong yang sengaja kita set
- **Undefined**: Nilai yang belum di-assign

### Union Type

Union type memungkinkan suatu variabel memiliki lebih dari satu tipe data.

```typescript
// Variabel ini bisa string atau undefined
let username: undefined | string = "Udin";

// Bisa juga diubah jadi undefined
username = undefined;

// Error jika diisi dengan tipe lain
username = 123; // Error: tipe number tidak compatible

// Union dengan banyak tipe
let value: string | number | boolean = "hello";
value = 42; // OK
value = true; // OK
```

**Kapan Digunakan:**
- Saat value bisa null/undefined
- Saat function bisa return berbagai tipe
- Saat property bisa berbagai tipe

### Object Type

Ada beberapa cara untuk define tipe object di TypeScript.

**Cara 1: Type Any (Tidak Direkomendasikan)**
```typescript
// Tipe 'object' terlalu general, hindari penggunaan ini
let person: object = { name: 'Udin', age: 22 };
```

**Cara 2: Explicit Property Types (Direkomendasikan)**
```typescript
// Define tipe untuk setiap property
let user: { name: string, age: number } = { 
  name: 'Fatoni', 
  age: 22 
};

// Lebih readable dengan line break
let product: {
  id: number;
  name: string;
  price: number;
  inStock: boolean;
} = {
  id: 1,
  name: 'Laptop',
  price: 5000000,
  inStock: true
};
```

**Cara 3: Interface (Best Practice untuk Object yang Kompleks)**
```typescript
// Define interface
interface User {
  name: string;
  age: number;
  email?: string; // Optional property (pakai ?)
}

// Gunakan interface
let user1: User = { name: 'Budi', age: 25 };
let user2: User = { name: 'Ani', age: 23, email: 'ani@mail.com' };
```

### Literal Type

Literal type membatasi nilai yang bisa digunakan, bukan hanya tipe data nya.

```typescript
// Function yang hanya menerima nilai spesifik
const findLocationInJakarta = (
  location: 'Utara' | 'Timur' | 'Selatan' | 'Barat'
): string => {
  return `Jakarta ${location}`;
};

// Usage yang benar
findLocationInJakarta('Utara');    // OK: "Jakarta Utara"
findLocationInJakarta('Selatan');  // OK: "Jakarta Selatan"

// Error - nilai tidak ada di list
findLocationInJakarta('Udin');     // Error!
findLocationInJakarta('Tengah');   // Error!
```

**Keuntungan Literal Type:**
- Mencegah typo
- IDE memberikan autocomplete dengan pilihan yang valid
- Code lebih safe karena nilai dibatasi

**Contoh Lain:**
```typescript
// Status order
type OrderStatus = 'pending' | 'processing' | 'shipped' | 'delivered';

function updateOrderStatus(status: OrderStatus) {
  console.log(`Order status: ${status}`);
}

updateOrderStatus('pending');    // OK
updateOrderStatus('cancelled');  // Error: tidak ada di list
```

---

## Percabangan dan Kondisi

TypeScript membantu kita saat menggunakan percabangan dengan type narrowing. Artinya, TypeScript bisa "mempersempit" tipe data berdasarkan kondisi.

### Type Narrowing dengan typeof

```typescript
// Variabel dengan union type
let data: string | number = "Hello";

// TypeScript tau kalau di dalam if, data pasti string
if (typeof data === "string") {
  console.log(data.toUpperCase()); // "HELLO"
  // Method string bisa digunakan tanpa error
}

// TypeScript tau kalau di sini data pasti number
if (typeof data === "number") {
  console.log(data.toFixed(2)); // Method number
}
```

**Penjelasan:**
- Di dalam `if (typeof data === "string")`, TypeScript tau bahwa `data` pasti string
- Jadi kita bisa pakai method string seperti `toUpperCase()` tanpa error
- Ini disebut "type narrowing" atau penyempitan tipe

### Contoh dengan Function

```typescript
function processValue(value: string | number) {
  if (typeof value === "string") {
    // Di sini value adalah string
    return value.toLowerCase();
  } else {
    // Di sini value pasti number (karena cuma 2 kemungkinan)
    return value * 2;
  }
}

console.log(processValue("HELLO")); // "hello"
console.log(processValue(10));      // 20
```

### Nullable Check

```typescript
function greet(name?: string) {
  if (name) {
    // Di sini name pasti ada (not null/undefined)
    console.log(`Hello, ${name.toUpperCase()}`);
  } else {
    console.log("Hello, Guest");
  }
}

greet("Budi");      // "Hello, BUDI"
greet();            // "Hello, Guest"
```

---

## Array di TypeScript

Array di TypeScript bisa memiliki tipe data spesifik untuk elemennya.

### Array Biasa

Ada 2 cara untuk mendefinisikan tipe array:

**Cara 1: Menggunakan []**
```typescript
// Array yang hanya bisa berisi number
let angka: number[] = [1, 2, 3, 4, 5];
angka.push(6);     // OK
angka.push("7");   // Error: tipe string tidak compatible

// Array yang hanya bisa berisi string
let buah: string[] = ["apel", "jeruk", "mangga"];
buah.push("durian"); // OK
buah.push(123);      // Error

// Array boolean
let flags: boolean[] = [true, false, true];
```

**Cara 2: Menggunakan Generic Array<T>**
```typescript
// Sama dengan number[], tapi pakai sintaks generic
let numbers: Array<number> = [1, 2, 3];

// Array string dengan generic
let names: Array<string> = ["Alice", "Bob", "Charlie"];
```

**Kapan Pakai Yang Mana?**
- `number[]` lebih simple dan umum digunakan
- `Array<number>` lebih eksplisit dan konsisten dengan sintaks generic lainnya
- Pilih salah satu dan konsisten di seluruh codebase

### Tuple

Tuple adalah array dengan jumlah element tetap dan tipe data yang sudah ditentukan untuk setiap posisi.

```typescript
// Tuple dengan 2 element: string dan number
let tuple: [string, number] = ["Age", 25];

// Urutan harus sesuai
let person: [string, number, boolean] = ["Budi", 25, true];

// Error jika urutan tidak sesuai
let wrong: [string, number] = [25, "Age"]; // Error!

// Error jika jumlah element tidak sesuai
let incomplete: [string, number] = ["Age"]; // Error!
```

**Keuntungan Tuple:**
- Memastikan struktur data tetap konsisten
- Berguna untuk return multiple values dari function
- Lebih type-safe daripada array biasa

**Contoh Praktis:**
```typescript
// Function yang return tuple
function getCoordinates(): [number, number] {
  return [10.5, 20.3]; // [latitude, longitude]
}

const [lat, long] = getCoordinates();
console.log(`Latitude: ${lat}, Longitude: ${long}`);
```

### Readonly Array

Readonly array adalah array yang tidak bisa diubah setelah dibuat.

```typescript
// Array yang tidak bisa dimodifikasi
const readOnlyArr: readonly number[] = [1, 2, 3];

// Bisa dibaca
console.log(readOnlyArr[0]); // 1

// Error jika mencoba memodifikasi
readOnlyArr.push(4);      // Error!
readOnlyArr[0] = 10;      // Error!
readOnlyArr.pop();        // Error!
```

**Kapan Digunakan:**
- Saat array tidak boleh diubah (immutable data)
- Untuk constant values
- Mencegah bug dari modifikasi yang tidak disengaja

**Contoh Praktis:**
```typescript
// Config yang tidak boleh diubah
const API_ENDPOINTS: readonly string[] = [
  'https://api.example.com/users',
  'https://api.example.com/products',
  'https://api.example.com/orders'
];

// Hanya bisa dibaca
console.log(API_ENDPOINTS[0]);

// Tidak bisa diubah
API_ENDPOINTS.push('new-endpoint'); // Error!
```

---

## Loop dan Perulangan

Loop di TypeScript sama dengan JavaScript, tapi dengan keuntungan type inference yang otomatis.

### For Loop Standar

```typescript
// Loop biasa dengan counter
for (let i = 0; i < 5; i++) {
  console.log(i); // 0, 1, 2, 3, 4
}

// Loop dengan step berbeda
for (let i = 0; i < 10; i += 2) {
  console.log(i); // 0, 2, 4, 6, 8
}

// Loop mundur
for (let i = 5; i > 0; i--) {
  console.log(i); // 5, 4, 3, 2, 1
}
```

### For...of Loop (Untuk Iterasi Value)

```typescript
const angka: number[] = [10, 20, 30, 40, 50];

// Loop yang langsung ambil value dari array
for (const num of angka) {
  console.log(num * 2); // 20, 40, 60, 80, 100
  // TypeScript otomatis tau 'num' adalah number
  // Jadi method number bisa langsung dipakai
}

// Contoh dengan string array
const names: string[] = ["Alice", "Bob", "Charlie"];
for (const name of names) {
  console.log(name.toUpperCase()); // Method string bisa langsung dipakai
}
```

**Keuntungan for...of:**
- Lebih simple dan readable
- Langsung dapat value, tidak perlu akses via index
- TypeScript otomatis inference tipe data

### For...in Loop (Untuk Iterasi Index/Key)

```typescript
const angka: number[] = [10, 20, 30];

// Loop yang ambil index dari array
for (const index in angka) {
  console.log(index);         // "0", "1", "2" (tipe: string!)
  console.log(angka[index]);  // 10, 20, 30
}

// For...in di object
const person = {
  name: "Budi",
  age: 25,
  city: "Jakarta"
};

for (const key in person) {
  console.log(`${key}: ${person[key]}`);
}
```

**Penting:**
- Index dari `for...in` bertipe **string**, bukan number!
- Untuk array, lebih baik pakai `for...of` daripada `for...in`
- `for...in` lebih cocok untuk object

### While dan Do-While

```typescript
// While loop
let count = 0;
while (count < 5) {
  console.log(count);
  count++;
}

// Do-while loop (minimal 1x eksekusi)
let i = 0;
do {
  console.log(i);
  i++;
} while (i < 5);
```

### Kapan Pakai Loop Apa?

| Loop Type | Kapan Digunakan |
|-----------|-----------------|
| `for` | Tau jumlah iterasi, perlu index |
| `for...of` | Iterasi value array/iterable |
| `for...in` | Iterasi key object atau index array |
| `while` | Iterasi sampai kondisi tercapai |
| `do...while` | Minimal 1x eksekusi, lalu cek kondisi |

---

## Function di TypeScript

Function di TypeScript memiliki type annotations untuk parameter dan return value.

### Function Biasa

```typescript
// Function dengan tipe parameter dan return value
function add(a: number, b: number): number {
  return a + b;
}

// Cara pakai
let result = add(5, 10);  // result: number = 15
console.log(result);

// Error jika tipe tidak sesuai
add("5", 10);   // Error: string tidak bisa dipakai sebagai number
add(5);         // Error: kurang parameter
```

**Penjelasan:**
- `a: number` - parameter a harus number
- `b: number` - parameter b harus number
- `: number` setelah () - function mengembalikan number
- TypeScript akan error jika return value tidak sesuai tipe

### Arrow Function

```typescript
// Arrow function dengan type annotation
const multiply = (x: number, y: number): number => x * y;

// Cara pakai
let result = multiply(5, 3); // 15

// Arrow function dengan body yang lebih panjang
const divide = (x: number, y: number): number => {
  if (y === 0) {
    throw new Error("Cannot divide by zero");
  }
  return x / y;
};
```

### Void Return Type

Function yang tidak return apa-apa menggunakan tipe `void`.

```typescript
// Function yang tidak return value
function greet(name: string): void {
  console.log(`Hello ${name}`);
  // Tidak ada return statement
}

// Cara pakai
greet("Budi"); // "Hello Budi"

// Error jika mencoba return value
function wrongGreet(name: string): void {
  return `Hello ${name}`; // Error: void function tidak boleh return value
}
```

### Optional Parameter

Parameter yang optional ditandai dengan `?` setelah nama parameter.

```typescript
// Parameter 'age' adalah optional
function greet(name: string, age?: number): void {
  if (age) {
    console.log(`Hello ${name}, you are ${age} years old`);
  } else {
    console.log(`Hello ${name}`);
  }
}

// Kedua cara ini valid
greet("Budi");           // "Hello Budi"
greet("Budi", 25);       // "Hello Budi, you are 25 years old"
```

**Aturan Optional Parameter:**
- Optional parameter harus setelah required parameter
- Bisa ada beberapa optional parameter
- Di dalam function, optional parameter bertipe `T | undefined`

**Contoh dengan Multiple Optional:**
```typescript
function createUser(
  name: string,
  age?: number,
  email?: string,
  phone?: number
): void {
  console.log(`Name: ${name}`);
  if (age) console.log(`Age: ${age}`);
  if (email) console.log(`Email: ${email}`);
  if (phone) console.log(`Phone: ${phone}`);
}

createUser("Budi");
createUser("Budi", 25);
createUser("Budi", 25, "budi@mail.com");
```

### Default Parameter

Parameter dengan default value otomatis menjadi optional.

```typescript
// Parameter dengan default value
function greet(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}!`;
}

console.log(greet("Budi"));              // "Hello, Budi!"
console.log(greet("Budi", "Hi"));        // "Hi, Budi!"
console.log(greet("Budi", "Good morning")); // "Good morning, Budi!"
```

### Function Overloading

Function overloading memungkinkan function memiliki berbagai signature tergantung parameter yang diberikan.

```typescript
// Overload signatures
function padLeft(value: string, padding: number): string;
function padLeft(value: string, padding: string): string;

// Implementation signature (harus compatible dengan semua overload)
function padLeft(value: string, padding: number | string): string {
  if (typeof padding === "number") {
    return " ".repeat(padding) + value;
  }
  return padding + value;
}

// Usage
console.log(padLeft("Hello", 4));     // "    Hello"
console.log(padLeft("Hello", ">> ")); // ">> Hello"
```

**Penjelasan:**
- Overload signature mendefinisikan cara function bisa dipanggil
- Implementation signature adalah code yang sebenarnya dijalankan
- Implementation harus bisa handle semua case dari overload

### Rest Parameters

```typescript
// Rest parameter untuk jumlah argument yang flexible
function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3));           // 6
console.log(sum(1, 2, 3, 4, 5));     // 15
console.log(sum());                  // 0
```

---

## Class dan OOP

Class di TypeScript memiliki fitur yang lebih lengkap dibanding JavaScript, termasuk access modifier dan type annotations.

### Membuat Class

```typescript
class Animal {
  // Property dengan tipe data
  name: string;
  private age: number;

  // Constructor
  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  // Method
  speak(): void {
    console.log(`${this.name} makes a noise`);
  }

  // Method yang return value
  getAge(): number {
    return this.age;
  }
}

// Cara pakai
const cat = new Animal("Kitty", 3);
cat.speak(); // "Kitty makes a noise"
console.log(cat.name); // "Kitty" (bisa diakses karena public)
// console.log(cat.age); // Error! private property tidak bisa diakses
```

### Shorthand Constructor

TypeScript punya cara yang lebih simple untuk define property di constructor:

```typescript
// Cara panjang (seperti contoh sebelumnya)
class Animal1 {
  name: string;
  private age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}

// Cara pendek (shorthand) - DIREKOMENDASIKAN
class Animal2 {
  constructor(public name: string, private age: number) {
    // Tidak perlu assign this.name dan this.age
    // TypeScript otomatis buat property dan assign value
  }
}

// Hasilnya sama
const dog = new Animal2("Rex", 5);
console.log(dog.name); // "Rex"
```

**Keuntungan Shorthand:**
- Code lebih singkat
- Tidak perlu declare property terpisah
- Tidak perlu assign manual di constructor
- Lebih readable

### Inheritance (Pewarisan)

Class bisa inherit dari class lain menggunakan `extends`.

```typescript
// Parent class
class Animal {
  constructor(public name: string, private age: number) {}

  speak(): void {
    console.log(`${this.name} makes a noise`);
  }

  getAge(): number {
    return this.age;
  }
}

// Child class yang inherit dari Animal
class Dog extends Animal {
  constructor(name: string, age: number, public breed: string) {
    // Harus panggil super() untuk jalankan constructor parent
    super(name, age);
  }

  // Override method dari parent
  speak(): void {
    console.log(`${this.name} barks: Woof woof!`);
  }

  // Method khusus Dog
  fetch(): void {
    console.log(`${this.name} is fetching the ball`);
  }
}

// Usage
const myDog = new Dog("Rex", 3, "Husky");

myDog.speak();        // "Rex barks: Woof woof!" (method yang di-override)
myDog.fetch();        // "Rex is fetching the ball"
console.log(myDog.name);   // "Rex" (dari parent)
console.log(myDog.breed);  // "Husky" (property khusus Dog)
console.log(myDog.getAge()); // 3 (method dari parent)
```

**Konsep Penting:**
- `extends` untuk inherit dari parent class
- `super()` harus dipanggil di constructor child class
- Child class dapat akses public/protected property dari parent
- Child class bisa override method parent

### Access Modifier

TypeScript punya 3 access modifier untuk control visibility property dan method:

**1. Public (Default)**
```typescript
class Person {
  public name: string; // Bisa diakses dari mana saja

  constructor(name: string) {
    this.name = name;
  }
}

const person = new Person("Budi");
console.log(person.name); // OK - public bisa diakses
```

**2. Private**
```typescript
class BankAccount {
  private balance: number; // Hanya bisa diakses di dalam class ini

  constructor(initialBalance: number) {
    this.balance = initialBalance;
  }

  // Method public untuk akses balance
  getBalance(): number {
    return this.balance; // OK - dalam class yang sama
  }

  deposit(amount: number): void {
    this.balance += amount; // OK - dalam class yang sama
  }
}

const account = new BankAccount(1000);
console.log(account.getBalance()); // OK - via method public
// console.log(account.balance);   // Error! private property
```

**3. Protected**
```typescript
class Vehicle {
  protected speed: number; // Bisa diakses di class ini dan child class

  constructor(speed: number) {
    this.speed = speed;
  }
}

class Car extends Vehicle {
  showSpeed(): void {
    console.log(this.speed); // OK - protected bisa diakses di child class
  }
}

const car = new Car(100);
car.showSpeed(); // OK
// console.log(car.speed); // Error! protected tidak bisa diakses dari luar
```

### Contoh Lengkap dengan Access Modifier

```typescript
class Animal {
  constructor(
    public name: string,      // Bisa diakses dari mana saja
    private age: number,      // Hanya dalam class Animal
    protected species: string // Dalam Animal dan child class-nya
  ) {}

  speak(): void {
    console.log(`${this.name} makes a noise`);
  }

  private getAge(): number {
    return this.age;
  }

  showInfo(): void {
    console.log(`${this.name} is ${this.age} years old`);
  }
}

class Dog extends Animal {
  constructor(name: string, age: number, public breed: string) {
    super(name, age, "Canine");
  }

  showDetails(): void {
    console.log(`${this.name} is a ${this.species}`); // OK - protected bisa diakses
    // console.log(this.age);  // Error! private tidak bisa diakses di child
  }
}

// Usage
const myDog = new Dog("Rex", 3, "Husky");

console.log(myDog.name);   // OK - public
console.log(myDog.breed);  // OK - public
// console.log(myDog.age);     // Error! - private
// console.log(myDog.species); // Error! - protected
// myDog.getAge();             // Error! - method private

myDog.speak();       // OK - public method
myDog.showInfo();    // OK - public method
myDog.showDetails(); // OK - public method
```

### Ringkasan Access Modifier

| Modifier | Dalam Class | Child Class | Luar Class |
|----------|-------------|-------------|------------|
| `public` | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ❌ |
| `private` | ✅ | ❌ | ❌ |

**Best Practice:**
- Gunakan `private` untuk property/method internal yang tidak boleh diakses dari luar
- Gunakan `protected` jika child class perlu akses
- Gunakan `public` (atau tidak pakai modifier) untuk API yang memang harus bisa diakses
- Default adalah `public` jika tidak ada modifier

### Getter dan Setter

```typescript
class Temperature {
  private _celsius: number = 0;

  // Getter
  get celsius(): number {
    return this._celsius;
  }

  // Setter dengan validasi
  set celsius(value: number) {
    if (value < -273.15) {
      throw new Error("Temperature cannot be below absolute zero");
    }
    this._celsius = value;
  }

  // Computed property
  get fahrenheit(): number {
    return (this._celsius * 9/5) + 32;
  }
}

// Usage
const temp = new Temperature();
temp.celsius = 25;              // Pakai setter
console.log(temp.celsius);      // 25 (pakai getter)
console.log(temp.fahrenheit);   // 77 (computed getter)
```

---

## Referensi dan Resources

### Official Documentation
- [TypeScript Official Website](https://www.typescriptlang.org/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [TypeScript Playground](https://www.typescriptlang.org/play) - Interactive online editor untuk belajar TypeScript

### Tools dan Converter
- [JS to TS Converter](https://js2ts.com/) - Convert JavaScript code ke TypeScript

### Tutorial dan Learning Resources
- [TypeScript for JavaScript Programmers](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)
- [TypeScript Deep Dive](https://basarat.gitbook.io/typescript/) - Free online book
- [TypeScript Exercises](https://typescript-exercises.github.io/) - Practice exercises

### Instalasi dan Setup References
- [Execute TypeScript File via Command Line](https://www.geeksforgeeks.org/how-to-execute-typescript-file-using-command-line/)
- [Running TypeScript with ts-node](https://www.digitalocean.com/community/tutorials/typescript-running-typescript-ts-node)
- [Troubleshooting ERR_UNKNOWN_FILE_EXTENSION](https://stackoverflow.com/questions/62096269/cant-run-my-node-js-typescript-project-typeerror-err-unknown-file-extension)

### Tips untuk Belajar TypeScript

1. **Mulai dari JavaScript yang Sudah Kamu Tau**: TypeScript adalah superset JavaScript, jadi semua JavaScript yang valid adalah TypeScript yang valid

2. **Gunakan Type Inference**: Tidak perlu define tipe untuk semua hal. TypeScript bisa infer tipe dari context

3. **Practice dengan Playground**: Gunakan TypeScript Playground untuk eksperimen tanpa setup

4. **Baca Error Messages**: TypeScript error messages sangat helpful. Baca baik-baik untuk mengerti problem nya

5. **Start Strict**: Gunakan strict mode (`"strict": true` di tsconfig.json) untuk dapat full benefit TypeScript

6. **Lihat Contoh Code**: Banyak library popular ditulis dengan TypeScript. Lihat source code mereka untuk belajar best practices

---
