# React JS

ReactJS adalah salah satu open source library Javascript yang digunakan untuk membuat user interface (UI) pada halaman website dan aplikasi mobile. ReactJS dibuat dan dikelola oleh Facebook (sekarang Meta) dan cukup populer di antara developer.

Beberapa contoh perusahaan besar yang menggunakan React adalah Netflix, Airbnb, dan Uber. 

ReactJS Library menggunakan konsep Virtual DOM (Document Object Model) yang membantu kita membuat representasi ringan dari DOM asli. Dengan Virtual DOM, proses update UI menjadi lebih efisien karena React hanya mengupdate bagian yang berubah saja, bukan seluruh halaman.

## Fitur Populer dari ReactJS

### JSX (JavaScript XML)
JSX adalah syntax extension untuk JavaScript yang memungkinkan kita menulis kode HTML di dalam JavaScript. Ini membuat kode lebih mudah dibaca dan ditulis.

### Virtual DOM
Representasi dari DOM yang lebih ringan, sehingga update UI bisa dilakukan lebih efisien. React membandingkan Virtual DOM dengan DOM asli dan hanya mengupdate bagian yang berubah.

### Component Based Architecture
Membantu kita untuk membuat komponen UI yang bisa digunakan kembali (reusable). Kamu bisa membuat komponen sekali dan menggunakannya di banyak tempat.

### One Way Data Binding
Menyajikan alur data yang simpel dan efisien untuk mengatur data di dalam aplikasi. Data mengalir dari parent ke child component.

### Declarative Programming
Memperbolehkan kita sebagai developer untuk mendeskripsikan bagaimana UI seharusnya terlihat, bukan bagaimana cara membuatnya. React akan mengurus sisanya.

ReactJS dapat dikombinasikan dengan banyak library dan framework seperti Next.js, Gatsby, dan lain-lain, yang menjadikan ReactJS semakin populer dan powerful.

## jQuery atau React?

Menurut pandangan umum di komunitas developer:

Kamu tidak harus mempelajari jQuery sebelum React. jQuery digunakan untuk manipulasi DOM secara manual, sedangkan React menggunakan pendekatan yang berbeda dengan Virtual DOM. Lebih baik langsung pelajari teknologi yang lebih modern seperti React, karena konsepnya lebih relevan dengan pengembangan web modern.

## Apa Itu Component React?

**Komponen React** adalah blok kode dasar dari aplikasi React. Komponen adalah potongan kode yang dapat kita gunakan kembali (reusable) yang mewakili bagian dari UI. Komponen dapat berupa element sederhana seperti button, atau bentuk yang lebih complex seperti form lengkap dengan validasi.

### Manfaat Komponen React

**Modularitas**
Komponen React adalah bagian kecil yang terpisah dari keseluruhan UI. Ini sangat memudahkan kita untuk melakukan maintenance dan pengembangan kode ke depannya. Kalau ada bug, kita bisa langsung tahu di komponen mana masalahnya.

**Reusability (Dapat Digunakan Kembali)**
Sama seperti konsep function, kita bisa membuat satu komponen dan menggunakannya berkali-kali di berbagai tempat dalam aplikasi.

**Encapsulation (Enkapsulasi)**
Semua variabel dan state di dalam komponen hanya bisa diakses oleh komponen tersebut sendiri. Ini membuat kode lebih aman dan tidak akan mempengaruhi komponen lain.

### Dua Jenis Komponen

React memiliki dua jenis komponen:

1. **Function Component** (lebih modern dan direkomendasikan)
2. **Class Component** (cara lama, tapi masih banyak dipakai)

## Variabel JSX 

Kamu bisa menyimpan JSX ke dalam variabel dan menggunakannya nanti:

```jsx
const buttonText = <button>Click Me!</button>;

function MyComponent() {
  return (
    <div>
      {buttonText}
    </div>
  );
}
```

## Comment pada JSX 

Cara menulis comment di JSX sedikit berbeda dari JavaScript biasa:

```jsx
// Ini adalah komentar satu baris tentang komponen

function MyComponent() {
  return (
    <div>
      {/* Ini adalah komentar multi-baris
          tentang isi komponen */}
      <h1>Hello, World!</h1>
    </div>
  );
}
```

