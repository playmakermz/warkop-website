# Ini adalah catatan penggunaan Shinny dengan R

## Catatan RAndom
- 'Shiny' ini sangat membantu programmer. Dikarenakan pada halaman website segala kerpluan akan dipersiapkan oleh sinny. Contoh: Kita cukup upload dataset, maka mereka yang akan menyediakan protokol penggunaan pada data set spesifik anda(Kita hanya perlu memangil saja).
-  Contoh seperti ` uiOutput("var_x")` disini akan ditampilkan semua kolom yang ada pada dataset


## Sctatter Plot
![image](https://github.com/user-attachments/assets/7dc1d9b9-6f3b-4108-acbb-d7b8e2ae1f72)

## Line Plot

![image](https://github.com/user-attachments/assets/622ad7e8-84a9-41ca-9cf4-a50c37c393e9)

## Bar Plot

![image](https://github.com/user-attachments/assets/1197dbbd-5915-4cea-a30b-2469b6c9ca3c)

## Table

![image](https://github.com/user-attachments/assets/9fdf3290-6678-4d23-a79f-8695976d2a5e)





## Referensi Utama yang digunakan
https://mastering-shiny.org/ 






```r
# Persiapkan Install Library
#install.packages(c("shiny", "ggplot2", "plotly", "DT"))

library(shiny) # Untuk membantu integrasi dengan HTTPS
library(ggplot2) # Plot Grafik
library(plotly) # Plot Grafik
library(DT) # Integrasi Data Tables | https://rstudio.github.io/DT/


UI <- fluidPage( # Ini adalah fungsi untuk membuat fluid page layouts.
  titlePanel("Aplikasi Visualisasi Data Interaktif Dengan Shiny"), 
  sidebarLayout( # Persiapkan panel UI untuk bagian kiri
    sidebarPanel( # Jelaskan fitur-fitur yang akan tersedia

      uiOutput("var_x"), # Pilih Variabel X (Kolom yang dituju)
      uiOutput("var_y"), # Pilih Variabel Y (Kolom Yang dituju)
      selectInput("plot_type", "Pilih Jenis Plot:", # Memilih jenis plot yang akan digunaka
                  choices = c("Scatter Plot", "Line Plot", "Bar Plot", "Tabel Data")) #List pilihan

    ),
    mainPanel(  # Panel UI untuk bagian kanan (Utama)

      conditionalPanel( 
        condition = "input.plot_type != 'Tabel Data'", # Tampilkan PLot jika yang dipilih user bukan tipe tabel
        plotlyOutput("plot", height = "600px")
      ),
      conditionalPanel(
        condition = "input.plot_type == 'Tabel Data'", # Langsung Tabel
        DTOutput("table")
      )

    )
  )
)


# Protokol yang akan menjelaskan algortima yang akan digunakan oleh UI
SERVER <- function(input, output) { # Menyiapkan alur untuk algoritma website

  data <- reactive({ # Persiapkan DataSet
    DataTugas <- "./weather.csv" # Dataset
    home_data <- read.csv(DataTugas, header = TRUE)
  })
  

  output$var_x <- renderUI({ 
    # Pada UI atur Form untuk pilihan X
    # Dan beri mereka pilihan dengan informasi kolom yang tersedia `names(data())`
    selectInput("var_x", "Pilih Variabel X:", choices = names(data()))

  })
  
  output$var_y <- renderUI({

       # Pada UI atur Form untuk pilihan Y
       # Dan beri mereka pilihan dengan informasi kolom yang tersedia `names(data())`
       selectInput("var_y", "Pilih Variabel Y:", choices = names(data()))

  })

  #Bagian utama yang akan menampilkan hasil grafik
  output$plot <- renderPlotly({

    req(input$var_x) # ambil data dari kolom x
    req(input$var_y) # ambil data dari kolom Y
    
    # Persiapkan variabel untuk ggpplot, yang dimana kita bisa berpindah-pindah plot nantinya.
    mainUi <- switch(input$plot_type,

                "Scatter Plot" = {
                  # data() = Dataframe
                  # Lalu seuaikan kolom X dan Y, sesuai kebutuhan
                  # Input format x dan y
                  # Atur Scatter plot
                  # Title
                ggplot(data(), aes_string(x = input$var_x, y = input$var_y)) + 
                geom_point()+
                geom_smooth(method=lm, se=FALSE, fullrange=TRUE)+
                labs(title="Scatter Plot Grafik", color = input$var_x) + 
                theme_classic()  
  
                },


                "Line Plot" = {
                  # data() = Dataframe
                  # Lalu seuaikan kolom X dan Y, sesuai kebutuhan
                  # Input format x dan y
                  # Atur baris grafik
                  # Atur point grafik
                  # Title
                  ggplot(data(), aes_string(x = input$var_x, y = input$var_y, group = 1)) +
                    geom_line(color = "steelblue", size = 1.5) +
                    geom_point(color = "darkblue", size = 3) +
                    labs(title = "Line Plot Grafik", color = input$var_x)
                },


                "Bar Plot" = {
                   # data() = Dataframe
                  # Lalu seuaikan kolom X dan Y, sesuai kebutuhan
                  # Input format x dan y
                  # Title
                  ggplot(data(), aes_string(x = input$var_x, y = input$var_y, group = 1)) +
                  geom_bar(stat="identity", color="steelblue", fill="white") +
                  labs(title = "Bar Plot Grafik", color = input$var_x) 

                })
    
    ggplotly(mainUi, tooltip = "text") %>% 
      layout(autosize = TRUE) # Ukuran akan selalu mengikuti perubahan lebar device.
      
  })
  
  # Tampilkan Data pada Dataset Secara menyeluruh
  output$table <- renderDT({ # Jalankan Render Data table
    datatable(data(), 
              options = list(scrollX = TRUE, pageLength = 10), # Atur agar 10 baris
              rownames = FALSE)
  })
}

# Jalankan Aplikasi
shinyApp(ui = UI, server = SERVER)
```
