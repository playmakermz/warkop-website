# Vue.js Guide

Vue.js adalah framework JavaScript yang progressif untuk membangun user interface. Konsepnya tidak jauh berbeda dengan React, namun Vue lebih mudah dipelajari untuk pemula dengan dokumentasi yang sangat baik.

## Daftar Isi

### Dasar Vue.js
1. [Bentuk Fundamental Vue (Options API)](#bentuk-fundamental-vue--options-api)
2. [Setup dan Instalasi](#menjalankan-vue)
3. [Struktur Folder Vue](#struktur-folder-vue)

### Konsep Inti Vue
4. [Declarative Rendering](#declarative-rendering)
5. [Attribute Binding](#attribute-binding)
6. [Event Listener](#event-listener)
7. [Form Binding](#form-binding)
8. [Conditional Rendering](#conditional-rendering)
9. [List Rendering](#list-rendering)
10. [Computed Property](#computed-property)

### Lanjutan
11. [Lifecycle Hooks](#lifecycle)
12. [Components](#components)
13. [Props](#props)
14. [Emits](#emits)
15. [Slots](#slots)
16. [Router](#router)

### Referensi
17. [Glosarium](#glosarium--kata-kunci)
18. [Latihan Vue](#latihan-vue)
19. [Referensi](#referensi)

---

## Bentuk Fundamental Vue | Options API

Ini adalah struktur dasar dari komponen Vue menggunakan Options API. Options API adalah cara tradisional menulis komponen Vue yang masih banyak digunakan.

```vue
<script>
export default {
  // Properties returned from data() become reactive state
  // and will be exposed on `this`.
  data() {
    return {
      count: 0
    }
  },

  // Methods are functions that mutate state and trigger updates.
  // They can be bound as event handlers in templates.
  methods: {
    increment() {
      this.count++
    }
  },

  // Lifecycle hooks are called at different stages
  // of a component's lifecycle.
  // This function will be called when the component is mounted.
  mounted() {
    console.log(`The initial count is ${this.count}.`)
  }
}
</script>

<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```

### Penjelasan Kode:

| Bagian | Penjelasan |
|--------|------------|
| `data()` | Tempat menyimpan state (data reaktif) komponen. Semua properti di dalam `return` akan menjadi reaktif dan bisa diakses dengan `this.namaProperty` |
| `methods` | Tempat menulis fungsi atau event handler. Function di sini bisa dipanggil dari template menggunakan event listener seperti `@click` |
| `mounted()` | Lifecycle hook yang dijalankan ketika komponen sudah selesai di-mount ke DOM. Cocok untuk melakukan inisialisasi atau fetch data |
| `@click` | Event listener untuk menangkap klik user. Bisa juga ditulis `v-on:click`. Sintaks `@` adalah shorthand yang lebih singkat |

**Catatan:**  
Selain Options API, Vue juga punya Composition API (dengan `<script setup>`) yang lebih modern dan fleksibel. Di dokumen ini kita akan lebih banyak menggunakan Composition API.

---

## Menjalankan Vue

### Instalasi Vue CLI (Command Line Interface)

```bash
# Install Vue CLI secara global
npm install -g @vue/cli

# Atau jika sudah terinstall, upgrade ke versi terbaru
npm update -g @vue/cli

# Cek versi Vue CLI
vue --version
```

### Membuat Project Vue

**Cara 1: Menggunakan Vue CLI**
```bash
# Buat project baru
vue create hello-world

# Pilih preset yang diinginkan (default atau manual)
# Ikuti wizard yang muncul

# Masuk ke folder project
cd hello-world

# Jalankan development server
npm run serve
```

**Cara 2: Menggunakan Vue UI (Interface Visual)**
```bash
# Buka Vue UI
vue ui

# Browser akan terbuka dengan interface visual
# Ikuti langkah-langkah untuk membuat project
```

**Cara 3: Menggunakan Vite (Rekomendasi untuk project baru)**
```bash
# Buat project dengan Vite (lebih cepat)
npm create vue@latest

# Ikuti wizard
# Masuk ke folder project
cd <nama-project>

# Install dependencies
npm install

# Jalankan development server
npm run dev
```

**Referensi:**
- [Vue Quick Start](https://vuejs.org/guide/quick-start)
- [Vue CLI Documentation](https://cli.vuejs.org/guide/installation.html)
- [Creating a Project](https://cli.vuejs.org/guide/creating-a-project.html)

---

## Struktur Folder Vue

### Halaman Utama Website

File utama Vue berada di `src/App.vue`. Ini adalah root component yang akan menampung semua komponen lainnya.

**Struktur folder standar:**
```
my-vue-app/
├── node_modules/
├── public/
│   └── index.html
├── src/
│   ├── assets/          # File gambar, font, dll
│   ├── components/      # Komponen-komponen Vue
│   │   └── HelloWorld.vue
│   ├── App.vue          # Komponen utama
│   └── main.js          # Entry point aplikasi
├── package.json
└── vite.config.js       # Konfigurasi Vite
```

### Import dan Export Komponen

**Step 1: Buat komponen baru di `src/components/`**

File: `src/components/Hello01.vue`
```vue
<script setup>
const message = 'Saya komponen baru'
</script>

<template>
  <h1>{{ message }}</h1>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
```

**Step 2: Import komponen ke `App.vue`**

File: `src/App.vue`
```vue
<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Hello01 from './components/Hello01.vue'
</script>

<template>
  <div>
    <HelloWorld />
    <Hello01 />
  </div>
</template>
```

**Catatan Penting:**
- Setiap komponen harus di-import sebelum bisa digunakan
- Nama komponen dalam template harus sama dengan nama saat import
- Gunakan PascalCase untuk nama komponen (contoh: `HelloWorld`, bukan `helloworld`)
- Tag `<style scoped>` membuat CSS hanya berlaku untuk komponen tersebut

---

## Declarative Rendering

Declarative Rendering adalah cara Vue untuk membuat dan mengelola state (data reaktif). Ketika state berubah, tampilan akan otomatis update tanpa perlu manipulasi DOM manual.

Ada dua cara utama untuk membuat reactive state:

### 1. reactive()

`reactive()` cocok untuk membuat object yang reaktif.

```javascript
import { reactive } from 'vue'

const counter = reactive({
  count: 0,
  name: 'Counter App'
})

console.log(counter.count) // 0
counter.count++ // Mengubah nilai menjadi 1
console.log(counter.name) // Counter App
```

**Penjelasan:**
- `reactive()` mengubah object biasa menjadi reactive object
- Semua property dalam object menjadi reaktif
- Akses property dengan `counter.count`
- Ubah nilai langsung tanpa `.value`

**Kapan pakai reactive():**
- Ketika butuh banyak state yang terkait dalam satu object
- Mirip seperti `useState` di React tapi untuk object

### 2. ref()

`ref()` cocok untuk nilai primitif (string, number, boolean) atau jika ingin state yang lebih fleksibel.

```javascript
import { ref } from 'vue'

const message = ref('Hello World!')
const count = ref(0)
const isActive = ref(true)

console.log(message.value) // "Hello World!"
message.value = 'Changed' // Ubah nilai

console.log(count.value) // 0
count.value++ // Increment
```

**Penjelasan:**
- Harus pakai `.value` untuk akses atau ubah nilai dalam script
- Di template, Vue otomatis unwrap `.value`, jadi cukup `{{ message }}`
- Lebih fleksibel karena bisa dipakai untuk semua tipe data

**Perbandingan:**

```vue
<script setup>
import { ref, reactive } from 'vue'

// Dengan ref
const count = ref(0)
const name = ref('John')

// Dengan reactive
const state = reactive({
  count: 0,
  name: 'John'
})
</script>

<template>
  <!-- Pakai ref -->
  <p>{{ count }}</p>
  <p>{{ name }}</p>
  
  <!-- Pakai reactive -->
  <p>{{ state.count }}</p>
  <p>{{ state.name }}</p>
</template>
```

**Rekomendasi:**
- Gunakan `ref()` untuk nilai tunggal atau sebagai default choice
- Gunakan `reactive()` untuk object kompleks yang saling terkait

---

## Attribute Binding

Attribute binding memungkinkan kita menggunakan state sebagai nilai attribute HTML secara dinamis.

### Contoh Dasar

```vue
<script setup>
import { ref } from 'vue'

const titleClass = ref('title')
const linkUrl = ref('https://vuejs.org')
const imageUrl = ref('/logo.png')
const isDisabled = ref(false)
</script>

<template>
  <!-- Binding class -->
  <h1 :class="titleClass">Make me red</h1>
  
  <!-- Binding href -->
  <a :href="linkUrl">Vue Documentation</a>
  
  <!-- Binding src -->
  <img :src="imageUrl" alt="Logo">
  
  <!-- Binding boolean attribute -->
  <button :disabled="isDisabled">Click Me</button>
</template>

<style>
.title {
  color: red;
  font-size: 24px;
}
</style>
```

### Sintaks Binding

Ada dua cara menulis attribute binding:

**Cara lengkap:**
```vue
<div v-bind:id="dynamicId"></div>
<div v-bind:class="className"></div>
```

**Cara singkat (shorthand):**
```vue
<div :id="dynamicId"></div>
<div :class="className"></div>
```

**Rekomendasi:** Gunakan cara singkat `:` karena lebih clean dan umum dipakai.

### Binding Multiple Attributes

```vue
<script setup>
import { ref, reactive } from 'vue'

const buttonAttrs = reactive({
  id: 'submit-button',
  class: 'btn btn-primary',
  disabled: false
})
</script>

<template>
  <!-- Bind semua attributes sekaligus -->
  <button v-bind="buttonAttrs">Submit</button>
</template>
```

### Class dan Style Binding

**Class Binding (Object Syntax):**
```vue
<script setup>
import { ref } from 'vue'

const isActive = ref(true)
const hasError = ref(false)
</script>

<template>
  <!-- Class akan apply jika value adalah true -->
  <div :class="{ active: isActive, 'text-danger': hasError }">
    Dynamic Classes
  </div>
</template>
```

**Style Binding:**
```vue
<script setup>
import { ref } from 'vue'

const activeColor = ref('red')
const fontSize = ref(30)
</script>

<template>
  <p :style="{ color: activeColor, fontSize: fontSize + 'px' }">
    Styled Text
  </p>
</template>
```

---

## Event Listener

Event listener memungkinkan Vue menangkap interaksi user seperti click, input, submit, dll.

### Contoh Dasar

```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment() {
  count.value++
}

function decrement() {
  count.value--
}

function reset() {
  count.value = 0
}
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <button @click="increment">Tambah</button>
    <button @click="decrement">Kurang</button>
    <button @click="reset">Reset</button>
  </div>
</template>
```

### Sintaks Event Listener

Ada dua cara:

**Cara lengkap:**
```vue
<button v-on:click="increment">Click</button>
```

**Cara singkat (shorthand):**
```vue
<button @click="increment">Click</button>
```

### Event dengan Parameter

```vue
<script setup>
import { ref } from 'vue'

const message = ref('')

function greet(name) {
  message.value = `Hello, ${name}!`
}
</script>

<template>
  <button @click="greet('John')">Greet John</button>
  <button @click="greet('Alice')">Greet Alice</button>
  <p>{{ message }}</p>
</template>
```

### Mengakses Event Object

```vue
<script setup>
function handleClick(event) {
  console.log('Button clicked!')
  console.log('Event:', event)
  console.log('Target element:', event.target)
}
</script>

<template>
  <!-- Kirim event object secara eksplisit -->
  <button @click="handleClick($event)">Click Me</button>
</template>
```

### Event Modifiers

Vue menyediakan modifier untuk operasi event yang umum:

```vue
<template>
  <!-- Prevent default behavior -->
  <form @submit.prevent="handleSubmit">
    <button type="submit">Submit</button>
  </form>
  
  <!-- Stop event propagation -->
  <div @click.stop="handleClick">Click</div>
  
  <!-- Event hanya trigger sekali -->
  <button @click.once="handleOnce">Click Once</button>
  
  <!-- Chain modifiers -->
  <form @submit.prevent.stop="handleSubmit">
    <button type="submit">Submit</button>
  </form>
</template>
```

### Jenis Event Umum

| Event | Deskripsi | Contoh |
|-------|-----------|--------|
| `@click` | Ketika element diklik | Button, div, link |
| `@input` | Ketika input value berubah | Input field |
| `@change` | Ketika input selesai berubah | Input, select |
| `@submit` | Ketika form di-submit | Form |
| `@keyup` | Ketika key dilepas | Input field |
| `@keydown` | Ketika key ditekan | Input field |
| `@mouseenter` | Mouse masuk element | Hover effects |
| `@mouseleave` | Mouse keluar element | Hover effects |

---

## Form Binding

Form binding menghubungkan input form dengan state Vue secara two-way (dua arah). Ketika input berubah, state ikut berubah. Ketika state berubah, input ikut update.

### Cara Manual (v-bind + v-on)

Ini cara lama yang masih valid:

```vue
<script setup>
import { ref } from 'vue'

const text = ref('')

function onInput(event) {
  // v-on handler menerima native DOM event sebagai argument
  text.value = event.target.value
}
</script>

<template>
  <input 
    :value="text" 
    @input="onInput"
    placeholder="Type here"
  >
  <p>You typed: {{ text }}</p>
</template>
```

**Penjelasan:**
- `:value="text"` untuk output (menampilkan value ke form)
- `@input="onInput"` untuk input (menangkap perubahan dari user)
- `event.target.value` mengambil nilai dari input
- `text.value` diupdate setiap ada perubahan

### Cara Otomatis (v-model)

Ini cara modern yang lebih simpel:

```vue
<script setup>
import { ref } from 'vue'

const text = ref('')
</script>

<template>
  <input v-model="text" placeholder="Type here">
  <p>You typed: {{ text }}</p>
</template>
```

**Keuntungan v-model:**
- Lebih singkat dan clean
- Tidak perlu buat function untuk handle input
- Two-way binding otomatis

### v-model untuk Berbagai Input

**Text Input:**
```vue
<script setup>
import { ref } from 'vue'

const username = ref('')
const email = ref('')
</script>

<template>
  <input v-model="username" placeholder="Username">
  <input v-model="email" type="email" placeholder="Email">
</template>
```

**Textarea:**
```vue
<script setup>
import { ref } from 'vue'

const message = ref('')
</script>

<template>
  <textarea v-model="message" rows="4" placeholder="Your message"></textarea>
  <p>Message length: {{ message.length }}</p>
</template>
```

**Checkbox (Single):**
```vue
<script setup>
import { ref } from 'vue'

const checked = ref(false)
</script>

<template>
  <label>
    <input type="checkbox" v-model="checked">
    Accept terms
  </label>
  <p>Status: {{ checked ? 'Accepted' : 'Not accepted' }}</p>
</template>
```

**Checkbox (Multiple):**
```vue
<script setup>
import { ref } from 'vue'

const hobbies = ref([])
</script>

<template>
  <label><input type="checkbox" value="reading" v-model="hobbies"> Reading</label>
  <label><input type="checkbox" value="gaming" v-model="hobbies"> Gaming</label>
  <label><input type="checkbox" value="coding" v-model="hobbies"> Coding</label>
  <p>Selected: {{ hobbies }}</p>
</template>
```

**Radio Button:**
```vue
<script setup>
import { ref } from 'vue'

const gender = ref('')
</script>

<template>
  <label><input type="radio" value="male" v-model="gender"> Male</label>
  <label><input type="radio" value="female" v-model="gender"> Female</label>
  <p>Selected: {{ gender }}</p>
</template>
```

**Select Dropdown:**
```vue
<script setup>
import { ref } from 'vue'

const selected = ref('')
</script>

<template>
  <select v-model="selected">
    <option disabled value="">Please select</option>
    <option value="vue">Vue.js</option>
    <option value="react">React</option>
    <option value="angular">Angular</option>
  </select>
  <p>You selected: {{ selected }}</p>
</template>
```

### v-model Modifiers

**`.lazy`** - Update saat blur, bukan setiap keystroke:
```vue
<input v-model.lazy="text">
```

**`.number`** - Otomatis convert ke number:
```vue
<input v-model.number="age" type="number">
```

**`.trim`** - Otomatis trim whitespace:
```vue
<input v-model.trim="username">
```

---

## Conditional Rendering

Conditional rendering memungkinkan kita menampilkan atau menyembunyikan element HTML berdasarkan kondisi (boolean).

### v-if, v-else-if, v-else

```vue
<script setup>
import { ref } from 'vue'

const awesome = ref(true)

function toggle() {
  awesome.value = !awesome.value
}
</script>

<template>
  <button @click="toggle">Toggle</button>
  
  <h1 v-if="awesome">Vue is awesome!</h1>
  <h1 v-else>Oh no 😢</h1>
</template>
```

**Dengan multiple conditions:**

```vue
<script setup>
import { ref } from 'vue'

const score = ref(85)
</script>

<template>
  <div>
    <p v-if="score >= 90">Grade: A</p>
    <p v-else-if="score >= 80">Grade: B</p>
    <p v-else-if="score >= 70">Grade: C</p>
    <p v-else>Grade: D</p>
  </div>
</template>
```

### v-show

`v-show` mirip dengan `v-if`, tapi cara kerjanya berbeda:

```vue
<script setup>
import { ref } from 'vue'

const isVisible = ref(true)
</script>

<template>
  <button @click="isVisible = !isVisible">Toggle</button>
  <p v-show="isVisible">This paragraph can be shown or hidden</p>
</template>
```

### Perbedaan v-if vs v-show

| Aspek | v-if | v-show |
|-------|------|--------|
| **Cara kerja** | Element dihapus/ditambahkan dari DOM | Element tetap di DOM, hanya toggle CSS `display` |
| **Performance awal** | Lebih berat saat toggle | Lebih ringan saat toggle |
| **Performance render** | Lebih ringan jika jarang toggle | Lebih berat di awal render |
| **Kapan pakai** | Kondisi jarang berubah | Kondisi sering berubah |
| **Lifecycle hooks** | Trigger lifecycle hooks | Tidak trigger lifecycle hooks |

**Rekomendasi:**
- Gunakan `v-if` untuk kondisi yang jarang berubah
- Gunakan `v-show` untuk toggle yang sering (seperti modal, dropdown)

### Conditional dengan template

Jika ingin conditional untuk multiple elements tanpa wrapper:

```vue
<template>
  <template v-if="isLoggedIn">
    <h1>Welcome back!</h1>
    <p>Your dashboard</p>
    <button>Logout</button>
  </template>
  <template v-else>
    <h1>Please login</h1>
    <button>Login</button>
  </template>
</template>
```

**Referensi:** [Vue Conditional Rendering](https://vuejs.org/guide/essentials/conditional.html)

---

## List Rendering

List rendering memungkinkan kita menampilkan array data ke dalam HTML dengan menggunakan directive `v-for`.

### Contoh Sederhana

```vue
<script setup>
import { ref } from 'vue'

const items = ref(['Apple', 'Banana', 'Orange'])
</script>

<template>
  <ul>
    <li v-for="item in items" :key="item">
      {{ item }}
    </li>
  </ul>
</template>
```

### Todo List Lengkap

Berikut contoh Todo List dengan fitur add dan remove:

```vue
<script setup>
import { ref } from 'vue'

// Counter untuk generate unique ID
let id = 0

const newTodo = ref('') // State untuk form input
const todos = ref([
  { id: id++, text: 'Learn HTML' },
  { id: id++, text: 'Learn JavaScript' },
  { id: id++, text: 'Learn Vue' }
])

function addTodo() {
  // Tambah item baru ke array todos
  todos.value.push({ 
    id: id++, 
    text: newTodo.value 
  })
  // Bersihkan form input
  newTodo.value = ''
}

function removeTodo(todo) {
  // Filter: simpan semua item kecuali yang akan dihapus
  todos.value = todos.value.filter((t) => t !== todo)
}
</script>

<template>
  <!-- Form untuk add todo -->
  <form @submit.prevent="addTodo">
    <input 
      v-model="newTodo" 
      required 
      placeholder="What needs to be done?"
    >
    <button>Add Todo</button>
  </form>

  <!-- List todo items -->
  <ul>
    <li v-for="todo in todos" :key="todo.id">
      <span>{{ todo.text }}</span>
      <button @click="removeTodo(todo)">❌</button>
    </li>
  </ul>
  
  <p v-if="todos.length === 0">No todos yet. Add one above!</p>
</template>

<style scoped>
form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

input {
  flex: 1;
  padding: 8px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #eee;
}

button {
  padding: 5px 10px;
  cursor: pointer;
}
</style>
```

### Pentingnya :key

Attribute `:key` sangat penting dalam `v-for`:

```vue
<!-- BENAR - dengan :key -->
<li v-for="todo in todos" :key="todo.id">
  {{ todo.text }}
</li>

<!-- SALAH - tanpa :key -->
<li v-for="todo in todos">
  {{ todo.text }}
</li>
```

**Kenapa perlu :key?**
- Membantu Vue track setiap item dengan efisien
- Mencegah bug saat items diubah urutannya
- Meningkatkan performance rendering
- `:key` harus unique untuk setiap item

### v-for dengan Index

```vue
<script setup>
import { ref } from 'vue'

const items = ref(['Apple', 'Banana', 'Orange'])
</script>

<template>
  <ul>
    <li v-for="(item, index) in items" :key="index">
      {{ index + 1 }}. {{ item }}
    </li>
  </ul>
</template>
```

**Catatan:** Hindari pakai index sebagai `:key` jika urutan items bisa berubah. Lebih baik pakai ID yang unique.

### v-for dengan Object

```vue
<script setup>
import { reactive } from 'vue'

const user = reactive({
  name: 'John Doe',
  age: 30,
  email: 'john@example.com'
})
</script>

<template>
  <ul>
    <li v-for="(value, key) in user" :key="key">
      {{ key }}: {{ value }}
    </li>
  </ul>
</template>
```

---

## Computed Property

Computed property adalah properti yang nilainya dihitung berdasarkan state lain. Computed property di-cache dan hanya re-compute ketika dependency-nya berubah.

### Todo List dengan Filter

Contoh Todo List yang bisa hide/show completed items:

```vue
<script setup>
import { ref, computed } from 'vue'

let id = 0

const newTodo = ref('')
const hideCompleted = ref(false)
const todos = ref([
  { id: id++, text: 'Learn HTML', done: true },
  { id: id++, text: 'Learn JavaScript', done: true },
  { id: id++, text: 'Learn Vue', done: false }
])

// Computed property untuk filter todos
const filteredTodos = computed(() => {
  // Jika hideCompleted true, tampilkan hanya yang belum done
  // Jika false, tampilkan semua
  return hideCompleted.value 
    ? todos.value.filter((t) => !t.done) 
    : todos.value
})

function addTodo() {
  todos.value.push({ 
    id: id++, 
    text: newTodo.value, 
    done: false 
  })
  newTodo.value = ''
}

function removeTodo(todo) {
  todos.value = todos.value.filter((t) => t !== todo)
}
</script>

<template>
  <form @submit.prevent="addTodo">
    <input v-model="newTodo" required placeholder="new todo">
    <button>Add Todo</button>
  </form>
  
  <ul>
    <li v-for="todo in filteredTodos" :key="todo.id">
      <input type="checkbox" v-model="todo.done">
      <span :class="{ done: todo.done }">{{ todo.text }}</span>
      <button @click="removeTodo(todo)">❌</button>
    </li>
  </ul>
  
  <button @click="hideCompleted = !hideCompleted">
    {{ hideCompleted ? 'Show all' : 'Hide completed' }}
  </button>
</template>

<style>
.done {
  text-decoration: line-through;
  opacity: 0.5;
}
</style>
```

### Computed vs Methods

```vue
<script setup>
import { ref, computed } from 'vue'

const count = ref(1)

// Computed property (di-cache)
const doubleCount = computed(() => {
  console.log('Computed dipanggil')
  return count.value * 2
})

// Method (selalu run)
function doubleCountMethod() {
  console.log('Method dipanggil')
  return count.value * 2
}
</script>

<template>
  <p>Count: {{ count }}</p>
  <p>Double (computed): {{ doubleCount }}</p>
  <p>Double (computed lagi): {{ doubleCount }}</p>
  <p>Double (method): {{ doubleCountMethod() }}</p>
  <p>Double (method lagi): {{ doubleCountMethod() }}</p>
  
  <button @click="count++">Increment</button>
</template>
```

**Output console:**
- Computed dipanggil hanya sekali (di-cache)
- Method dipanggil dua kali

**Kapan pakai computed:**
- Untuk kalkulasi yang kompleks atau expensive
- Ketika butuh caching
- Ketika nilai bergantung pada reactive state

**Kapan pakai method:**
- Untuk operasi yang butuh parameter
- Untuk operasi yang harus selalu run (tidak perlu cache)

---

## Lifecycle

Lifecycle hooks adalah function yang dipanggil pada tahap tertentu dalam hidup komponen Vue.

### Lifecycle Hooks dan Template Refs

Template refs memungkinkan kita mengakses DOM element secara langsung:

```vue
<script setup>
import { ref, onMounted } from 'vue'

// Buat reference untuk DOM element
const pElementRef = ref(null)

// onMounted dipanggil setelah component di-mount
onMounted(() => {
  // Sekarang kita bisa akses DOM element
  pElementRef.value.textContent = 'mounted!'
  console.log('Component sudah mounted')
})
</script>

<template>
  <!-- Hubungkan ref dengan element -->
  <p ref="pElementRef">Hello</p>
</template>
```

### Lifecycle Hooks Utama

```vue
<script setup>
import { 
  ref,
  onBeforeMount,
  onMounted,
  onBeforeUpdate,
  onUpdated,
  onBeforeUnmount,
  onUnmounted
} from 'vue'

const count = ref(0)

// Sebelum component di-mount
onBeforeMount(() => {
  console.log('1. Before Mount - Component belum di-render')
})

// Setelah component di-mount
onMounted(() => {
  console.log('2. Mounted - Component sudah di-render')
  // Tempat terbaik untuk:
  // - Fetch data dari API
  // - Setup event listeners
  // - Inisialisasi libraries third-party
})

// Sebelum component di-update (state berubah)
onBeforeUpdate(() => {
  console.log('3. Before Update - State akan berubah')
})

// Setelah component di-update
onUpdated(() => {
  console.log('4. Updated - State sudah berubah, DOM sudah update')
})

// Sebelum component di-unmount (dihapus)
onBeforeUnmount(() => {
  console.log('5. Before Unmount - Component akan dihapus')
  // Tempat terbaik untuk:
  // - Cleanup event listeners
  // - Clear timers/intervals
})

// Setelah component di-unmount
onUnmounted(() => {
  console.log('6. Unmounted - Component sudah dihapus')
})
</script>

<template>
  <button @click="count++">Count: {{ count }}</button>
</template>
```

### Lifecycle Flow

```
Creation Phase:
└─> onBeforeMount
    └─> onMounted

Update Phase (ketika state berubah):
└─> onBeforeUpdate
    └─> onUpdated

Destruction Phase:
└─> onBeforeUnmount
    └─> onUnmounted
```

### Contoh Praktis: Fetch Data

```vue
<script setup>
import { ref, onMounted } from 'vue'

const users = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users')
    users.value = await response.json()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="error">Error: {{ error }}</div>
  <ul v-else>
    <li v-for="user in users" :key="user.id">
      {{ user.name }}
    </li>
  </ul>
</template>
```

---

## Components

Components adalah building block utama dalam Vue. Kita bisa membuat komponen reusable dan menyusunnya menjadi aplikasi yang kompleks.

### Membuat dan Menggunakan Component

**File: `ChildComp.vue`**
```vue
<script setup>
import { ref } from 'vue'

const message = ref('Hello from Child Component!')
</script>

<template>
  <div class="child">
    <h2>{{ message }}</h2>
    <p>This is a reusable component</p>
  </div>
</template>

<style scoped>
.child {
  padding: 20px;
  border: 2px solid #42b983;
  border-radius: 8px;
}
</style>
```

**File: `App.vue` (Parent Component)**
```vue
<script setup>
// Import child component
import ChildComp from './components/ChildComp.vue'
</script>

<template>
  <div>
    <h1>Parent Component</h1>
    
    <!-- Render child component -->
    <ChildComp />
    
    <!-- Bisa render multiple kali -->
    <ChildComp />
    <ChildComp />
  </div>
</template>
```

### Keuntungan Components

- **Reusability**: Komponen bisa dipakai berulang kali
- **Maintainability**: Kode lebih terorganisir dan mudah di-maintain
- **Separation of Concerns**: Setiap komponen fokus pada tugasnya sendiri
- **Testability**: Lebih mudah untuk ditest secara terpisah

---

## Props

Props adalah cara parent component mengirim data ke child component. Props bersifat one-way data flow (dari parent ke child).

### Contoh Dasar Props

**File: `ChildComp.vue` (Child Component)**
```vue
<script setup>
// Define props yang akan diterima
const props = defineProps({
  msg: String,
  count: Number
})
</script>

<template>
  <div>
    <h2>{{ msg || 'No props passed yet' }}</h2>
    <p>Count: {{ count }}</p>
  </div>
</template>
```

**File: `App.vue` (Parent Component)**
```vue
<script setup>
import { ref } from 'vue'
import ChildComp from './components/ChildComp.vue'

const greeting = ref('Hello from parent')
const number = ref(42)
</script>

<template>
  <ChildComp :msg="greeting" :count="number" />
  
  <button @click="number++">Increment</button>
</template>
```

### Props dengan Validation

```vue
<script setup>
const props = defineProps({
  // Basic type check
  title: String,
  
  // Multiple possible types
  age: [Number, String],
  
  // Required prop
  name: {
    type: String,
    required: true
  },
  
  // Prop dengan default value
  isActive: {
    type: Boolean,
    default: false
  },
  
  // Object dengan default value
  user: {
    type: Object,
    default: () => ({ name: 'Guest' })
  },
  
  // Custom validator
  score: {
    type: Number,
    validator: (value) => {
      return value >= 0 && value <= 100
    }
  }
})
</script>

<template>
  <div>
    <h1>{{ title }}</h1>
    <p>Name: {{ name }}</p>
    <p>Age: {{ age }}</p>
    <p>Active: {{ isActive }}</p>
  </div>
</template>
```

### Props sebagai Reactive Data

Props adalah reactive. Ketika parent mengubah props, child otomatis update:

**Child Component:**
```vue
<script setup>
const props = defineProps({
  count: Number
})
</script>

<template>
  <p>Received count: {{ count }}</p>
</template>
```

**Parent Component:**
```vue
<script setup>
import { ref } from 'vue'
import ChildComp from './ChildComp.vue'

const count = ref(0)
</script>

<template>
  <ChildComp :count="count" />
  <button @click="count++">Increment</button>
</template>
```

### Catatan Penting

- **Jangan ubah props di child component** (read-only)
- Props bersifat one-way: parent → child
- Jika perlu ubah nilai, copy ke local state dulu atau emit event ke parent
- `defineProps()` adalah compiler macro, tidak perlu import

---

## Emits

Emits adalah cara child component berkomunikasi dengan parent component. Ini kebalikan dari Props (child → parent).

### Contoh Dasar Emits

**File: `ChildComp.vue` (Child Component)**
```vue
<script setup>
// Define events yang akan di-emit
const emit = defineEmits(['response'])

// Emit event dengan data
emit('response', 'hello from child')
</script>

<template>
  <h2>Child component</h2>
</template>
```

**File: `App.vue` (Parent Component)**
```vue
<script setup>
import { ref } from 'vue'
import ChildComp from './components/ChildComp.vue'

const childMsg = ref('No child msg yet')
</script>

<template>
  <!-- Listen to 'response' event dari child -->
  <ChildComp @response="(msg) => childMsg = msg" />
  
  <!-- Tampilkan pesan dari child -->
  <p>{{ childMsg }}</p>
</template>
```

### Emits dengan Event Handler Function

**Child Component:**
```vue
<script setup>
const emit = defineEmits(['increment', 'decrement'])

function handleIncrement() {
  emit('increment')
}

function handleDecrement() {
  emit('decrement')
}
</script>

<template>
  <div>
    <button @click="handleIncrement">+</button>
    <button @click="handleDecrement">-</button>
  </div>
</template>
```

**Parent Component:**
```vue
<script setup>
import { ref } from 'vue'
import Counter from './Counter.vue'

const count = ref(0)

function increment() {
  count.value++
}

function decrement() {
  count.value--
}
</script>

<template>
  <p>Count: {{ count }}</p>
  <Counter @increment="increment" @decrement="decrement" />
</template>
```

### Emits dengan Multiple Parameters

**Child:**
```vue
<script setup>
const emit = defineEmits(['submit'])

function handleSubmit() {
  const formData = {
    name: 'John',
    age: 30
  }
  
  // Kirim multiple parameters
  emit('submit', formData, 'success')
}
</script>

<template>
  <button @click="handleSubmit">Submit</button>
</template>
```

**Parent:**
```vue
<script setup>
function onSubmit(data, status) {
  console.log('Data:', data)
  console.log('Status:', status)
}
</script>

<template>
  <ChildForm @submit="onSubmit" />
</template>
```

### Emits Validation

```vue
<script setup>
const emit = defineEmits({
  // Basic validation
  submit: null,
  
  // Validation dengan function
  increment: (value) => {
    // Return true jika valid
    if (value > 0) {
      return true
    } else {
      console.warn('Increment value must be positive')
      return false
    }
  }
})

// Emit dengan validation
function handleClick() {
  emit('increment', 1) // Valid
  emit('increment', -1) // Invalid, akan warning
}
</script>
```

**Catatan:**
- `defineEmits()` adalah compiler macro, tidak perlu import
- Emits membuat komponen lebih reusable dan decoupled
- Parent tidak perlu tahu implementasi detail dari child

---

## Slots

Slots memungkinkan parent component mengirim konten (HTML/text) ke child component. Ini seperti "placeholder" di child yang akan diisi oleh parent.

### Contoh Dasar Slots

**File: `ChildComp.vue` (Child Component)**
```vue
<template>
  <div class="card">
    <h2>Card Title</h2>
    <!-- Slot akan diganti dengan konten dari parent -->
    <slot>Fallback content (jika parent tidak kirim apa-apa)</slot>
    <p>Footer text</p>
  </div>
</template>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 8px;
}
</style>
```

**File: `App.vue` (Parent Component)**
```vue
<script setup>
import ChildComp from './components/ChildComp.vue'
</script>

<template>
  <!-- Kirim konten melalui slot -->
  <ChildComp>
    <p>This content comes from parent!</p>
    <button>Click me</button>
  </ChildComp>
  
  <!-- Tanpa konten, akan tampil fallback -->
  <ChildComp />
</template>
```

**Output:**
```
Card Title
This content comes from parent!
[Button: Click me]
Footer text
```

### Named Slots

Untuk multiple slots dalam satu component:

**Child Component:**
```vue
<template>
  <div class="container">
    <header>
      <!-- Slot untuk header -->
      <slot name="header">Default Header</slot>
    </header>
    
    <main>
      <!-- Default slot (unnamed) -->
      <slot>Default Content</slot>
    </main>
    
    <footer>
      <!-- Slot untuk footer -->
      <slot name="footer">Default Footer</slot>
    </footer>
  </div>
</template>
```

**Parent Component:**
```vue
<script setup>
import ChildComp from './components/ChildComp.vue'
</script>

<template>
  <ChildComp>
    <!-- Kirim konten ke named slot dengan v-slot atau # -->
    <template #header>
      <h1>My Custom Header</h1>
    </template>
    
    <!-- Default slot (tanpa nama) -->
    <p>Main content goes here</p>
    
    <template #footer>
      <p>Custom Footer © 2025</p>
    </template>
  </ChildComp>
</template>
```

### Scoped Slots

Scoped slots memungkinkan child mengirim data ke parent melalui slot:

**Child Component:**
```vue
<script setup>
import { ref } from 'vue'

const items = ref([
  { id: 1, name: 'Apple', price: 100 },
  { id: 2, name: 'Banana', price: 50 },
  { id: 3, name: 'Orange', price: 80 }
])
</script>

<template>
  <ul>
    <li v-for="item in items" :key="item.id">
      <!-- Kirim item data ke parent melalui slot -->
      <slot :item="item" :index="item.id">
        {{ item.name }}
      </slot>
    </li>
  </ul>
</template>
```

**Parent Component:**
```vue
<script setup>
import ItemList from './ItemList.vue'
</script>

<template>
  <!-- Terima data dari child dan custom tampilan -->
  <ItemList v-slot="{ item, index }">
    <strong>{{ index }}.</strong> 
    {{ item.name }} - 
    <span style="color: green;">Rp {{ item.price }}</span>
  </ItemList>
</template>
```

### Kapan Pakai Slots

- **Basic Slot**: Ketika butuh component wrapper yang fleksibel
- **Named Slots**: Ketika butuh multiple insertion points
- **Scoped Slots**: Ketika parent butuh akses ke child data untuk custom rendering

**Contoh Use Case:**
- Modal/Dialog components
- Card/Panel components
- Layout components (header, sidebar, content)
- List components dengan custom item rendering

---

## Router

Vue Router adalah library official untuk routing di Vue. Router memungkinkan kita membuat Single Page Application (SPA) dengan multiple halaman/views.

### Instalasi Vue Router

```bash
npm install vue-router@4
```

### Setup Dasar Router

**File: `router/index.js`**
```javascript
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

**File: `main.js`**
```javascript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')
```

**File: `App.vue`**
```vue
<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
  </nav>
  
  <!-- View akan render di sini -->
  <RouterView />
</template>
```

### Navigasi Programmatic

```vue
<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function goToAbout() {
  router.push('/about')
}

function goBack() {
  router.back()
}
</script>

<template>
  <button @click="goToAbout">Go to About</button>
  <button @click="goBack">Go Back</button>
</template>
```

### Route Parameters

**Router setup:**
```javascript
{
  path: '/user/:id',
  name: 'User',
  component: User
}
```

**Component:**
```vue
<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()
const userId = computed(() => route.params.id)
</script>

<template>
  <p>User ID: {{ userId }}</p>
</template>
```

### Query Parameters

```vue
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

// URL: /search?q=vue&page=2
console.log(route.query.q) // 'vue'
console.log(route.query.page) // '2'
</script>
```

### Lazy Loading Routes

Untuk performance, load component hanya saat dibutuhkan:

```javascript
const routes = [
  {
    path: '/',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/about',
    component: () => import('../views/About.vue')
  }
]
```

**Dokumentasi Lengkap:**  
Untuk penjelasan lebih detail tentang Vue Router, lihat: [Route Vue Js](./vue/router.md)

---

## Glosarium | Kata Kunci

### Declarative Rendering

Adalah paradigma programming dimana kita mendeskripsikan "apa yang ingin ditampilkan" bukan "bagaimana cara menampilkannya". Vue menggunakan template syntax untuk menulis HTML di dalam JavaScript dengan cara yang deklaratif.

Contoh:
```vue
<template>
  <!-- Deklaratif: kita deklarasikan apa yang ingin ditampilkan -->
  <p>{{ message }}</p>
</template>
```

Vs imperative (manual):
```javascript
// Imperatif: kita harus tulis step by step cara manipulasi DOM
const p = document.createElement('p')
p.textContent = message
document.body.appendChild(p)
```

### Reactivity

Vue secara otomatis melakukan tracking terhadap perubahan JavaScript state dan mengupdate DOM dengan efisien. Ini yang disebut reactivity system.

Ketika state berubah → Vue tahu → DOM diupdate otomatis

```vue
<script setup>
import { ref } from 'vue'

const count = ref(0) // Reactive state

// Ketika count berubah, tampilan otomatis update
</script>

<template>
  <button @click="count++">{{ count }}</button>
</template>
```

### Single-File Components (SFC)

Adalah format file Vue yang menggabungkan HTML, JavaScript, dan CSS dalam satu file dengan ekstensi `.vue`.

```vue
<!-- Ini adalah Single-File Component -->
<script setup>
import { ref } from 'vue'
const count = ref(0)
</script>

<template>
  <button @click="count++">Count is: {{ count }}</button>
</template>

<style scoped>
button {
  font-weight: bold;
  color: blue;
}
</style>
```

**Keuntungan SFC:**
- Semua logic komponen dalam satu file
- Syntax highlighting dan autocomplete yang baik
- Scoped CSS (tidak conflict dengan komponen lain)
- Format rekomendasi official Vue

### Composition API

Cara baru (Vue 3) untuk menulis logic komponen menggunakan `<script setup>`. Lebih fleksibel dan mudah untuk compose logic.

```vue
<script setup>
// Composition API syntax
import { ref, computed } from 'vue'

const count = ref(0)
const doubled = computed(() => count.value * 2)

function increment() {
  count.value++
}
</script>
```

### Options API

Cara tradisional (Vue 2) untuk menulis komponen dengan object options.

```vue
<script>
export default {
  data() {
    return { count: 0 }
  },
  computed: {
    doubled() {
      return this.count * 2
    }
  },
  methods: {
    increment() {
      this.count++
    }
  }
}
</script>
```

---

## Latihan Vue

Untuk latihan dan praktik lebih lanjut, kamu bisa coba:

1. **Vue.js Official Tutorial**
   - [https://vuejs.org/tutorial/](https://vuejs.org/tutorial/)
   - Tutorial interaktif step-by-step

2. **Membuat Project Sederhana**
   - Todo List dengan localStorage
   - Weather App dengan API
   - Blog sederhana dengan routing

3. **Latihan Halaman**
   - [Latihan Quiz Vue](./latihan-bahasa/latihan-vue.md)

### Tips Belajar Vue

- Mulai dari basic: reactive state, event handling, conditional
- Praktik dengan membuat project kecil
- Baca dokumentasi official (sangat lengkap dan jelas)
- Join komunitas Vue Indonesia
- Ikuti Vue Mastery atau Vue School untuk tutorial advanced

---

## Referensi

### Dokumentasi Official
- [Vue.js Official Guide](https://vuejs.org/guide/introduction.html) - Panduan lengkap Vue.js
- [Vue.js API Reference](https://vuejs.org/api/) - Referensi API Vue
- [Vue Router](https://router.vuejs.org/) - Dokumentasi Vue Router
- [Pinia](https://pinia.vuejs.org/) - State management (pengganti Vuex)

### Tutorial & Course
- [Vue.js Tutorial](https://vuejs.org/tutorial/) - Tutorial interaktif official
- [Vue Mastery](https://www.vuemastery.com/) - Video courses (gratis & berbayar)
- [Vue School](https://vueschool.io/) - Premium Vue courses

### Komunitas
- [Vue.js Developers Indonesia](https://www.facebook.com/groups/vuejsindonesia/) - Facebook Group
- [Vue Discord](https://discord.com/invite/vue) - Discord Server
- [Vue Forum](https://forum.vuejs.org/) - Official Forum

### Tools & Ecosystem
- [Vite](https://vitejs.dev/) - Build tool modern untuk Vue
- [Nuxt.js](https://nuxt.com/) - Framework Vue untuk SSR/SSG
- [VueUse](https://vueuse.org/) - Collection of Vue Composition utilities
- [Vuetify](https://vuetifyjs.com/) - Material Design component library

### Artikel & Blog
- [Vue.js Blog](https://blog.vuejs.org/) - Official blog
- [Awesome Vue](https://github.com/vuejs/awesome-vue) - Curated list of Vue resources

---

**Progress Belajar:**  
Terakhir update: 19 Maret 2025  
Progress saat ini: [https://vuejs.org/tutorial/#step-14](https://vuejs.org/tutorial/#step-14)

---
