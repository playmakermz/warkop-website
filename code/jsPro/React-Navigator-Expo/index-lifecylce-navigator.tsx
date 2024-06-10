import * as React from 'react';
import { Button, View, Text } from 'react-native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { useFocusEffect } from '@react-navigation/native';

const Tab = createBottomTabNavigator(); // Main Container
const SettingsStack = createNativeStackNavigator(); // child container
const HomeStack = createNativeStackNavigator(); // child container

// ============== App =============

function App(){
  return (
    <Tab.Navigator screenOptions={{ headerShown: false }}>
 <Tab.Screen name="First">

 {() => (
            <SettingsStack.Navigator>
              <SettingsStack.Screen name="Settings" component={SettingsScreen}/>
              <SettingsStack.Screen name="Profile" component={ProfileScreen} />
            </SettingsStack.Navigator>
          )}

 </Tab.Screen>
 <Tab.Screen name="Second">

 {() => (
            <HomeStack.Navigator>
              <HomeStack.Screen name="Home" component={HomeScreen} />
              <HomeStack.Screen name="Details" component={DetailsScreen} />
            </HomeStack.Navigator>
          )}

</Tab.Screen>

    </Tab.Navigator>
  )
}

// =========== SettingsScreen ==========
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

// =========== ProfileScreen ==========
function ProfileScreen({ navigation }) {
  useFocusEffect(
    React.useCallback(() => {
      alert('Screen was focused');
      // Do something when the screen is focused
      // Awal masuk screen
      return () => {
        alert('Screen was unfocused');
        // Do something when the screen is unfocused
        // keluar dari screen
        // Useful for cleanup functions
      };
    }, [])
  )}

// ============== HomeScreen ============
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

// =========== DetailScreen ==========
function DetailsScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
      <Button
        title="Go to Details... again"
        onPress={() => navigation.push('Details')}
      />
    </View>
  );
}




export default App