## Aturan JSX 

Ada beberapa aturan penting yang harus diikuti saat menulis JSX:

### 1. Gunakan camelCase untuk Attribute HTML
Untuk beberapa attribute HTML, kita harus menggunakan "camelCase" sebagai penulisan.
- Contoh: `onClick`, `onChange`, `onSubmit`

### 2. className, Bukan class
Untuk penamaan attribute class, gunakan `className` bukan `class`
```jsx
<div className="container">Content</div>
```

### 3. Self-Closing Tag
Untuk single tag atau tag yang tidak memiliki konten, gunakan format self-closing dan harus memiliki penutup `/`
```jsx
<img src="#" />
<br />
<hr />
<input type="text" />
```

### 4. Inline Style dengan Object
Penulisan inline CSS harus menggunakan object JavaScript dengan properti camelCase:
```jsx
<p style={{ color: 'red', fontSize: '20px' }}>
  Teks merah dengan ukuran 20px
</p>
```

### 5. String dalam Curly Braces
Saat menulis JavaScript di dalam JSX, perhatikan tipe data yang digunakan:
```jsx
<button onClick={() => alert("Hello, World!")}>Click</button>
```

### 6. Harus Ada Container Parent
Perhatikan dalam membuat JSX, harus ada satu container parent yang membungkus semua element!
```jsx
// ❌ Salah - tidak ada parent container
function App() {
  return (
    <h1>Title</h1>
    <p>Paragraph</p>
  );
}

// ✅ Benar - ada div sebagai parent
function App() {
  return (
    <div>
      <h1>Title</h1>
      <p>Paragraph</p>
    </div>
  );
}

// ✅ Atau gunakan Fragment
function App() {
  return (
    <>
      <h1>Title</h1>
      <p>Paragraph</p>
    </>
  );
}
```

Sumber: https://legacy.reactjs.org/docs/introducing-jsx.html

## JSX (JavaScript XML)

JSX adalah extension syntax yang memungkinkan interaksi antara JavaScript dengan HTML. Kita bisa menambahkan kode JavaScript dengan HTML secara bersamaan.

Contoh sederhana:

```jsx
<p>{1 + 2}</p>
```

Hasilnya akan menampilkan angka 3 di browser.

Kamu juga bisa menggunakan variabel atau expression JavaScript apapun:

```jsx
const name = "Budi";
const greeting = <h1>Halo, {name}!</h1>;
```

## State 

State adalah konsep penting di React untuk menyimpan data yang bisa berubah. Data di state bisa kita panggil dan ubah kapan saja. Konsep `state` ini mirip seperti `property` pada class di pemrograman berorientasi objek.

### State di Class Component

```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }
  
  render() {
    return <h1>{this.state.count}</h1>;
  }
}
```

### State di Function Component (dengan Hooks)

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  
  return <h1>{count}</h1>;
}
```

## Event 

Event di dalam React adalah fungsi yang memungkinkan user berinteraksi dengan komponen yang kita buat. Untuk menanganinya, kita menggunakan event handler (method) untuk menerima interaksi.

Contoh event handler:

```jsx
<button onClick={() => {this.handleClick()}}>Tambah</button>
```

Event yang umum digunakan:
- `onClick` - saat element diklik
- `onChange` - saat input berubah
- `onSubmit` - saat form disubmit
- `onMouseEnter` - saat mouse masuk ke element
- `onMouseLeave` - saat mouse keluar dari element

## Mengakses State 

Cara menampilkan state ke dalam JSX:

### Di Class Component
```jsx
<h1>{this.state.count}</h1>
```

### Di Function Component
```jsx
<h1>{count}</h1>
```

## Memperbarui State  

### Di Class Component
```jsx
this.setState({ count: this.state.count + 1 })
```

Penjelasan:
- `setState` adalah method yang digunakan untuk melakukan perubahan state
- `count` adalah state yang dipilih untuk diubah
- `this.state.count` adalah cara mengakses nilai di dalam state
- Hasil dari operasi aritmatika tersebut akan disimpan ke state `count`

### Di Function Component (dengan Hooks)
```jsx
setCount(count + 1)
```

**Penting:** Jangan pernah ubah state secara langsung! Selalu gunakan `setState` (class) atau setter function (hooks).

```jsx
// ❌ Salah
this.state.count = 5;

