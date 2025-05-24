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
- Underline | _Menulis underline_
- textit | *Italic style*

## Membuat referensi untuk gambar

```
\begin{figure}[h]
    \centering
    \includegraphics[width=0.75\textwidth]{mesh}
    \caption{A nice plot.}
    \label{fig:mesh1}
\end{figure}

% Contoh, code menautkan gambar

\ref{fig:mesh1}

% Memangil nama gambar

\pageref{fig:mesh1}.

% Memangil halaman berapa gambar tersebut
```

## Membuat titik-titik hitam untuk list (Unordered List)

```
\begin{itemize}
  \item The individual entries are indicated with a black dot, a so-called bullet.
  \item The text in the entries may be of any length.
\end{itemize}
```

## Ordered list 

```
\begin{enumerate}
  \item This is the first entry in our list.
  \item The list numbers increase with each entry we add.
\end{enumerate}
```

Membuat list dengan penomoran

## Inline Math

```
$...$
```
tulis code math didalam "..."

Contoh:

```
In physics, the mass-energy equivalence is stated 
by the equation $E=mc^2$, discovered in 1905 by Albert Einstein.
```

## Abstract

Pada karya ilmiah biasannya memiliki bagian absctract. Kita bisa tulis denga latex seperti ini:

```
\documentclass{article}
\begin{document}


\begin{abstract}
This is a simple paragraph at the beginning of the 
document. A brief introduction about the main subject.
\end{abstract}


\end{document}
```


 <!-- ============ Table of content harus dibawah === -->
## Table of content
- [Kenapa Harus Latex](#kenapa-harus-latex)
- [Dokumen minmal](#contoh-dokumen-minimal)
- [Penulisan identitas dokumen](#penulisan-identitas-author-dll)
- [Penulisan comment pada dokumen](#menulis-comment-pada-latex)
- [Penulisan Text style(Bold, underline, italic)](#text-style)
- [Mencantumkan gambar dan referensi](#membuat-referensi-untuk-gambar)
- [unordered List](#membuat-titik-titik-hitam-untuk-list-Unordered-list)
- [Ordered List](#ordered-list)
- [Inline Math](#inline-math)
- [Abstract](#abstract)



