# Vue Js Guide

Memiliki konsep yang tidak beda jauh dari React. 

## Table of Content
- [Halaman Utama web](#halaman-utama-website-disini)
- [menerima komponent](#tahapan-menerima-komponent)
- [menerapkan komponent](#tahapan-untuk-menempelkan-komponent-ke-html-halaman)
- [export package](#package-yang-di-export)
- [menjalankan-vue](#menjalankan-vue)
- [declarative-rendering](#declarative-rendering)
- [attribute-binding](#attribute-binding)
- [event-listener](#event-listener)
- [form-binding](#form-binding)
- [contoh-form-binding](#contoh-form-binding)
- [conditional-rendering](#conditional-rendering)
- [List Rendering](#list-rendering)
- [computed property](#computed-property)
- [Lifecyle](#Lifecyle)
- [Components](#Components)
- [Props](#Props)
- [Emits](#Emits)
- [Slots](#Slots)
- [Router](#Router)



## Bentuk Fundamental dari vue | Options API

```html

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
**BreakDown code:**

- 'data()'    : adalah bagian dimana kita menyampan State 
- 'methods'   : adalah bagian dimana kita menuliskan event
- 'mounted()' : adalah dimana code akan dijalankan setiap ada perubahan state, dan awal halaman dimuat.
- '@click'    : adalah attribute fungsi yang akan menjalankan component jika user melakukan interaksi ( life cycle ).




<!--0000000000000000000000000000000000000000000000000000000000000000000000000 Abstract Note 0000000000000000000000000000000000000000000000000000000000000000000000000000000000 -->
***
# Abstract Note
***

## Halaman utama website disini
Tempat pengerjaan halaman awal pada vue adalah 'src/App.vue'

## Tahapan menerima komponent

'src/components'

Setelah membuat component, jangan lupa untuk export dan import ke halaman yang dituju!

contoh:

```html
<script setup>

import HelloWorld from './components/HelloWorld.vue'
import Hello01 from '.'component/Hello01.vue

</script>
```

## Tahapan untuk menempelkan komponent ke HTML halaman

```html
<template>

<Hello01/>

<template/>
```


## Package yang di export 

```html

<script setup>

const count = 'Saya komponen baru'

</script>





<template>

<h1>{{ count }}</h1>

</template>





<style scoped>

.read-the-docs {

  color: #888;

}

</style>
```


## Menjalankan vue 

```html
# Instalasi vue js
npm install -g @vue/cli

# Atau upgrade dengan ini
# npm update -g @vue/cli

# Buat Vue App
vue create hello-world 

# Atau gunakan versi GUI untuk build
# vue ui

cd <your-project-name>

npm run serve

# Atau ini
# npm run dev
```

Ref: https://vuejs.org/guide/quick-start

Panduan instalasi: https://cli.vuejs.org/guide/installation.html
- https://cli.vuejs.org/guide/creating-a-project.html#vue-cli-service-build

## Declarative Rendering

Adalah tindakan untuk membuat state dan melakukan perubahan kepada state tersebut.
Terdapat dua cara untuk melakukannya:
- Reactive() 
- ref()

**Reactive()**
```Js
import { reactive } from 'vue'

const counter = reactive({
  count: 0
})

console.log(counter.count) // 0
counter.count++
```
Breakdowcode:
- Memangil fungsi reactive
- Membuat sebuah array of object (tempat menyimpan state)
- 'count' adalah state
- 'counter.count' adalah cara menampilkan value didalam state
- 'counter.count++' adalah melakukan perubahan data

Reactive bekerja seperti halnya perintah 'map' dan 'set' didalam array.

**ref()**
```Js
import { ref } from 'vue'

const message = ref('Hello World!')

console.log(message.value) // "Hello World!"
message.value = 'Changed'

```
Breakdowncode:
- Panggil 'ref'
- buat sebuah variabel yang akan menjadi state
- 'message.value' adalah cara menampilkan state
- `message.value = 'Changed'` adalah cara melakukan perubahan state

## Attribute binding

Adalah metode mengunakan state ditempat lain.

```html
<script setup>
import { ref } from 'vue'

const titleClass = ref('title')
</script>

<template>
  <h1 :class="titleClass">Make me red ({{titleClass}})</h1> <!-- add dynamic class binding here -->
</template>

<style>
.title {
  color: red;
}
</style>
```
Breakdown:
- Gunakan 'ref'
- Dan buat state (titleClass)
- State bisa digunakan sebagai txt value atau sebagai judul yang merujuk ke class css
- state dengan value 'title' merujuk kepada class css.

Contoh penggunaan lainnya adalah 

```html
<div v-bind:id="dynamicId"></div>
```

Atau 

```html
<div :id="dynamicId"></div>
```

## Event listener

Adalah fungsi vue yang dimana dia akan memperhatikan interaksi yang diberikan oleh user. 
Sebagai contoh dibawah ini adalah, vue memperhatikan aksi 'click' yang dilakukan oleh user.

```html
<script setup>
import { ref } from 'vue'

const count = ref(0) // State 

function increment() { // blok fungsi 
  count.value++ 
}
</script>

<template>
  <!-- Fungsi Event Listener -->
  <button @click="increment">Tambah : {{ count }}</button>
</template>
```
Breakdown code:
- Panggil ref 
- tentukan state awal
- buat blok fungsi, yang dimana dia akan dijalankan setiap kali ada interaksi (Event Listener)
- Buat pembuka event listener (@click)


Pembuka event listener memiliki dua macam:


`<button v-on:click="increment">{{ count }}</button>`


atau bentuk shorthand


`<button @click="increment">{{ count }}</button>`

## Form Binding

adalah fungsi dimana vue akan menjadi perantara form dan code fungsi javascript kita.
terdapat dua cara untuk melakukan Form Binding:

### Cara lama ( Manual )

```<input :value="text" @input="onInput">```

Disini:
- ':value=text' -- adalah sebagai output (menampilkan value ke form)
- '@input'      -- adalah sebagai input (mengirim value ke state onInput)


```html
function onInput(e) {
  // a v-on handler receives the native DOM event
  // as the argument.
  text.value = e.target.value
}
```

Disini:
- 'text.value' adalah state yang akan ditampikan oleh form
- 'e.target.value' adalah nilai yang didapatkan form
- 'text' akan berubah setiap kali ada data baru dari fungsi onInput()


### Cara baru (Automatis)

```html
<input v-model="text">
```

adalah bentuk penyederhanaan dari proses diatas. 
Kita tidak perlu lagi membuat function yang harus menerima setiap interaksi didalam form.

'v-model' juga bisa digunakan untuk checkbox.


### Contoh Form binding

```html

<script setup>
import { ref } from 'vue'

const text = ref('') // adalah state

</script>

<template>
  <!-- v-model -->
  <input v-model="text" placeholder="Type here">
  <!-- menampilkan hasil state -->
  <p>{{ text }}</p>
</template>
```

Ref: https://vuejs.org/tutorial/#step-5


## Conditional Rendering

Disini element HTMl hanya akan dilakukan rendering oleh vue jika condition ( boolean ) adalah True. 

```html
<script setup>
import { ref } from 'vue'

const awesome = ref(true) // boolean state 

function toggle() {
  awesome.value = !awesome.value // timpa value bollean lama ke baru '!state'
}
</script>

<template>
  <button @click="toggle">Toggle</button> <!-- Event listener ke blok 'toggle'  -->
  <h1 v-if="awesome">Vue is awesome!</h1> <!-- Mengacu ke boolean state  -->
  <h1 v-else>Oh no 😢</h1> <!-- akan menjadi ini jika state adalah FALSE -->
</template>
```

Ref: https://vuejs.org/guide/essentials/conditional.html

## List Rendering

adalah cara untuk menampilkan data array kedalam halaman HTML.

Berikut adalah contoh Todo list sederhana:

```html
<script setup>
import { ref } from 'vue'

// give each todo a unique id
let id = 0 

const newTodo = ref('') // ini sebagai form state
const todos = ref([
  { id: id++, text: 'Learn HTML' },
  { id: id++, text: 'Learn JavaScript' },
  { id: id++, text: 'Learn Vue' }
])

function addTodo() { // ini adalah item yang terprint
  todos.value.push({ id: id++, text: newTodo.value }) // tambahkan value kedalam todos array
  newTodo.value = '' // bersihkan form state
}

function removeTodo(todo) { // ini adalah aksesoris delete tambahan
  todos.value = todos.value.filter((t) => t !== todo) // hapus item yang dipilih
  // filter, simpan semua item kecuali yang memiliki id sama dengan 't' atau 'todo'
}
</script>

<template>
  <!-- Form Start -->
  <form @submit.prevent="addTodo">
    <input v-model="newTodo" required placeholder="new todo">
    <button>Add Todo</button>
  </form>
  <!-- Form End -->

   <!-- Pack -->
  <ul>
    <!-- 1 pcs -->
    <li v-for="todo in todos" :key="todo.id">
      <p>
        {{ todo.text }}
      </p>
      <button @click="removeTodo(todo)">X</button>
    </li>
    <!-- 1 pcs -->
  </ul>
  <!-- Pack -->
</template>
```

## computed property 

disini kita akan membuat fungsi 'done' dimana pada todo list yang kita buat dapat menyembunyikan item yang 'done'

contoh code seperti ini:

```html

<script setup>
import { ref, computed } from 'vue'

let id = 0

const newTodo = ref('') // form state
const hideCompleted = ref(false) // indikator hide and show dari element tersebut
const todos = ref([
  { id: id++, text: 'Learn HTML', done: true },
  { id: id++, text: 'Learn JavaScript', done: true },
  { id: id++, text: 'Learn Vue', done: false }
])

const filteredTodos = computed(() => { 
  return hideCompleted.value ? todos.value.filter((t) => !t.done) : todos.value // True : False
  // Jika True, maka
  // tampilkan hasil filter dari 'todos.value.filter((t) => !t.done)'
  // nilai default adalah false 'todos.value'
})

function addTodo() {
  todos.value.push({ id: id++, text: newTodo.value, done: false }) // tambahkan item kedalamn state
  newTodo.value = '' // refresh form
}

function removeTodo(todo) {
  todos.value = todos.value.filter((t) => t !== todo) // hapus item sesuai dengan id yang dipilih
}
</script>

<template>
  <form @submit.prevent="addTodo">
    <input v-model="newTodo" required placeholder="new todo">
    <button>Add Todo</button>
  </form>
  <ul>
    <!-- 'li' akan diduplikasi sebanyak item di filteredTodos -->
    <li v-for="todo in filteredTodos" :key="todo.id">
      <input type="checkbox" v-model="todo.done">
      <span :class="{ done: todo.done }">{{ todo.text }}</span>
      <button @click="removeTodo(todo)">X</button>
    </li>
  </ul>
  <button @click="hideCompleted = !hideCompleted">
    {{ hideCompleted ? 'Show all' : 'Hide completed' }}
  </button>
</template>

<style>
.done {
  text-decoration: line-through;
}
</style>
```

## Lifecyle
### LifeCyle and template Refs
Adalah panduan untuk melakukan configurasi DOM secara manual tidak lagi otomatis seperti sebelumnya. 

```html

<script setup>
import { ref, onMounted } from 'vue' 

// Ambil alamat dengan 'Template Ref'
const pElementRef = ref(null)

onMounted(() => {
  // onMounted adalah kondisi status saat component Mounted didalam LifeCyle
  // ini adalah blok code yang akan di eksekusi jika statusnya adalah mounted
  pElementRef.value.textContent = 'mounted!' // timpa text
})

</script>

<template>
  <!-- Gunakan alamat tersebut di element HTML yang dituju -->
  <p ref="pElementRef">Hello</p>
</template>
```

 Kondisi component ( hooks  ):
 - onMounted
 - onUpdate 
 - onUnmounted

 ## Components

 salah satu hal yang akan menjadi media terbaik dari vue adalah components.
 Yaitu dimana kita akan membuat component dan akan dilekatkan kepada component lain.

 Contoh:
 ```html
<script setup>
// Panggil component lain
import ChildComp from './ChildComp.vue'
</script>

<template>
  <!-- render child component -->
   <!-- Tempel mereka disini -->
  <ChildComp />
</template>
 ```

 ## Props

 adalah metode mengirim data kepada component lain dari penerima.
 bentuknya seperti ini:
- Komponen A (Import / penerima / Parent component) adalah sebagai penerima komponen lain
- Komponen B (Export / pengirim / child component) adalah komponen lain yang akan melengkapi

Code Komponen A (Parent component)
```html
<script setup>
import { ref } from 'vue'
import ChildComp from './ChildComp.vue' // panggil komponen B

const greeting = ref('Hello from parent') // buat state
</script>

<template>
  <ChildComp :msg="greeting" /> <!-- Kirim data State ke komponen B -->
</template>
```


code komponen B (child component)
```html
<script setup>
const props = defineProps({ // Buat metode menerima data
  msg: String // 'msg' adalah alamat variabel yang digunakan untuk menerima
})
</script>

<template>
  <h2>{{ msg || 'No props passed yet' }}</h2> <!-- pasang variabel -->
</template>

```
Note:
- 'defineProps()' sudah built-in, oleh karena itu komponen B tidak perlu melakukan import


## Emits

adalah aksi parent (Komponent A) mengirim state ke komponent child (Komponent B)

```html
<script setup>
  // ========= Ini adalah komponent parent (Komponent A) =======
import { ref } from 'vue'
import ChildComp from './ChildComp.vue' // panggil komponent child

const childMsg = ref('No child msg yet') // Buat state
</script>

<template>
  <!-- panggil 'ChildComp' untuk menggambil state component child-->
   <!-- ChildComp hanya akan menampilkkan 'template' saja-->
  <ChildComp @response="(msg) => childMsg = msg" />
  <!-- 'hello from child' akan ditampikan dibawah sini (state awal di timpa)-->
  <p>{{ childMsg }}</p>
</template>
```


```html
<script setup>
   // ========= Ini adalah komponent child (Komponent B) =======
const emit = defineEmits(['response'])

emit('response', 'hello from child')
</script>

<template>
  <h2>Child component</h2>
</template>
```

## Slots

adalah metode parent component untuk mengirimkan dara ke child component.

Data dari parent akan dikirim ke element "slot", dan tidak akan mengangu element lainnya.

content didalam element "slot" akan ditimpa oleh data dari parent

```html
<template>
  <!-- Ini adalah child components -->
  <slot>Fallback content</slot>
  <p>
    hanya elemnt "slot" yang diubah
  </p>
</template>
```


dibawah ini adalah parent components

```html
<script setup>
  // Ini adalah parent component
import { ref } from 'vue'
import ChildComp from './ChildComp.vue'

const msg = ref('from parent')
</script>

<template>
  <ChildComp>Message: {{ msg }}</ChildComp>
</template>
```

## Router

Adalah Fungsi Untuk berpindah komponent, penjelasan lebih detail ada disini

[Route Vue Js](./vue/router.md)



<!-- 
// ===========================================================   Progress saat ini ================================================================
// Pastikan ini selalu di bagian bawah dari (abstract)
// 03/19/2025
// https://vuejs.org/tutorial/#step-14
// ===========================================================   Progress saat ini ================================================================
-->



<!--0000000000000000000000000000000000000000000000000000000000000000000000000 Glosariunm 0000000000000000000000000000000000000000000000000000000000000000000000000000000000 -->
***
# Glosarium | Kata kunci 
***

### Declarative Rendering | DR 

adalah perpanjangan dari vue yang membantu kita  untuk menulis HTML didalam file berebntuk JavaScript


### Reactivity

Vue akan secara otomatis melakukan tracking terhadap perubaha JavaScript 'state' dan melakukan perubahan kepada DOM dengan seksama.

### Single-File Components | SFL 

adalah sebuah format file yang mengabungkan antara: HTML, JavaScript, CSS dengan nama format adalah '*.vue'

```JavaScript
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

}

</style>
```

Format ini adalah bentuk rekomendasi dari Author ( official Vue )


## Latihan Vue
[Latihan Halaman Quiz vue](./latihan-bahasa/latihan-vue.md)


***
# Reference 
***

- https://vuejs.org/guide/introduction.html
