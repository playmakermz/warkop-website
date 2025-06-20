# Catatan R 


## Note 1.
```r
# Langkah 1: Buat data contoh (tinggi badan dalam cm)
tinggi_badan <- c(165, 170, 155, 160, 175, 180, 168, 172, 158, 162)

# Langkah 2: Hitung statistik dasar
mean_tinggi <- mean(tinggi_badan)
sd_tinggi <- sd(tinggi_badan)
median_tinggi <- median(tinggi_badan)

# Tampilkan hasil
cat("Mean:", mean_tinggi, "\n")
cat("Standar Deviasi:", sd_tinggi, "\n")
cat("Median:", median_tinggi, "\n")

# Langkah 3: Plot sederhana (plot titik)
plot(tinggi_badan, 
     main = "Plot Tinggi Badan",
     xlab = "Urutan Orang",
     ylab = "Tinggi (cm)",
     col = "blue",
     pch = 19)

# Langkah 4: Histogram
hist(tinggi_badan,
     main = "Histogram Tinggi Badan",
     xlab = "Tinggi (cm)",
     ylab = "Frekuensi",
     col = "lightgreen",
     border = "black")
```

## Note 2. 

```r
# Install package ggplot2 jika belum terinstall
# install.packages("ggplot2")

# Load library ggplot2
library(ggplot2)

# Gunakan dataset built-in R: mtcars
data(mtcars)

# Lihat struktur data
head(mtcars)

# BOXPLOT DENGAN GGPLOT2
ggplot(data = mtcars, aes(x = factor(cyl), y = mpg)) +  # 1. Set data dan mapping aesthetic:
                                                       #   - x: silinder (cyl) diubah jadi faktor
                                                       #   - y: mpg (mile per gallon)
  geom_boxplot(fill = "skyblue", alpha = 0.7) +        # 2. Tambahkan layer boxplot:
                                                       #   - fill: warna biru langit
                                                       #   - alpha: transparansi 70%
  labs(                                                # 3. Tambahkan label:
    title = "Konsumsi Bensin Berdasarkan Jumlah Silinder",  #   - judul plot
    subtitle = "Dataset mtcars",                       #   - subtitle
    x = "Jumlah Silinder",                             #   - label sumbu x
    y = "Miles per Gallon (MPG)",                      #   - label sumbu y
    caption = "Sumber: dataset mtcars"                 #   - caption bawah
  ) +
  theme_minimal() +                                    # 4. Gunakan tema minimal (background bersih)
  geom_jitter(width = 0.2, alpha = 0.5, color = "red") # 5. Tambahkan titik data aktual:
                                                       #   - jitter: titik tersebar (hindari overlap)
                                                       #   - warna merah dengan transparansi 50%

# SIMPLE PLOT DENGAN GGPLOT2 (Scatter Plot)
ggplot(mtcars, aes(x = wt, y = mpg)) +                 # 1. Set data dan mapping:
                                                       #   - x: berat mobil (wt)
                                                       #   - y: mpg
  geom_point(size = 3, aes(color = factor(cyl))) +     # 2. Layer titik:
                                                       #   - size: ukuran titik
                                                       #   - color: warna berdasarkan silinder (sebagai faktor)
  geom_smooth(method = "lm", se = FALSE) +             # 3. Tambahkan garis regresi linear:
                                                       #   - method: "lm" (linear model)
                                                       #   - se = FALSE: tanpa area confidence interval
  labs(
    title = "Hubungan Berat Mobil dan Konsumsi Bensin",
    x = "Berat Mobil (1000 lbs)",
    y = "MPG",
    color = "Silinder"                                 # 4. Ubah judul legend color
  )
```