// ✅ Benar
this.setState({ count: 5 });
```

---
# Bagian 2: Styling dan Component
---

## Membuat Style (Inline CSS) 

Ada beberapa cara untuk styling di React:

### 1. Inline Style dengan Object

```jsx
function App() {
  return (
    <p style={styles.colorP}>Ini berwarna merah</p>
  );
}

// Styles bisa ditempatkan di luar function
const styles = { 
  colorP: { color: 'red', fontSize: '40px' },
  colorH1: { color: 'blue', fontSize: '40px' },
};
```

### 2. CSS Module

```css
/* styles.module.css */
.colorP {
  color: red;
  font-size: 40px;
}
```

```jsx
import styles from './styles.module.css';

function App() {
  return <p className={styles.colorP}>Ini berwarna merah</p>;
}
```

## Membuat Banyak Component 

Kamu bisa membuat banyak komponen dan menggunakannya di komponen lain.

[Source Code](../code/jsPro/membuat-banyak-component)

## Method map() 

Method `map()` sangat berguna untuk merender array data menjadi list element JSX:

```jsx
function TodoList() {
  const todos = [
    { id: 1, name: 'apple', completed: false },
    { id: 2, name: 'mango', completed: false },
    { id: 3, name: 'banana', completed: false }
  ];

  return (
    <div>
      {todos.map((item) => {
        return <p key={item.id}>{item.name}</p>
      })}
    </div>
  );
}
```

**Penting:** Selalu tambahkan prop `key` yang unique saat menggunakan `map()`. Ini membantu React mengidentifikasi element mana yang berubah.

## Pemanggilan JSX 

Terdapat dua cara pemanggilan JSX:

### 1. JSX sebagai Variabel
```jsx
function App() {
  const abc = <p>Saya adalah JSX Variabel</p>;

  return (
    <div>
      {abc}
    </div>
  );
}
```

### 2. JSX sebagai Function/Component
```jsx
function App() {
  // Untuk render Element JSX, nama function wajib huruf besar di awal
  function Acc() {
    return <h1>Saya adalah JSX Function</h1>;
  }

  return (
    <div>
      <Acc />
    </div>
  );
}
```

**Aturan Penting:**
- Aturan di atas berlaku untuk Function Component
- Jika menggunakan Class Component, cara pemanggilannya: `{this.Acc()}`
- Method yang dipanggil sebagai JSX harus menggunakan huruf besar di awal (PascalCase)

## Conditional Rendering dengan Ternary Operator

Kamu bisa merender element secara kondisional menggunakan ternary operator `? :`:

```jsx
class PokeDetail extends React.Component {
  constructor(props) {
    super(props);
    this.state = { ch: true };
  }

  Acc() {
    return <h1>Saya adalah JSX Function</h1>;
  }

  render() {
    return (
      <div>
        {this.state.ch ? this.Acc() : <p>hi</p>}
      </div>
    );
  }
}
```

Penjelasan:
Ini adalah konsep sederhana conditional rendering. Kita menempatkan dua element, dan salah satu element akan di-render berdasarkan kondisi `this.state.ch`.
- Jika `this.state.ch` bernilai `true`, maka `this.Acc()` yang akan di-render
- Jika `false`, maka `<p>hi</p>` yang akan di-render

Cara lain untuk conditional rendering:

```jsx
// 1. Menggunakan && (AND operator)
{isLoggedIn && <UserProfile />}

// 2. Menggunakan if-else
function Greeting(props) {
  if (props.isLoggedIn) {
    return <h1>Welcome back!</h1>;
  }
  return <h1>Please sign in.</h1>;
}
```

---
# Bagian 3: Cheatsheet dan Best Practices
---

## Cheatsheet 

### Menambahkan Variabel JSX

```jsx
// Single line
const csx = <p>Ini adalah p</p>;

