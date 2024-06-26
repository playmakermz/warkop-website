# Expo 

## React Native 

React Native adalah framework open-source yang dapat membantu kita untuk melakukan pengembangan suatu aplikasi mobile dengan javascriopt. 

Kelebihan React Native:
- **Pengembangan lintas platfrom**: Satu code, bisa digunakan untuk android atau IOS. 

## Expo 

Expo adalah aplikasi yang dibangung diatas React Native. Expo dapat digunakan untuk mempercepat pengembangan aplikasi dengan React Native. 

Keuntungan dengan EXPO:
- Dengan Expo, kita bisa melewati beberapa configurasi yang diperlukan untuk membuat app. 
- "Expo SDK", menyediakan Module dan library yang siap pakai seperti "navigasi" dan lain-lain. 
- "Expo CLI", Digunakan untuk membangun dan menjalankan app.
- "Expo-Go", digunakan untuk membantu kita menjalankan aplikasi tanpa harus melakukan build dan deployment.



***

adalah tool yang dapat membantu kita untuk membuat App android dan IOS. 

Untuk IDX tetap pakai `yarn`

cara instalasi dengan yarn:
```
npm install -g yarn

yarn add global expo-cli
yarn add global expo
# =================== atau seperti ini =============
npm install expo-cli
npm install expo

npx expo-cli upgrade // jika mengalami error karena version
```
ref: https://medium.com/@blackpintz/how-to-install-expo-cli-using-yarn-92efe8ed78f5

```
npx create-expo-app my-app


# =========== Jalankan App pada website ===========
npm run web
```


## tool tambahan

install `Expo Go` untuk melakukan testing didalam android


***
# Informasi 
***

jika menggunakan github codespace check area ini 
```
/app/(tabs)/index.tsx
```

contoh code 

```Js
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


***
# Component Inti React Native
***
Beberapa Component bawaan dari "Expo"

1. Daftar Component dasar dalam UI 
- view
- Text 
- StyleSheet
- Image
- TextInput

2. View yang dapat scroll
- ScrollView
- FlatList

3. View yang dapat touch 
- Button 
- TouchableOpacity

# Component dasar 
Berserta penjelasan fungsi 

### view 
```Js
import { View, Text } from 'react-native'
... 

return (
<View>

<View style={{ alignItems: 'center' }}>
        <Text style={{ fontSize: 40 }}>Hello React Native</Text>
      </View>

<View style={{ alignItems: 'center' }}>
        <Text style={{ fontSize: 40 }}>Hello React Native</Text>
      </View>

</View>
)
```

Mereka berfungsi sebagai container pembungkus. sama seperti kita menggunakan `<div>`

### Text 

```Js
<Text style={{ fontSize: 30 }}>

<Text>Ini ukuran akan berubah <Text>

<View>
<Text>Ini ukuran tidak akan berubah </Text>
</View>

</Text>
```

ini adalah seoperti bentuk string. Kita tidak bisa memasukan string kepada component `<View>`. Cara diatas dapat digunakan untuk mewariskan style kepada `Text` dibawahnya, kecuali terdapat text didalam view atau component lain.

### StyleSheet

```Js
import { StyleSheet, Text, View } from 'react-native'

...

<Text style={styles.title}>React Native - Prograte</Text>


const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 24,
    backgroundColor: '#eaeaea',
  },})
```

Infile CSS 

### Image 

```Js
import { View, Image, StyleSheet } from 'react-native'

 <Image style={styles.image} source={require('./assets/icon.png')} />
```
Sama seperti Tag `image`

Ref: https://www.tutorialspoint.com/react_native/react_native_images.htm

### TextInput
```Js 
import { View, StyleSheet, TextInput } from 'react-native'

const [name, setName] = useState()

<TextInput
        style={styles.input}
        placeholder="Masukan Nama"
        onChangeText={setName}
        value={name}
      />
```

Adalaj bentuk form. Untuk lebih detail mengenai form TextInput: https://reactnative.dev/docs/textinput#props

***
# Bagian View dan Scroll 
***

**Attribute** special untuk component container: 

```Js 
contentContainerStyle={styles.wrapper}
```

Berfungsi sebagai penerima css bagi container. 

ref: https://stackoverflow.com/questions/46032604/scrollview-child-layout-must-be-applied-through-the-contentcontainerstyle-prop

### ScrollView

adalah suatu component yang dapat membantu kita untuk membungkus content yang melewati batas dari size screen.

```Js
import { StyleSheet, View, ScrollView, Text } from 'react-native'

