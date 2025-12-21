# Data management practice

# MODULE 2: DATA CLEANING & PREPARATION
## Quick Reference Guide for Caelus

### Core Principle:
**GIGO (Garbage In, Garbage Out)** – Jika data input buruk, tidak ada algoritma yang bisa menyelamatkan. 50-80% pekerjaan data science adalah membersihkan data, bukan modeling.

---

## Urutan Pengelolahan Dataset

### 1. ANALISA DATASET SECARA MANUAL

```python
import pandas as pd

df = pd.read_csv('file.csv')
print(df.head())           # Lihat 5 baris pertama
print(df.info())           # Tipe data & memory
print(df.describe())       # Statistik dasar
print(df.isnull().sum())   # Hitung nilai yang hilang
```

**Tujuan:** Pahami struktur, tipe data, dan masalah umum dalam dataset.

---

### 2. ATUR FORMAT ITEM STRINGS DALAM KOLOM
Mulai dari huruf besar kecil dan spasi kosong:

```python
# Hapus spasi di awal dan akhir
df['Name'] = df['Name'].str.strip()

# Kapitalisasi dengan benar (Title Case)
df['Name'] = df['Name'].str.title()

# Contoh: 'john doe' → 'John Doe'
# Contoh: '  john  ' → 'John'
```

**Tujuan:** Standarisasi format teks agar konsisten di seluruh dataset.

---

### 3. MENGURUSI DUPLIKAT PERSIS
Mulai dari ID dan seluruhnya:

```python
# Hapus duplikat yang benar-benar sama di semua kolom
df_clean = df.drop_duplicates(keep='first')  # Simpan kemunculan pertama

# Verifikasi
print(df.duplicated().sum())  # Harus menunjukkan 0
```

**Kunci:** Hapus duplikat persis secara otomatis. Jangan ragu karena ini adalah data yang identik 100%.

---

### 4. MENANDAI YANG MIRIP TETAPI BISA DI INVESTIGASI
(Suspicious Duplicates - sama di beberapa kolom, tapi ID berbeda):

```python
# Cari duplikat berdasarkan kolom tertentu
sus = df_clean[df_clean.duplicated(subset=['Col1', 'Col2'], keep=False)]
print(sus)  # TANDAI untuk review manual, jangan auto-remove

# Simpan ke file terpisah untuk investigasi
sus.to_csv('suspicious_duplicates.csv', index=False)
```

**Kunci:** Tandai untuk review manusia. Ini mungkin data berbeda dengan kebetulan sama, atau benar-benar duplikat yang perlu diteliti lebih lanjut.

---

### 5. MANAGE DAN MENGURUSI DATA YANG HILANG

Pilih strategi berdasarkan **tipe data**:

| Tipe Data | Strategi | Kode | Kapan |
|-----------|----------|------|-------|
| **Numerik** | Median | `df['col'].fillna(df['col'].median())` | Default untuk angka (tahan terhadap outlier) |
| **Numerik** | Mean | `df['col'].fillna(df['col'].mean())` | Hanya jika data sangat bersih & normal |
| **Kategori** | Mode (Paling sering) | `df['col'].fillna(df['col'].mode()[0])` | Untuk kategori (Warna, Region, Tipe) |
| **Nama/Teks** | Placeholder khusus | `df['col'].fillna('Unknown')` | Ketika perlu menandai data hilang |
| **Tanggal** | Drop baris ATAU isi default | `df.dropna(subset=['Date'])` | Jika sedikit; jika banyak, isi dengan hati-hati |

**Contoh implementasi:**

```python
# Amount (numerik) → Gunakan median
df_clean['Amount'] = df_clean['Amount'].fillna(df_clean['Amount'].median())

# Region (kategori) → Gunakan mode
df_clean['Region'] = df_clean['Region'].fillna(df_clean['Region'].mode()[0])

# Donor_Name (teks) → Gunakan placeholder
df_clean['Donor_Name'] = df_clean['Donor_Name'].fillna('Unknown_Donor')

# Donation_Date (tanggal) → Drop jika sedikit, isi jika banyak
df_clean = df_clean.dropna(subset=['Donation_Date'])
```

**Ingat - Mean vs Median (Real Example):**
- Usia: [18, 19, 20, 23, 300] (300 = error/outlier)
- **Mean** = (18+19+20+23+300)/5 = **76** ✗ (tidak masuk akal)
- **Median** = Nilai tengah = **20** ✓ (akurat)

**Aturan Robin:** Gunakan median ~90% waktu. Mean hanya untuk data yang sangat bersih.

---

