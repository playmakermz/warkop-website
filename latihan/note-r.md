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