// Multi line
const csx = (
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
  </ul>
);
```

### Menambahkan Comment 

```jsx
const csx = (
  <ul>
    <li>Item 1</li>
    {/* Ini adalah comment */}
    <li>Item 2</li>
  </ul>
);
```

Ref: https://forum.freecodecamp.org/t/freecodecamp-challenge-guide-add-comments-in-jsx/301376

### Membuat Component 

**Komponen React** adalah blok kode dasar dari aplikasi React. Komponen adalah potongan kode yang dapat kita gunakan kembali yang mewakili bagian dari UI.

### Function Component (Modern Way)

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

### Class Component (Traditional Way)

```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

### Render Component ke DOM

Menimpa element lama dengan element dari React:

```jsx
import React from 'react';
import ReactDOM from 'react-dom';

const element = <h1>Hello, world!</h1>;

// React 17 dan sebelumnya
ReactDOM.render(element, document.getElementById('root'));

// React 18 (cara baru)
import { createRoot } from 'react-dom/client';
const root = createRoot(document.getElementById('root'));
root.render(element);
```

### Penempatan JSX 

JSX hanya ditempatkan pada bagian "return" di Function Component.

Untuk Class Component, JSX harus berada di dalam method "render()".

```jsx
import React from 'react';

const text = "Halo dunia ini";

// Function Component
function App() {
  return <h1>{text}</h1>;
}

// Class Component
class App extends React.Component {
  render() {
    return <h1>{text}</h1>;
  }
}

export default App;
```

Untuk menggunakan JavaScript expression di dalam JSX, gunakan curly braces:
```jsx
{namaVariabel}
{1 + 2}
{functionCall()}
```

### Mengatur Style dari JSX | Menambahkan Class

```jsx
import React from 'react';

function MyComponent() {
  return (
    <div className="my-class">
      <h1>Hello, world!</h1>
      <p>This is my component.</p>
    </div>
  );
}
```

**Penting:** Gunakan `className` bukan `class` karena `class` adalah reserved keyword di JavaScript.

### Aturan Penting untuk Render JSX

Pada render JSX **hanya diperbolehkan mengirim satu element parent**. Tidak boleh ada banyak container di level teratas!

```jsx
// ❌ Salah
function App() {
  return (
    <h1>Title</h1>
    <p>Content</p>
  );
}

// ✅ Benar
function App() {
  return (
    <div>
      <h1>Title</h1>
      <p>Content</p>
    </div>
  );
}

// ✅ Atau gunakan Fragment
function App() {
  return (
    <>
      <h1>Title</h1>
      <p>Content</p>
    </>
  );
}
```

### Self-Closing Tag

Untuk tag element yang tidak memiliki konten, gunakan self-closing tag:

```jsx
import React from 'react';

function MyComponent() {
  return (
    <div className="my-class">
      <h1>Hello, world!</h1>
      <br /> 
      <hr />
      <img src="image.jpg" alt="description" />
      <input type="text" />
      <p>This is my component.</p>
    </div>
  );
}
```

Yang awalnya `<br>` di HTML biasa, kita tulis menjadi `<br />` di JSX.

### Contoh Class Component Lengkap

```jsx
import React from 'react';

class App extends React.Component {
  render() {
    return (
      <h1>React Berjalan</h1>
    );
  }
}

export default App;
```

### Menulis Comment pada JSX

```jsx
function App() {
  return (
    <div>
      {/* Ini adalah comment di dalam JSX */}
      <h1>Hello</h1>
    </div>
  );
}
```

### Memasukkan Attribute DOM ke dalam JSX 

```jsx
import React from 'react';

class App extends React.Component {
  render() {
    return (
      <div> 
        <h1>Test Button</h1>
        <button onClick={() => {console.log('halo terminal')}}>
          Click me!
        </button>
      </div>
    );
  }
}
```

### Tool Penting pada React 

#### Event
Event adalah bentuk interaksi dari user dengan JSX. Contoh: `onClick`, `onChange`, `onSubmit`.

```jsx
<button onClick={handleClick}>Click me</button>
<input onChange={handleChange} />
<form onSubmit={handleSubmit}>
```

#### State
State adalah nilai yang dapat kita ubah berdasarkan adanya tindakan dari user atau logic aplikasi.

