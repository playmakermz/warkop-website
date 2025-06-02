# Ini adalah catatan penggunaan Shinny dengan R

```
#install.packages(c("shiny", "ggplot2", "plotly", "DT"))
library(shiny) # Untuk membantu integrasi dengan HTTPS
library(ggplot2) # Plot Grafik
library(plotly) # Plot Grafik
library(DT) # 

# Protokol dasar yang akan digunakan pada Aplikasi website
ui <- fluidPage(
  titlePanel("Aplikasi Visualisasi Data Interaktif Dengan Shiny"),
  sidebarLayout(
    sidebarPanel(
      selectInput("dataset", "Pilih Dataset:",
                  choices = c("mtcars", "iris", "diamonds")),
      uiOutput("var_x"),
      uiOutput("var_y"),
      selectInput("plot_type", "Pilih Jenis Plot:",
                  choices = c("Scatter Plot", "Line Plot", "Bar Plot", "Tabel Data"))
    ),
    mainPanel(
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

# Server
server <- function(input, output) {
  # Reactive data
  data <- reactive({
    get(input$dataset)
  })
  
  # Dynamic UI for variable selection
  output$var_x <- renderUI({
    selectInput("var_x", "Pilih Variabel X:", choices = names(data()))
  })
  
  output$var_y <- renderUI({
    if(input$plot_type != "Bar Plot") {
      selectInput("var_y", "Pilih Variabel Y:", choices = names(data()))
    }
  })
  
  # Main plot rendering
  output$plot <- renderPlotly({
    req(input$var_x)
    if(input$plot_type != "Bar Plot") req(input$var_y)
    
    p <- switch(input$plot_type,
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
    
    ggplotly(p, tooltip = "text") %>% 
      layout(autosize = TRUE)
  })
  
  # Data table
  output$table <- renderDT({
    datatable(data(), 
              options = list(scrollX = TRUE, pageLength = 10),
              rownames = FALSE)
  })
}

# Run aplikasi
shinyApp(ui = ui, server = server)
```


## Referensi Utama yang digunakan
https://mastering-shiny.org/ 
