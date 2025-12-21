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

# Part 1
print(""" 

1. Row Count: 20. Column: 5 
2. Column missing value: Volunteer_ID, Volunteer_Name, Hours_Volunteered, Start_Date, Volunteer_Region
3. row apperas duplicate: row 0 and 5. Serra and serra with same Hours_Volunteered
4. From: float, string, float, date 
""")

# ========== Part 2 ===================

"""
"Now clean the data using strategies from Module 2:"

Remove exact duplicate rows
Flag suspicious duplicates (same name/hours but different IDs)
Handle missing Volunteer_ID (decide: fill or drop?)
Handle missing Volunteer_Name (use placeholder)
Handle missing Hours_Volunteered (use median)
Handle missing Start_Date (decide: fill or drop?)
Handle missing Volunteer_Region (use mode)
Standardize all names (proper capitalization, remove underscores)
Verify no missing values remain
Save the cleaned data to CSV
"""

# We should fix the word first.
df['Volunteer_Name'] = df['Volunteer_Name'].str.title()
df['Volunteer_Name'] = df['Volunteer_Name'].str.strip()


print(len(df))
df = df.drop_duplicates(keep='first')
# Remove exact duplicate. 
print(len(df))

# Flag issue
# Check duplicate
print("\nDuplicate Rows:")
print(df[df.duplicated()])

sus = df[df.duplicated(subset=['Volunteer_Name', 'Hours_Volunteered'], keep=False)]
print("\nDuplicate Rows: " + str(sus))

# Manual flag
if len(sus) > 0:
    print("\n⚠️  WARNING: These entries have matching name/amount/date but different IDs.")
    print("Manual review recommended before deciding if they're legitimate or errors.")

# ======= Remove or manage none.
df['Volunteer_ID'] = df['Volunteer_ID'].fillna(df['Volunteer_ID'].max() + 1)
# Because as we can see, everyone is already got their own id except Jane Doe. So we could manually input the id based on empty id. 

df['Volunteer_Name'] = df['Volunteer_Name'].fillna('Unknown')
# This was label that mean we need a direct manual investigation for the name.

df['Hours_Volunteered'] = df['Hours_Volunteered'].fillna(df['Hours_Volunteered'].median())
# Just use median to predict the hours

df['Start_Date'] = df['Start_Date'].fillna(df['Start_Date'].mode()[0])
# We predict based on mode. when people usually.

df['Volunteer_Region'] = df['Volunteer_Region'].fillna(df['Volunteer_Region'].mode()[0])
# We predict based on mode. when people usually.


# Clean complete
# ============= Read the data 
print(f""" Analze the hours 

mean: {df['Hours_Volunteered'].mean()}
median: {df['Hours_Volunteered'].median()}
mode: {df['Hours_Volunteered'].mode()[0]}
""")

print("It means they data was close and consistance. No suprsising outlier. Also it means the voluntree was equally dedicated")

# ============ Descriptive statistic 

print(f""" 

range: {df['Hours_Volunteered'].max() - df['Hours_Volunteered'].min()}
variance: {df['Hours_Volunteered'].var()}
standard deviation: {df['Hours_Volunteered'].std()}
mean: {df['Hours_Volunteered'].mean()}

Interpret: yes, the voluntree was consistent without any suprise outlier
""")

# ============= Shape 

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

print("No, we got what we predict. There's only so little near outlier like 50.0 or 52.0 . But it's still whithin range of expetance")




# Check final status
print(df.isnull().sum())      # Should be all zeros
print(df.duplicated().sum())  # Should be zero
print("=== RAW DATA ===")
print(df)
print(f"\nShape: {df.shape}")
print(f"\nMissing Values:\n{df.isnull().sum()}")