**Contoh Deklarasi State di Class Component:**

```jsx
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { name: 'Nama Ku' };
  }
}
```

**Contoh Penggunaan State di JSX:**

```jsx
import React from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { name: 'Nama Ku' };
  }

  render() {
    return (
      <h1>Selamat Datang {this.state.name}!</h1>
    );
  }
}

export default App;
```

---
# Life Cycle
---

Lifecycle adalah siklus hidup komponen React dari saat dibuat (mount) sampai dihapus (unmount).

## Lifecycle dengan Hooks (Function Component)

```jsx
import React, { useState, useEffect } from 'react';

function Counter({ setGCount, gCount }) {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  const decrement = () => {
    setCount(count - 1);
  };

  // componentDidMount - dijalankan saat component pertama kali di-render
  useEffect(() => {
    console.log('Component Counter() mounted!');
  }, []); // Array kosong = hanya run sekali saat mount

  // componentDidUpdate - dijalankan setiap kali count berubah
  useEffect(() => {
    setGCount(gCount + 1);
    console.log(`Nilai Count: ${count}`);
  }, [count]); // Run setiap kali count berubah

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
}

// ======================== Hit Component =============
function Hit() {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  const decrement = () => {
    setCount(count - 1);
  };

  // componentDidMount
  useEffect(() => {
    console.log('Component Hit() mounted!');
  }, []);

  // componentDidUpdate untuk count
  useEffect(() => {
    console.log(`Nilai Count: ${count}`);
  }, [count]);

  return (
    <div>
      <p>Hit: {count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
    </div>
  );
}

// ====================== App Component =============
function App() {
  const [gCount, setGCount] = useState(0);
  
  console.log(`gCount main container: ${gCount}`);
  
  // componentWillUnmount
  useEffect(() => {
    return () => {
      console.log('Component unmounted!');
    };
  }, []);

  return (
    <>
      <Counter setGCount={setGCount} gCount={gCount} />
      <h1>============ H1 ============</h1>
      <Hit />
    </>
  );
}

export default App;
```

## Tiga Fase Lifecycle

### 1. Mounting (Pemasangan)
Component sedang dibuat dan dimasukkan ke dalam DOM.

**Urutan method:**
- `constructor()`
- `render()`
- `componentDidMount()` (atau `useEffect` dengan empty dependency)

### 2. Updating (Pembaruan)
Component mengalami perubahan karena props atau state berubah.

**Urutan method:**
- `render()`
- `componentDidUpdate()` (atau `useEffect` dengan dependency)

### 3. Unmounting (Penghapusan)
Component akan dihapus dari DOM.

**Method:**
- `componentWillUnmount()` (atau `useEffect` cleanup function)

## useEffect Dependency Array

```jsx
// Run sekali saat mount
useEffect(() => {
  console.log('Mount');
}, []);

// Run setiap kali component render
useEffect(() => {
  console.log('Every render');
});

// Run saat count berubah
useEffect(() => {
  console.log('Count changed');
}, [count]);

// Cleanup saat unmount
useEffect(() => {
  return () => {
    console.log('Unmount');
  };
}, []);
```

---
# useMemo Hook
---

`useMemo` adalah React Hook yang digunakan untuk memoization (menyimpan hasil perhitungan) agar tidak perlu menghitung ulang jika dependencies tidak berubah.

```jsx
import { View, Button, Text } from 'react-native';
import { useState, useMemo } from 'react';

function Home() {
  console.log(`Component Home() telah di-render`);

  return (
    <View>
      <App />
    </View>
  );
}

function App() {
  const [count, setCount] = useState(0);
  console.log(`Component App telah terpanggil (Re-Render)`);
  
  // Gunakan useMemo agar Item tidak di-render ulang jika count tidak berubah
  const ItemOr = useMemo(() => Item(count), [count]);
  
  // Atau bisa seperti ini jika tidak ada dependency
  // const ItemOr = useMemo(() => Item(), [])

  return (
    <View>
      <Text>This is Counter App</Text>
      <Text>Count: {count}</Text>
      <Button onPress={() => setCount(count + 1)} title="Count Button" />
      {ItemOr}
    </View>
  );
}

function Item(count) {
  console.log(`Component count dikirim: ${count}`);
  console.log(`Component Item telah terpanggil (Re-Render)`);
  
  return (
    <View>
      <Text>This Content From Item: {count}</Text>
    </View>
  );
}

export default Home;
```

