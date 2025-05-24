# LaTex

LaTeX (Pengucapan "Lay-tek" atau "LAH-tek") adalah sebuah tool untuk typesetting dokumen profesional. 

Latex berbdeda dengan aplikasi penulis dokumen biasa, seperti ms word, libre office dan lain-lain. 

Pada Latex disini berfokus command line type untuk membuat dokumen, dan akan dikonfersi menjadi PDF setelah selesai. 

## Kenapa Harus LateX

Latex adalah typesetting yang sangat mendukung dalam penulisan karya ilmiah advacne dan penulisan rumus matematika advance. 

## Contoh dokumen minimal

Dibawah ini adalah contoh dokumen minimal pada Latex

```
\documentclass{article}
\begin{document}

Dokumen pertama. Ini adalah contoh sederhana, tanpa paramer dan lain-lain. 

\end{document}

```

Istilah yang digunakan untuk setiap command dan content diantara `\begin{document}`  adalah **Preamble**

## Penulisan identitas author dll

```
\documentclass[12pt, letterpaper]{article}
\title{Nama Dokumen Bebas}
\author{Anonymus\thanks{
    Referensi panduang dari Overleaf.
}}
\date{May 2025}
\begin{document}
\maketitle
Ini adalah paragraph
\end{document}
```
breakdown:
- 'maketitle' adalah fungsi yang harus ada dan berfungsi untuk mengikat informasi identitas diatasnya

## Menulis comment pada Latex

```
% Ini adalah deklarasi untuk comment
```
Comment disini tidak akan dirender, hanya bisa dilihat dari sisi editor/penulis.

## Text style

```
Some of the \textbf{greatest}
discoveries in \underline{science} 
were made by \textbf{\textit{accident}}.
```

Break:
- Textbf | **Penulisan Bold**
- Underline | <u>Menulis underline</u>
- textit | *Italic style*



 <!-- ============ Table of content harus dibawah === -->
## Table of content
- [Kenapa Harus Latex](#kenapa-harus-latex)
