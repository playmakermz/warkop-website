# Data management practice

## 1.1 Membersihkan data 

```
import pandas as pd

data = {
    'Donor_ID': [1, 2, 3, 4, 5, 6, 7],
    'Donor_Name': ['Serra', 'Unknown', 'Elara', None, 'Merchant_A', None, 'Priestess_B'],
    'Amount': [5000, None, 7500, 3000, None, 6000, 4500],
    'Donation_Date': ['2025-01-15', '2025-01-16', '2025-01-17', '2025-01-18', '2025-01-19', None, '2025-01-21'],
    'Region': ['Lumora', None, 'Harbor', 'Lumora', 'Capital', None, 'Lumora']
}

df = pd.DataFrame(data)

# Check null
print(df.isnull())
print(df.isnull().sum())

print("Data loaded successfully!")
print(df.columns)  # Print all column names EXACTLY as they appear
print(df.head())   # Show first 5 rows
print(repr(df.columns.tolist()))

# Clean data


name = 'Amount'
df[name] = df[name].fillna(df[name].median(skipna=True))

df = df.dropna(subset=['Donation_Date'])
# it's little sad to drop but it need to do. 

df['Region'] = df['Region'].fillna(df['Region'].mode()[0])

print(df.head())

df.to_csv('temple_donation_copy.csv', index = False)

# Still same error, celestine!
#Raise KeyError(key) from err
#KeyError: 'Amount'




```
