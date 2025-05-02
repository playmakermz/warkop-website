# Typescript

## Instalasi 

```Sh 
npm install -g ts-node

ts-node <file-name>

// Setelah itu, pastikan pada file "package.json" kita tidak menggunakan "module" import.
```

Ref: 

- https://www.geeksforgeeks.org/how-to-execute-typescript-file-using-command-line/ | Instalasi 
- https://www.digitalocean.com/community/tutorials/typescript-running-typescript-ts-node | Instalasi dan contoh 
- https://stackoverflow.com/questions/62096269/cant-run-my-node-js-typescript-project-typeerror-err-unknown-file-extension | informasi jika error. 

## TypeScript: Memperkuat JavaScript dengan Tipe Data

Di era modern, pengembangan web telah menjadi semakin kompleks. Aplikasi web modern membutuhkan fungsionalitas yang lebih canggih dan basis kode yang lebih besar. Hal ini dapat menyebabkan berbagai masalah, seperti bug dan inkonsistensi kode.

TypeScript hadir sebagai solusi untuk mengatasi masalah tersebut. TypeScript adalah superset dari JavaScript yang menambahkan sistem tipe data statis. Sistem tipe data ini memungkinkan pengembang untuk mendefinisikan tipe data untuk variabel, fungsi, dan parameter. Hal ini membantu meningkatkan keandalan dan kemudahan pemeliharaan kode JavaScript.

**Keuntungan Menggunakan TypeScript:**

* **Meningkatkan Keamanan Kode:** TypeScript membantu mencegah bug dengan mendeteksi kesalahan tipe data pada saat kompilasi. Hal ini membantu pengembang untuk menemukan dan memperbaiki bug lebih awal dalam proses pengembangan, sehingga menghemat waktu dan tenaga.
* **Mempermudah Pemahaman Kode:** Sistem tipe data TypeScript membuat kode JavaScript lebih mudah dipahami dan dibaca. Hal ini membantu pengembang lain untuk memahami maksud dari kode dan meningkatkan kolaborasi dalam proyek pengembangan.
* **Meningkatkan Refactoring Kode:** TypeScript membantu pengembang untuk melakukan refactoring kode dengan lebih aman. Sistem tipe data memastikan bahwa perubahan yang dilakukan pada kode tidak menyebabkan bug yang tidak terduga.
* **Mempercepat Pengembangan:** TypeScript dapat membantu mempercepat pengembangan dengan menyediakan fitur autocompletion dan IntelliSense. Fitur-fitur ini membantu pengembang untuk menulis kode dengan lebih cepat dan efisien.

**Contoh Penggunaan TypeScript:**

Berikut adalah contoh bagaimana TypeScript dapat digunakan untuk mendefinisikan tipe data untuk variabel, fungsi, dan parameter:

```typescript
// Mendefinisikan variabel dengan tipe string
let name: string = "John Doe";

// Mendefinisikan fungsi dengan parameter bertipe number dan mengembalikan nilai bertipe number
function add(a: number, b: number): number {
  return a + b;
}

// Memanggil fungsi dengan argumen bertipe number
let sum = add(10, 20);
console.log(sum); // Output: 30
```

**Belajar TypeScript:**

TypeScript adalah bahasa pemrograman yang mudah dipelajari bagi para pengembang JavaScript. Banyak sumber daya yang tersedia untuk membantu pengembang mempelajari TypeScript, termasuk:

* [Dokumentasi Resmi TypeScript](https://www.typescriptlang.org/docs/handbook/intro.html)
* [Tutorial Interaktif TypeScript](https://www.typescriptlang.org/play)
* Kursus Online TypeScript [URL yang tidak valid dihapus]

**Kesimpulan:**

TypeScript adalah alat yang berharga bagi para pengembang JavaScript yang ingin meningkatkan kualitas dan keandalan kode mereka. Dengan sistem tipe data statisnya, TypeScript membantu mencegah bug, meningkatkan pemahaman kode, mempermudah refactoring kode, dan mempercepat pengembangan. Jika Anda ingin meningkatkan skill pengembangan web Anda, mempelajari TypeScript adalah langkah yang tepat.

***
# TypeScript Fundamental
***

```JavaScript

let name: string = "udin"
let age: number = 10 
let isReady: boolean = true 
let x: null = null 
let array1: number[] = [1,2]
let array2: string[] = ["udin"]
let array3: boolean[] = [true, false]
let namaku: undefined | string = "udin" // Bisa dua tipe data yang masuk

let abc: object = {name:'udin',age:22}
let acc: {name: string, age: number} = {name: 'fatoni', age: 22}

// =============== TS 

const hello = (name: string): string => {
  return `Hello ${name}`
}


function mat(item: number): number {
  return item + 1;
}

// ====================== Eliminate parameter

const findLocationInJakarta = (
  location: 'Utara' | 'Timur' | 'Selatan' | 'Barat',
): string => {
  return `Jakarta ${location}`
}

findLocationInJakarta('Utara')

findLocationInJakarta('Selatan')

findLocationInJakarta('udin') // Error
```


## if statement 


Percabangan 

```Js 

// Contoh If statement 
let data: string | number = "Hello";
if (typeof data === "string") {
  console.log(data.toUpperCase()); // Mengubah huruf kecil ke besar
}
```

## Array 

```js
// Array number
let angka: number[] = [1, 2, 3];
let names: Array<string> = ["Alice", "Bob"];

// array dibawah ini, tipe datanya tetap
let tuple: [string, number] = ["Age", 25];

// Readonly array
const readOnlyArr: readonly number[] = [1, 2, 3];
```

## Loop 

Untuk loop sederhana seperti dibawah, tidak ada configurasi tambahan dari typescript.

```js
// Default for loop
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// For loop yang akan mengambil value item pada array 'angka'
for (const num of angka) {
  console.log(num * 2); // num otomatis number
}

// for loop yang akan mengambil nomor index sebagai value mereka.
for (const index in angka) {
  console.log(index); // string: "0", "1", "2"
}
```

## Function 

```js
// Fungsi dasar
function add(a: number, b: number): number {
  return a + b;
}

// Arrow function
const multiply = (x: number, y: number): number => x * y;

// Parameter opsional
function greet(name: string, age?: number): void {
  console.log(`Hello ${name}${age ? ` (${age})` : ''}`);
}

// Function overloading
function padLeft(value: string, padding: number | string): string {
  // Implementasi
}
```

## Class

```js
class Animal {
  // Menjabarkan tipe data untuk setiap parameter yang ada
  constructor(public name: string, private age: number) {}

  // Method
  speak(): void {
    console.log(`${this.name} makes a noise`);
  }
}

class Dog extends Animal {
  constructor(name: string, age: number, public breed: string) {
    super(name, age);
  }

  // Override method
  speak(): void {
    console.log("Woof!");
  }
}

// Penggunaan
const myDog = new Dog("Rex", 3, "Husky");
myDog.speak(); // "Woof!"
```

Note:
- Mengenai parameter private, sederhananya parameter terssebut hanya bisa diakses dialam code class saja, oject instance yang tercipta tidak termasuk.

contohnya begini:
```js
console.log(myDog.name) // Rex
console.log(myDog.age) // Error javascript!
```



## Reference
- https://www.typescriptlang.org/
- https://js2ts.com/ | Convert Js to Ts
