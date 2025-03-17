# Vue Js Guide

Memiliki konsep yang tidak beda jauh dari React. 

## Bentuk Fundamental dari vue | Options API

```JavaScript

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


***
# Abstract Note
***

## Halaman utama website disini
Tempat pengerjaan halaman awal pada vue adalah 'src/App.vue'

## Tahapan menerima komponent

'src/components'

Setelah membuat component, jangan lupa untuk export dan import ke halaman yang dituju!

contoh:

```javascript 
<script setup>

import HelloWorld from './components/HelloWorld.vue'
import Hello01 from '.'component/Hello01.vue

</script>
```

## Tahapan untuk menempelkan komponent ke HTML halaman

```
<template>

<Hello01/>

<template/>
```


## Package yang di export 

```

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

```
cd <your-project-name>

npm install

npm run dev
```

Ref: https://vuejs.org/guide/quick-start




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



***
# Reference 
***

- https://vuejs.org/guide/introduction.html
