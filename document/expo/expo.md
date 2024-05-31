# Expo 

adalah tool yang dapat membantu kita untuk membuat App android dan IOS. 

cara instalasi:

```
npx create-expo-app my-app


npx expo start
```


## tool tambahan

install `Expo Go` untuk melakukan testing didalam android


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

# Reference:
- https://www.freecodecamp.org/news/responsive-layout-react-native/ | App sangat sederhana <Begginer Recommended>