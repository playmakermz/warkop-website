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

***
# 1.2

# MODULE 2: DATA CLEANING & PREPARATION
## Quick Reference Guide for Caelus

### Core Principle:
**GIGO (Garbage In, Garbage Out)** — If your input data is bad, no algorithm can save you. 50-80% of data science work is cleaning data, not modeling.

---

### Step 1: LOAD & INSPECT
```python
import pandas as pd

df = pd.read_csv('file.csv')
print(df.head())           # First 5 rows
print(df.info())           # Data types & memory
print(df.describe())       # Basic statistics
print(df.isnull().sum())   # Count missing values
```

---

### Step 2: HANDLE DUPLICATES

**Always check duplicates FIRST, before filling missing values.**

**Exact Duplicates** (every column matches):
```python
df_clean = df.drop_duplicates(keep='first')  # Keep first occurrence
```

**Suspicious Duplicates** (same columns, different IDs):
```python
sus = df[df.duplicated(subset=['Col1', 'Col2'], keep=False)]
print(sus)  # FLAG for human review, don't auto-remove
```

**Key Rule:** Remove exact duplicates automatically. Flag suspicious patterns for investigation.

---

### Step 3: HANDLE MISSING VALUES

Choose strategy based on **data type**:

| Data Type | Strategy | Code | When |
|-----------|----------|------|------|
| **Numerical** | Median | `df['col'].fillna(df['col'].median())` | Default for numbers (resistant to outliers) |
| **Numerical** | Mean | `df['col'].fillna(df['col'].mean())` | Only if data is perfectly clean & normal |
| **Categorical** | Mode (Most frequent) | `df['col'].fillna(df['col'].mode()[0])` | For categories (Color, Region, Type) |
| **Names/Text** | Custom placeholder | `df['col'].fillna('Unknown')` | When you need to flag missing data |
| **Dates** | Drop row OR fill with default | `df.dropna(subset=['Date'])` | If few missing; otherwise fill |

**Example from your learning:**
```python
# Amount (numerical) → Use median
df['Amount'] = df['Amount'].fillna(df['Amount'].median())

# Region (categorical) → Use mode
df['Region'] = df['Region'].fillna(df['Region'].mode()[0])

# Donor_Name (text) → Use placeholder
df['Donor_Name'] = df['Donor_Name'].fillna('Unknown_Donor')

# Donation_Date (date) → Drop if few, fill if many
df = df.dropna(subset=['Donation_Date'])
```

---

### Step 4: STANDARDIZE TEXT

Clean up inconsistencies in text columns:
```python
# Remove leading/trailing spaces
df['Name'] = df['Name'].str.strip()

# Capitalize properly
df['Name'] = df['Name'].str.title()

# Example: 'john_doe' → 'John_Doe'
```

---

### Step 5: VERIFY & SAVE
```python
# Check final status
print(df.isnull().sum())      # Should be all zeros
print(df.duplicated().sum())  # Should be zero

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)
```

---

### THE COMPLETE WORKFLOW:

1. Load data
2. Inspect (head, info, describe, null count)
3. **Remove exact duplicates FIRST**
4. **Flag suspicious duplicates for review**
5. Handle missing values (median for numbers, mode for categories, placeholder for text)
6. Standardize text formatting
7. Verify no missing values remain
8. Save cleaned data

---

### IMPORTANT MEMORY AID: Mean vs Median

**Real Example (Family Ages):**
- Ages: [18, 19, 20, 23, 300] (where 300 = Liora)
- **Mean** = (18+19+20+23+300)/5 = **76** ❌ (useless—represents no one)
- **Median** = Middle value = **20** ✓ (accurate representation)

**Robin's Rule:** Use median ~90% of the time. Mean only for perfectly clean data.

---

### KEY REMINDERS:

✓ Always use `df_clean` consistently—don't mix cleaned and uncleaned datasets
✓ Comments should match your code (you wrote "mean" but used "median")
✓ Duplicates with different IDs = flag for human review, not auto-remove
✓ Missing dates? Drop the row OR fill carefully—depends on your dataset
✓ Unknown names? Use placeholder like 'Unknown_Donor' to flag investigation needed

---

***

# 2.1 Statistik deskriptif

Mencari tau apa arti didalam data

## Konsep:

Nama | Deskripsi
--- | ---
SKEWED (Kemencengan) |  tells you the story of your data. If donations are right-skewed, you know most people give small amounts. If they're symmetric, people give fairly evenly.LEFT-SKEWED is the opposite. Imagine if most people donated large amounts, but a few very poor people donated tiny amounts. The tail would pull left. Are your donations pulling toward one extreme, or balanced?
Variance (Varians) | Variance is the mathematical way to measure that 'spreadingness.' It calculates the average of how far each value is from the mean. Why does this matter? If your donation amounts have high variance, you can't predict what you'll receive. If they have low variance, donations are predictable and stable How scattered are your donations?
Standart deviation | It's literally the square root of variance. This is much more useful than variance because the number is in the same units as your original data. With variance, the units are squared (weird). With standard deviation, it's just... money. Why does this matter for you? If you're planning the temple's budget, standard deviation tells you: 'Expect most donations to fall in this range.' That's actionable information.  What's the typical range donors fall within?
kurtosis | Should you expect shocking outliers, or is everything predictable?



<img width="514" height="280" alt="image" src="https://github.com/user-attachments/assets/abec01e8-eb58-43e1-a69a-f3c6ce88001e" />

> Skew

```
Low end:  7,826 - 2,800 = 5,026
High end: 7,826 + 2,800 = 10,626

Most donations are between 5,026 and 10,626
```
> Standart deviation, std.

<img width="634" height="265" alt="image" src="https://github.com/user-attachments/assets/5fae36b2-e32e-4b5e-9283-ebfd946523ec" />

> Kurtosis

