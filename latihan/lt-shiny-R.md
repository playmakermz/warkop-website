# Ini adalah catatan penggunaan Shinny dengan R

## Catatan RAndom
- 'Shiny' ini sangat membantu programmer. Dikarenakan pada halaman website segala kerpluan akan dipersiapkan oleh sinny. Contoh: Kita cukup upload dataset, maka mereka yang akan menyediakan protokol penggunaan pada data set spesifik anda(Kita hanya perlu memangil saja).
-  Contoh seperti ` uiOutput("var_x")` disini akan ditampilkan semua kolom yang ada pada dataset

```R
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
        condition = "input.plot_type != 'Tabel Data'",
        plotlyOutput("plot", height = "600px")
      ),
      conditionalPanel(
        condition = "input.plot_type == 'Tabel Data'",
        DTOutput("table")
      )
    )
  )
)


# Protokol yang akan menjelaskan algortima yang akan digunakan oleh UI
server <- function(input, output) { # Menyiapkan alur untuk algoritma website
  # Reactive data
  data <- reactive({ # Persiapkan DataSet
    #get(input$dataset) # Dataset ini 
    DataTugas <- "./weather.csv"
    home_data <- read.csv(DataTugas, header = TRUE)
  })
  
  # Dynamic UI for variable selection
  output$var_x <- renderUI({ 
    # Pada UI atur Form untuk pilihan X
    # Dan beri mereka pilihan dengan informasi kolom yang tersedia `names(data())`
    selectInput("var_x", "Pilih Variabel X:", choices = names(data()))
  })
  
  output$var_y <- renderUI({
    if(input$plot_type != "Bar Plot") {
      # Algoritma var_y hanya akan digunakan jika tipe plot yang dipilih bukan 'Bar Plot' 
       # Pada UI atur Form untuk pilihan Y
       # Dan beri mereka pilihan dengan informasi kolom yang tersedia `names(data())`
      
      selectInput("var_y", "Pilih Variabel Y:", choices = names(data()))
    }
  })

  #Bagian utama yang akan menampilkan hasil grafik
  output$plot <- renderPlotly({
    req(input$var_x) # ambil data dari kolom x
    if(input$plot_type != "Bar Plot") req(input$var_y) # Pastikan sekali lagi, plot yang digunakan bukan bar plot
    
    # Persiapkan variabel untuk ggpplot, yang dimana kita bisa berpindah-pindah plot nantinya.
    mainUi <- switch(input$plot_type,
                "Scatter Plot" = {
                  ggplot(data(), aes_string(x = input$var_x, y = input$var_y)) +
                    geom_point(aes(color = if(is.numeric(data()[[input$var_x]])) data()[[input$var_x]] else NULL), 
                               size = 3, alpha = 0.7) +
                    labs(title = "Scatter Plot Interaktif", color = input$var_x)
                },
                "Line Plot" = {
                  ggplot(data(), aes_string(x = input$var_x, y = input$var_y, group = 1)) +
                    geom_line(color = "steelblue", size = 1.5) +
                    geom_point(color = "darkblue", size = 3) +
                    labs(title = "Line Plot Interaktif")
                },
                "Bar Plot" = {
                  if(is.numeric(data()[[input$var_x]])) {
                    ggplot(data(), aes_string(x = reorder(seq_along(data()[[input$var_x]])), 
                                              y = input$var_x)) +
                      geom_bar(stat = "identity", fill = "skyblue") +
                      labs(x = "Index", y = input$var_x, title = "Bar Plot Numerik")
                  } else {
                    ggplot(data(), aes_string(x = input$var_x)) +
                      geom_bar(fill = "salmon") +
                      labs(title = "Bar Plot Kategorikal") +
                      theme(axis.text.x = element_text(angle = 45))
                  }
                })
    
    ggplotly(mainUi, tooltip = "text") %>% 
      layout(autosize = TRUE) # Ukuran akan selalu mengikuti perubahan lebar device.
  })
  
  # Tampilkan Data pada Dataset Secara menyeluruh
  output$table <- renderDT({ # Jalankan Render Data table
    datatable(data(), 
              options = list(scrollX = TRUE, pageLength = 10),
              rownames = FALSE)
  })
}

# Run aplikasi
shinyApp(ui = UI, server = server)
```


## Referensi Utama yang digunakan
https://mastering-shiny.org/ 