<View style={styles.container}>
      <ScrollView style={styles.scrollView}>
        <Text style={styles.text}>
          {/* Tuliskan teks panjang di sini */}
        </Text>
      </ScrollView>
    </View>
```

Reference: https://reactnative.dev/docs/using-a-scrollview

### FlatList

menyerupai dengan ScrollView, tetapi memiliki perbedaan kapan harus digunakan. Dimana `FlatList` digunakan saat kita memangil banyak item dari array. 

```Js
const App = () => {
  const renderItem = ({ item }) => <Item title={item.title} />

  return (
    <View style={styles.container}>
      <FlatList
        data={items}
        renderItem={renderItem}
        keyExtractor={(item) => item.id}
      />
    </View>
  )
}

```

Break: dimana pada fungsi `App()` kita memangil item satu demi satu. 
- `data` - adalah item spesifik 
- `renderItem` - adalah list item 
- `keyExtractor` - adalah `key.id` pada react biasa. konsep untuk penanda item list

Ref: https://reactnative.dev/docs/flatlist

### perbedaan scrollView dan FlatList

- ScrollView digunakan jika data yang kita render sedikit, meningkatkan performa app 
- FlatList digunakan disaat kita merender data yang super besar dan banyak.


***
# Button and TouchableOpacity
***

### Button 

```Js
import { View, Button, Alert, StyleSheet } from 'react-native'

<Button
          title="Color Button"
          color="#f194ff"
          onPress={() => Alert.alert('Color Button')}
        />
```

disini button bisa kita gunakan seperti biasa, pemangilan fungsi dan lain-lain.

### TouchableOpacity

```Js 
import { View, StyleSheet, TouchableOpacity, Text }

<TouchableOpacity style={styles.button} onPress={onPress}>
        <Text style={styles.buttonText}>Press Here</Text>
      </TouchableOpacity>
```

adalah sebuah wrapper seperti `div` dimana kita bisa membuatnya sebagai pengganti button. seperti pada HTML biasa kita bisa menggunakan `div` sebagai alternative tag `button`

***
# expo-linear-gradient
***

Instalasi 
```js 
// npm install expo-linear-gradient
// Instalasi 

import LinearGradient from 'expo-linear-gradient';

<LinearGradient
  colors={['#FF0000', '#FFFF00', '#00FF00']}
  start={[0, 0]}
  end={[1, 1]}
>
  <View>
    {/* Content to display within the gradient */}
  </View>
</LinearGradient>

```

Pada contoh diatas, akan dibuat suatu transisi dari kiri ke kanan. dimana component semua item pada component "view". 

Manfaat: 
- Meningkatkan kualitas visual 
- dapat kita gunakan untuk memberikan Highlight pada area spesifik. 

Ref: 
- https://github.com/react-native-linear-gradient/react-native-linear-gradient | 
- https://codesandbox.io/s/react-hv1g9e | contoh hasil
- https://docs.expo.dev/versions/latest/sdk/linear-gradient/ | Contoh Official

***
# ImageBackground 
***
```Js 
import {ImageBackground, StyleSheet, Text, View} from 'react-native';

const image = {uri: 'https://legacy.reactjs.org/logo-og.png'};

const App = () => (
  <View style={styles.container}>
    <ImageBackground source={image} resizeMode="cover" style={styles.image}>
      <Text style={styles.text}>Inside</Text>
    </ImageBackground>
  </View>
);
```

berfungsi untuk menambahkan item didalam gambar. 

ref: https://reactnative.dev/docs/imagebackground

***
# FontAwesome (Logo)
***

```Js 

import { FontAwesome } from '@expo/vector-icons'

<FontAwesome name="star" size={16} color="yellow" />
```

Ref: https://icons.expo.fyi/Index 

***
# catatan tambahan
***
### deklarasi state
state harus kita deklarasi didalam function, tidak boleh diluar function.

***
***
# Note 
- [Simpel todo App](./note-app-expo.md)
- [Api-test](../project-react/Api-Axios.md)
- [Expo Navigator](../project-react/Expo-Navigator.md)


# Reference:
- https://www.freecodecamp.org/news/responsive-layout-react-native/ | App sangat sederhana <Begginer Recommended>

- [React Expo Debugging](https://shift.infinite.red/start-using-reactotron-in-your-expo-project-today-in-3-easy-steps-a03d11032a7a)