### 6. PASTIKAN TIDAK ADA NILAI KOSONG

```python
print(df_clean.isnull().sum())  # Semua harus 0
```

Jika masih ada nilai kosong, kembali ke langkah 5. Pastikan setiap kolom bersih sebelum melanjutkan.

---

### 7. PRINT DAN SAVE DATA

```python
# Verifikasi status akhir
print(df_clean.head())         # Lihat hasil akhir
print(df_clean.info())         # Tipe data final
print(df_clean.isnull().sum()) # Konfirmasi no nulls
print(df_clean.duplicated().sum())  # Konfirmasi no duplicates

# Simpan data yang sudah dibersihkan
df_clean.to_csv('cleaned_data.csv', index=False)
print("✓ Data berhasil disimpan sebagai 'cleaned_data.csv'")
```

---

## RINGKASAN WORKFLOW LENGKAP:

1. ✓ Analisa dataset secara manual
2. ✓ Atur format item strings dalam kolom
3. ✓ Mengurusi duplikat persis
4. ✓ Menandai yang mirip tetapi bisa di investigasi
5. ✓ Manage dan mengurusi data yang hilang
6. ✓ Pastikan tidak ada nilai kosong
7. ✓ Print dan save data

---

## POIN PENTING:

✓ Selalu gunakan `df_clean` secara konsisten – jangan campur dataset bersih dan kotor
✓ Komentar harus sesuai dengan kode (jangan tulis "mean" tapi pakai "median")
✓ Duplikat persis = hapus otomatis. Duplikat mirip = tandai untuk review manual
✓ Data tanggal kosong? Drop atau isi dengan hati-hati sesuai konteks
✓ Nama tidak diketahui? Gunakan placeholder seperti 'Unknown_Donor' untuk menandai investigasi diperlukan
***

# 3.1 Statistik deskriptif

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


## 3.2

# MODULE 3: STATISTIK DESKRIPTIF (DESCRIPTIVE STATISTICS)
## Understanding Your Data Through Numbers

### Core Concept:
Descriptive statistics help us **understand the story** our data is telling through numbers instead of just looking at raw values. It answers questions like:
- What's typical?
- How scattered is the data?
- Are there outliers?
- Is the data balanced or lopsided?

---

## 1. UKURAN TENDENSI SENTRAL (Measures of Central Tendency)

These tell us where the "center" or "typical" value of the data is.

### MEAN (Rata-rata)
**Definition:** The average. Sum all values and divide by count.

**Formula:**
```
Mean = (x₁ + x₂ + x₃ + ... + xₙ) / n
```

**Python:**
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'Donation': [5000, 7500, 3000, 12000, 6500]})
mean_value = df['Donation'].mean()
print(f"Mean: {mean_value}")  # Output: 6800.0
```

**When to use:** When data is clean with no extreme outliers.

**Important:** Mean is sensitive to outliers. One huge value can pull the average up significantly.

---

### MEDIAN (Nilai Tengah)
**Definition:** The middle value when data is sorted from smallest to largest.

**Python:**
```python
median_value = df['Donation'].median()
print(f"Median: {median_value}")  # Output: 6500.0
```

**When to use:** Default choice for most real-world data. Resistant to outliers.

**Why it matters:** If you have [100, 200, 300, 400, 50000], the mean is 10200 (useless). The median is 300 (accurate).

---

### MODE (Modus / Paling Sering)
**Definition:** The value that appears most frequently in the dataset.

**Python:**
```python
mode_value = df['Donation'].mode()[0]
print(f"Mode: {mode_value}")  # Output: most frequent value
```

**When to use:** For categorical data (colors, regions, types) or when you need the most common value.

**Example:** If donations are [1000, 1000, 1000, 5000, 10000], mode is 1000 (appears 3 times).

---

### Comparing Mean, Median, Mode:
```python
data = [5000, 7500, 3000, 12000, 6500]
df = pd.DataFrame({'Amount': data})

mean = df['Amount'].mean()      # 6800
median = df['Amount'].median()  # 6500
mode = df['Amount'].mode()[0]   # All appear once, no clear mode

print(f"Mean:   {mean}")
print(f"Median: {median}")
print(f"Mode:   {mode}")

# Check if data is skewed
if mean > median:
    print("Mean > Median: RIGHT-SKEWED")
elif mean < median:
    print("Mean < Median: LEFT-SKEWED")
else:
    print("Mean ≈ Median: SYMMETRIC")
