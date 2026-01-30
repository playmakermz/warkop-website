# Panduan Belajar Expo dan React Native

## Daftar Isi

1. [Pengenalan React Native](#react-native)
2. [Pengenalan Expo](#expo)
3. [Instalasi dan Setup](#instalasi-dan-setup)
4. [Tool Tambahan](#tool-tambahan)
5. [Struktur Project dan Lokasi File](#informasi-struktur-project)
6. [Component Inti React Native](#component-inti-react-native)
   - [Component Dasar untuk UI](#component-dasar-untuk-ui)
   - [Component untuk Scroll](#component-untuk-scroll)
   - [Component untuk Interaksi Touch](#component-untuk-interaksi-touch)
7. [Penjelasan Detail Component](#penjelasan-detail-component)
   - [View](#view)
   - [Text](#text)
   - [StyleSheet](#stylesheet)
   - [Image](#image)
   - [TextInput](#textinput)
8. [ScrollView dan FlatList](#scrollview-dan-flatlist)
   - [ScrollView](#scrollview)
   - [FlatList](#flatlist)
   - [Perbedaan ScrollView dan FlatList](#perbedaan-scrollview-dan-flatlist)
9. [Button dan TouchableOpacity](#button-dan-touchableopacity)
10. [Expo Linear Gradient](#expo-linear-gradient)
11. [ImageBackground](#imagebackground)
12. [FontAwesome Icons](#fontawesome-icons)
13. [Catatan Penting](#catatan-penting)
14. [Referensi Tambahan](#referensi-tambahan)

---

## React Native

React Native adalah framework open source yang membantu kita mengembangkan aplikasi mobile menggunakan JavaScript. Framework ini sangat populer karena memungkinkan developer web untuk membuat aplikasi mobile tanpa harus belajar bahasa native seperti Java (Android) atau Swift (iOS).

### Kelebihan React Native

**Pengembangan lintas platform**: Dengan satu codebase, aplikasi bisa berjalan di Android maupun iOS. Ini sangat menghemat waktu dan biaya development karena kita tidak perlu menulis kode terpisah untuk setiap platform.

---

## Expo

Expo adalah framework yang dibangun di atas React Native. Expo mempermudah dan mempercepat proses pengembangan aplikasi dengan React Native, terutama untuk pemula.

### Keuntungan Menggunakan Expo

**Setup yang lebih mudah**: Dengan Expo, kita bisa melewati berbagai konfigurasi rumit yang biasanya diperlukan saat membuat aplikasi React Native dari nol.

**Expo SDK**: Menyediakan berbagai module dan library yang sudah siap pakai, seperti navigasi, kamera, sensor, dan masih banyak lagi. Kita tidak perlu install dan konfigurasi library satu per satu.

**Expo CLI**: Command line interface yang digunakan untuk membangun dan menjalankan aplikasi dengan perintah yang simpel.

**Expo Go**: Aplikasi yang sangat membantu untuk testing. Dengan Expo Go, kita bisa langsung menjalankan aplikasi di smartphone tanpa harus melakukan build dan deployment yang ribet.

---

## Instalasi dan Setup

Untuk menggunakan Expo di environment IDX atau development lokal, tetap gunakan `yarn` sebagai package manager.

### Cara Instalasi dengan Yarn

```bash
# Install yarn secara global
npm install -g yarn

# Install expo CLI dan expo
yarn add global expo-cli
yarn add global expo

# Atau bisa juga dengan npm
npm install expo-cli
npm install expo

# Jika mengalami error karena versi, upgrade dengan perintah ini
npx expo-cli upgrade
```

**Referensi**: [How to Install Expo CLI Using Yarn](https://medium.com/@blackpintz/how-to-install-expo-cli-using-yarn-92efe8ed78f5)

### Membuat Project Baru

```bash
# Membuat project expo baru
npx create-expo-app my-app

# Menjalankan aplikasi di browser (web)
npm run web
```

---

## Tool Tambahan

Install aplikasi **Expo Go** di smartphone Android atau iOS untuk melakukan testing aplikasi secara langsung. Aplikasi ini bisa didownload gratis di Play Store (Android) atau App Store (iOS).

Dengan Expo Go, kita bisa scan QR code yang muncul di terminal saat menjalankan `npm start`, dan aplikasi akan langsung berjalan di smartphone kita.

---

## Informasi Struktur Project

Jika menggunakan GitHub Codespace atau environment development lainnya, file utama untuk halaman home biasanya berada di:

```
/app/(tabs)/index.tsx
```

### Contoh Kode Sederhana

```javascript
import { View, Text } from 'react-native';
import { HelloWave } from '@/components/HelloWave';
import ParallaxScrollView from '@/components/ParallaxScrollView';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';

export default function HomeScreen() {
  return (
    <View>
      <View style={{ alignItems: 'center' }}>
        <Text style={{ fontSize: 40 }}>Hello React Native</Text>
      </View>

      <View style={{ alignItems: 'center' }}>
        <Text style={{ fontSize: 40 }}>Hello React Native</Text>
      </View>
    </View>
  );
}
```

---

## Component Inti React Native

React Native menyediakan berbagai component bawaan yang siap digunakan. Berikut ini daftar component yang paling sering dipakai:

### Component Dasar untuk UI

- **View**: Container untuk layout
- **Text**: Menampilkan teks
- **StyleSheet**: Untuk styling component
- **Image**: Menampilkan gambar
- **TextInput**: Input field untuk form

### Component untuk Scroll

- **ScrollView**: Container yang bisa di-scroll untuk konten yang panjang
- **FlatList**: List yang efficient untuk menampilkan banyak data

### Component untuk Interaksi Touch

- **Button**: Tombol standar
- **TouchableOpacity**: Area yang bisa di-touch dengan efek opacity

---

## Penjelasan Detail Component

### View

Component View berfungsi sebagai container pembungkus, mirip seperti tag `<div>` di HTML.

```javascript
import { View, Text } from 'react-native';

return (
  <View>
    <View style={{ alignItems: 'center' }}>
      <Text style={{ fontSize: 40 }}>Hello React Native</Text>
    </View>

    <View style={{ alignItems: 'center' }}>
      <Text style={{ fontSize: 40 }}>Hello React Native</Text>
    </View>
  </View>
);
```

View digunakan untuk mengatur layout dan posisi component lain di dalamnya.

### Text

Component Text digunakan untuk menampilkan string atau teks di aplikasi. Berbeda dengan HTML, di React Native kita tidak bisa langsung menulis teks di dalam View, harus dibungkus dengan component Text.

```javascript
<Text style={{ fontSize: 30 }}>
  Ini ukuran akan berubah
  <Text>Teks ini mewarisi style dari parent</Text>
  
  <View>
    <Text>Ini ukuran tidak akan berubah</Text>
  </View>
</Text>
```

Style pada Text akan diturunkan ke Text yang ada di dalamnya, kecuali jika Text tersebut berada di dalam View atau component lain.

### StyleSheet

StyleSheet adalah cara untuk menulis CSS di React Native. Dengan StyleSheet, kita bisa membuat style yang terorganisir dan efficient.

```javascript
import { StyleSheet, Text, View } from 'react-native';

// Menggunakan style
<Text style={styles.title}>React Native - Progate</Text>

// Mendefinisikan style
const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 24,
    backgroundColor: '#eaeaea',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
});
```

Konsepnya mirip dengan inline CSS, tapi lebih terstruktur dan performanya lebih baik.

### Image

Component Image digunakan untuk menampilkan gambar di aplikasi.

```javascript
import { View, Image, StyleSheet } from 'react-native';

// Untuk gambar lokal (dari folder assets)
<Image 
  style={styles.image} 
  source={require('./assets/icon.png')} 
/>

// Untuk gambar dari URL
<Image 
  style={styles.image}
  source={{ uri: 'https://example.com/image.png' }}
/>
```

**Referensi**: [React Native Images Tutorial](https://www.tutorialspoint.com/react_native/react_native_images.htm)

### TextInput

Component TextInput digunakan untuk membuat input field seperti form.

```javascript
import { View, StyleSheet, TextInput } from 'react-native';
import { useState } from 'react';

const [name, setName] = useState('');

<TextInput
  style={styles.input}
  placeholder="Masukan Nama"
  onChangeText={setName}
  value={name}
/>
```

TextInput memiliki banyak props yang bisa digunakan untuk berbagai keperluan seperti keyboard type, auto-capitalize, dan lain-lain.

**Referensi Detail**: [React Native TextInput Props](https://reactnative.dev/docs/textinput#props)

---

## ScrollView dan FlatList

### Attribute Khusus untuk Container

Untuk component container yang bisa di-scroll, ada attribute khusus bernama `contentContainerStyle`:

```javascript
contentContainerStyle={styles.wrapper}
```

Attribute ini berfungsi untuk memberikan style pada konten di dalam scroll container. Ini berbeda dengan `style` biasa yang hanya mengatur container-nya saja.

**Referensi**: [Penjelasan contentContainerStyle](https://stackoverflow.com/questions/46032604/scrollview-child-layout-must-be-applied-through-the-contentcontainerstyle-prop)

### ScrollView

ScrollView adalah component yang memungkinkan konten di dalamnya bisa di-scroll jika melebihi ukuran layar.

```javascript
import { StyleSheet, View, ScrollView, Text } from 'react-native';

<View style={styles.container}>
  <ScrollView style={styles.scrollView}>
    <Text style={styles.text}>
      Teks yang sangat panjang akan bisa di-scroll...
      Lorem ipsum dolor sit amet consectetur adipisicing elit...
    </Text>
  </ScrollView>
</View>
```

ScrollView cocok digunakan untuk konten yang tidak terlalu banyak dan sudah diketahui jumlahnya.

**Referensi**: [React Native ScrollView](https://reactnative.dev/docs/using-a-scrollview)

### FlatList

FlatList mirip dengan ScrollView, tapi lebih efficient untuk menampilkan data dalam jumlah banyak dari array.

```javascript
import { View, FlatList, Text, StyleSheet } from 'react-native';

const items = [
  { id: '1', title: 'Item 1' },
  { id: '2', title: 'Item 2' },
  { id: '3', title: 'Item 3' },
];

const App = () => {
  const renderItem = ({ item }) => (
    <View style={styles.item}>
      <Text>{item.title}</Text>
    </View>
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={items}
        renderItem={renderItem}
        keyExtractor={(item) => item.id}
      />
    </View>
  );
};
```

**Penjelasan Props:**
- `data`: Array yang berisi data yang akan ditampilkan
- `renderItem`: Function yang menentukan bagaimana setiap item akan di-render
- `keyExtractor`: Function yang menentukan key unik untuk setiap item (mirip dengan key di React)

**Referensi**: [React Native FlatList](https://reactnative.dev/docs/flatlist)

### Perbedaan ScrollView dan FlatList

**ScrollView:**
- Digunakan untuk konten yang sedikit dan sudah pasti jumlahnya
- Me-render semua item sekaligus
- Lebih simple untuk konten yang tidak dinamis
- Cocok untuk konten yang jumlahnya kurang dari 20-30 item

**FlatList:**
- Digunakan untuk data yang banyak (ratusan atau ribuan item)
- Me-render item secara lazy (hanya yang terlihat di layar)
- Lebih efficient dan performa lebih baik untuk data besar
- Cocok untuk data dinamis yang diambil dari API

---

## Button dan TouchableOpacity

### Button

Component Button adalah tombol standar yang sudah ada styling bawaannya.

```javascript
import { View, Button, Alert, StyleSheet } from 'react-native';

<Button
  title="Color Button"
  color="#f194ff"
  onPress={() => Alert.alert('Button di-klik!')}
/>
```

Button bisa digunakan untuk trigger function atau navigasi ke halaman lain.

### TouchableOpacity

TouchableOpacity adalah component wrapper yang bisa dijadikan tombol kustom dengan styling sesuai keinginan.

```javascript
import { View, StyleSheet, TouchableOpacity, Text } from 'react-native';

const onPress = () => {
  console.log('Button dipencet!');
};

<TouchableOpacity style={styles.button} onPress={onPress}>
  <Text style={styles.buttonText}>Press Here</Text>
</TouchableOpacity>
```

TouchableOpacity memberikan efek opacity (transparansi) saat di-touch, sehingga user tau bahwa element tersebut bisa di-klik. Component ini sangat flexible dan bisa kita styling sesuai kebutuhan design kita.

---

## Expo Linear Gradient

Linear Gradient digunakan untuk membuat efek gradasi warna pada background component.

### Instalasi

```bash
npm install expo-linear-gradient
```

### Cara Penggunaan

```javascript
import { LinearGradient } from 'expo-linear-gradient';
import { View, Text } from 'react-native';

<LinearGradient
  colors={['#FF0000', '#FFFF00', '#00FF00']}
  start={[0, 0]}
  end={[1, 1]}
  style={{ padding: 20 }}
>
  <View>
    <Text style={{ color: 'white' }}>
      Konten dengan background gradient
    </Text>
  </View>
</LinearGradient>
```

Pada contoh di atas, gradient akan berjalan dari kiri atas ke kanan bawah dengan transisi warna dari merah ke kuning ke hijau.

### Manfaat Linear Gradient

- Meningkatkan kualitas visual aplikasi
- Bisa digunakan untuk memberikan highlight pada area tertentu
- Membuat UI lebih menarik dan modern

**Referensi:**
- [React Native Linear Gradient GitHub](https://github.com/react-native-linear-gradient/react-native-linear-gradient)
- [Contoh Demo Interaktif](https://codesandbox.io/s/react-hv1g9e)
- [Expo Linear Gradient Official Docs](https://docs.expo.dev/versions/latest/sdk/linear-gradient/)

---

## ImageBackground

ImageBackground memungkinkan kita untuk menampilkan konten di atas gambar background.

```javascript
import { ImageBackground, StyleSheet, Text, View } from 'react-native';

const image = { uri: 'https://legacy.reactjs.org/logo-og.png' };

const App = () => (
  <View style={styles.container}>
    <ImageBackground 
      source={image} 
      resizeMode="cover" 
      style={styles.image}
    >
      <Text style={styles.text}>Teks di atas gambar</Text>
    </ImageBackground>
  </View>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  image: {
    flex: 1,
    justifyContent: 'center',
  },
  text: {
    color: 'white',
    fontSize: 42,
    fontWeight: 'bold',
    textAlign: 'center',
    backgroundColor: 'rgba(0,0,0,0.5)',
  },
});
```

Component ini sangat berguna untuk membuat hero section, banner, atau card dengan background image.

**Referensi**: [React Native ImageBackground](https://reactnative.dev/docs/imagebackground)

---

## FontAwesome Icons

FontAwesome adalah library icon yang sangat lengkap dan mudah digunakan di Expo.

### Cara Penggunaan

```javascript
import { FontAwesome } from '@expo/vector-icons';

// Icon bintang dengan warna kuning
<FontAwesome name="star" size={16} color="yellow" />

// Icon heart dengan warna merah
<FontAwesome name="heart" size={24} color="red" />

// Icon user
<FontAwesome name="user" size={32} color="blue" />
```

Expo sudah menyediakan berbagai icon library selain FontAwesome, seperti MaterialIcons, Ionicons, dan lain-lain.

**Referensi**: [Expo Icons Directory](https://icons.expo.fyi/Index) (kamu bisa cari icon yang dibutuhkan di sini)

---

## Catatan Penting

### Deklarasi State

State **harus** dideklarasikan di dalam function component, tidak boleh di luar function. Ini adalah aturan React Hooks.

**Benar:**
```javascript
const App = () => {
  const [count, setCount] = useState(0); // State di dalam function
  
  return (
    <View>
      <Text>{count}</Text>
    </View>
  );
};
```

**Salah:**
```javascript
const [count, setCount] = useState(0); // Salah! State di luar function

const App = () => {
  return (
    <View>
      <Text>{count}</Text>
    </View>
  );
};
```

---

## Referensi Tambahan

### Tutorial dan Dokumentasi

- [Simple Todo App dengan Expo](./note-app-expo.md)
- [API Testing dengan Axios](../project-react/Api-Axios.md)
- [Expo Navigator (Navigasi antar halaman)](../project-react/Expo-Navigator.md)

### Artikel Bermanfaat

- [Responsive Layout in React Native](https://www.freecodecamp.org/news/responsive-layout-react-native/) - Tutorial sangat sederhana, direkomendasikan untuk pemula
- [React Expo Debugging dengan Reactotron](https://shift.infinite.red/start-using-reactotron-in-your-expo-project-today-in-3-easy-steps-a03d11032a7a)

### Repository GitHub

Source code note ini bisa dilihat di: [Warkop Website Repository](https://github.com/playmakermz/warkop-website)

---

**Selamat belajar! Jangan ragu untuk eksperimen dan coba berbagai component yang ada. Practice makes perfect!** 🚀
