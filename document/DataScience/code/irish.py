import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Create Irish Flower Dataset
n_samples = 150

data = {
    'Flower_ID': range(1, n_samples + 1),
    'Petal_Length_cm': np.random.normal(loc=5.8, scale=1.2, size=n_samples),
    'Petal_Width_cm': np.random.normal(loc=2.0, scale=0.6, size=n_samples),
    'Sepal_Length_cm': np.random.normal(loc=5.9, scale=0.8, size=n_samples),
    'Sepal_Width_cm': np.random.normal(loc=3.1, scale=0.4, size=n_samples),
    'Color_Intensity': np.random.uniform(low=40, high=100, size=n_samples),
    'Bloom_Duration_Days': np.random.uniform(15, 45, size=n_samples), # This is already float, so no `astype(float)` needed yet
    'Magical_Essence_Level': np.random.normal(loc=7.5, scale=1.5, size=n_samples),
    'Distance_from_Center_m': np.random.uniform(0, 5, size=n_samples),
    'Health_Score': np.random.randint(60, 100, size=n_samples),
}

# Create DataFrame
df = pd.DataFrame(data)

# Introduce some missing values (realistic)
missing_indices = np.random.choice(n_samples, size=15, replace=False)
df.loc[missing_indices[:5], 'Color_Intensity'] = np.nan
df.loc[missing_indices[5:10], 'Magical_Essence_Level'] = np.nan
df.loc[missing_indices[10:15], 'Bloom_Duration_Days'] = np.nan

# Introduce some duplicates (administrative error)
duplicate_rows = df.iloc[:3].copy()
df = pd.concat([df, duplicate_rows], ignore_index=True)

# Introduce some outliers (unusual magical flowers)
df.loc[df.index[-10], 'Magical_Essence_Level'] = 15.2  # Unusually high
df.loc[df.index[-9], 'Petal_Length_cm'] = 12.5  # Very large


# ========== Data cleaning ==================

# Delete the exact same item
df = df.drop_duplicates(keep='first')

# since Color_Intensity, Magical_Essence_Level, and Bloom_Duration_Days had NaN value, then we are going to use median to fill the blank
# Since the data could be predicted by median.
df['Color_Intensity'] = df['Color_Intensity'].fillna(df['Color_Intensity'].median())
df['Magical_Essence_Level'] = df['Magical_Essence_Level'].fillna(df['Magical_Essence_Level'].median())
df['Bloom_Duration_Days'] = df['Bloom_Duration_Days'].fillna(df['Bloom_Duration_Days'].median())


# ================== Statistic ===================

df_mean = df['Petal_Length_cm'].mean()
df_median = df['Petal_Length_cm'].median()
df_std = df['Petal_Length_cm'].std()
df_var = df['Petal_Length_cm'].var()

print("==" * 60)
print("IRISH FLOWER DATASET - RAW DATA")
print("==" * 60)
print(f"Mean: {df_mean:.4f}")
print(f"Median: {df_median:.4f}")
print(f"Standard Deviation: {df_std:.4f}")
print(f"Variance: {df_var:.4f}")

# Scipy
skew = stats.skew(df['Petal_Length_cm'])
kurtosis = stats.kurtosis(df['Petal_Length_cm'])
print(f"Skewness: {skew:.4f}") # Apply formatting here. tail(dimana letak outlier yang menarik garis)
print(f"Kurtosis: {kurtosis:.4f}") # Apply formatting here
print(f"Range: {df['Petal_Length_cm'].max() - df['Petal_Length_cm'].min():.4f}")
print(f"Quartiles: {df['Petal_Length_cm'].quantile([0.25, 0.5, 0.75])}")


# ====================== [Plot show] ============

plt.figure(figsize=(12, 5))
plt.hist(df['Petal_Length_cm'], bins=30, edgecolor='black', alpha=0.7, color='orange' )
plt.axvline(df['Petal_Length_cm'].quantile(0.25), color='orange', linestyle='--', linewidth=2, label=f'Q1: {df["Petal_Length_cm"].quantile(0.25):.4f}')
plt.axvline(df['Petal_Length_cm'].quantile(0.5), color='red', linestyle='--', linewidth=2, label=f'Q2: {df["Petal_Length_cm"].quantile(0.5):.4f}')
plt.axvline(df['Petal_Length_cm'].quantile(0.75), color='green', linestyle='--', linewidth=2, label=f'Q3: {df["Petal_Length_cm"].quantile(0.75):.4f}')
plt.title('Petal Length Distribution')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


# ==================================== [Let it be] ==================================
print("=" * 60)
print("IRISH FLOWER DATASET - RAW DATA")
print("=" * 60)
print(df.head(10))
print(f"\nDataset Shape: {df.shape}")
print(f"\nDataset Info:")
print(df.info())
print(f"\nMissing Values:")
print(df.isnull().sum())
df.to_csv('raw_data.csv', index=False)
