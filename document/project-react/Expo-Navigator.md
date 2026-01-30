# Panduan Lengkap Expo Navigator

## Daftar Isi

1. [Instalasi React Navigation](#instalasi-react-navigation)
2. [Konsep Dasar React Navigation](#konsep-dasar-react-navigation)
3. [Stack Navigator](#stack-navigator)
   - [Membuat Basic Stack Navigator](#membuat-basic-stack-navigator)
   - [Mengatur Tampilan Route](#mengatur-tampilan-route)
4. [Tab Navigation dan Nesting Navigators](#tab-navigation-dan-nesting-navigators)
   - [Cara Kerja Nesting Navigator](#cara-kerja-nesting-navigator)
   - [Navigasi antar Screen di Navigator Berbeda](#navigasi-antar-screen-di-navigator-berbeda)
   - [Contoh Project Nesting](#contoh-project-nesting)
5. [Navigation Lifecycle](#navigation-lifecycle)
   - [Mendeteksi Screen Focus dan Unfocus](#mendeteksi-screen-focus-dan-unfocus)
6. [Navigasi Antar Screen](#navigasi-antar-screen)
   - [Navigate vs Push vs GoBack](#navigate-vs-push-vs-goback)
7. [Passing Parameters ke Routes](#passing-parameters-ke-routes)
   - [Mengirim Parameter](#mengirim-parameter)
   - [Menerima Parameter](#menerima-parameter)
   - [Initial Params](#initial-params)
8. [useNavigation Hook](#usenavigation-hook)
9. [Stack Actions](#stack-actions)
   - [Push vs Replace](#push-vs-replace)
10. [Preventing Going Back](#preventing-going-back)
11. [Referensi dan Resources](#referensi-dan-resources)

---

## Instalasi React Navigation

Untuk menggunakan React Navigation di project Expo, kita perlu menginstall beberapa package. Ikuti langkah instalasi berikut secara berurutan:

### Langkah 1: Install React Navigation Core

```bash
npm install @react-navigation/native
```

Package ini adalah core library dari React Navigation yang wajib diinstall.

### Langkah 2: Install Dependencies untuk Expo

```bash
npx expo install react-native-screens react-native-safe-area-context
```

**Atau bisa juga dengan:**

```bash
npm install react-native-screens react-native-safe-area-context
```

Package `react-native-screens` dan `react-native-safe-area-context` adalah dependencies yang diperlukan untuk React Navigation bekerja dengan baik di Expo.

### Langkah 3: Install Stack Navigator

```bash
npm install @react-navigation/native-stack
```

Package ini untuk membuat stack navigation (navigasi bertumpuk seperti stack).

### Langkah 4: Install React Native Navigation (Opsional)

```bash
npm install --save react-native-navigation
```

Package ini opsional, digunakan untuk navigation yang lebih advanced.

### Langkah 5: Install Drawer Navigator (Opsional)

```bash
npm install @react-navigation/drawer
```

Package ini untuk membuat drawer navigation (menu samping yang bisa di-slide).

### Langkah 6: Install Bottom Tab Navigator

```bash
npm install @react-navigation/bottom-tabs
```

Package ini untuk membuat bottom tab navigation (tab di bagian bawah layar).

### Langkah 7: Install Gesture Handler dan Reanimated (Untuk Drawer)

```bash
npm install react-native-gesture-handler react-native-reanimated
```

Package ini diperlukan jika menggunakan drawer navigator atau animasi advanced.

---

## Konsep Dasar React Navigation

React Navigation bekerja mirip seperti navigasi di web browser. Saat kita klik link `<a>` di web, kita akan diarahkan ke halaman baru. Kita bisa kembali ke halaman sebelumnya dengan klik tombol "Back" di browser. Tombol back ini mengambil informasi dari history browser.

**React Navigation bekerja dengan cara yang sama**, tapi dengan beberapa perbedaan penting:

### Perbedaan Kunci

**Gesture dan Animasi Native:**
React Navigation menyediakan gesture (gerakan) dan animasi perpindahan halaman yang sesuai dengan ekspektasi user di platform mobile (Android dan iOS). Misalnya:
- Di iOS: Swipe dari kiri untuk kembali
- Di Android: Tombol back hardware
- Animasi slide yang smooth

### Terminologi Penting

Sebelum mulai, mari kita pahami istilah-istilah penting dalam React Navigation:

**Navigator:** Component React yang menentukan screen mana yang akan di-render dan mengatur bagaimana perpindahan antar screen.

**Router:** Kumpulan function yang membantu kita handle perubahan action dan state di dalam navigator.

**Screen Component:** Component yang kita gunakan untuk konfigurasi route (jalur navigasi).

**Navigation Prop:** Object yang berisi berbagai method untuk navigasi, seperti `navigate`, `push`, `goBack`, dll.

**Route:** Jalur atau path menuju suatu screen, diidentifikasi dengan `name`.

---

## Stack Navigator

Stack Navigator adalah tipe navigator yang paling umum digunakan. Stack Navigator mengatur screen dalam bentuk stack (tumpukan), mirip seperti kartu yang ditumpuk. Screen baru ditambahkan di atas stack, dan saat kita back, screen teratas dihapus dari stack.

### Membuat Basic Stack Navigator

Function `createNativeStackNavigator` akan menghasilkan 2 property penting: `Screen` dan `Navigator`. Keduanya adalah React component untuk konfigurasi navigator.

**Penempatan NavigationContainer:**
`NavigationContainer` harus ditempatkan di bagian paling luar aplikasi, biasanya di file `index.tsx` atau `App.tsx`.

### Contoh Implementasi

```javascript
import * as React from 'react';
import { View, Text, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

// Screen pertama - Home
function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
      <Button
        title="Go to Details"
        onPress={() => navigation.navigate('Details')}
      />
    </View>
  );
}

// Screen kedua - Details
function DetailsScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
    </View>
  );
}

// Membuat Stack Navigator
const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        {/* Mendefinisikan route dengan nama "Home" */}
        <Stack.Screen name="Home" component={HomeScreen} />
        {/* Mendefinisikan route dengan nama "Details" */}
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

**Penjelasan Code:**

1. **Import Modules**: Import semua library yang diperlukan
2. **Create Stack**: `createNativeStackNavigator()` membuat stack navigator
3. **NavigationContainer**: Wrapper yang wajib ada di root aplikasi
4. **Stack.Navigator**: Container untuk semua screen
5. **Stack.Screen**: Mendefinisikan setiap route dengan `name` dan `component`
6. **initialRouteName**: Menentukan screen mana yang ditampilkan pertama kali

**Cara Kerja Route:**
- Pemilihan route didasarkan pada property `name`
- Saat kita panggil `navigation.navigate('Details')`, React Navigation akan mencari screen dengan `name="Details"`
- Component yang ada di property `component` akan di-render

### Mengatur Tampilan Route

Kita bisa mengatur tampilan header dan opsi lain untuk setiap route menggunakan property `options` atau `screenOptions`.

**Menggunakan `options` (per screen):**

```javascript
<Stack.Screen 
  name="Home" 
  component={HomeScreen}
  options={{
    title: 'Beranda',
    headerStyle: {
      backgroundColor: '#f4511e',
    },
    headerTintColor: '#fff',
    headerTitleStyle: {
      fontWeight: 'bold',
    },
  }}
/>
```

**Menggunakan `screenOptions` (untuk semua screen):**

```javascript
<Stack.Navigator
  screenOptions={{
    headerStyle: {
      backgroundColor: '#f4511e',
    },
    headerTintColor: '#fff',
  }}
>
  <Stack.Screen name="Home" component={HomeScreen} />
  <Stack.Screen name="Details" component={DetailsScreen} />
</Stack.Navigator>
```

**Referensi Lengkap:** [Specifying Options](https://reactnavigation.org/docs/hello-react-navigation#specifying-options)

---

## Tab Navigation dan Nesting Navigators

Nesting Navigator adalah teknik untuk merender navigator di dalam screen dari navigator lain. Ini sangat berguna untuk membuat struktur navigasi yang kompleks.

**Referensi:** [Nesting Navigators](https://reactnavigation.org/docs/nesting-navigators)

### Cara Kerja Nesting Navigator

Tujuan dari nesting adalah untuk membuat struktur navigasi berlapis. Misalnya, kita punya Tab Navigator di dalam Stack Navigator.

### Contoh Struktur Nesting

```javascript
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Tab = createBottomTabNavigator();
const Stack = createNativeStackNavigator();

// Tab Navigator sebagai screen di Stack Navigator
function Home() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Feed" component={Feed} />
      <Tab.Screen name="Messages" component={Messages} />
    </Tab.Navigator>
  );
}

// Stack Navigator sebagai root navigator
function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Home"
          component={Home}
          options={{ headerShown: false }}
        />
        <Stack.Screen name="Profile" component={Profile} />
        <Stack.Screen name="Settings" component={Settings} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

**Visualisasi Struktur:**

```
NavigationContainer
└── Stack.Navigator
    ├── Home (Tab.Navigator)
    │   ├── Feed (Screen)
    │   └── Messages (Screen)
    ├── Profile (Screen)
    └── Settings (Screen)
```

**Catatan Penting:**
- Untuk penggunaan di local computer, kamu bisa menghilangkan tag `<NavigationContainer>` di dalam component jika sudah ada di root
- `options={{ headerShown: false }}` digunakan untuk menyembunyikan header bawaan Stack Navigator

### Navigasi antar Screen di Navigator Berbeda

Setiap navigator memiliki history mereka sendiri. Jika kamu menjalankan navigator di dalam screen, kamu bisa kembali ke navigator parent.

**Hal Penting yang Perlu Diperhatikan:**
[How Nesting Affects Behaviour](https://reactnavigation.org/docs/nesting-navigators#how-nesting-navigators-affects-the-behaviour)

### Contoh Project Nesting

Mari kita buat contoh aplikasi dengan struktur navigasi yang lebih kompleks.

**Requirements:**
- Screen `Profile` (standalone)
- Screen `Home` (Tab Navigator dengan 2 tab)
- Tab `Settings` di dalam Home
- Screen `EditPost` (dapat diakses dari Profile)

**Struktur yang Akan Dibuat:**
- Di `Home` screen, kita bisa akses `Profile` dan `Settings` (via Tab)
- Di component App, kita buat Stack Navigator utama yang bisa diakses dari mana saja

```javascript
import * as React from 'react';
import { Button, View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

// Membuat navigator instances
const Tab = createBottomTabNavigator();
const Stack = createNativeStackNavigator();

// Screen Profile dengan navigasi ke EditPost
function Profile({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Profile Screen</Text>
      <Button
        onPress={() => navigation.navigate('EditPost')}
        title="Go to Edit Post"
      />
    </View>
  );
}

// Empty/Dummy Screen
function EmptyScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Hai, this is Empty and dummy screen</Text>
    </View>
  );
}

// Home dengan Tab Navigator
function Home() {
  // PENTING: Hanya boleh ada Stack.Screen atau Tab.Screen di dalam Navigator
  // Tidak boleh ada component lain di dalam Navigator
  return (
    <Tab.Navigator>
      <Tab.Screen name="Profile" component={Profile} />
      <Tab.Screen name="Settings" component={EmptyScreen} />
    </Tab.Navigator>
  );
}

// Root Navigator
function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        {/* Home adalah screen pertama yang akan ditampilkan */}
        <Stack.Screen 
          name="Home" 
          component={Home} 
          options={{ headerShown: false }}
        />
        {/* EditPost bisa diakses dari Profile melalui navigation.navigate */}
        <Stack.Screen name="EditPost" component={EmptyScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

**Penjelasan Cara Kerja:**

1. **Halaman Awal**: Stack.Screen pertama (`Home`) adalah halaman yang muncul pertama kali
2. **Akses EditPost**: Untuk akses Stack.Screen kedua (`EditPost`), kita bisa panggil dari component `Profile` menggunakan `navigation.navigate('EditPost')`
3. **Tab Navigation**: Di dalam `Home`, ada Tab Navigator dengan 2 tab (Profile dan Settings)
4. **Screen Scope**: 
   - Screen di dalam Tab Navigator (Profile, Settings) hanya bisa navigasi ke screen di Tab yang sama ATAU ke screen di parent Stack Navigator
   - Profile bisa navigasi ke EditPost karena EditPost ada di parent Stack Navigator

**Penting Diingat:**
- Tidak boleh ada element selain Screen di dalam Navigator
- Header Stack Navigator disembunyikan dengan `headerShown: false` agar tidak bertumpuk dengan header Tab Navigator

---

## Navigation Lifecycle

Lifecycle dalam React Navigation mengacu pada event yang terjadi saat screen di-mount, di-focus, di-unfocus, atau di-unmount.

### Pertanyaan Penting

- Apa yang terjadi saat kita navigasi jauh dari screen `Home`?
- Bagaimana cara kita tau user pergi dari suatu screen?
- Bagaimana cara kita tau user kembali ke screen?

### Mendeteksi Screen Focus dan Unfocus

Kita bisa menggunakan `useFocusEffect` hook untuk menjalankan code saat screen di-focus atau di-unfocus.

```javascript
import { useState, useCallback } from 'react';
import { Text, View } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';

function ProfileScreen() {
  const [count, setCount] = useState(0);

  useFocusEffect(
    useCallback(() => {
      // Code ini akan dijalankan saat screen di-FOCUS (ditampilkan)
      console.log('Screen was focused (Mount)');
      
      // Return function akan dijalankan saat screen di-UNFOCUS (ditinggalkan)
      return () => {
        console.log('Screen was unfocused (Unmount)');
        setCount(0); // Reset counter saat user meninggalkan screen
      };
    }, [])
  );

  return (
    <View>
      <Text>Profile Screen</Text>
      <Text>Count: {count}</Text>
    </View>
  );
}
```

**Penjelasan:**
- `useFocusEffect` mirip dengan `useEffect`, tapi khusus untuk navigation lifecycle
- Code di dalam callback akan dijalankan setiap kali screen di-focus
- Code di dalam return function akan dijalankan saat screen di-unfocus
- `useCallback` digunakan untuk optimasi performa

**Use Case:**
- Fetch data baru saat screen ditampilkan
- Reset state saat user meninggalkan screen
- Start/stop timer atau subscription
- Track analytics

### Contoh Kompleks dengan Multiple Navigators

```javascript
import * as React from 'react';
import { Button, View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Tab = createBottomTabNavigator();
const HomeStack = createNativeStackNavigator();
const SettingsStack = createNativeStackNavigator();

// Screens
function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
      <Button
        title="Go to Details"
        onPress={() => navigation.navigate('Details')}
      />
    </View>
  );
}

function DetailsScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
    </View>
  );
}

function SettingsScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Settings Screen</Text>
      <Button
        title="Go to Profile"
        onPress={() => navigation.navigate('Profile')}
      />
    </View>
  );
}

function ProfileScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Profile Screen</Text>
    </View>
  );
}

// Root App dengan Tab Navigator
function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator screenOptions={{ headerShown: false }}>
        {/* Tab pertama dengan Home Stack */}
        <Tab.Screen name="First">
          {() => (
            <SettingsStack.Navigator>
              <SettingsStack.Screen name="Settings" component={SettingsScreen} />
              <SettingsStack.Screen name="Profile" component={ProfileScreen} />
            </SettingsStack.Navigator>
          )}
        </Tab.Screen>

        {/* Tab kedua dengan Settings Stack */}
        <Tab.Screen name="Second">
          {() => (
            <HomeStack.Navigator>
              <HomeStack.Screen name="Home" component={HomeScreen} />
              <HomeStack.Screen name="Details" component={DetailsScreen} />
            </HomeStack.Navigator>
          )}
        </Tab.Screen>
      </Tab.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

**Tujuan dan Aturan:**
- Screen awal yang ditampilkan adalah tab "First" (Settings)
- Ada 2 tab utama: "First" (Settings Stack) dan "Second" (Home Stack)
- **Pembatasan Navigasi:**
  - Home hanya bisa akses Details (dalam stack yang sama)
  - Settings hanya bisa akses Profile (dalam stack yang sama)
  - Tidak bisa navigasi antar screen di stack yang berbeda

**Konsep Penting:**
Setiap Stack Navigator memiliki history mereka sendiri. Screen di dalam satu stack tidak bisa langsung navigasi ke screen di stack lain kecuali melalui parent navigator.

---

## Navigasi Antar Screen

Setelah setup navigator, kita perlu tau cara berpindah antar screen. Ada beberapa method yang bisa digunakan, masing-masing dengan behavior berbeda.

### Navigate vs Push vs GoBack

```javascript
import * as React from 'react';
import { Button, View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
      <Button
        title="Go to Details"
        onPress={() => navigation.navigate('Details')}
      />
    </View>
  );
}

function DetailsScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
      
      {/* PUSH - Tambah screen baru ke stack */}
      <Button
        title="Go to Details... again"
        onPress={() => navigation.push('Details')}
      />
      
      {/* NAVIGATE - Navigasi ke screen (tidak duplikat) */}
      <Button 
        title="Go to Home" 
        onPress={() => navigation.navigate('Home')} 
      />
      
      {/* GOBACK - Kembali ke screen sebelumnya */}
      <Button 
        title="Go back" 
        onPress={() => navigation.goBack()} 
      />
      
      {/* POPTOTOP - Kembali ke screen paling awal */}
      <Button
        title="Go back to first screen"
        onPress={() => navigation.popToTop()}
      />
    </View>
  );
}

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

### Penjelasan Setiap Method

**1. navigation.navigate('ScreenName')**
```javascript
navigation.navigate('Details')
```
- Navigasi ke screen dengan nama tertentu
- Jika screen sudah ada di stack, akan kembali ke screen tersebut (tidak membuat duplikat)
- Paling sering digunakan untuk navigasi normal

**2. navigation.push('ScreenName')**
```javascript
navigation.push('Details')
```
- Selalu menambah screen baru ke stack, bahkan jika screen dengan nama sama sudah ada
- Berguna jika ingin membuat multiple instance dari screen yang sama
- Contoh: Detail produk → Detail produk related → Detail produk related lagi

**3. navigation.goBack()**
```javascript
navigation.goBack()
```
- Kembali ke screen sebelumnya di stack
- Sama seperti tombol back di Android atau swipe back di iOS
- Jika sudah di screen paling awal, tidak akan ada efek

**4. navigation.popToTop()**
```javascript
navigation.popToTop()
```
- Langsung kembali ke screen paling awal di stack
- Menghapus semua screen di antara screen saat ini dan screen awal

### Kapan Menggunakan Apa?

| Method | Kapan Digunakan |
|--------|-----------------|
| `navigate()` | Navigasi normal ke screen lain |
| `push()` | Perlu multiple instance dari screen yang sama |
| `goBack()` | Kembali ke screen sebelumnya |
| `popToTop()` | Langsung ke screen paling awal |

**Referensi:** [Difference between push and navigate](https://stackoverflow.com/questions/51090135/react-navigation-v2-difference-between-navigation-push-and-navigation-navigate)

---

## Passing Parameters ke Routes

Sering kali kita perlu mengirim data dari satu screen ke screen lain. React Navigation menyediakan cara untuk passing parameters.

### Mengirim Parameter

```javascript
function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
      <Button
        title="Go to Details"
        onPress={() => {
          // Kirim params ke Details screen
          navigation.navigate('Details', {
            itemId: 86,
            otherParam: 'anything you want here',
          });
        }}
      />
    </View>
  );
}
```

**Cara Kerja:**
- Parameter dikirim sebagai object di argument kedua `navigate()`
- Bisa mengirim berbagai tipe data: string, number, object, array, dll.

### Menerima Parameter

```javascript
function DetailsScreen({ route, navigation }) {
  // Destructure params dari route.params
  const { itemId, otherParam } = route.params;
  
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
      <Text>itemId: {JSON.stringify(itemId)}</Text>
      <Text>otherParam: {JSON.stringify(otherParam)}</Text>
      
      {/* Kirim params baru saat push */}
      <Button
        title="Go to Details... again"
        onPress={() =>
          navigation.push('Details', {
            itemId: Math.floor(Math.random() * 100),
          })
        }
      />
      
      <Button 
        title="Go to Home" 
        onPress={() => navigation.navigate('Home')} 
      />
      <Button 
        title="Go back" 
        onPress={() => navigation.goBack()} 
      />
    </View>
  );
}
```

**Cara Kerja:**
- Parameter diterima melalui `route.params`
- Gunakan destructuring untuk ambil parameter yang dibutuhkan
- `JSON.stringify()` digunakan untuk menampilkan object/array sebagai string

### Contoh Lengkap

```javascript
import * as React from 'react';
import { Button, View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

// Screen dengan form untuk input data
function HomeScreen({ navigation }) {
  const [userId, setUserId] = React.useState('123');
  const [userName, setUserName] = React.useState('John Doe');

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
      <Button
        title="View User Details"
        onPress={() => {
          // Kirim multiple params
          navigation.navigate('Details', {
            userId: userId,
            userName: userName,
            timestamp: new Date().getTime(),
          });
        }}
      />
    </View>
  );
}

// Screen yang menerima dan menampilkan data
function DetailsScreen({ route, navigation }) {
  // Ambil semua params
  const { userId, userName, timestamp } = route.params;
  
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
      <Text>User ID: {userId}</Text>
      <Text>User Name: {userName}</Text>
      <Text>Timestamp: {timestamp}</Text>
      
      <Button 
        title="Go back" 
        onPress={() => navigation.goBack()} 
      />
    </View>
  );
}

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

### Initial Params

Kita juga bisa set default parameter untuk suatu screen dengan `initialParams`.

```javascript
<Stack.Screen
  name="Details"
  component={DetailsScreen}
  initialParams={{ itemId: 42, userName: 'Guest' }}
/>
```

**Cara Kerja:**
- `initialParams` digunakan sebagai default value
- Jika ada parameter yang dikirim via `navigate()`, parameter tersebut akan override `initialParams`
- Berguna untuk set default values yang bisa di-override

### Updating Params

Kita juga bisa update parameter yang sudah ada menggunakan `setParams`.

```javascript
function DetailsScreen({ route, navigation }) {
  const { itemId } = route.params;

  return (
    <View>
      <Text>Item ID: {itemId}</Text>
      <Button
        title="Update Item ID"
        onPress={() => navigation.setParams({ itemId: 999 })}
      />
    </View>
  );
}
```

---

## useNavigation Hook

`useNavigation` adalah hook yang memungkinkan kita mengakses `navigation` object dari component mana saja, bahkan jika component tersebut bukan screen component.

**Referensi:** [useNavigation Hook](https://reactnavigation.org/docs/use-navigation/)

### Kapan Menggunakan useNavigation?

Gunakan `useNavigation` saat:
- Component berada di dalam nested component (bukan direct screen component)
- Tidak ingin pass `navigation` prop secara manual ke banyak level component

### Contoh Penggunaan

```javascript
import { useNavigation } from '@react-navigation/native';
import { Button, View, Text } from 'react-native';

// Component biasa (bukan screen component)
function CustomButton() {
  // Akses navigation tanpa props
  const navigation = useNavigation();

  return (
    <Button
      title="Go to Details"
      onPress={() => navigation.navigate('Details')}
    />
  );
}

// Screen component
function HomeScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
      {/* CustomButton bisa akses navigation tanpa props */}
      <CustomButton />
    </View>
  );
}
```

**Keuntungan:**
- Tidak perlu pass `navigation` prop secara manual
- Component lebih reusable
- Code lebih clean

**Catatan:**
`useNavigation` hanya bisa digunakan di component yang ada di dalam `NavigationContainer`.

---

## Stack Actions

Stack Actions adalah sekumpulan action methods untuk memanipulasi navigation stack dengan cara yang lebih advanced.

**Referensi:** [Stack Actions](https://reactnavigation.org/docs/stack-actions/)

### Push vs Replace

Ada 2 method utama dalam Stack Actions yang perlu dipahami:

#### 1. Push Action

```javascript
import { StackActions } from '@react-navigation/native';

// Menggunakan push
navigation.dispatch(StackActions.push('Details', { itemId: 42 }));

// Atau langsung dengan method push
navigation.push('Details', { itemId: 42 });
```

**Cara Kerja:**
- Menambah screen baru ke stack
- Screen sebelumnya tetap ada di stack
- User bisa kembali ke screen sebelumnya dengan tombol back
- Bisa membuat multiple instance dari screen yang sama

**Kapan Digunakan:**
- Ingin menambah screen baru ke history navigasi
- Perlu multiple instance dari screen yang sama (misalnya: detail → related detail → related detail)
- User harus bisa kembali ke screen sebelumnya

#### 2. Replace Action

```javascript
import { StackActions } from '@react-navigation/native';

// Menggunakan replace
navigation.dispatch(StackActions.replace('Details', { itemId: 42 }));

// Atau langsung dengan method replace
navigation.replace('Details', { itemId: 42 });
```

**Cara Kerja:**
- Mengganti screen saat ini dengan screen baru
- Screen lama dihapus dari stack
- User TIDAK bisa kembali ke screen sebelumnya
- Tidak ada duplikasi screen

**Kapan Digunakan:**
- Setelah login: replace screen login dengan home (user tidak bisa back ke login)
- Setelah onboarding: replace onboarding dengan home
- Form wizard yang sudah selesai: replace dengan hasil
- Saat tidak ingin user kembali ke screen sebelumnya

### Contoh Praktis

```javascript
import * as React from 'react';
import { Button, View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { StackActions } from '@react-navigation/native';

const Stack = createNativeStackNavigator();

// Screen Login
function LoginScreen({ navigation }) {
  const handleLogin = () => {
    // Setelah login berhasil, replace login screen dengan home
    // User tidak bisa back ke login screen
    navigation.dispatch(
      StackActions.replace('Home', {
        user: 'John Doe',
      })
    );
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Login Screen</Text>
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
}

// Screen Home
function HomeScreen({ route, navigation }) {
  const { user } = route.params || {};

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Welcome, {user}!</Text>
      
      {/* Push: User bisa kembali ke Home */}
      <Button
        title="View Details (with back)"
        onPress={() => navigation.push('Details')}
      />
      
      {/* Replace: User tidak bisa kembali ke Home */}
      <Button
        title="View Details (without back)"
        onPress={() => navigation.replace('Details')}
      />
    </View>
  );
}

// Screen Details
function DetailsScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
      <Button title="Go Back" onPress={() => navigation.goBack()} />
    </View>
  );
}

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

### Ringkasan Push vs Replace

| Aspek | Push | Replace |
|-------|------|---------|
| Stack History | Ditambahkan ke stack | Mengganti screen di stack |
| Tombol Back | Bisa kembali | Tidak bisa kembali |
| Use Case | Navigasi normal | Setelah proses yang tidak bisa di-undo |
| Multiple Instance | Ya | Tidak |

**Tips:**
- Gunakan **Push** untuk navigasi biasa dimana user perlu bisa kembali
- Gunakan **Replace** untuk flow yang sifatnya one-way (login, onboarding, dll)

---

## Preventing Going Back

Kadang kita perlu mencegah user untuk kembali ke screen sebelumnya, atau menampilkan confirmation dialog sebelum user meninggalkan screen.

**Referensi:** [Preventing Going Back](https://reactnavigation.org/docs/preventing-going-back)

### Use Case

- Form yang belum disimpan: Tanya user apakah mau discard changes
- Proses yang sedang berjalan: Warn user sebelum cancel
- Screen yang tidak boleh di-back: Seperti hasil payment success

### Implementasi Basic

```javascript
import * as React from 'react';
import { Alert, Button, View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

function EditScreen({ navigation }) {
  const [hasUnsavedChanges, setHasUnsavedChanges] = React.useState(false);

  React.useEffect(() => {
    // Prevent back navigation jika ada unsaved changes
    const unsubscribe = navigation.addListener('beforeRemove', (e) => {
      if (!hasUnsavedChanges) {
        // Jika tidak ada perubahan, allow navigation
        return;
      }

      // Prevent default action (back)
      e.preventDefault();

      // Tampilkan confirmation dialog
      Alert.alert(
        'Discard changes?',
        'You have unsaved changes. Are you sure you want to discard them?',
        [
          { text: "Don't leave", style: 'cancel', onPress: () => {} },
          {
            text: 'Discard',
            style: 'destructive',
            onPress: () => navigation.dispatch(e.data.action),
          },
        ]
      );
    });

    return unsubscribe;
  }, [navigation, hasUnsavedChanges]);

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Edit Screen</Text>
      <Text>Has unsaved changes: {hasUnsavedChanges ? 'Yes' : 'No'}</Text>
      
      <Button
        title="Make Changes"
        onPress={() => setHasUnsavedChanges(true)}
      />
      
      <Button
        title="Save Changes"
        onPress={() => {
          setHasUnsavedChanges(false);
          Alert.alert('Changes saved!');
        }}
      />
      
      <Button
        title="Go Back"
        onPress={() => navigation.goBack()}
      />
    </View>
  );
}

function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
      <Button
        title="Go to Edit"
        onPress={() => navigation.navigate('Edit')}
      />
    </View>
  );
}

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Edit" component={EditScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
```

**Penjelasan:**

1. **beforeRemove Event**: Listener yang dipanggil sebelum screen di-remove dari stack
2. **e.preventDefault()**: Mencegah default back action
3. **Alert.alert()**: Menampilkan confirmation dialog
4. **navigation.dispatch(e.data.action)**: Melanjutkan action back jika user confirm

**Tips:**
- Jangan overuse fitur ini karena bisa mengganggu user experience
- Gunakan hanya untuk kasus yang benar-benar penting (unsaved data, payment process, dll)

---

## Referensi dan Resources

### Official Documentation
- [React Navigation Official Docs](https://reactnavigation.org/docs/getting-started)
- [Nesting Navigators](https://reactnavigation.org/docs/nesting-navigators)
- [Navigation Lifecycle](https://reactnavigation.org/docs/navigation-lifecycle)
- [Stack Actions](https://reactnavigation.org/docs/stack-actions/)
- [Preventing Going Back](https://reactnavigation.org/docs/preventing-going-back)

### Tools dan Playground
- [Expo Snack](https://snack.expo.dev/) - Online playground untuk testing React Native code

### Tutorial dan Artikel
- [Nested Navigation Tutorial](https://medium.com/@tbgarza2/nested-navigation-react-navigation-4518c273b71e)
- [React Native Navigation Library](https://wix.github.io/react-native-navigation/docs/installing)

### Tips untuk Belajar

1. **Mulai dari yang Simple**: Jangan langsung bikin struktur navigasi yang kompleks. Mulai dengan Stack Navigator sederhana.

2. **Eksperimen di Expo Snack**: Gunakan Expo Snack untuk coba-coba tanpa harus setup project lokal.

3. **Pahami Lifecycle**: Penting untuk pahami kapan component di-mount, di-focus, dan di-unmount.

4. **Lihat Example Code**: React Navigation punya banyak example di docs mereka. Lihat dan coba modifikasi.

5. **Debug dengan Console.log**: Gunakan `console.log` untuk tracking navigation flow dan params.

---

**Selamat belajar React Navigation!** 🚀

Jangan lupa untuk praktek langsung dan eksperimen dengan berbagai kombinasi navigator. Trial and error adalah cara terbaik untuk memahami cara kerja navigation di React Native!
