# Vue Router 

adalah extension Vue yang dapat membantu kita untuk berpindah-pindah component sesuai dengan Route path (Link url kita)

Contoh Hasil Vue Router ada disini: https://play.vuejs.org/#eNqFVVtv2zYU/itn6gArmC05btEHTXXTFcWyYZeiLfYy7UGWji02EsmRlOPA8H/fIambnaRD4Fg61++c7yN9DJqc8eirDpKANVIoA0coFOYG30kJJ9gq0cBs3+Is412AEq1B1Xmi2L+ObpvX+3IpI5+b8aFqSJ+rjANErcbQp/v3RrTchLMXlDa7CuZBl07YUoONrCl/bQPT6np9i3UtbLPv0phenVm6L3rQRgm+W79vlULeIQaZmypJ484HxyN87xzRtq3rj+SE08mViX2dlOf7vuAnh/I3xu/AiDdZEGfB+mdBz3ArGkzj0f9sRr4hy5D2zr49ykvjvmdqeTmv9RfDe4i7uM6dxsNiaF9+l0+y+Ts2Qj3cMm3oa94Zfd0py4uBzYFPO6Br3ZPaGzpme9rtQGdxg2WUgOC6Y0PDG/jbjnL0vMAsnhEsQcU4UZaMbU/z8zC3x/PYsbcN/ueilaJW03nDoy1Y+VUkT+0nvHI9PVB6PJE8M44HN2iJ27yt+9q09ek+rFR1oZg0RM5FgmvboKlEqRP/BrATX4SDH171JgBD4CIvThXJVldhP7Y7J9DtxP4nxZKk+470cnFQVuseHh2TlTduWmMEh5uiZsUdSXPAcKlOH/hIZmfEjhODRtPaozNKjyiiGcqn75Ej0Pl3lMyHp2fFeMHnEB/SRia+ict6ep/GXBWV1UGHyGtgh5O1K0KvuC8T/duieoi6tLdvYUYg+rXTmKH3jLmeKoW0owLDI7h8IrnvfAKrIargxfQ/lA0LHjmr8w3W3X3w2dVMIGWchoH9ohEl1pFRrCE2fccsgCY/1Mh3piLjaknc+pujr3TOqedk0eSSrg/BiVU3WtY5dBYMks2CkRtrzoLKGKmTOG65vNtFtON4jLh5Fb2MlnFJJ2tijVA3i40S99rdV1ngNmtr31BQXOLeCFHrRS7Zcy0eBd68jl5H13HNNjFVjxkv8eBq94unMY0mQWzZ7mJIKwtWo/pTGkaCORs2p9+Z+1+dzagWB6BFhcXdE/av+uAhf1RI0+1xMpzJFWnOuz98/gMP9Dw4icW2puhvOD+hFnVrMfqwn1peEuxJnEP7i+OM8d0X/eFgkOt+KAt0FLIj8v03Rh/hvoxeTbaozUONOiq0/aGhX6w5aY1xn7cRqkSVwEoegMCyEl4sl8sf3d1H5RhfbATdKk0C10t5cHaZlyWBHSzUJeNUFtaQww/08Tenz65xSzf+NLJaTTuP5UcARVFMACSwpL9VVyE4/QesCg/V 


## Penggunaan

### Instalasi 

```npm install vue-router@4```

Install vue extension

### Router Js

Buat File baru didalam folder 'src' dengan nama 'router.js'

```HTML
// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import Readme from './components/README.vue'; // <== Sesuaikan sesuai kebutuhan
import Httml from './components/HTML.vue'; // <== Sesuaikan sesuai kebutuhan 

const routes = [
  { path: '/', component: Readme }, // <== Sesuaikan sesuai kebutuhan
  { path: '/html', component: Httml }, // <== Sesuaikan sesuai kebutuhan
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
```
Lakukan configurasi ulang pada code diatas, sesuai kebutuhan.

Konfigurasi bagian ini:
- 'Readme'
- 'Httml'


### Main js

Didalam folder 'src', lakukan configurasi pada file 'Main.js'

```Html
// src/main.js
import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'; // Import router


createApp(App).use(router).mount('#app') // Jalankan Route dan mount bersama CSS
```

Seharusnya configurasi diatas sudah cukup, tidak perlu ada tambahan lagi kecuali jika menggunakan ekstension lain.

## App js

Pada halaman utama, cukup beri configurasi didalam 'template'

```Html
<template>
<nav>
    <RouterLink to="/">Go to Home</RouterLink>
    <RouterLink to="/html">Go to HTML</RouterLink>
  </nav>
  <main>
    <RouterView />
  </main>
</template>
```

Yang dimana item didalam Nav adalah Link untuk berpindah komponent, sedangkan Item didalam Main adalah bagian yang akan menampilkan component.

### Catatan tambahan

Konsep pada 'App js' juga bisa diaplikasikan kepada component lainnnya juga, tampa ada konfigurasi lain.

Hanya saja "RouteView" tidak akan dipakai pada kompoennt lain, oleh karena itu selain file "Main.js" tidak perlu ada container 'Main' dan item didalamnya. 


### Penjelasan breakdown

*RouterLink* adalah Sebuah tools yang akan membantu kita melakukan perpindahan komponent. 


*RouterView* adalah tools yang akan menampilkan perpindahan komponent tersebut, semisal dari 'readme' ke 'HTML' komponent. 

## Reference
- https://router.vuejs.org/guide/ 
