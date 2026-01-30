# JavaScript Synchronous dan Asynchronous

## Daftar Isi
- [Synchronous Programming](#synchronous-programming)
- [Asynchronous Programming](#asynchronous-programming)
- [Callback](#callback)
- [Callback Hell](#callback-hell)
- [Promise](#promise)
  - [Promise Basics](#promise-basics)
  - [Promise State dan Result](#promise-state-dan-result)
  - [Then, Catch, Finally](#then-catch-finally)
  - [Promise Chaining](#promise-chaining)
  - [Error Handling](#error-handling)
- [Async/Await](#asyncawait)
  - [Async Function](#async-function)
  - [Await Keyword](#await-keyword)
  - [Error Handling dengan Try-Catch](#error-handling-dengan-try-catch)
- [Promise Methods](#promise-methods)
  - [Promise.all](#promiseall)
  - [Promise.race](#promiserace)
  - [Promise.allSettled](#promiseallsettled)
  - [Promise.any](#promiseany)
- [Fetch API](#fetch-api)
- [Best Practices](#best-practices)

## Synchronous Programming

Synchronous (sinkron) adalah cara kerja program secara default di JavaScript, di mana semua baris kode dijalankan secara berurutan, satu per satu, dari atas ke bawah.

**Analogi:**
Seperti antrian di kasir. Orang pertama harus selesai dilayani dulu, baru orang kedua bisa dilayani, dan seterusnya.

**Contoh:**

```javascript
console.log('a')
console.log('b')
console.log('c')

// Output (berurutan):
// a
// b
// c
```

**Contoh dengan Function:**

```javascript
function step1() {
    console.log('Step 1 selesai')
}

function step2() {
    console.log('Step 2 selesai')
}

function step3() {
    console.log('Step 3 selesai')
}

step1()
step2()
step3()

// Output:
// Step 1 selesai
// Step 2 selesai
// Step 3 selesai
```

**Masalah Synchronous:**

Kalau ada operasi yang membutuhkan waktu lama (misal ambil data dari server), program akan "freeze" menunggu operasi selesai.

```javascript
function downloadFile() {
    // Simulasi download yang lama (blocking)
    for (let i = 0; i < 1000000000; i++) {
        // Do nothing, just wait
    }
    return "File downloaded"
}

console.log('Start download')
let file = downloadFile()  // Program freeze di sini!
console.log(file)
console.log('Continue program')

// Program akan terasa hang saat download
```

## Asynchronous Programming

Asynchronous (asinkron) memungkinkan program menjalankan beberapa proses secara bersamaan tanpa harus menunggu satu proses selesai.

**Analogi:**
Seperti waiter di restoran. Mereka bisa menerima pesanan dari beberapa meja sekaligus, tidak perlu menunggu makanan meja 1 selesai baru terima pesanan meja 2.

**Contoh dengan setTimeout:**

```javascript
console.log('Start')

setTimeout(() => {
    console.log('Ini jalan setelah 2 detik')
}, 2000)

console.log('End')

// Output:
// Start
// End
// Ini jalan setelah 2 detik
```

**Cara Kerja:**
1. `console.log('Start')` → Jalan langsung
2. `setTimeout()` → Dijadwalkan untuk jalan nanti (2 detik)
3. `console.log('End')` → Jalan langsung tanpa tunggu setTimeout
4. Setelah 2 detik → setTimeout jalan

**Contoh Praktis:**

```javascript
console.log('Mulai proses')

// Simulasi fetch data dari server
setTimeout(() => {
    console.log('Data dari server diterima')
}, 3000)

// Program tetap jalan, tidak freeze
console.log('Proses lain tetap jalan')
console.log('User tetap bisa klik button')

// Output langsung:
// Mulai proses
// Proses lain tetap jalan
// User tetap bisa klik button
// (tunggu 3 detik)
// Data dari server diterima
```

## Callback

Callback adalah function yang dikirim sebagai parameter ke function lain, untuk dijalankan nanti setelah operasi selesai.

**Sintaks:**

```javascript
function doSomething(callback) {
    // Lakukan sesuatu
    callback()  // Panggil callback
}
```

**Contoh Dasar:**

```javascript
function greet(name, callback) {
    console.log('Hello, ' + name)
    callback()
}

function sayGoodbye() {
    console.log('Goodbye!')
}

greet('Budi', sayGoodbye)
// Output:
// Hello, Budi
// Goodbye!
```

**Contoh dengan Async:**

```javascript
function fetchData(callback) {
    console.log('Fetching data...')
    
    setTimeout(() => {
        let data = { id: 1, name: 'Budi' }
        callback(data)
    }, 2000)
}

function processData(data) {
    console.log('Data received:', data)
}

fetchData(processData)
// Output:
// Fetching data...
// (tunggu 2 detik)
// Data received: { id: 1, name: 'Budi' }
```

**Callback dengan Error Handling:**

```javascript
function fetchUser(userId, onSuccess, onError) {
    setTimeout(() => {
        if (userId > 0) {
            onSuccess({ id: userId, name: 'Budi' })
        } else {
            onError('Invalid user ID')
        }
    }, 1000)
}

// Success case
fetchUser(1, 
    (user) => console.log('User:', user),
    (error) => console.log('Error:', error)
)
// Output: User: { id: 1, name: 'Budi' }

// Error case
fetchUser(-1,
    (user) => console.log('User:', user),
    (error) => console.log('Error:', error)
)
// Output: Error: Invalid user ID
```

## Callback Hell

Callback hell terjadi saat kita punya banyak callback bersarang (nested), membuat kode sulit dibaca dan maintain.

**Contoh Callback Hell:**

```javascript
// Ambil user, lalu posts, lalu comments
getUser(1, (user) => {
    console.log('User:', user.name)
    
    getUserPosts(user.id, (posts) => {
        console.log('Posts:', posts.length)
        
        getPostComments(posts[0].id, (comments) => {
            console.log('Comments:', comments.length)
            
            getCommentAuthor(comments[0].id, (author) => {
                console.log('Author:', author.name)
                
                // ... dan seterusnya (pyramid of doom!)
            })
        })
    })
})
```

**Masalah:**
- Kode berbentuk piramid (pyramid of doom)
- Sulit dibaca dan di-maintain
- Error handling jadi kompleks
- Sulit untuk debug

**Solusi:**
Gunakan Promise atau Async/Await!

## Promise

Promise adalah object yang merepresentasikan hasil akhir dari operasi asynchronous yang akan selesai di masa depan.

### Analogi Sederhana

Bayangkan kamu pesen makanan online:

**Tanpa Promise:**
"Saya mau pesen nasi goreng. Tunggu dulu ya..." (program freeze)

**Dengan Promise:**
"Saya mau pesen nasi goreng. Nanti saya kasih tau kalau udah siap atau kalau ada masalah."

Program bisa lanjut ngerjain hal lain sambil nunggu makanan.

### Analogi Band Musik

Ada band musik yang punya banyak fans. Fans tiap hari kirim surat mau denger album baru.

Biar tidak repot, band kasih formulir ke fans untuk isi email dan alamat. Kalau ada update, fans akan dapat info:
- Album sudah rilis (resolve) ✓
- Album tertunda (reject) ✗

**Hubungannya dengan Code:**
- **Producing code** = Band musik (yang buat Promise)
- **Consuming code** = Fans (yang pakai Promise)
- **Promise** = Penghubung antara keduanya

### Promise Basics

**Membuat Promise:**

```javascript
let promise = new Promise((resolve, reject) => {
    // Code asynchronous di sini
    
    // Kalau sukses, panggil resolve
    resolve(value)
    
    // Kalau gagal, panggil reject
    reject(error)
})
```

**Contoh Sederhana:**

```javascript
let promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        let success = true
        
        if (success) {
            resolve('Berhasil!')
        } else {
            reject('Gagal!')
        }
    }, 1000)
})

// Pakai promise
promise.then(
    (result) => console.log(result),  // Jalan kalau resolve
    (error) => console.log(error)     // Jalan kalau reject
)
```

### Promise State dan Result

Setiap Promise punya 2 internal property:

**1. State (Status):**
- **pending** (menunggu): State awal, operasi masih berjalan
- **fulfilled** (berhasil): Operasi selesai dengan sukses
- **rejected** (gagal): Operasi gagal

**2. Result (Hasil):**
- **undefined**: State awal (pending)
- **value**: Nilai yang di-pass ke resolve (fulfilled)
- **error**: Error yang di-pass ke reject (rejected)

**Diagram State:**

```
           ┌─────────┐
    ┌──────│ pending │──────┐
    │      └─────────┘      │
    │                       │
    ▼                       ▼
┌───────────┐         ┌──────────┐
│ fulfilled │         │ rejected │
│ (resolve) │         │ (reject) │
└───────────┘         └──────────┘
```

**Contoh:**

```javascript
let promise = new Promise((resolve, reject) => {
    console.log('State: pending')
    
    setTimeout(() => {
        resolve('Success!')  // State jadi fulfilled
        // reject('Error!')  // State jadi rejected
    }, 1000)
})

promise.then(
    (result) => console.log('Fulfilled:', result),
    (error) => console.log('Rejected:', error)
)
```

### Then, Catch, Finally

**1. then() - Handle Success:**

```javascript
promise.then((result) => {
    console.log(result)
})
```

**2. catch() - Handle Error:**

```javascript
promise.catch((error) => {
    console.log(error)
})
```

**3. finally() - Jalan Apapun Hasilnya:**

```javascript
promise.finally(() => {
    console.log('Selesai, entah sukses atau gagal')
})
```

**Contoh Lengkap:**

```javascript
let promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        let randomNum = Math.random()
        
        if (randomNum > 0.5) {
            resolve('Berhasil! Angka: ' + randomNum)
        } else {
            reject('Gagal! Angka: ' + randomNum)
        }
    }, 1000)
})

promise
    .then((result) => {
        console.log('✓', result)
    })
    .catch((error) => {
        console.log('✗', error)
    })
    .finally(() => {
        console.log('Promise selesai diproses')
    })
```

**Contoh Promise Success:**

```javascript
let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve('Selesai!'), 1000)
})

promise.then(
    (result) => console.log(result),  // "Selesai!" (jalan)
    (error) => console.log(error)     // (tidak jalan)
)
```

**Contoh Promise Reject:**

```javascript
let promise = new Promise((resolve, reject) => {
    setTimeout(() => reject(new Error('Ups, error!')), 1000)
})

promise.then(
    (result) => console.log(result),  // (tidak jalan)
    (error) => console.log(error)     // Error: Ups, error! (jalan)
)
```

**Finally - Tidak Terpengaruh Hasil:**

```javascript
let promise = new Promise((resolve, reject) => {
    setTimeout(() => reject(new Error('Error!')), 1000)
})

promise
    .finally(() => {
        console.log('Ini jalan dulu, tidak peduli sukses atau gagal')
    })
    .then(
        (result) => console.log(result),
        (error) => console.log(error.message)
    )

// Output:
// Ini jalan dulu, tidak peduli sukses atau gagal
// Error!
```

### Promise Chaining

Promise bisa di-chain (rantai) untuk melakukan operasi berurutan tanpa callback hell.

**Masalah tanpa Promise:**

```javascript
function tampilkan(item) {
    console.log(item)
}

function math(x, y) {
    setTimeout(() => {
        return x ** y  // Return tidak jalan di async!
    }, 1000)
}

let hasil = math(2, 3)
tampilkan(hasil)  // Output: undefined (bukan 8)
```

**Masalah:** Function `tampilkan()` sudah selesai duluan sebelum `math()`. Mereka jalan bersamaan tapi tidak terkoordinasi.

**Solusi dengan Promise:**

```javascript
function proses(a, b) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(a + b)
        }, 1000)
    })
}

proses(1, 2)
    .then((result) => {
        console.log('Hasil:', result)  // 3
        return result * 2  // Pass ke then berikutnya
    })
    .then((result) => {
        console.log('Dikali 2:', result)  // 6
        return result + 10
    })
    .then((result) => {
        console.log('Ditambah 10:', result)  // 16
    })
    .catch((error) => {
        console.log('Error:', error)
    })

// Output:
// Hasil: 3
// Dikali 2: 6
// Ditambah 10: 16
```

**Contoh Real World (Fetch User Data):**

```javascript
function getUser(userId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (userId > 0) {
                resolve({ id: userId, name: 'Budi' })
            } else {
                reject('Invalid user ID')
            }
        }, 1000)
    })
}

function getUserPosts(userId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve([
                { id: 1, title: 'Post 1' },
                { id: 2, title: 'Post 2' }
            ])
        }, 1000)
    })
}

function getPostComments(postId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve([
                { id: 1, text: 'Comment 1' },
                { id: 2, text: 'Comment 2' }
            ])
        }, 1000)
    })
}

// Promise chaining (lebih clean dari callback hell!)
getUser(1)
    .then((user) => {
        console.log('User:', user.name)
        return getUserPosts(user.id)
    })
    .then((posts) => {
        console.log('Posts:', posts.length)
        return getPostComments(posts[0].id)
    })
    .then((comments) => {
        console.log('Comments:', comments)
    })
    .catch((error) => {
        console.log('Error:', error)
    })
```

### Error Handling

**Cara 1: then() dengan 2 Parameter:**

```javascript
promise.then(
    (result) => console.log(result),
    (error) => console.log(error)
)
```

**Cara 2: Pakai catch():**

```javascript
promise
    .then((result) => console.log(result))
    .catch((error) => console.log(error))
```

**Cara 3: Error di Chain:**

```javascript
getUser(1)
    .then((user) => {
        if (!user.name) {
            throw new Error('User name is required')
        }
        return getUserPosts(user.id)
    })
    .then((posts) => {
        return getPostComments(posts[0].id)
    })
    .catch((error) => {
        // Tangkap semua error di chain
        console.log('Error occurred:', error.message)
    })
    .finally(() => {
        console.log('Cleanup atau loading spinner off')
    })
```

## Async/Await

Async/await adalah syntactic sugar untuk Promise, membuat code asynchronous terlihat seperti synchronous (lebih mudah dibaca).

### Async Function

Function yang ditandai dengan keyword `async` akan selalu return Promise.

**Sintaks:**

```javascript
async function namaFunction() {
    // Code
}
```

**Contoh:**

```javascript
async function greet() {
    return 'Hello!'
}

// Sama dengan:
function greet2() {
    return Promise.resolve('Hello!')
}

// Pakai
greet().then((message) => console.log(message))  // Hello!
```

**Return Value:**

```javascript
async function test() {
    return 42
}

// Otomatis jadi Promise
test().then((value) => console.log(value))  // 42
```

### Await Keyword

`await` membuat JavaScript menunggu Promise selesai dan return hasilnya. Hanya bisa dipakai di dalam `async` function.

**Sintaks:**

```javascript
let result = await promise
```

**Contoh Tanpa Await:**

```javascript
function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve('Data dari server')
        }, 2000)
    })
}

async function getData() {
    let data = fetchData()
    console.log(data)  // Promise { <pending> }
}

getData()
```

**Contoh Dengan Await:**

```javascript
function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve('Data dari server')
        }, 2000)
    })
}

async function getData() {
    let data = await fetchData()  // Tunggu sampai selesai
    console.log(data)  // "Data dari server"
}

getData()
```

**Perbandingan Promise vs Async/Await:**

```javascript
// Dengan Promise (then)
function getUserData() {
    getUser(1)
        .then((user) => {
            console.log(user)
            return getUserPosts(user.id)
        })
        .then((posts) => {
            console.log(posts)
        })
        .catch((error) => {
            console.log(error)
        })
}

// Dengan Async/Await (lebih clean!)
async function getUserData() {
    try {
        let user = await getUser(1)
        console.log(user)
        
        let posts = await getUserPosts(user.id)
        console.log(posts)
    } catch (error) {
        console.log(error)
    }
}
```

**Contoh Multiple Await:**

```javascript
async function processData() {
    console.log('Start')
    
    let user = await getUser(1)
    console.log('User:', user.name)
    
    let posts = await getUserPosts(user.id)
    console.log('Posts:', posts.length)
    
    let comments = await getPostComments(posts[0].id)
    console.log('Comments:', comments.length)
    
    console.log('Done')
}

processData()
```

### Error Handling dengan Try-Catch

Dengan async/await, kita pakai try-catch seperti synchronous code.

**Sintaks:**

```javascript
async function getData() {
    try {
        let result = await promise
        // Handle success
    } catch (error) {
        // Handle error
    } finally {
        // Cleanup
    }
}
```

**Contoh:**

```javascript
function fetchUser(userId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (userId > 0) {
                resolve({ id: userId, name: 'Budi' })
            } else {
                reject(new Error('Invalid user ID'))
            }
        }, 1000)
    })
}

async function getUser() {
    try {
        let user = await fetchUser(1)
        console.log('User:', user.name)
    } catch (error) {
        console.log('Error:', error.message)
    } finally {
        console.log('Request completed')
    }
}

getUser()
// Output:
// User: Budi
// Request completed
```

**Multiple Operations:**

```javascript
async function processOrder() {
    try {
        console.log('Processing order...')
        
        let user = await validateUser()
        console.log('User validated')
        
        let payment = await processPayment(user.id)
        console.log('Payment processed')
        
        let shipment = await scheduleShipment(payment.orderId)
        console.log('Shipment scheduled')
        
        return 'Order completed'
        
    } catch (error) {
        console.log('Order failed:', error.message)
        // Rollback atau cleanup
        await cancelOrder()
    } finally {
        console.log('Process finished')
    }
}
```

**Nested Try-Catch:**

```javascript
async function complexOperation() {
    try {
        let user = await getUser(1)
        
        try {
            let posts = await getUserPosts(user.id)
            console.log('Posts loaded')
        } catch (error) {
            console.log('Failed to load posts:', error)
            // Tetap lanjut walaupun posts gagal
        }
        
        let profile = await getUserProfile(user.id)
        console.log('Profile loaded')
        
    } catch (error) {
        console.log('Fatal error:', error)
    }
}
```

## Promise Methods

### Promise.all

Menjalankan beberapa Promise secara bersamaan dan tunggu sampai semua selesai.

**Sintaks:**

```javascript
Promise.all([promise1, promise2, promise3])
```

**Karakteristik:**
- Semua Promise jalan bersamaan (parallel)
- Return array hasil sesuai urutan
- Kalau satu gagal, semua dianggap gagal

**Contoh:**

```javascript
function fetchUser() {
    return new Promise((resolve) => {
        setTimeout(() => resolve('User data'), 1000)
    })
}

function fetchPosts() {
    return new Promise((resolve) => {
        setTimeout(() => resolve('Posts data'), 1500)
    })
}

function fetchComments() {
    return new Promise((resolve) => {
        setTimeout(() => resolve('Comments data'), 800)
    })
}

// Tanpa Promise.all (sequential - 3.3 detik total)
async function getData1() {
    let user = await fetchUser()        // 1 detik
    let posts = await fetchPosts()      // 1.5 detik
    let comments = await fetchComments() // 0.8 detik
    console.log(user, posts, comments)
}

// Dengan Promise.all (parallel - 1.5 detik total!)
async function getData2() {
    let [user, posts, comments] = await Promise.all([
        fetchUser(),
        fetchPosts(),
        fetchComments()
    ])
    console.log(user, posts, comments)
}

getData2()
// Output: User data Posts data Comments data
```

**Contoh dengan Error:**

```javascript
let promise1 = Promise.resolve('Success 1')
let promise2 = Promise.reject('Error!')
let promise3 = Promise.resolve('Success 3')

Promise.all([promise1, promise2, promise3])
    .then((results) => {
        console.log(results)
    })
    .catch((error) => {
        console.log('One failed:', error)  // "One failed: Error!"
    })
```

**Contoh Praktis (Load Multiple APIs):**

```javascript
async function loadDashboard() {
    try {
        let [users, products, orders] = await Promise.all([
            fetch('/api/users').then(r => r.json()),
            fetch('/api/products').then(r => r.json()),
            fetch('/api/orders').then(r => r.json())
        ])
        
        console.log('Users:', users.length)
        console.log('Products:', products.length)
        console.log('Orders:', orders.length)
    } catch (error) {
        console.log('Failed to load dashboard:', error)
    }
}
```

### Promise.race

Return Promise pertama yang selesai (entah resolve atau reject).

**Sintaks:**

```javascript
Promise.race([promise1, promise2, promise3])
```

**Contoh:**

```javascript
let promise1 = new Promise((resolve) => {
    setTimeout(() => resolve('Fast'), 1000)
})

let promise2 = new Promise((resolve) => {
    setTimeout(() => resolve('Slow'), 3000)
})

Promise.race([promise1, promise2])
    .then((result) => {
        console.log('Winner:', result)  // "Winner: Fast"
    })
```

**Contoh Praktis (Timeout):**

```javascript
function fetchWithTimeout(url, timeout) {
    return Promise.race([
        fetch(url),
        new Promise((_, reject) => {
            setTimeout(() => reject(new Error('Timeout!')), timeout)
        })
    ])
}

// Fetch dengan timeout 5 detik
fetchWithTimeout('/api/data', 5000)
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.log('Error:', error.message))
```

### Promise.allSettled

Tunggu semua Promise selesai (entah resolve atau reject), return status semua Promise.

**Sintaks:**

```javascript
Promise.allSettled([promise1, promise2, promise3])
```

**Karakteristik:**
- Tidak peduli ada yang gagal
- Return array dengan status setiap Promise

**Contoh:**

```javascript
let promise1 = Promise.resolve('Success 1')
let promise2 = Promise.reject('Error!')
let promise3 = Promise.resolve('Success 3')

Promise.allSettled([promise1, promise2, promise3])
    .then((results) => {
        results.forEach((result, index) => {
            if (result.status === 'fulfilled') {
                console.log(`Promise ${index + 1}: Success -`, result.value)
            } else {
                console.log(`Promise ${index + 1}: Failed -`, result.reason)
            }
        })
    })

// Output:
// Promise 1: Success - Success 1
// Promise 2: Failed - Error!
// Promise 3: Success - Success 3
```

**Contoh Praktis:**

```javascript
async function uploadFiles(files) {
    let uploadPromises = files.map((file) => uploadFile(file))
    
    let results = await Promise.allSettled(uploadPromises)
    
    let successful = results.filter(r => r.status === 'fulfilled')
    let failed = results.filter(r => r.status === 'rejected')
    
    console.log(`Berhasil: ${successful.length}`)
    console.log(`Gagal: ${failed.length}`)
    
    return { successful, failed }
}
```

### Promise.any

Return Promise pertama yang berhasil (resolve). Kalau semua gagal, baru reject.

**Sintaks:**

```javascript
Promise.any([promise1, promise2, promise3])
```

**Contoh:**

```javascript
let promise1 = Promise.reject('Error 1')
let promise2 = new Promise((resolve) => {
    setTimeout(() => resolve('Success!'), 1000)
})
let promise3 = Promise.reject('Error 3')

Promise.any([promise1, promise2, promise3])
    .then((result) => {
        console.log('First success:', result)  // "First success: Success!"
    })
    .catch((error) => {
        console.log('All failed:', error)
    })
```

**Contoh Praktis (Load from Multiple Servers):**

```javascript
async function loadFromMirrors(file) {
    return Promise.any([
        fetch(`https://server1.com/${file}`),
        fetch(`https://server2.com/${file}`),
        fetch(`https://server3.com/${file}`)
    ])
    .then((response) => response.json())
    .then((data) => {
        console.log('Data loaded from fastest server')
        return data
    })
    .catch((error) => {
        console.log('All servers failed')
    })
}
```

## Fetch API

Fetch API adalah cara modern untuk melakukan HTTP request, return Promise.

**Sintaks Dasar:**

```javascript
fetch(url, options)
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.log(error))
```

### GET Request

```javascript
// Basic GET
fetch('https://api.example.com/users')
    .then((response) => {
        if (!response.ok) {
            throw new Error('HTTP error! status: ' + response.status)
        }
        return response.json()
    })
    .then((data) => {
        console.log('Users:', data)
    })
    .catch((error) => {
        console.log('Error:', error.message)
    })
```

**Dengan Async/Await:**

```javascript
async function getUsers() {
    try {
        let response = await fetch('https://api.example.com/users')
        
        if (!response.ok) {
            throw new Error('HTTP error! status: ' + response.status)
        }
        
        let data = await response.json()
        console.log('Users:', data)
        return data
        
    } catch (error) {
        console.log('Error:', error.message)
    }
}

getUsers()
```

### POST Request

```javascript
async function createUser(userData) {
    try {
        let response = await fetch('https://api.example.com/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        })
        
        if (!response.ok) {
            throw new Error('Failed to create user')
        }
        
        let newUser = await response.json()
        console.log('User created:', newUser)
        return newUser
        
    } catch (error) {
        console.log('Error:', error.message)
    }
}

// Pakai
createUser({
    name: 'Budi',
    email: 'budi@email.com'
})
```

### PUT Request

```javascript
async function updateUser(userId, userData) {
    try {
        let response = await fetch(`https://api.example.com/users/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        })
        
        let updatedUser = await response.json()
        console.log('User updated:', updatedUser)
        return updatedUser
        
    } catch (error) {
        console.log('Error:', error.message)
    }
}
```

### DELETE Request

```javascript
async function deleteUser(userId) {
    try {
        let response = await fetch(`https://api.example.com/users/${userId}`, {
            method: 'DELETE'
        })
        
        if (response.ok) {
            console.log('User deleted successfully')
        }
    } catch (error) {
        console.log('Error:', error.message)
    }
}
```

### Fetch dengan Headers

```javascript
async function fetchWithAuth() {
    try {
        let response = await fetch('https://api.example.com/protected', {
            headers: {
                'Authorization': 'Bearer your-token-here',
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        })
        
        let data = await response.json()
        return data
        
    } catch (error) {
        console.log('Error:', error.message)
    }
}
```

### Fetch dengan Timeout

```javascript
async function fetchWithTimeout(url, timeout = 5000) {
    try {
        let response = await Promise.race([
            fetch(url),
            new Promise((_, reject) =>
                setTimeout(() => reject(new Error('Timeout')), timeout)
            )
        ])
        
        let data = await response.json()
        return data
        
    } catch (error) {
        console.log('Error:', error.message)
    }
}
```

## Best Practices

### 1. Pakai Async/Await untuk Readability

```javascript
// Bad - Promise chain panjang
function getData() {
    return fetchUser()
        .then((user) => {
            return fetchPosts(user.id)
                .then((posts) => {
                    return fetchComments(posts[0].id)
                })
        })
}

// Good - Async/await lebih clean
async function getData() {
    let user = await fetchUser()
    let posts = await fetchPosts(user.id)
    let comments = await fetchComments(posts[0].id)
    return comments
}
```

### 2. Selalu Handle Error

```javascript
// Bad - Tidak handle error
async function getData() {
    let data = await fetch('/api/data')
    return data.json()
}

// Good - Handle error dengan try-catch
async function getData() {
    try {
        let response = await fetch('/api/data')
        
        if (!response.ok) {
            throw new Error('Request failed')
        }
        
        return await response.json()
    } catch (error) {
        console.log('Error:', error.message)
        return null
    }
}
```

### 3. Gunakan Promise.all untuk Parallel Operations

```javascript
// Bad - Sequential (lambat)
async function loadData() {
    let users = await fetchUsers()       // 1 detik
    let products = await fetchProducts() // 1 detik
    let orders = await fetchOrders()     // 1 detik
    // Total: 3 detik
}

// Good - Parallel (cepat)
async function loadData() {
    let [users, products, orders] = await Promise.all([
        fetchUsers(),
        fetchProducts(),
        fetchOrders()
    ])
    // Total: 1 detik (yang paling lama)
}
```

### 4. Avoid Async dalam Loops

```javascript
// Bad - Async di loop (lambat, sequential)
async function processUsers(users) {
    for (let user of users) {
        await updateUser(user.id)  // Tunggu satu-satu
    }
}

// Good - Process semua bersamaan
async function processUsers(users) {
    await Promise.all(
        users.map((user) => updateUser(user.id))
    )
}
```

### 5. Cleanup dengan Finally

```javascript
async function fetchData() {
    showLoadingSpinner()
    
    try {
        let response = await fetch('/api/data')
        let data = await response.json()
        displayData(data)
    } catch (error) {
        showError(error.message)
    } finally {
        hideLoadingSpinner()  // Jalan apapun hasilnya
    }
}
```

### 6. Return Promises dari Async Function

```javascript
// Good - Return promise
async function getData() {
    return await fetch('/api/data')
        .then(r => r.json())
}

// Better - Langsung return promise (tidak perlu await)
async function getData() {
    return fetch('/api/data')
        .then(r => r.json())
}
```

### 7. Avoid Promise Constructor Anti-Pattern

```javascript
// Bad - Tidak perlu wrap promise
async function getData() {
    return new Promise((resolve, reject) => {
        fetch('/api/data')
            .then(r => r.json())
            .then(data => resolve(data))
            .catch(error => reject(error))
    })
}

// Good - Langsung return promise
async function getData() {
    let response = await fetch('/api/data')
    return response.json()
}
```

### 8. Nama Function Descriptive

```javascript
// Bad
async function get() { }
async function process() { }

// Good
async function fetchUserProfile() { }
async function updateUserSettings() { }
async function deleteUserAccount() { }
```

### 9. Handle Multiple Errors

```javascript
async function complexOperation() {
    try {
        let data = await riskyOperation1()
        return data
    } catch (error) {
        if (error.code === 'NETWORK_ERROR') {
            console.log('Network error, retrying...')
            return await retryOperation()
        } else if (error.code === 'AUTH_ERROR') {
            console.log('Authentication failed')
            redirectToLogin()
        } else {
            console.log('Unknown error:', error)
            throw error
        }
    }
}
```

### 10. Don't Mix Promise and Async/Await Styles

```javascript
// Bad - Mixing styles
async function getData() {
    let user = await getUser()
    return getUserPosts(user.id)
        .then((posts) => posts.length)  // Tidak konsisten
}

// Good - Konsisten pakai async/await
async function getData() {
    let user = await getUser()
    let posts = await getUserPosts(user.id)
    return posts.length
}
```

## Ringkasan

| Konsep | Kapan Pakai | Keuntungan |
|--------|-------------|------------|
| **Callback** | Simple async operations | Straightforward |
| **Promise** | Avoid callback hell | Better error handling, chainable |
| **Async/Await** | Modern async code | Clean syntax, easy to read |
| **Promise.all** | Parallel operations | Faster execution |
| **Promise.race** | Timeout, fastest response | Get first result |
| **Promise.allSettled** | Need all results | No fail-fast behavior |

**Flow Pembelajaran:**
1. Pahami Synchronous vs Asynchronous
2. Pelajari Callback (dan masalahnya)
3. Pakai Promise untuk solve callback hell
4. Upgrade ke Async/Await untuk clean code
5. Pakai Promise methods untuk advanced scenarios

***

## Referensi
- https://javascript.info/promise-basics
- https://javascript.info/async-await
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
- https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- https://www.freecodecamp.org/news/javascript-promises-explained/
