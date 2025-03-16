# Vue Js Guide

Memiliki konsep yang tidak beda jauh dari React. 

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


