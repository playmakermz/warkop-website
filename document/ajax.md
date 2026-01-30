# AJAX (Asynchronous JavaScript And XML)

## Daftar Isi
- [Apa itu AJAX](#apa-itu-ajax)
- [Kenapa Pakai AJAX](#kenapa-pakai-ajax)
- [Cara Kerja AJAX](#cara-kerja-ajax)
- [XMLHttpRequest](#xmlhttprequest)
  - [Membuat XMLHttpRequest Object](#membuat-xmlhttprequest-object)
  - [GET Request](#get-request)
  - [POST Request](#post-request)
  - [ReadyState dan Status](#readystate-dan-status)
  - [Response Types](#response-types)
- [Contoh Lengkap](#contoh-lengkap)
- [Error Handling](#error-handling)
- [Fetch API (Modern Alternative)](#fetch-api-modern-alternative)
- [Axios Library](#axios-library)
- [AJAX vs Fetch vs Axios](#ajax-vs-fetch-vs-axios)
- [Best Practices](#best-practices)

## Apa itu AJAX

AJAX (Asynchronous JavaScript And XML) bukan sebuah bahasa pemrograman, tapi sebuah teknik untuk membuat aplikasi web yang lebih interaktif dan responsif.

**Komponen AJAX:**
- **Asynchronous:** Proses berjalan di background tanpa block halaman
- **JavaScript:** Bahasa pemrograman untuk handle request/response
- **XML:** Format data (sekarang lebih sering pakai JSON)

**XML (Extensible Markup Language):**
Format untuk menyimpan dan mengirim data dari web server. Meskipun namanya XML, sekarang AJAX lebih sering pakai JSON karena lebih ringan dan mudah dipakai.

**Contoh XML:**

```xml
<user>
    <name>Budi</name>
    <age>25</age>
    <email>budi@email.com</email>
</user>
```

**Contoh JSON (Lebih Populer):**

```json
{
    "name": "Budi",
    "age": 25,
    "email": "budi@email.com"
}
```

## Kenapa Pakai AJAX

### Tanpa AJAX (Traditional Web)

```
User klik button → Full page refresh → Tunggu loading → Tampil hasil
```

**Masalah:**
- Seluruh halaman reload (lambat)
- User experience kurang smooth
- Boros bandwidth
- Loading spinner di seluruh halaman

**Contoh:**
Bayangkan kamu buka Facebook dan setiap kali klik "Like", seluruh halaman reload. Sangat tidak efisien!

### Dengan AJAX (Modern Web)

```
User klik button → Request di background → Halaman tetap jalan → Update bagian tertentu saja
```

**Keuntungan:**
- Halaman tidak reload
- Update hanya bagian yang perlu
- User tetap bisa scroll atau klik yang lain
- Lebih cepat dan smooth
- Hemat bandwidth

**Contoh:**
Facebook Like button, Twitter auto-refresh timeline, Google Maps panning, search suggestions saat kamu ngetik, dll.

### Kapan Pakai AJAX

**Good use cases:**
- Load data tanpa refresh (comments, posts)
- Form submission tanpa reload
- Auto-complete search
- Real-time updates (chat, notifications)
- Infinite scroll
- Filter dan sort data

**Not good for:**
- SEO-critical pages (search engines sulit index)
- Initial page load (pakai server-side rendering)
- Large file downloads

## Cara Kerja AJAX

**Flow AJAX:**

```
1. User Action (klik button, submit form, dll)
      ↓
2. JavaScript membuat XMLHttpRequest
      ↓
3. Request dikirim ke server (di background)
      ↓
4. Server memproses request
      ↓
5. Server kirim response (XML/JSON/HTML)
      ↓
6. JavaScript terima response
      ↓
7. JavaScript update DOM (halaman web)
```

**Visualisasi:**

```
┌─────────────┐                      ┌─────────────┐
│   Browser   │                      │   Server    │
│  (Client)   │                      │             │
└──────┬──────┘                      └──────┬──────┘
       │                                    │
       │  1. User klik button              │
       │                                    │
       │  2. XMLHttpRequest                │
       ├───────────────────────────────────>│
       │       (GET /api/users)            │
       │                                    │
       │                                    │  3. Process
       │                                    │
       │  4. Response (JSON data)          │
       │<───────────────────────────────────┤
       │                                    │
       │  5. Update DOM                    │
       │     (tampil di halaman)           │
       │                                    │
```

**Komponen Utama:**

1. **XMLHttpRequest Object:**  
   API berbentuk object untuk transfer data antara browser dan server

2. **HTML DOM:**  
   Saat browser load halaman, otomatis buat Document Object Model yang bisa kita manipulasi dengan JavaScript

## XMLHttpRequest

XMLHttpRequest (XHR) adalah API bawaan browser untuk melakukan HTTP request.

### Membuat XMLHttpRequest Object

**Sintaks:**

```javascript
let xhr = new XMLHttpRequest()
```

**Contoh:**

```javascript
// Cara lama (IE5/IE6)
var xhttp = new XMLHttpRequest()

// Cara modern
let xhr = new XMLHttpRequest()
const request = new XMLHttpRequest()
```

### GET Request

GET request digunakan untuk mengambil (retrieve) data dari server.

**Sintaks Dasar:**

```javascript
let xhr = new XMLHttpRequest()

// Setup request
xhr.open("GET", "url", async)

// Send request
xhr.send()
```

**Parameter open():**
- Method: "GET", "POST", "PUT", "DELETE", dll
- URL: Endpoint API atau file
- Async: true (asynchronous) atau false (synchronous)

**Contoh GET Request:**

```javascript
function getData() {
    let xhr = new XMLHttpRequest()
    
    // Event handler saat request selesai
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log('Data:', xhr.responseText)
        } else {
            console.log('Error:', xhr.status)
        }
    }
    
    // Setup dan kirim request
    xhr.open("GET", "https://api.example.com/users", true)
    xhr.send()
}

getData()
```

**Contoh Load Text File:**

```javascript
function loadContent() {
    let xhr = new XMLHttpRequest()
    
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("content").innerHTML = this.responseText
        }
    }
    
    xhr.open("GET", "content.txt", true)
    xhr.send()
}
```

**Contoh dengan Query Parameters:**

```javascript
function searchUsers(query) {
    let xhr = new XMLHttpRequest()
    
    xhr.onload = function() {
        if (xhr.status === 200) {
            let users = JSON.parse(xhr.responseText)
            displayUsers(users)
        }
    }
    
    // Tambah query params
    xhr.open("GET", `https://api.example.com/users?search=${query}`, true)
    xhr.send()
}

searchUsers("Budi")
```

### POST Request

POST request digunakan untuk mengirim data ke server (create atau update).

**Sintaks:**

```javascript
let xhr = new XMLHttpRequest()

xhr.open("POST", "url", true)

// Set header untuk JSON
xhr.setRequestHeader("Content-Type", "application/json")

// Send dengan data
xhr.send(data)
```

**Contoh POST JSON:**

```javascript
function createUser(userData) {
    let xhr = new XMLHttpRequest()
    
    xhr.onload = function() {
        if (xhr.status === 201) {
            console.log('User created:', xhr.responseText)
        } else {
            console.log('Failed:', xhr.status)
        }
    }
    
    xhr.open("POST", "https://api.example.com/users", true)
    xhr.setRequestHeader("Content-Type", "application/json")
    
    let data = JSON.stringify(userData)
    xhr.send(data)
}

// Pakai
createUser({
    name: "Budi",
    email: "budi@email.com",
    age: 25
})
```

**Contoh POST Form Data:**

```javascript
function submitForm() {
    let xhr = new XMLHttpRequest()
    
    xhr.onload = function() {
        if (xhr.status === 200) {
            alert('Form submitted!')
        }
    }
    
    xhr.open("POST", "https://api.example.com/submit", true)
    
    // FormData object
    let formData = new FormData()
    formData.append("name", "Budi")
    formData.append("email", "budi@email.com")
    
    xhr.send(formData)
}
```

**Contoh Upload File:**

```javascript
function uploadFile(file) {
    let xhr = new XMLHttpRequest()
    
    xhr.upload.addEventListener("progress", function(e) {
        if (e.lengthComputable) {
            let percent = (e.loaded / e.total) * 100
            console.log(`Upload: ${percent}%`)
        }
    })
    
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log('File uploaded!')
        }
    }
    
    xhr.open("POST", "https://api.example.com/upload", true)
    
    let formData = new FormData()
    formData.append("file", file)
    
    xhr.send(formData)
}
```

### ReadyState dan Status

**ReadyState Values:**

| Value | State | Description |
|-------|-------|-------------|
| 0 | UNSENT | XMLHttpRequest dibuat, tapi open() belum dipanggil |
| 1 | OPENED | open() sudah dipanggil |
| 2 | HEADERS_RECEIVED | send() sudah dipanggil, headers dan status sudah tersedia |
| 3 | LOADING | Downloading, responseText sudah punya data partial |
| 4 | DONE | Operasi selesai |

**HTTP Status Codes:**

**Success (2xx):**
- `200` - OK (request berhasil)
- `201` - Created (resource baru dibuat)
- `204` - No Content (berhasil tapi tidak ada data)

**Client Error (4xx):**
- `400` - Bad Request (request salah format)
- `401` - Unauthorized (tidak ada authentication)
- `403` - Forbidden (tidak ada permission)
- `404` - Not Found (resource tidak ditemukan)

**Server Error (5xx):**
- `500` - Internal Server Error (error di server)
- `502` - Bad Gateway (server tidak dapat dijangkau)
- `503` - Service Unavailable (server sedang down)

**Contoh Cek ReadyState dan Status:**

```javascript
let xhr = new XMLHttpRequest()

xhr.onreadystatechange = function() {
    console.log('ReadyState:', xhr.readyState)
    
    if (xhr.readyState == 4) {
        console.log('Status:', xhr.status)
        
        if (xhr.status == 200) {
            console.log('Success:', xhr.responseText)
        } else if (xhr.status == 404) {
            console.log('Not found')
        } else if (xhr.status == 500) {
            console.log('Server error')
        }
    }
}

xhr.open("GET", "https://api.example.com/data", true)
xhr.send()
```

**Event Handlers:**

```javascript
let xhr = new XMLHttpRequest()

// Cara lama (pakai onreadystatechange)
xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText)
    }
}

// Cara modern (pakai onload)
xhr.onload = function() {
    if (xhr.status === 200) {
        console.log(xhr.responseText)
    }
}

// Error events
xhr.onerror = function() {
    console.log('Network error')
}

xhr.ontimeout = function() {
    console.log('Request timeout')
}

xhr.onprogress = function(e) {
    console.log(`Progress: ${e.loaded}/${e.total}`)
}
```

### Response Types

**1. responseText (Default):**

```javascript
xhr.onload = function() {
    let text = xhr.responseText
    console.log(text)
}
```

**2. responseXML:**

```javascript
xhr.responseType = 'document'
xhr.onload = function() {
    let xml = xhr.responseXML
    let users = xml.getElementsByTagName('user')
}
```

**3. response (General):**

```javascript
xhr.responseType = 'json'
xhr.onload = function() {
    let data = xhr.response  // Sudah jadi object
    console.log(data.name)
}
```

**Response Type Options:**
- `""` - String (default)
- `"text"` - String
- `"json"` - JavaScript object (auto-parsed)
- `"document"` - XML Document
- `"blob"` - Binary data (untuk files)
- `"arraybuffer"` - Binary data (untuk processing)

## Contoh Lengkap

### Example 1: Load Content dari File

**HTML:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>AJAX Example</title>
</head>
<body>

<div id="content">
    <h2>XMLHttpRequest Demo</h2>
    <button onclick="loadContent()">Load Content</button>
</div>

<script>
function loadContent() {
    let xhr = new XMLHttpRequest()
    
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("content").innerHTML = this.responseText
        }
    }
    
    xhr.open("GET", "content.txt", true)
    xhr.send()
}
</script>

</body>
</html>
```

**content.txt:**

```
<h2>Content Loaded!</h2>
<p>Ini adalah content dari file eksternal yang di-load dengan AJAX.</p>
<p>Halaman tidak perlu reload!</p>
```

### Example 2: Fetch Users dari API

**HTML:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>User List</title>
    <style>
        .user-card {
            border: 1px solid #ddd;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .loading {
            color: #888;
        }
    </style>
</head>
<body>

<h2>User List</h2>
<button onclick="loadUsers()">Load Users</button>
<div id="users"></div>

<script>
function loadUsers() {
    let xhr = new XMLHttpRequest()
    let usersDiv = document.getElementById('users')
    
    usersDiv.innerHTML = '<p class="loading">Loading...</p>'
    
    xhr.onload = function() {
        if (xhr.status === 200) {
            let users = JSON.parse(xhr.responseText)
            displayUsers(users)
        } else {
            usersDiv.innerHTML = '<p>Error loading users</p>'
        }
    }
    
    xhr.onerror = function() {
        usersDiv.innerHTML = '<p>Network error</p>'
    }
    
    xhr.open("GET", "https://jsonplaceholder.typicode.com/users", true)
    xhr.send()
}

function displayUsers(users) {
    let html = ''
    
    users.forEach(user => {
        html += `
            <div class="user-card">
                <h3>${user.name}</h3>
                <p>Email: ${user.email}</p>
                <p>Phone: ${user.phone}</p>
            </div>
        `
    })
    
    document.getElementById('users').innerHTML = html
}
</script>

</body>
</html>
```

### Example 3: Form Submission

**HTML:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
</head>
<body>

<h2>Contact Form</h2>
<form id="contactForm">
    <input type="text" id="name" placeholder="Name" required><br><br>
    <input type="email" id="email" placeholder="Email" required><br><br>
    <textarea id="message" placeholder="Message" required></textarea><br><br>
    <button type="submit">Submit</button>
</form>

<div id="result"></div>

<script>
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault()
    
    let name = document.getElementById('name').value
    let email = document.getElementById('email').value
    let message = document.getElementById('message').value
    
    let xhr = new XMLHttpRequest()
    
    xhr.onload = function() {
        if (xhr.status === 200) {
            document.getElementById('result').innerHTML = 
                '<p style="color: green">Message sent successfully!</p>'
            document.getElementById('contactForm').reset()
        } else {
            document.getElementById('result').innerHTML = 
                '<p style="color: red">Failed to send message</p>'
        }
    }
    
    xhr.open("POST", "https://api.example.com/contact", true)
    xhr.setRequestHeader("Content-Type", "application/json")
    
    let data = JSON.stringify({
        name: name,
        email: email,
        message: message
    })
    
    xhr.send(data)
})
</script>

</body>
</html>
```

### Example 4: Search dengan Debounce

```html
<!DOCTYPE html>
<html>
<head>
    <title>Search Users</title>
</head>
<body>

<h2>Search Users</h2>
<input type="text" id="searchInput" placeholder="Search users...">
<div id="searchResults"></div>

<script>
let debounceTimer

document.getElementById('searchInput').addEventListener('input', function(e) {
    let query = e.target.value
    
    // Clear previous timer
    clearTimeout(debounceTimer)
    
    // Set new timer
    debounceTimer = setTimeout(() => {
        if (query.length > 2) {
            searchUsers(query)
        } else {
            document.getElementById('searchResults').innerHTML = ''
        }
    }, 500)  // Wait 500ms setelah user berhenti ngetik
})

function searchUsers(query) {
    let xhr = new XMLHttpRequest()
    
    xhr.onload = function() {
        if (xhr.status === 200) {
            let users = JSON.parse(xhr.responseText)
            displayResults(users)
        }
    }
    
    xhr.open("GET", `https://api.example.com/users?search=${query}`, true)
    xhr.send()
}

function displayResults(users) {
    let html = '<ul>'
    users.forEach(user => {
        html += `<li>${user.name} - ${user.email}</li>`
    })
    html += '</ul>'
    
    document.getElementById('searchResults').innerHTML = html
}
</script>

</body>
</html>
```

## Error Handling

Error handling yang baik sangat penting untuk user experience.

**Basic Error Handling:**

```javascript
let xhr = new XMLHttpRequest()

xhr.onload = function() {
    if (xhr.status === 200) {
        // Success
        console.log(xhr.responseText)
    } else {
        // HTTP error
        console.log('HTTP Error:', xhr.status, xhr.statusText)
    }
}

xhr.onerror = function() {
    // Network error
    console.log('Network error')
}

xhr.ontimeout = function() {
    // Timeout
    console.log('Request timeout')
}

xhr.open("GET", "https://api.example.com/data", true)
xhr.timeout = 5000  // 5 seconds timeout
xhr.send()
```

**Comprehensive Error Handling:**

```javascript
function makeRequest(url, method, data = null) {
    return new Promise((resolve, reject) => {
        let xhr = new XMLHttpRequest()
        
        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 300) {
                // Success (2xx)
                try {
                    let response = JSON.parse(xhr.responseText)
                    resolve(response)
                } catch (e) {
                    resolve(xhr.responseText)
                }
            } else if (xhr.status >= 400 && xhr.status < 500) {
                // Client error (4xx)
                reject({
                    type: 'client_error',
                    status: xhr.status,
                    message: xhr.statusText
                })
            } else if (xhr.status >= 500) {
                // Server error (5xx)
                reject({
                    type: 'server_error',
                    status: xhr.status,
                    message: 'Server error occurred'
                })
            }
        }
        
        xhr.onerror = function() {
            reject({
                type: 'network_error',
                message: 'Network connection failed'
            })
        }
        
        xhr.ontimeout = function() {
            reject({
                type: 'timeout',
                message: 'Request timeout'
            })
        }
        
        xhr.open(method, url, true)
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.timeout = 10000  // 10 seconds
        
        if (data) {
            xhr.send(JSON.stringify(data))
        } else {
            xhr.send()
        }
    })
}

// Pakai dengan error handling
makeRequest('https://api.example.com/users', 'GET')
    .then(data => {
        console.log('Success:', data)
    })
    .catch(error => {
        switch(error.type) {
            case 'network_error':
                alert('No internet connection')
                break
            case 'timeout':
                alert('Request took too long')
                break
            case 'client_error':
                if (error.status === 404) {
                    alert('Data not found')
                } else if (error.status === 401) {
                    alert('Please login first')
                }
                break
            case 'server_error':
                alert('Server error, please try again later')
                break
        }
    })
```

**Retry Logic:**

```javascript
function makeRequestWithRetry(url, maxRetries = 3) {
    return new Promise((resolve, reject) => {
        let retryCount = 0
        
        function attempt() {
            let xhr = new XMLHttpRequest()
            
            xhr.onload = function() {
                if (xhr.status === 200) {
                    resolve(JSON.parse(xhr.responseText))
                } else {
                    if (retryCount < maxRetries) {
                        retryCount++
                        console.log(`Retry ${retryCount}/${maxRetries}`)
                        setTimeout(attempt, 1000 * retryCount)  // Exponential backoff
                    } else {
                        reject('Max retries reached')
                    }
                }
            }
            
            xhr.onerror = function() {
                if (retryCount < maxRetries) {
                    retryCount++
                    setTimeout(attempt, 1000 * retryCount)
                } else {
                    reject('Network error after retries')
                }
            }
            
            xhr.open("GET", url, true)
            xhr.send()
        }
        
        attempt()
    })
}
```

## Fetch API (Modern Alternative)

Fetch API adalah cara modern untuk melakukan HTTP request, menggantikan XMLHttpRequest dengan sintaks yang lebih clean dan return Promise.

**Kenapa Fetch Lebih Baik:**
- Sintaks lebih clean (pakai Promise/Async-Await)
- Built-in JSON parsing
- Lebih mudah di-chain
- Support modern browsers

**Sintaks Dasar:**

```javascript
fetch(url, options)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
```

**Contoh GET Request:**

```javascript
// Fetch API
fetch('https://api.example.com/users')
    .then(response => {
        if (!response.ok) {
            throw new Error('HTTP error! status: ' + response.status)
        }
        return response.json()
    })
    .then(data => {
        console.log('Users:', data)
    })
    .catch(error => {
        console.log('Error:', error.message)
    })

// Dengan Async/Await (lebih clean!)
async function getUsers() {
    try {
        let response = await fetch('https://api.example.com/users')
        
        if (!response.ok) {
            throw new Error('HTTP error! status: ' + response.status)
        }
        
        let data = await response.json()
        console.log('Users:', data)
        
    } catch (error) {
        console.log('Error:', error.message)
    }
}
```

**Contoh POST Request:**

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
        
    } catch (error) {
        console.log('Error:', error.message)
    }
}

createUser({
    name: 'Budi',
    email: 'budi@email.com'
})
```

**Perbandingan XMLHttpRequest vs Fetch:**

```javascript
// XMLHttpRequest (Lama)
let xhr = new XMLHttpRequest()
xhr.onload = function() {
    if (xhr.status === 200) {
        let data = JSON.parse(xhr.responseText)
        console.log(data)
    }
}
xhr.open("GET", "https://api.example.com/users", true)
xhr.send()

// Fetch API (Modern)
fetch('https://api.example.com/users')
    .then(response => response.json())
    .then(data => console.log(data))

// Fetch dengan Async/Await (Paling Clean!)
async function getUsers() {
    let response = await fetch('https://api.example.com/users')
    let data = await response.json()
    console.log(data)
}
```

## Axios Library

Axios adalah library JavaScript populer untuk HTTP request, lebih powerful dari Fetch.

**Install Axios:**

```html
<!-- CDN -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

<!-- NPM -->
npm install axios
```

**Kenapa Axios:**
- Automatic JSON transformation
- Request/Response interceptors
- Cancel requests
- Timeout support
- Progress tracking
- Wide browser support (termasuk IE11)

**Contoh GET Request:**

```javascript
// GET request
axios.get('https://api.example.com/users')
    .then(response => {
        console.log('Users:', response.data)
    })
    .catch(error => {
        console.log('Error:', error.message)
    })

// Dengan Async/Await
async function getUsers() {
    try {
        let response = await axios.get('https://api.example.com/users')
        console.log('Users:', response.data)
    } catch (error) {
        console.log('Error:', error.message)
    }
}
```

**Contoh POST Request:**

```javascript
async function createUser(userData) {
    try {
        let response = await axios.post('https://api.example.com/users', userData)
        console.log('User created:', response.data)
    } catch (error) {
        if (error.response) {
            // Server responded with error status
            console.log('Error:', error.response.status, error.response.data)
        } else if (error.request) {
            // Request made but no response
            console.log('No response from server')
        } else {
            // Something else happened
            console.log('Error:', error.message)
        }
    }
}
```

**Axios Config:**

```javascript
// Global config
axios.defaults.baseURL = 'https://api.example.com'
axios.defaults.headers.common['Authorization'] = 'Bearer token123'
axios.defaults.timeout = 10000

// Request with custom config
axios.get('/users', {
    params: {
        page: 1,
        limit: 10
    },
    headers: {
        'Custom-Header': 'value'
    },
    timeout: 5000
})
```

**Interceptors:**

```javascript
// Request interceptor
axios.interceptors.request.use(
    config => {
        // Modify config before sending (add token, dll)
        config.headers.Authorization = 'Bearer ' + getToken()
        console.log('Request:', config.url)
        return config
    },
    error => {
        return Promise.reject(error)
    }
)

// Response interceptor
axios.interceptors.response.use(
    response => {
        // Modify response data
        console.log('Response:', response.status)
        return response
    },
    error => {
        // Global error handling
        if (error.response.status === 401) {
            redirectToLogin()
        }
        return Promise.reject(error)
    }
)
```

## AJAX vs Fetch vs Axios

| Feature | XMLHttpRequest | Fetch API | Axios |
|---------|---------------|-----------|-------|
| **Sintaks** | Verbose | Clean | Very Clean |
| **Promise** | ❌ Manual | ✓ Native | ✓ Native |
| **JSON Parsing** | Manual | Manual | ✓ Automatic |
| **Error Handling** | onreadystatechange | then/catch | then/catch |
| **Timeout** | ✓ xhr.timeout | ❌ Manual | ✓ Native |
| **Cancel Request** | ✓ xhr.abort() | ✓ AbortController | ✓ CancelToken |
| **Progress** | ✓ onprogress | ✓ Reader | ✓ onUploadProgress |
| **Interceptors** | ❌ | ❌ | ✓ |
| **Browser Support** | All | Modern | All (polyfill) |
| **Bundle Size** | Native | Native | ~15KB |

**Kapan Pakai Mana:**

**XMLHttpRequest:**
- Legacy browser support (IE9/IE10)
- Progress tracking penting
- Sudah familiar dengan API

**Fetch:**
- Modern browsers
- Native solution (no library)
- Simple requests
- Tidak butuh advanced features

**Axios:**
- Need interceptors
- Complex error handling
- Automatic retries
- Request/Response transformation
- Large applications

## Best Practices

### 1. Gunakan Async/Await

```javascript
// Bad - Callback hell
xhr.onload = function() {
    let data = JSON.parse(xhr.responseText)
    anotherRequest(data, function(result) {
        // Nested callback...
    })
}

// Good - Async/Await
async function getData() {
    let response = await fetch('/api/data')
    let data = await response.json()
    let result = await processData(data)
    return result
}
```

### 2. Handle Errors Properly

```javascript
// Bad - No error handling
fetch('/api/data')
    .then(response => response.json())

// Good - Comprehensive error handling
async function getData() {
    try {
        let response = await fetch('/api/data')
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
        }
        
        let data = await response.json()
        return data
        
    } catch (error) {
        console.error('Error:', error.message)
        showErrorToUser(error.message)
        return null
    }
}
```

### 3. Set Timeout

```javascript
// Dengan XMLHttpRequest
xhr.timeout = 10000  // 10 seconds

// Dengan Fetch (manual)
const controller = new AbortController()
const timeoutId = setTimeout(() => controller.abort(), 10000)

fetch('/api/data', { signal: controller.signal })
    .then(response => {
        clearTimeout(timeoutId)
        return response.json()
    })

// Dengan Axios (built-in)
axios.get('/api/data', { timeout: 10000 })
```

### 4. Show Loading State

```javascript
async function loadData() {
    let loadingEl = document.getElementById('loading')
    let contentEl = document.getElementById('content')
    
    try {
        loadingEl.style.display = 'block'
        contentEl.style.display = 'none'
        
        let response = await fetch('/api/data')
        let data = await response.json()
        
        contentEl.innerHTML = renderData(data)
        
    } catch (error) {
        contentEl.innerHTML = '<p>Error loading data</p>'
    } finally {
        loadingEl.style.display = 'none'
        contentEl.style.display = 'block'
    }
}
```

### 5. Debounce Search Requests

```javascript
let debounceTimer

function handleSearch(query) {
    clearTimeout(debounceTimer)
    
    debounceTimer = setTimeout(() => {
        if (query.length > 2) {
            fetchSearchResults(query)
        }
    }, 300)  // Wait 300ms after user stops typing
}

document.getElementById('search').addEventListener('input', (e) => {
    handleSearch(e.target.value)
})
```

### 6. Cache Responses

```javascript
let cache = {}

async function fetchWithCache(url) {
    // Check cache first
    if (cache[url]) {
        console.log('Using cached data')
        return cache[url]
    }
    
    // Fetch if not in cache
    let response = await fetch(url)
    let data = await response.json()
    
    // Store in cache
    cache[url] = data
    
    return data
}
```

### 7. Use AbortController untuk Cancel Request

```javascript
let controller = new AbortController()

async function fetchData() {
    try {
        let response = await fetch('/api/data', {
            signal: controller.signal
        })
        let data = await response.json()
        return data
    } catch (error) {
        if (error.name === 'AbortError') {
            console.log('Request cancelled')
        } else {
            console.log('Error:', error.message)
        }
    }
}

// Cancel request
function cancelRequest() {
    controller.abort()
    controller = new AbortController()  // Create new for next request
}
```

### 8. Validate Response

```javascript
async function fetchUser(userId) {
    try {
        let response = await fetch(`/api/users/${userId}`)
        
        if (!response.ok) {
            throw new Error('User not found')
        }
        
        let user = await response.json()
        
        // Validate response data
        if (!user.id || !user.name || !user.email) {
            throw new Error('Invalid user data')
        }
        
        return user
        
    } catch (error) {
        console.log('Error:', error.message)
        return null
    }
}
```

### 9. Use Request Headers Properly

```javascript
async function apiRequest(url, data) {
    let response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + getToken(),
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(data)
    })
    
    return response.json()
}
```

### 10. Centralize API Calls

```javascript
// api.js - Centralized API module
const API = {
    baseURL: 'https://api.example.com',
    
    async request(endpoint, options = {}) {
        try {
            let response = await fetch(this.baseURL + endpoint, {
                ...options,
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + getToken(),
                    ...options.headers
                }
            })
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`)
            }
            
            return await response.json()
        } catch (error) {
            console.error('API Error:', error.message)
            throw error
        }
    },
    
    get(endpoint) {
        return this.request(endpoint)
    },
    
    post(endpoint, data) {
        return this.request(endpoint, {
            method: 'POST',
            body: JSON.stringify(data)
        })
    },
    
    put(endpoint, data) {
        return this.request(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data)
        })
    },
    
    delete(endpoint) {
        return this.request(endpoint, {
            method: 'DELETE'
        })
    }
}

// Usage
API.get('/users')
    .then(users => console.log(users))

API.post('/users', { name: 'Budi', email: 'budi@email.com' })
    .then(user => console.log('Created:', user))
```

## Ringkasan

**AJAX memungkinkan:**
- Update halaman tanpa reload
- Request data di background
- Send data ke server asynchronous
- Aplikasi web lebih interaktif dan responsif

**Pilihan Teknologi:**

| Skenario | Rekomendasi |
|----------|-------------|
| Legacy support (IE9/IE10) | XMLHttpRequest |
| Simple modern app | Fetch API |
| Complex application | Axios |
| React/Vue/Angular | Axios atau Fetch |

**Flow Pembelajaran:**
1. Pahami konsep Synchronous vs Asynchronous
2. Pelajari XMLHttpRequest (fundamental)
3. Upgrade ke Fetch API (modern)
4. Pakai Axios untuk advanced features
5. Practice dengan real API

***

## Referensi
- https://www.freecodecamp.org/news/ajax-tutorial/
- https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX
- https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
- https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- https://axios-http.com/docs/intro
- https://javascript.info/xmlhttprequest
- https://javascript.info/fetch
