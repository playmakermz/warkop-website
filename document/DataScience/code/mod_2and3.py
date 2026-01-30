import pandas as pd
import numpy as np
from scipy import stats

# MESSY VOLUNTEER DATA
data = {
    'Volunteer_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 12, 13, None, 14, 15, 16, 17, 18],
    'Volunteer_Name': ['Serra', 'john_smith', 'Elara', None, 'merchant_b', 'serra', 'priestess_c',
                       'David Lee', 'unknown', 'Sarah', 'Serra', 'michael_j', 'Anna Wong', 'tom_brown',
                       'Jane Doe', 'robert_park', 'lisa_anderson', 'chris_martin', 'emma_jones', 'david_kim'],
    'Hours_Volunteered': [40, None, 35, 50, 45, 40, 38, None, 30, 42, 40, 48, 36, 52, 41, 39, 44, 37, 46, 43],
    'Start_Date': ['2025-01-15', '2025-01-16', '2025-01-17', '2025-01-18', '2025-01-19',
                   '2025-01-15', '2025-01-21', None, '2025-01-23', '2025-01-24',
                   '2025-01-15', '2025-01-26', '2025-01-27', '2025-01-28', '2025-01-29',
                   None, '2025-01-31', '2025-02-01', '2025-02-02', '2025-02-03'],
    'Volunteer_Region': ['Lumora', 'Harbor', None, 'Capital', 'Lumora', 'Lumora', 'Harbor',
                        'Capital', None, 'Lumora', 'Lumora', 'Harbor', 'Capital', 'Lumora',
                        'Harbor', 'Capital', 'Lumora', 'Harbor', 'Capital', 'Lumora']
}

df = pd.DataFrame(data)

# Atur format dengan standart kapital dan hapus spasi
df['Volunteer_Name'] = df['Volunteer_Name'].str.strip()
df['Volunteer_Name'] = df['Volunteer_Name'].str.title()
# Example: 'john_doe' → 'John_Doe'

# Hapus duplikat persis
df = df.drop_duplicates(keep='first')  # Keep first occurrence
# Kabari kalau ada duplikat yang mirip, tetapi dengan id yang berbeda
sus = df[df.duplicated(subset=['Volunteer_Name', 'Hours_Volunteered'], keep=False)]
print(f"/Data ini perlu dicaritau secara manual: {sus}") 


# Menyelesaikan masalah data hilang 
df['Volunteer_ID'] = df['Volunteer_ID'].fillna(df['Volunteer_ID'].max() + 1)
df['Volunteer_Name'] = df['Volunteer_Name'].fillna('Unknown')
df['Hours_Volunteered'] = df['Hours_Volunteered'].fillna(df['Hours_Volunteered'].median())
df = df.dropna(subset=['Start_Date']) # Hapus baris
df['Volunteer_Region'] = df['Volunteer_Region'].fillna(df['Volunteer_Region'].mode()[0])

# Prhitungan statistik 
print(f""" Analze the hours

mean: {df['Hours_Volunteered'].mean()}
median: {df['Hours_Volunteered'].median()}
mode: {df['Hours_Volunteered'].mode()[0]}
""")


print(f"""

range: {df['Hours_Volunteered'].max() - df['Hours_Volunteered'].min()}
variance: {df['Hours_Volunteered'].var()}
standard deviation: {df['Hours_Volunteered'].std()}
mean: {df['Hours_Volunteered'].mean()}

""")

print(f"""

skew: {stats.skew(df['Hours_Volunteered'])}
kurtosis: {stats.kurtosis(df['Hours_Volunteered'])}
""")

# Check if data is skewed
mean = df['Hours_Volunteered'].mean()
median = df['Hours_Volunteered'].median()
if mean > median:
    print("Mean > Median: RIGHT-SKEWED")
elif mean < median:
    print("Mean < Median: LEFT-SKEWED")
else:
    print("Mean ≈ Median: SYMMETRIC")


# Buat Baca, simpan aja ini terus dibagian bawah code agar bisa kita jadikan bacaan dan test.
# Check final status
print(df.isnull().sum())      # Should be all zeros
print(df.duplicated().sum())  # Should be zero

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)
print(df)           # First 5 rows
print(df.info())           # Data types & memory
print(df.describe())       # Basic statistics
print(df.isnull().sum())   # Count missing values