```

---

## 2. UKURAN DISPERSI (Measures of Spread/Variation)

These tell us how scattered or spread out the data is.

### RANGE (Jangkauan)
**Definition:** The difference between the maximum and minimum values.

**Formula:**
```
Range = Max - Min
```

**Python:**
```python
range_value = df['Donation'].max() - df['Donation'].min()
print(f"Range: {range_value}")  # Output: 12000 - 3000 = 9000
```

**Limitation:** Only looks at extremes, ignores everything in between.

---

### VARIANCE (Varians)
**Definition:** The average of how far each value is from the mean, squared.

**Formula:**
```
Variance = Σ(x - mean)² / n
```

**Python:**
```python
variance = df['Donation'].var()
print(f"Variance: {variance}")  # Output: some large number
```

**Interpretation:**
- **Low variance:** Data is clustered tightly (predictable)
- **High variance:** Data is scattered widely (unpredictable)

**Problem:** Units are squared (weird). Use Standard Deviation instead.

---

### STANDARD DEVIATION (Standar Deviasi)
**Definition:** The square root of variance. Shows typical distance of values from the mean.

**Formula:**
```
Std Dev = √Variance
```

**Python:**
```python
std_dev = df['Donation'].std()
print(f"Standard Deviation: {std_dev}")
```

**The 68-95-99.7 Rule (Empirical Rule):**
```
Mean ± 1 Std Dev:  Contains ~68% of data
Mean ± 2 Std Dev:  Contains ~95% of data
Mean ± 3 Std Dev:  Contains ~99.7% of data
```

**Practical Example:**
```python
mean = 7826
std_dev = 2800

low_end = mean - std_dev    # 5026
high_end = mean + std_dev   # 10626

print(f"Most donations fall between {low_end} and {high_end}")
# Interpretation: 68% of donations are between 5026 and 10626
```

**Why use this:** Same units as original data. Easy to interpret and use for budgeting.

---

## 3. BENTUK DISTRIBUSI (Distribution Shape)

These tell us about the *shape* of the data distribution.

### SKEWNESS (Kemencengan)
**Definition:** Measures whether the distribution is symmetric or lopsided. Does the data tail pull left or right?

**Python:**
```python
from scipy import stats

skewness = stats.skew(df['Donation'])
print(f"Skewness: {skewness}")
```

**Interpretation:**

| Skewness | Distribution | Meaning |
|----------|--------------|---------|
| ≈ 0 | SYMMETRIC | Data is balanced, bell-shaped |
| > 0.5 | RIGHT-SKEWED | Tail pulls right, few large values |
| < -0.5 | LEFT-SKEWED | Tail pulls left, few small values |

**Visual:**
```
RIGHT-SKEWED:        SYMMETRIC:          LEFT-SKEWED:
    ___                  ___                 ___
   /   \___          ___/   \___        ___/   \
  /        \___  ___/            \  ___/        \
_/____________\_/________________\_/___________\___
                              
Tail →                                        ← Tail
```

**Real-world example:**
- **Right-skewed donations:** Most people give 5,000-7,000. Few rich people give 20,000+.
- **Left-skewed donations:** Most people give 10,000-15,000. Few poor people give 1,000-2,000.
- **Symmetric donations:** People give evenly across the range.

---

### KURTOSIS (Keruncingan)
**Definition:** Measures whether there are more or fewer extreme outliers than expected. Is the peak sharp or flat?

**Python:**
```python
kurtosis = stats.kurtosis(df['Donation'])
print(f"Kurtosis: {kurtosis}")
```

**Interpretation:**

| Kurtosis | Type | Meaning |
|----------|------|---------|
| > 0 | LEPTOKURTIC | Sharp peak, thick tails (many outliers) |
| ≈ 0 | MESOKURTIC | Normal bell curve (expected outliers) |
| < 0 | PLATYKURTIC | Flat peak, thin tails (few outliers) |

**Visual:**
```
LEPTOKURTIC:       MESOKURTIC:         PLATYKURTIC:
(Sharp peak)       (Normal peak)       (Flat peak)

     /\                /\              ___________
    /  \              /  \            /           \
   /    \            /    \          /             \
__/______\__    ___/______\____  ___/_______________\____
```

**Real-world example:**
- **High kurtosis:** Most donations are stable at 7,000, but occasionally get shocking extremes (500 or 50,000). Unpredictable outliers.
- **Low kurtosis:** Donations are spread evenly from 2,000 to 15,000 with no sharp clusters or surprises.
- **Normal kurtosis:** Donations cluster around the mean with occasional expected outliers.

---

## 4. COMPLETE PYTHON WORKFLOW
```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Load or create data
data = {
    'Donation_Amount': [5000, 7500, 3000, 12000, 6500, 4200, 8900, 15000, 3500, 9200,
                        5800, 11000, 4500, 7200, 6000, 13000, 2800, 10500, 7800, 5300],
    'Donor_Age': [25, 34, 45, 28, 52, 31, 39, 47, 23, 41,
                  35, 50, 29, 38, 44, 33, 27, 49, 36, 42]
}
df = pd.DataFrame(data)