## Kapan Menggunakan useMemo?

`useMemo` adalah React Hook yang mirip dengan "Event Listener". Component atau perhitungan hanya akan dijalankan ulang jika terjadi perubahan pada dependency yang ditentukan.

**Gunakan useMemo ketika:**
- Ada perhitungan yang berat/kompleks
- Ingin mencegah re-render yang tidak perlu
- Membuat derived state dari state lain

**Jangan gunakan useMemo untuk:**
- Perhitungan sederhana
- Setiap function (berlebihan)
- Tanpa mengukur performance dulu

Ref: https://www.w3schools.com/react/react_usememo.asp

Contoh lebih lanjut: https://www.joshwcomeau.com/react/why-react-re-renders/

## Perbedaan useMemo dan useCallback

```jsx
// useMemo - memoize VALUE (hasil perhitungan)
const expensiveValue = useMemo(() => {
  return calculateExpensiveValue(input);
}, [input]);

// useCallback - memoize FUNCTION
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

---
# Catatan Tambahan dan Resources
---

## Catatan Tambahan

- [Membuat component sederhana](./project-react/single-comp.md)
- [Membuat banyak content](./react02.md)
- [Membuat element interaktif](./react03.md)
- [Instalasi React](./react-install.md)
- [Membuat formulir interaktif](./react-formulir.md)
- [Add, Update, List JSX](./project-react/add-update-list.md)
- [Context API](./project-react/context.md)
- [useEffect Hook](./project-react/useEffect.md)

## Contoh Project

- [Membuat button menambahkan element](./project-react/add-component.md)
- [Membuat konsep counter](./project-react/counter.md)
- [Membuat element muncul dan hilang](./project-react/add-delete.md)
- [Membuat Form lengkap dengan fitur](./project-react/form-react.md)
- [Todo App](./project-react/todo.md)

## Tips Penting untuk Pemula

1. **Mulai dengan Function Component**
   Function Component dengan Hooks adalah cara modern dan lebih mudah dipelajari.

2. **Pahami Props dan State**
   Props untuk passing data dari parent ke child, State untuk data yang bisa berubah.

3. **Gunakan React DevTools**
   Install React Developer Tools di browser untuk debugging.

4. **Breakdown ke Component Kecil**
   Jangan buat satu component besar, pecah menjadi component-component kecil yang reusable.

5. **Ikuti Naming Convention**
   - Component: PascalCase (UserProfile)
   - Function/Variable: camelCase (getUserData)
   - File: PascalCase untuk component, lowercase untuk lainnya

6. **Destructuring Props**
   ```jsx
   // ❌ Kurang bagus
   function User(props) {
     return <h1>{props.name}</h1>;
   }
   
   // ✅ Lebih bagus
   function User({ name }) {
     return <h1>{name}</h1>;
   }
   ```

7. **Key Prop di List**
   Selalu tambahkan unique key saat mapping array.

## Kesimpulan

React adalah library yang powerful untuk membuat UI yang interaktif dan dynamic. Kunci utamanya:

- **Component** = Building block aplikasi
- **Props** = Data yang dikirim dari parent ke child
- **State** = Data yang bisa berubah di dalam component
- **JSX** = Syntax untuk menulis HTML di JavaScript
- **Hooks** = Function untuk menggunakan fitur React (useState, useEffect, dll)
- **Virtual DOM** = Membuat update UI lebih efisien

Terus praktik dan buat project-project kecil untuk meningkatkan skill React kamu!

## Referensi

- https://www.niagahoster.co.id/blog/react-js-adalah/
- https://react.dev/ (Dokumentasi resmi React)
- https://legacy.reactjs.org/docs/getting-started.html
- https://www.freecodecamp.org/news/learn-react-js/
- https://react.dev/learn (React Beta Docs - sangat direkomendasikan)
