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

## note 3

```r
# Load library yang diperlukan
library(lmtest)  # Untuk uji Breusch-Pagan (bptest)

# Gunakan dataset built-in R: mtcars
data(mtcars)

### 1. Uji Normalitas Shapiro-Wilk ###
# Uji normalitas pada variabel mpg
shapiro_test <- shapiro.test(mtcars$mpg)

# Cetak hasil
print(shapiro_test)
# Interpretasi:
# - p-value > 0.05: data normal (gagal tolak H0)
# - p-value < 0.05: data tidak normal (tolak H0)

### 2. Uji Korelasi Pearson ###
cor_test <- cor.test(mtcars$mpg, mtcars$wt, method = "pearson")
print(cor_test)
# Interpretasi:
# - p-value: signifikansi hubungan
# - cor: koefisien korelasi (-1 sampai 1)

### 3. Regresi Linear Sederhana ###
# Buat model regresi: mpg sebagai respon, wt sebagai prediktor
model <- lm(mpg ~ wt, data = mtcars)

# Tampilkan ringkasan model
summary(model)
# Interpretasi:
# - Coefficients: intercept (b0) dan slope (b1)
# - R-squared: proporsi variasi yang dijelaskan model
# - p-value: signifikansi koefisien

### 4. Uji Heteroskedastisitas (Breusch-Pagan) ###
bp_test <- bptest(model)
print(bp_test)
# Interpretasi:
# - p-value > 0.05: homoskedastisitas (variansi error konstan)
# - p-value < 0.05: heteroskedastisitas (masalah heteroskedastisitas)

### 5. Plot Data dan Garis Regresi ###
# Scatter plot hubungan mpg dan wt
plot(mtcars$wt, mtcars$mpg, 
     main = "Hubungan Berat Mobil dan Konsumsi BBM",
     xlab = "Berat Mobil (1000 lbs)",
     ylab = "Miles per Gallon (MPG)",
     pch = 19,         # Bentuk titik: bulat padat
     col = "darkblue")  # Warna titik

# Tambahkan garis regresi
abline(model, 
       col = "red",    # Warna garis
       lwd = 2)        # Lebar garis

# Tambahkan teks koefisien di plot
text(3.5, 30, 
     paste("Persamaan: mpg =", 
           round(coef(model)[1], 1),   # Intercept
           round(coef(model)[2], 1),   # Slope
           "* wt"),
     col = "red")

# Tambahkan R-squared
text(3.5, 28, 
     paste("R-squared =", 
           round(summary(model)$r.squared, 2)),
     col = "red")
```

## Note 4 

```r
# Load library yang diperlukan
library(shiny)
library(ggplot2)

# UI (User Interface) - Mendefinisikan tampilan aplikasi
ui <- fluidPage(
  titlePanel("Visualisasi Data mtcars"),  # Judul aplikasi
  
  sidebarLayout(
    sidebarPanel(
      # Input 1: Pilih jenis plot
      selectInput("plot_type", "Pilih Jenis Plot:",
                  choices = c("Scatter Plot", "Line Plot", "Bar Plot"),
                  selected = "Scatter Plot"),
      
      # Input 2: Pilih variabel sumbu X
      selectInput("x_var", "Pilih Variabel X:",
                  choices = names(mtcars),
                  selected = "wt"),
      
      # Input 3: Pilih variabel sumbu Y (hanya untuk scatter dan line plot)
      conditionalPanel(
        condition = "input.plot_type != 'Bar Plot'",
        selectInput("y_var", "Pilih Variabel Y:",
                    choices = names(mtcars),
                    selected = "mpg")
      ),
      
      # Input 4: Pilih warna plot
      selectInput("color", "Pilih Warna:",
                  choices = c("Biru" = "blue", "Merah" = "red", "Hijau" = "green"),
                  selected = "blue"),
      
      # Input 5: Slider untuk ukuran titik (scatter plot saja)
      conditionalPanel(
        condition = "input.plot_type == 'Scatter Plot'",
        sliderInput("point_size", "Ukuran Titik:",
                    min = 1, max = 10, value = 5)
      )
    ),
    
    mainPanel(
      plotOutput("plot_output")  # Output: Area untuk menampilkan plot
    )
  )
)

# Server - Logika pemrosesan data dan pembuatan plot
server <- function(input, output) {
  
  output$plot_output <- renderPlot({
    # Membuat plot berdasarkan pilihan pengguna
    if (input$plot_type == "Scatter Plot") {
      # SCATTER PLOT: Hubungan antara dua variabel numerik
      ggplot(mtcars, aes_string(x = input$x_var, y = input$y_var)) +
        geom_point(size = input$point_size, color = input$color) +  # Titik dengan ukuran dan warna
        labs(title = "Scatter Plot mtcars",
             x = input$x_var,
             y = input$y_var) +
        theme_minimal()
      
    } else if (input$plot_type == "Line Plot") {
      # LINE PLOT: Tren perubahan nilai Y terhadap X
      ggplot(mtcars, aes_string(x = input$x_var, y = input$y_var)) +
        geom_line(color = input$color, linewidth = 1.5) +  # Garis berkelanjutan
        geom_point(color = "black", size = 2) +  # Titik sebagai penanda
        labs(title = "Line Plot mtcars",
             x = input$x_var,
             y = input$y_var) +
        theme_minimal()
      
    } else if (input$plot_type == "Bar Plot") {
      # BAR PLOT: Perbandingan nilai satu variabel
      ggplot(mtcars, aes_string(x = input$x_var)) +
        geom_bar(fill = input$color, alpha = 0.8) +  # Batang dengan warna dan transparansi
        labs(title = "Bar Plot mtcars",
             x = input$x_var,
             y = "Frekuensi") +
        theme_minimal()
    }
  })
}

# Jalankan aplikasi Shiny
shinyApp(ui = ui, server = server)
```