print("=== DESCRIPTIVE STATISTICS ===\n")

# Measures of Central Tendency
print("TENDENSI SENTRAL (Center):")
print(f"Mean:   {df['Donation_Amount'].mean():,.0f}")
print(f"Median: {df['Donation_Amount'].median():,.0f}")
print(f"Mode:   {df['Donation_Amount'].mode()[0]:,.0f}")

# Measures of Spread
print("\nDISPERSI (Spread):")
print(f"Range:             {df['Donation_Amount'].max() - df['Donation_Amount'].min():,.0f}")
print(f"Variance:          {df['Donation_Amount'].var():,.0f}")
print(f"Std Deviation:     {df['Donation_Amount'].std():,.0f}")

# Distribution Shape
print("\nBENTUK DISTRIBUSI (Shape):")
print(f"Skewness:  {stats.skew(df['Donation_Amount']):.4f}")
print(f"Kurtosis:  {stats.kurtosis(df['Donation_Amount']):.4f}")

# Interpretation
mean = df['Donation_Amount'].mean()
std = df['Donation_Amount'].std()
print(f"\nINTERPRETASI:")
print(f"Most donations fall between {mean - std:,.0f} and {mean + std:,.0f}")
print(f"(Mean ± 1 Std Dev = 68% of data)")
```

---

## 5. KEY CONCEPTS SUMMARY

### When to Use Each Metric:

| Question | Use | Python |
|----------|-----|--------|
| What's typical? | Median (or Mean if no outliers) | `.median()` or `.mean()` |
| How scattered? | Standard Deviation | `.std()` |
| Expected range? | Mean ± 1 Std Dev | `.mean()` and `.std()` |
| Is it lopsided? | Skewness | `stats.skew()` |
| Expect outliers? | Kurtosis | `stats.kurtosis()` |

---

## 6. REAL-WORLD APPLICATION FOR LUMORA TEMPLE
```python
# Temple donation analysis
donations = df['Donation_Amount']

print(f"Typical donation: {donations.median():,.0f}")
print(f"Variability: ±{donations.std():,.0f}")
print(f"Budget range: {donations.mean() - donations.std():,.0f} to {donations.mean() + donations.std():,.0f}")
print(f"Data pattern: ", end="")

if stats.skew(donations) > 0.5:
    print("We get more small donations with occasional large ones")
elif stats.skew(donations) < -0.5:
    print("We get more large donations with occasional small ones")
else:
    print("Donations are evenly distributed")

if stats.kurtosis(donations) > 0:
    print("Expect surprising outliers—keep an emergency fund")
else:
    print("Donations are predictable—budget confidently")
```

---

## 7. MEMORY AID: Mean vs Median

**Real Family Example:**
```
Ages: [18, 19, 20, 23, 300]  (where 300 = Liora)

Mean:   (18+19+20+23+300)/5 = 76  ❌ (useless—represents no one)
Median: Middle value = 20          ✓ (accurate representation)
```

**Robin's Rule:** Use median ~90% of the time in real data.

---

## 8. COMMON MISTAKES TO AVOID

❌ Using mean when there are extreme outliers
❌ Confusing variance with standard deviation (variance is squared)
❌ Mixing up left-skewed and right-skewed (remember: tail direction)
❌ Ignoring kurtosis when planning budgets (outliers happen!)
✓ Always visualize your data with histograms alongside statistics
✓ Report both median AND standard deviation for complete picture

---

***
# Kesimpulan Bab 1-3

# Urutan pengelolahan dataset.

1. Analisa dataset secara manual 
2. Atur format item strings didalam kolomn. mulai dari huruf besar kecil dan spasi kossong
3. Mengurusi duplikat persis(mulai dari id dan seluruhnya)
4. Menandai yang mirip tetapi bisa di investigasi
5. Manage dan mengurusi data yang hilang (Dengan: mean, median, mode, dll)
6. Pastikan tidak ada nilai kosong. `print(df.isnull().sum())`
7. Lakukan perhitungan statistik
8. Print dan save data

Praktik: [https://github.com/playmakermz/warkop-website/blob/main/document/DataScience/code/mod_2and3.py]


