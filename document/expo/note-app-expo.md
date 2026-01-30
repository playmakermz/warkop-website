# Tutorial Membuat Aplikasi Note dengan Expo

## Daftar Isi

1. [Tujuan Project](#tujuan-project)
2. [Persiapan Awal](#persiapan-awal)
   - [Struktur Folder dan File](#struktur-folder-dan-file)
   - [Aturan CSS di React Native](#aturan-css-di-react-native)
3. [Membuat Component Dasar](#membuat-component-dasar)
   - [Custom Button Component](#custom-button-component)
   - [Custom Text Input Component](#custom-text-input-component)
   - [Home Component](#home-component)
   - [File Index Utama](#file-index-utama)
4. [Membuat Halaman Navigasi](#membuat-halaman-navigasi)
   - [Setup Folder Screen](#setup-folder-screen)
   - [Add Note Screen](#add-note-screen)
   - [Edit Note Screen](#edit-note-screen)
   - [Update Home Component](#update-home-component)
   - [Update Index dengan Navigation Logic](#update-index-dengan-navigation-logic)
5. [Implementasi Form Input](#implementasi-form-input)
6. [Finishing dan Source Code](#finishing-dan-source-code)
7. [Referensi Tambahan](#referensi-tambahan)

---

## Tujuan Project

Dalam tutorial ini, kita akan membuat aplikasi note sederhana mirip seperti Todo App. Aplikasi ini akan memiliki fitur:

- **Input data** baru
- **Membuat form** untuk menambah note
- **Menutup form** setelah selesai
- **Submit input** untuk menyimpan data
- **Menampilkan hasil** submit di list

---

## Persiapan Awal

### Struktur Folder dan File

Kita akan menggunakan Expo App yang berasal dari React template codespace. Berikut struktur folder yang akan kita buat:

```
/(tabs)
  └── index.tsx
  └── /components
      ├── Style.tsx
      ├── Home.tsx
      ├── customTextInput.tsx
      └── customButton.tsx
  └── /screens
      ├── addNote.tsx
      ├── editNote.tsx
      └── home.tsx
```

**Penjelasan File:**

- `Style.tsx` - File khusus untuk semua styling CSS. File ini hanya fokus pada style dan tidak menyentuh component lain
- `customButton.tsx` - Component button yang bisa dipakai ulang
- `customTextInput.tsx` - Component input field yang bisa dipakai ulang
- `Home.tsx` - Component untuk halaman utama
- `index.tsx` - File utama aplikasi yang mengelola state dan routing

### Aturan CSS di React Native

Sebelum mulai coding, penting untuk memahami aturan CSS di React Native:

**Perbedaan dengan CSS Web:**
- React Native tidak menggunakan file CSS terpisah seperti `.css` atau `.scss`
- Semua styling ditulis menggunakan JavaScript object

**Aturan Property:**
- Property seperti `backgroundColor` bisa digunakan pada container untuk mengatur warna latar belakang
- Container **tidak bisa** mengatur property `color` untuk text yang ada di dalamnya
- Oleh karena itu: gunakan `backgroundColor` untuk container, dan `color` untuk text/item di dalamnya

**Contoh:**
```javascript
// Benar
<View style={{ backgroundColor: 'blue' }}>
  <Text style={{ color: 'white' }}>Halo</Text>
</View>

// Salah - color di View tidak akan berpengaruh
<View style={{ color: 'white' }}>
  <Text>Halo</Text>
</View>
```

---

## Membuat Component Dasar

### Custom Button Component

Pertama, kita akan membuat component button yang bisa dipakai berulang kali dengan text dan function yang berbeda.

```javascript
// components/customButton.tsx

import React from 'react';
import { TouchableOpacity, Text } from 'react-native';
import { styles } from './Style';

function CustomButton({ text, onPress }) {
  return (
    <TouchableOpacity style={styles.button} onPress={onPress}>
      <Text style={styles.buttonText}>{text}</Text>
    </TouchableOpacity>
  );
}

export default CustomButton;
```

**Penjelasan:**
- Function `CustomButton` menerima 2 parameter:
  - `text` - Text yang akan ditampilkan di button
  - `onPress` - Function yang akan dijalankan saat button diklik
- Parameter ini dikirim dari component parent yang menggunakan CustomButton
- Dengan cara ini, kita bisa membuat banyak button dengan teks dan fungsi yang berbeda tanpa menulis ulang code

### Custom Text Input Component

Selanjutnya, kita buat component untuk input field yang juga bisa dipakai ulang.

```javascript
// components/customTextInput.tsx

import React from 'react';
import { TextInput, Text, View } from 'react-native';
import { styles } from './Style';

function CustomTextInput({ text, onChange, label, multiline, numberOfLines }) {
  return (
    <View style={styles.inputContainer}>
      <Text style={styles.inputLabel}>{label}</Text>
      
      <TextInput
        style={styles.textInput}
        multiline={multiline}
        numberOfLines={numberOfLines}
        placeholder={label}
        onChangeText={onChange}
        defaultValue={text}
      />
    </View>
  );
}

export default CustomTextInput;
```

**Penjelasan Parameter:**
- `text` - Nilai default yang akan ditampilkan di input field
- `onChange` - Function yang dipanggil setiap kali user mengetik
- `label` - Label yang ditampilkan di atas input field
- `multiline` - Boolean untuk mengatur apakah input bisa multi baris
- `numberOfLines` - Jumlah baris jika multiline diaktifkan

### Home Component

Component ini akan menampilkan list note dan button untuk menambah atau mengedit note.

```javascript
// components/Home.tsx

import React from 'react';
import { FlatList, View, Text } from 'react-native';
import CustomButton from './customButton';
import { styles } from './Style';

// Component untuk menampilkan satu card note
function NoteCard({ item }) {
  return (
    <View style={styles.noteCard}>
      <Text style={styles.noteTitle}>{item.title}</Text>
      <Text style={styles.noteDesc}>{item.desc}</Text>

      {/* Container untuk button Ubah dan Hapus */}
      <View style={styles.buttonContainer}>
        <CustomButton
          text="Ubah"
          onPress={() => {}}
        />

        <CustomButton
          text="Hapus"
          onPress={() => {}}
        />
      </View>
    </View>
  );
}

// Component utama Home
function Home({ noteList }) {
  return (
    <View style={styles.container}>
      <CustomButton
        text="Tambahkan Note"
        onPress={() => {}}
      />

      {/* FlatList untuk menampilkan semua note */}
      <FlatList
        showsVerticalScrollIndicator={false}
        data={noteList}
        renderItem={NoteCard}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
}

export default Home;
```

**Penjelasan:**
- `NoteCard` - Function component untuk menampilkan satu item note
- `Home` - Function component utama yang menerima `noteList` dari parent
- `FlatList` digunakan untuk menampilkan array note secara efficient
- Property `renderItem` menentukan component apa yang akan dirender untuk setiap item
- Property `keyExtractor` memberikan key unik untuk setiap item (penting untuk performa)

### File Index Utama

File ini adalah pusat aplikasi yang mengelola state dan menampilkan component Home.

```javascript
// index.tsx

import React, { useState } from 'react';
import { View } from 'react-native';
import Home from './components/Home';
import { styles } from './components/Style';

function App() {
  // State untuk menyimpan list note
  const [noteList, setNoteList] = useState([
    {
      id: 1,
      title: 'Note pertama',
      desc: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
    },
  ]);

  return (
    <View style={styles.appContainer}>
      <View style={styles.mainContent}>
        <Home noteList={noteList} />
      </View>
    </View>
  );
}

export default App;
```

**Penjelasan:**
- `useState` digunakan untuk membuat state `noteList` yang berisi array note
- State `noteList` dikirim ke component `Home` sebagai props
- Kita membuat satu note default untuk testing

---

## Membuat Halaman Navigasi

Sekarang kita akan menambahkan kemampuan navigasi antar halaman (Home, Add Note, Edit Note).

### Setup Folder Screen

Buat folder baru bernama `screens` di dalam project, sejajar dengan folder `components`. Di dalam folder screens, buat 3 file berikut:

### Add Note Screen

```javascript
// screens/addNote.tsx

import React from 'react';
import { View, Text } from 'react-native';
import { styles } from '../components/Style';

const AddNote = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.pageTitle}>Tambahkan Note</Text>
      {/* Form akan ditambahkan nanti */}
    </View>
  );
};

export default AddNote;
```

### Edit Note Screen

```javascript
// screens/editNote.tsx

import React from 'react';
import { View, Text } from 'react-native';
import { styles } from '../components/Style';

const EditNote = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.pageTitle}>Ubah Note</Text>
      {/* Form akan ditambahkan nanti */}
    </View>
  );
};

export default EditNote;
```

### Update Home Component

Sekarang kita update component Home agar button-nya bisa navigasi ke halaman lain.

```javascript
// components/Home.tsx

import React from 'react';
import { FlatList, View, Text } from 'react-native';
import CustomButton from './customButton';
import { styles } from './Style';

// Component untuk satu card note
function NoteCard({ item, setCurrentPage }) {
  return (
    <View style={styles.noteCard}>
      <Text style={styles.noteTitle}>{item.title}</Text>
      <Text style={styles.noteDesc}>{item.desc}</Text>

      <View style={styles.buttonContainer}>
        {/* Button Ubah - navigasi ke halaman edit */}
        <CustomButton
          text="Ubah"
          onPress={() => setCurrentPage('edit')}
        />

        {/* Button Hapus - untuk delete note */}
        <CustomButton
          text="Hapus"
          onPress={() => {}}
        />
      </View>
    </View>
  );
}

// Component utama Home
function Home({ noteList, setCurrentPage }) {
  return (
    <View style={styles.container}>
      {/* Button untuk navigasi ke halaman tambah note */}
      <CustomButton
        text="Tambahkan Note"
        onPress={() => setCurrentPage('add')}
      />

      <FlatList
        showsVerticalScrollIndicator={false}
        data={noteList}
        renderItem={({ item }) => (
          <NoteCard item={item} setCurrentPage={setCurrentPage} />
        )}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
}

export default Home;
```

**Perubahan Penting:**
- Tambahkan parameter `setCurrentPage` di function `Home` dan `NoteCard`
- `renderItem` sekarang menggunakan arrow function untuk mengirim props `setCurrentPage` ke `NoteCard`
- Button "Tambahkan Note" memanggil `setCurrentPage('add')` untuk navigasi ke halaman add
- Button "Ubah" memanggil `setCurrentPage('edit')` untuk navigasi ke halaman edit

**Cara Kerja `renderItem`:**
```javascript
// Method map() bekerja seperti ini di belakang layar:
noteList.map((item) => (
  <NoteCard item={item} setCurrentPage={setCurrentPage} />
))
```

### Update Index dengan Navigation Logic

Sekarang kita update file index untuk menambahkan logika navigasi menggunakan switch case.

```javascript
// index.tsx

import React, { useState } from 'react';
import { View } from 'react-native';
import Home from './components/Home';
import AddNote from './screens/addNote';
import EditNote from './screens/editNote';
import { styles } from './components/Style';

// Function untuk menentukan halaman mana yang ditampilkan
function CurrentPageWidget({ currentPage, noteList, setCurrentPage }) {
  switch (currentPage) {
    case 'home':
      return (
        <Home
          noteList={noteList}
          setCurrentPage={setCurrentPage}
        />
      );
    case 'add':
      return <AddNote setCurrentPage={setCurrentPage} />;
    case 'edit':
      return <EditNote setCurrentPage={setCurrentPage} />;
    default:
      return <Home noteList={noteList} setCurrentPage={setCurrentPage} />;
  }
}

function App() {
  // State untuk mengatur halaman mana yang sedang aktif
  const [currentPage, setCurrentPage] = useState('home');

  // State untuk menyimpan list note
  const [noteList, setNoteList] = useState([
    {
      id: 1,
      title: 'Note pertama',
      desc: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
    },
  ]);

  return (
    <View style={styles.appContainer}>
      <View style={styles.mainContent}>
        <CurrentPageWidget
          currentPage={currentPage}
          setCurrentPage={setCurrentPage}
          noteList={noteList}
        />
      </View>
    </View>
  );
}

export default App;
```

**Penjelasan Switch Case:**
- Function `CurrentPageWidget` menerima 3 props: `currentPage`, `setCurrentPage`, dan `noteList`
- Switch case mengecek nilai `currentPage`:
  - Jika `'home'` - tampilkan component Home
  - Jika `'add'` - tampilkan component AddNote
  - Jika `'edit'` - tampilkan component EditNote
  - Default - kembali ke Home

**Konsep yang Sama dengan Ternary:**
```javascript
// Switch case di atas sama seperti:
currentPage === 'home' ? <Home /> : 
currentPage === 'add' ? <AddNote /> : 
currentPage === 'edit' ? <EditNote /> : <Home />
```

**Cara Kerja Navigation:**
1. User klik button "Tambahkan Note"
2. Function `setCurrentPage('add')` dipanggil
3. State `currentPage` berubah menjadi `'add'`
4. React re-render dan switch case menampilkan component `<AddNote />`
5. Halaman berganti ke Add Note screen

---

## Implementasi Form Input

Sekarang kita implementasi form untuk menambah dan edit note menggunakan component CustomTextInput yang sudah kita buat.

### Update Add Note Screen dengan Form

```javascript
// screens/addNote.tsx

import React, { useState } from 'react';
import { View, Text, ScrollView } from 'react-native';
import CustomTextInput from '../components/customTextInput';
import CustomButton from '../components/customButton';
import { styles } from '../components/Style';

const AddNote = ({ setCurrentPage, noteList, setNoteList }) => {
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('');

  const handleSubmit = () => {
    // Validasi input
    if (title.trim() === '' || desc.trim() === '') {
      alert('Judul dan deskripsi tidak boleh kosong!');
      return;
    }

    // Membuat note baru
    const newNote = {
      id: noteList.length + 1,
      title: title,
      desc: desc,
    };

    // Menambahkan note baru ke list
    setNoteList([...noteList, newNote]);

    // Reset form
    setTitle('');
    setDesc('');

    // Kembali ke halaman home
    setCurrentPage('home');
  };

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.pageTitle}>Tambahkan Note Baru</Text>

      <CustomTextInput
        text={title}
        onChange={setTitle}
        label="Judul Note"
        placeholder="Masukkan judul note"
        multiline={false}
      />

      <CustomTextInput
        text={desc}
        onChange={setDesc}
        label="Deskripsi"
        placeholder="Masukkan deskripsi note"
        multiline={true}
        numberOfLines={4}
      />

      <View style={styles.buttonGroup}>
        <CustomButton
          text="Simpan"
          onPress={handleSubmit}
        />

        <CustomButton
          text="Batal"
          onPress={() => setCurrentPage('home')}
        />
      </View>
    </ScrollView>
  );
};

export default AddNote;
```

**Penjelasan:**
- Gunakan `useState` untuk state `title` dan `desc`
- Function `handleSubmit`:
  1. Validasi input tidak boleh kosong
  2. Buat object note baru dengan id, title, dan desc
  3. Tambahkan note baru ke `noteList` menggunakan spread operator `[...noteList, newNote]`
  4. Reset form dan kembali ke home
- `ScrollView` digunakan agar form bisa di-scroll jika keyboard muncul

### Update Edit Note Screen dengan Form

```javascript
// screens/editNote.tsx

import React, { useState } from 'react';
import { View, Text, ScrollView } from 'react-native';
import CustomTextInput from '../components/customTextInput';
import CustomButton from '../components/customButton';
import { styles } from '../components/Style';

const EditNote = ({ setCurrentPage, selectedNote, noteList, setNoteList }) => {
  const [title, setTitle] = useState(selectedNote.title);
  const [desc, setDesc] = useState(selectedNote.desc);

  const handleUpdate = () => {
    // Validasi input
    if (title.trim() === '' || desc.trim() === '') {
      alert('Judul dan deskripsi tidak boleh kosong!');
      return;
    }

    // Update note di list
    const updatedNoteList = noteList.map((note) => {
      if (note.id === selectedNote.id) {
        return {
          ...note,
          title: title,
          desc: desc,
        };
      }
      return note;
    });

    setNoteList(updatedNoteList);
    setCurrentPage('home');
  };

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.pageTitle}>Ubah Note</Text>

      <CustomTextInput
        text={title}
        onChange={setTitle}
        label="Judul Note"
        placeholder="Masukkan judul note"
        multiline={false}
      />

      <CustomTextInput
        text={desc}
        onChange={setDesc}
        label="Deskripsi"
        placeholder="Masukkan deskripsi note"
        multiline={true}
        numberOfLines={4}
      />

      <View style={styles.buttonGroup}>
        <CustomButton
          text="Update"
          onPress={handleUpdate}
        />

        <CustomButton
          text="Batal"
          onPress={() => setCurrentPage('home')}
        />
      </View>
    </ScrollView>
  );
};

export default EditNote;
```

**Penjelasan:**
- State `title` dan `desc` di-initialize dengan nilai dari `selectedNote`
- Function `handleUpdate`:
  1. Validasi input
  2. Map semua note di `noteList`
  3. Jika id note sama dengan `selectedNote.id`, update title dan desc-nya
  4. Set `noteList` dengan array yang sudah di-update
  5. Kembali ke home

### Update Index untuk Handle Edit dan Delete

```javascript
// index.tsx

import React, { useState } from 'react';
import { View } from 'react-native';
import Home from './components/Home';
import AddNote from './screens/addNote';
import EditNote from './screens/editNote';
import { styles } from './components/Style';

function CurrentPageWidget({ 
  currentPage, 
  noteList, 
  setNoteList,
  setCurrentPage,
  selectedNote 
}) {
  switch (currentPage) {
    case 'home':
      return (
        <Home
          noteList={noteList}
          setCurrentPage={setCurrentPage}
          setSelectedNote={setSelectedNote}
          setNoteList={setNoteList}
        />
      );
    case 'add':
      return (
        <AddNote
          setCurrentPage={setCurrentPage}
          noteList={noteList}
          setNoteList={setNoteList}
        />
      );
    case 'edit':
      return (
        <EditNote
          setCurrentPage={setCurrentPage}
          selectedNote={selectedNote}
          noteList={noteList}
          setNoteList={setNoteList}
        />
      );
    default:
      return (
        <Home
          noteList={noteList}
          setCurrentPage={setCurrentPage}
        />
      );
  }
}

function App() {
  const [currentPage, setCurrentPage] = useState('home');
  const [selectedNote, setSelectedNote] = useState(null);

  const [noteList, setNoteList] = useState([
    {
      id: 1,
      title: 'Note pertama',
      desc: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
    },
  ]);

  return (
    <View style={styles.appContainer}>
      <View style={styles.mainContent}>
        <CurrentPageWidget
          currentPage={currentPage}
          setCurrentPage={setCurrentPage}
          noteList={noteList}
          setNoteList={setNoteList}
          selectedNote={selectedNote}
          setSelectedNote={setSelectedNote}
        />
      </View>
    </View>
  );
}

export default App;
```

### Update Home Component dengan Delete Function

```javascript
// components/Home.tsx

import React from 'react';
import { FlatList, View, Text, Alert } from 'react-native';
import CustomButton from './customButton';
import { styles } from './Style';

function NoteCard({ item, setCurrentPage, setSelectedNote, setNoteList, noteList }) {
  const handleDelete = () => {
    Alert.alert(
      'Hapus Note',
      'Apakah kamu yakin ingin menghapus note ini?',
      [
        {
          text: 'Batal',
          style: 'cancel',
        },
        {
          text: 'Hapus',
          onPress: () => {
            const filteredNotes = noteList.filter((note) => note.id !== item.id);
            setNoteList(filteredNotes);
          },
          style: 'destructive',
        },
      ]
    );
  };

  const handleEdit = () => {
    setSelectedNote(item);
    setCurrentPage('edit');
  };

  return (
    <View style={styles.noteCard}>
      <Text style={styles.noteTitle}>{item.title}</Text>
      <Text style={styles.noteDesc}>{item.desc}</Text>

      <View style={styles.buttonContainer}>
        <CustomButton
          text="Ubah"
          onPress={handleEdit}
        />

        <CustomButton
          text="Hapus"
          onPress={handleDelete}
        />
      </View>
    </View>
  );
}

function Home({ noteList, setCurrentPage, setSelectedNote, setNoteList }) {
  return (
    <View style={styles.container}>
      <CustomButton
        text="Tambahkan Note"
        onPress={() => setCurrentPage('add')}
      />

      {noteList.length === 0 ? (
        <View style={styles.emptyState}>
          <Text style={styles.emptyText}>Belum ada note. Yuk tambahkan!</Text>
        </View>
      ) : (
        <FlatList
          showsVerticalScrollIndicator={false}
          data={noteList}
          renderItem={({ item }) => (
            <NoteCard
              item={item}
              setCurrentPage={setCurrentPage}
              setSelectedNote={setSelectedNote}
              setNoteList={setNoteList}
              noteList={noteList}
            />
          )}
          keyExtractor={(item) => item.id.toString()}
        />
      )}
    </View>
  );
}

export default Home;
```

**Penjelasan Function Delete:**
- `handleDelete` menampilkan confirmation dialog menggunakan `Alert.alert`
- Jika user klik "Hapus", filter `noteList` untuk menghapus note dengan id yang sesuai
- `filter()` membuat array baru yang tidak termasuk note yang dihapus

**Penjelasan Function Edit:**
- `handleEdit` menyimpan note yang dipilih ke state `selectedNote`
- Navigasi ke halaman edit dengan `setCurrentPage('edit')`

---

## Finishing dan Source Code

Selamat! Kamu sudah berhasil membuat aplikasi note sederhana dengan fitur lengkap:
- ✅ Menampilkan list note
- ✅ Menambah note baru
- ✅ Edit note yang sudah ada
- ✅ Hapus note
- ✅ Navigasi antar halaman

### Yang Bisa Ditambahkan Selanjutnya

Untuk mengembangkan aplikasi ini lebih lanjut, kamu bisa menambahkan fitur:

1. **Persistent Storage** - Simpan note ke AsyncStorage agar data tidak hilang saat aplikasi ditutup
2. **Search Function** - Tambahkan fitur pencarian note
3. **Categories/Tags** - Tambahkan kategori atau tag untuk note
4. **Date/Time** - Tampilkan kapan note dibuat atau diubah
5. **Better Styling** - Perbaiki tampilan dengan warna dan layout yang lebih menarik

### Source Code Lengkap

Source code lengkap untuk project ini bisa kamu lihat di: [Note Todo App Expo](../../code/jsPro/note-todoApp-expo)

---

## Referensi Tambahan

### Tutorial dan Artikel

- [Handling User Input in React Native Expo](https://medium.com/@yildizfatma/handling-user-input-in-react-native-expo-text-input-buttons-6e7931bc227a) - Tutorial tentang cara handle input dan button di Expo

- [Make Todo List Application Using React Native Expo](https://medium.com/nerd-for-tech/make-todo-list-application-using-react-native-expo-for-ios-and-android-device-1de436168f86) - Tutorial lengkap membuat Todo App

- [Use External Style Sheet in React Native](https://codeflarelimited.com/blog/use-external-style-sheet-in-react-native/) - Cara mengorganisir CSS di React Native

### Tips Penting

**Debugging:**
- Gunakan `console.log()` untuk debugging state dan props
- Pastikan semua props dikirim dengan benar antar component
- Cek error di terminal atau di Expo Go app

**Best Practice:**
- Pisahkan styling ke file terpisah agar lebih mudah di-maintain
- Buat component yang reusable seperti CustomButton dan CustomTextInput
- Gunakan meaningful variable names agar code mudah dibaca

**Performance:**
- Gunakan FlatList untuk list yang panjang, bukan ScrollView dengan map
- Hindari inline function di FlatList renderItem jika memungkinkan
- Gunakan `keyExtractor` dengan benar untuk performa optimal

---

**Selamat belajar dan happy coding!** 🚀

Jangan lupa untuk eksperimen dan modifikasi aplikasi ini sesuai kebutuhanmu. Trial and error adalah cara terbaik untuk belajar!
