# LaTeX

LaTeX (dibaca "Lay-tek" atau "Lah-tek") adalah sistem typesetting untuk membuat dokumen profesional dengan kualitas publikasi. LaTeX sangat populer di kalangan akademisi, peneliti, dan siapapun yang perlu menulis dokumen teknis dengan formula matematika yang kompleks.

## Daftar Isi

1. [Kenapa Harus LaTeX](#kenapa-harus-latex)
2. [Perbedaan LaTeX dengan Word Processor](#perbedaan-latex-dengan-word-processor)
3. [Dokumen Minimal](#contoh-dokumen-minimal)
4. [Struktur Dokumen LaTeX](#struktur-dokumen-latex)
5. [Identitas Dokumen](#penulisan-identitas-dokumen)
6. [Comment](#menulis-comment-pada-latex)
7. [Text Formatting](#text-formatting)
8. [Paragraf dan Line Break](#paragraf-dan-line-break)
9. [Gambar dan Referensi](#membuat-referensi-untuk-gambar)
10. [Unordered List](#membuat-unordered-list)
11. [Ordered List](#ordered-list)
12. [Inline Math](#inline-math)
13. [Display Math](#display-math)
14. [Abstract](#abstract)
15. [Sections dan Subsections](#sections-dan-subsections)
16. [Table of Contents](#table-of-contents)
17. [Packages](#packages-yang-berguna)
18. [Tips dan Tricks](#tips-dan-tricks)
19. [Referensi](#referensi)

---

## Kenapa Harus LaTeX

LaTeX memiliki beberapa keunggulan yang membuatnya menjadi pilihan utama untuk penulisan dokumen akademis dan teknis:

**1. Typesetting Matematika yang Superior**  
LaTeX adalah standar industri untuk penulisan formula matematika. Hasilnya jauh lebih professional dan mudah dibaca dibanding word processor biasa.

**2. Konsistensi Format**  
Sekali kamu set format, semua dokumen akan konsisten. Tidak perlu pusing dengan formatting manual seperti di Word.

**3. Manajemen Referensi yang Baik**  
LaTeX punya sistem built-in untuk manage citations, bibliography, cross-references, dan numbering otomatis.

**4. Gratis dan Open Source**  
Tidak perlu bayar lisensi. Tersedia untuk semua platform (Windows, Mac, Linux).

**5. Format yang Stabil**  
File .tex adalah plain text, jadi tidak akan corrupt dan bisa dibuka kapan saja, bahkan puluhan tahun kemudian.

**6. Version Control Friendly**  
Karena plain text, sangat cocok untuk Git atau sistem version control lainnya.

**Kapan Pakai LaTeX:**
- Menulis skripsi, tesis, atau disertasi
- Membuat paper ilmiah
- Menulis buku teknis
- Dokumen dengan banyak formula matematika
- Dokumen yang butuh konsistensi tinggi

---

## Perbedaan LaTeX dengan Word Processor

### Word Processor (Word, LibreOffice, Google Docs)

**WYSIWYG (What You See Is What You Get)**
- Kamu langsung lihat hasil akhir saat mengetik
- Fokus pada tampilan visual
- Click dan drag untuk formatting
- Mudah untuk dokumen sederhana

### LaTeX

**Markup Language**
- Kamu tulis kode/command, lalu compile jadi PDF
- Fokus pada struktur dan konten
- Formatting dilakukan dengan command
- Learning curve lebih tinggi, tapi hasil lebih professional

**Analogi:**  
LaTeX seperti HTML/CSS untuk dokumen. Kamu tulis markup, lalu system yang handle tampilan. Word processor seperti Canva, langsung design visual.

---

## Contoh Dokumen Minimal

Ini adalah template paling sederhana untuk membuat dokumen LaTeX:

```latex
\documentclass{article}

\begin{document}

Halo dunia! Ini adalah dokumen LaTeX pertama saya.

Ini adalah paragraf kedua. LaTeX otomatis mengatur spacing dan justification.

\end{document}
```

**Cara menggunakan:**
1. Save kode di atas sebagai `dokumen.tex`
2. Compile dengan command: `pdflatex dokumen.tex`
3. Hasilnya: file PDF bernama `dokumen.pdf`

**Penjelasan:**
- `\documentclass{article}` mendefinisikan jenis dokumen (article, report, book, dll)
- `\begin{document}` menandai awal konten
- `\end{document}` menandai akhir konten
- Text di antara keduanya adalah konten dokumen

---

## Struktur Dokumen LaTeX

Dokumen LaTeX terdiri dari dua bagian utama:

### 1. Preamble

Bagian sebelum `\begin{document}`. Di sini kita set konfigurasi dokumen:

```latex
\documentclass[12pt, a4paper]{article}  % Jenis dan ukuran dokumen
\usepackage[utf8]{inputenc}              % Encoding
\usepackage[bahasa]{babel}               % Bahasa Indonesia
\usepackage{amsmath}                     % Package untuk math
\usepackage{graphicx}                    % Package untuk gambar

\title{Judul Dokumen}
\author{Nama Penulis}
\date{\today}
```

### 2. Body/Content

Bagian di antara `\begin{document}` dan `\end{document}`:

```latex
\begin{document}

\maketitle  % Tampilkan judul

\section{Pendahuluan}
Ini adalah konten dokumen...

\end{document}
```

**Istilah Penting:**
- **Preamble**: Bagian konfigurasi sebelum `\begin{document}`
- **Environment**: Blok yang dimulai dengan `\begin{...}` dan diakhiri `\end{...}`
- **Command**: Instruksi yang dimulai dengan backslash `\`
- **Package**: Library tambahan untuk fitur ekstra

---

## Penulisan Identitas Dokumen

Untuk membuat title page dengan informasi lengkap:

```latex
\documentclass[12pt, a4paper]{article}

% Informasi dokumen
\title{Pengaruh Media Sosial terhadap Produktivitas Mahasiswa}
\author{
    Ahmad Fauzi\thanks{Mahasiswa Teknik Informatika, Universitas ABC} \\
    NIM: 123456789 \\
    Email: ahmad@example.com
}
\date{Mei 2025}

\begin{document}

\maketitle  % Command ini WAJIB untuk menampilkan title

\section{Pendahuluan}
Ini adalah bagian pendahuluan dari dokumen...

\end{document}
```

**Penjelasan:**

| Command | Fungsi |
|---------|--------|
| `\title{...}` | Judul dokumen |
| `\author{...}` | Nama penulis |
| `\date{...}` | Tanggal (gunakan `\today` untuk tanggal otomatis) |
| `\thanks{...}` | Footnote di title page (biasanya untuk afiliasi) |
| `\maketitle` | Command untuk render title page (WAJIB) |
| `\\` | Line break dalam author/title |

**Multiple Authors:**
```latex
\author{
    Ahmad Fauzi\thanks{Universitas ABC} \and
    Budi Santoso\thanks{Universitas XYZ}
}
```

---

## Menulis Comment pada LaTeX

Comment adalah catatan yang tidak akan muncul di output PDF:

```latex
% Ini adalah comment satu baris
% Comment berguna untuk:
% - Catatan untuk diri sendiri
% - Menonaktifkan kode sementara
% - Dokumentasi kode LaTeX

\section{Pendahuluan}
Ini akan muncul di PDF.  % Ini tidak akan muncul

% \section{Draft}
% Bagian yang di-comment tidak akan di-render
```

**Multi-line Comment:**
```latex
\iffalse
Ini adalah comment
yang panjang dan
bisa beberapa baris
\fi
```

Atau gunakan package `verbatim`:
```latex
\usepackage{verbatim}

\begin{comment}
Ini juga comment
multi-line
\end{comment}
```

---

## Text Formatting

LaTeX menyediakan berbagai command untuk formatting text:

### Basic Formatting

```latex
\textbf{Text ini bold (tebal)}

\textit{Text ini italic (miring)}

\underline{Text ini underline (garis bawah)}

\texttt{Text ini monospace (seperti code)}

\textsc{Text Ini Small Caps}
```

### Combining Styles

```latex
Beberapa dari \textbf{penemuan terbesar} dalam \underline{sains} 
dibuat secara \textbf{\textit{tidak sengaja}}.
```

**Output:**  
Beberapa dari **penemuan terbesar** dalam <u>sains</u> dibuat secara ***tidak sengaja***.

### Text Size

```latex
{\tiny Sangat kecil}
{\small Kecil}
{\normalsize Normal (default)}
{\large Besar}
{\Large Lebih Besar}
{\LARGE Sangat Besar}
{\huge Huge}
{\Huge Paling Besar}
```

### Text Color (butuh package xcolor)

```latex
\usepackage{xcolor}

\textcolor{red}{Text merah}
\textcolor{blue}{Text biru}
\textcolor{green}{Text hijau}
```

### Font Family

```latex
\textrm{Roman Family (default)}
\textsf{Sans Serif Family}
\texttt{Typewriter Family (monospace)}
```

---

## Paragraf dan Line Break

### Paragraf Baru

```latex
Ini adalah paragraf pertama. LaTeX otomatis mengatur spacing dan justification 
untuk membuat tampilan yang rapi dan professional.

Ini adalah paragraf kedua. Cukup buat baris kosong untuk paragraf baru.
Tidak perlu indent manual, LaTeX yang atur.

Ini paragraf ketiga.
```

**Catatan:**  
- Satu baris kosong = paragraf baru dengan indent otomatis
- Multiple baris kosong = tetap dianggap satu paragraf break

### Manual Line Break

```latex
Baris pertama \\
Baris kedua \\
Baris ketiga

% Atau dengan spacing tambahan
Baris pertama \\[0.5cm]
Baris kedua dengan jarak 0.5cm
```

### Prevent Indent

```latex
\noindent Paragraf ini tidak di-indent.

Paragraf ini di-indent seperti biasa.
```

---

## Membuat Referensi untuk Gambar

LaTeX punya sistem yang sangat baik untuk manage gambar dan referensi:

### Setup (di Preamble)

```latex
\usepackage{graphicx}  % Package untuk gambar
\graphicspath{{images/}}  % Folder tempat gambar (optional)
```

### Insert Gambar

```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.75\textwidth]{mesh}
    \caption{Visualisasi mesh untuk simulasi CFD.}
    \label{fig:mesh1}
\end{figure}
```

**Penjelasan:**

| Command | Fungsi |
|---------|--------|
| `\begin{figure}[h]` | Mulai environment figure. `[h]` = "here" (coba tempatkan di sini) |
| `\centering` | Center gambar |
| `\includegraphics[width=...]{filename}` | Load gambar. Width bisa px, cm, atau ratio dari textwidth |
| `\caption{...}` | Caption gambar (muncul di bawah gambar) |
| `\label{fig:...}` | Label untuk referensi |

### Positioning Options

```latex
[h]   % here - coba di posisi kode ditulis
[t]   % top - di bagian atas halaman
[b]   % bottom - di bagian bawah halaman
[p]   % page - di halaman khusus untuk float
[H]   % HERE - paksa di sini (butuh package float)
```

Bisa combine: `[htb]` = coba here, kalau ga bisa top, kalau ga bisa bottom.

### Referensi Gambar

```latex
Seperti terlihat pada Gambar \ref{fig:mesh1}, mesh yang digunakan...

Visualisasi mesh dapat dilihat di halaman \pageref{fig:mesh1}.
```

**Output:**  
"Seperti terlihat pada Gambar 2.1, mesh yang digunakan..."  
"Visualisasi mesh dapat dilihat di halaman 15."

### Size Options

```latex
% Dengan width
\includegraphics[width=8cm]{mesh}

% Dengan height
\includegraphics[height=5cm]{mesh}

% Relative terhadap text width
\includegraphics[width=0.5\textwidth]{mesh}  % 50% lebar text

% Dengan aspect ratio
\includegraphics[width=0.8\textwidth, height=6cm, keepaspectratio]{mesh}

% Scale
\includegraphics[scale=0.5]{mesh}  % 50% ukuran asli
```

### Multiple Gambar (Subfigure)

```latex
\usepackage{subcaption}

\begin{figure}[h]
    \centering
    \begin{subfigure}{0.45\textwidth}
        \includegraphics[width=\textwidth]{image1}
        \caption{Gambar pertama}
        \label{fig:sub1}
    \end{subfigure}
    \hfill
    \begin{subfigure}{0.45\textwidth}
        \includegraphics[width=\textwidth]{image2}
        \caption{Gambar kedua}
        \label{fig:sub2}
    \end{subfigure}
    \caption{Perbandingan dua metode}
    \label{fig:comparison}
\end{figure}
```

---

## Membuat Unordered List

Unordered list (bullet points) menggunakan environment `itemize`:

```latex
\begin{itemize}
    \item Item pertama dengan bullet point
    \item Item kedua
    \item Item ketiga
\end{itemize}
```

### Nested List

```latex
\begin{itemize}
    \item Item level 1
    \item Item level 1 lagi
    \begin{itemize}
        \item Sub-item level 2
        \item Sub-item level 2 lagi
        \begin{itemize}
            \item Sub-sub-item level 3
        \end{itemize}
    \end{itemize}
    \item Item level 1 lagi
\end{itemize}
```

### Custom Bullet Symbol

```latex
\begin{itemize}
    \item[$\star$] Item dengan bintang
    \item[$\checkmark$] Item dengan checkmark
    \item[$\rightarrow$] Item dengan panah
\end{itemize}
```

---

## Ordered List

Ordered list (numbered) menggunakan environment `enumerate`:

```latex
\begin{enumerate}
    \item Ini adalah entry pertama dalam list
    \item Nomor list akan bertambah otomatis
    \item Entry ketiga
\end{enumerate}
```

### Nested Numbered List

```latex
\begin{enumerate}
    \item Item pertama
    \item Item kedua
    \begin{enumerate}
        \item Sub-item 2.1
        \item Sub-item 2.2
    \end{enumerate}
    \item Item ketiga
\end{enumerate}
```

**Output:**
```
1. Item pertama
2. Item kedua
   a. Sub-item 2.1
   b. Sub-item 2.2
3. Item ketiga
```

### Custom Numbering

```latex
\usepackage{enumerate}

\begin{enumerate}[a)]  % a), b), c)
    \item Item pertama
    \item Item kedua
\end{enumerate}

\begin{enumerate}[i.]  % i., ii., iii.
    \item Item pertama
    \item Item kedua
\end{enumerate}
```

### Mixed Lists

```latex
\begin{enumerate}
    \item Item numbered
    \begin{itemize}
        \item Sub-item bullet
        \item Sub-item bullet lagi
    \end{itemize}
    \item Item numbered lagi
\end{enumerate}
```

---

## Inline Math

Inline math digunakan untuk menulis formula matematika di dalam kalimat:

### Sintaks Dasar

```latex
Dalam fisika, ekuivalensi massa-energi dinyatakan dengan persamaan 
$E=mc^2$, ditemukan tahun 1905 oleh Albert Einstein.
```

**Output:**  
Dalam fisika, ekuivalensi massa-energi dinyatakan dengan persamaan E=mc², ditemukan tahun 1905 oleh Albert Einstein.

### Contoh Formula Inline

```latex
% Variabel dengan subscript
Nilai $x_1$ dan $x_2$ adalah solusi dari persamaan.

% Superscript (pangkat)
Formula $a^2 + b^2 = c^2$ adalah teorema Pythagoras.

% Fraction
Probabilitas kejadian A adalah $P(A) = \frac{n(A)}{n(S)}$.

% Greek letters
Sudut $\theta$ dan $\phi$ membentuk segitiga.

% Kombinasi
Rumus kuadrat: $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$
```

---

## Display Math

Display math untuk formula yang berdiri sendiri (centered, di baris terpisah):

### Sintaks Dasar

```latex
% Cara 1: $$...$$
$$
E = mc^2
$$

% Cara 2: \[...\] (lebih direkomendasikan)
\[
E = mc^2
\]

% Cara 3: equation environment (dengan numbering)
\begin{equation}
E = mc^2
\label{eq:einstein}
\end{equation}
```

### Equation dengan Referensi

```latex
Persamaan Einstein (\ref{eq:einstein}) menunjukkan...

% Atau dengan eqref (tambah tanda kurung otomatis)
\usepackage{amsmath}
Persamaan Einstein \eqref{eq:einstein} menunjukkan...
```

### Multiple Equations

```latex
% Align environment (untuk align pada '=')
\begin{align}
x &= 2y + 3 \\
y &= 3x - 1
\end{align}

% Tanpa numbering
\begin{align*}
f(x) &= x^2 + 2x + 1 \\
     &= (x+1)^2
\end{align*}
```

### Common Math Symbols

```latex
% Operators
$a + b$       % Plus
$a - b$       % Minus
$a \times b$  % Kali
$a \div b$    % Bagi
$\frac{a}{b}$ % Fraction

% Subscript dan Superscript
$x_1, x_2, x_3$     % Subscript
$x^2, x^3$          % Superscript
$x_1^2$             % Kombinasi

% Greek letters
$\alpha, \beta, \gamma, \delta$
$\theta, \phi, \psi, \omega$
$\Sigma, \Pi, \Omega$

% Relations
$a = b$       % Sama dengan
$a \neq b$    % Tidak sama dengan
$a < b$       % Lebih kecil
$a > b$       % Lebih besar
$a \leq b$    % Lebih kecil atau sama dengan
$a \geq b$    % Lebih besar atau sama dengan

% Set notation
$x \in A$     % x anggota A
$A \cup B$    % Union
$A \cap B$    % Intersection
$A \subset B$ % Subset

% Calculus
$\int_a^b f(x) dx$        % Integral
$\sum_{i=1}^n x_i$        % Summation
$\lim_{x \to \infty} f(x)$ % Limit
$\frac{dy}{dx}$           % Derivative

% Matrix
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
```

### Contoh Kompleks

```latex
\begin{equation}
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
\end{equation}

\begin{equation}
f(x) = \begin{cases}
    x^2 & \text{if } x \geq 0 \\
    -x^2 & \text{if } x < 0
\end{cases}
\end{equation}
```

---

## Abstract

Abstract adalah ringkasan singkat dari isi dokumen, biasanya ada di paper ilmiah:

```latex
\documentclass{article}
\usepackage[bahasa]{babel}

\title{Judul Paper}
\author{Nama Penulis}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
Ini adalah abstrak dari paper. Abstrak berisi ringkasan singkat 
tentang tujuan penelitian, metodologi yang digunakan, hasil yang 
didapat, dan kesimpulan. Biasanya panjang abstrak adalah 150-250 kata.

\textbf{Kata kunci:} machine learning, neural network, classification
\end{abstract}

\section{Pendahuluan}
Ini adalah bagian pendahuluan...

\end{document}
```

**Tips Menulis Abstract:**
- Ringkas dan jelas (150-250 kata)
- Jelaskan tujuan penelitian
- Sebutkan metodologi secara singkat
- Highlight hasil utama
- Tulis kesimpulan
- Tambahkan kata kunci (keywords)

---

## Sections dan Subsections

LaTeX punya hierarki heading yang terstruktur:

```latex
\section{Pendahuluan}
Ini adalah section level 1.

\subsection{Latar Belakang}
Ini adalah subsection (level 2).

\subsubsection{Definisi Masalah}
Ini adalah subsubsection (level 3).

\paragraph{Scope Penelitian}
Ini adalah paragraph heading (level 4).

\subparagraph{Detail Scope}
Ini adalah subparagraph (level 5).
```

### Numbering

Secara default, sections akan numbered otomatis:
```
1 Pendahuluan
  1.1 Latar Belakang
      1.1.1 Definisi Masalah
```

### Section Tanpa Numbering

```latex
\section*{Acknowledgments}
Terima kasih kepada...

\subsection*{Funding}
Penelitian ini didanai oleh...
```

**Catatan:** Section dengan `*` tidak akan muncul di Table of Contents kecuali ditambahkan manual.

---

## Table of Contents

LaTeX bisa generate table of contents otomatis:

```latex
\documentclass{article}

\title{Judul Dokumen}
\author{Penulis}
\date{\today}

\begin{document}

\maketitle

\tableofcontents  % Generate TOC otomatis

\newpage  % Mulai konten di halaman baru

\section{Pendahuluan}
Lorem ipsum...

\subsection{Latar Belakang}
Lorem ipsum...

\section{Metodologi}
Lorem ipsum...

\subsection{Desain Penelitian}
Lorem ipsum...

\end{document}
```

**Cara Kerja:**
1. LaTeX scan semua `\section`, `\subsection`, dll
2. Generate TOC dengan numbering dan page numbers
3. Butuh compile 2 kali untuk update TOC yang benar

### Customize TOC Depth

```latex
% Hanya tampilkan sampai subsection
\setcounter{tocdepth}{2}

% 0 = chapter (untuk book/report)
% 1 = section
% 2 = subsection
% 3 = subsubsection
```

### List of Figures & Tables

```latex
\listoffigures  % Daftar gambar
\listoftables   % Daftar tabel
```

---

## Packages yang Berguna

Packages extend fungsi LaTeX:

### Essential Packages

```latex
% Preamble
\usepackage[utf8]{inputenc}      % Input encoding
\usepackage[T1]{fontenc}         % Font encoding
\usepackage[bahasa]{babel}       % Bahasa Indonesia
\usepackage{graphicx}            % Gambar
\usepackage{amsmath, amssymb}    % Math symbols
\usepackage{hyperref}            % Clickable links di PDF
```

### Layout & Formatting

```latex
\usepackage{geometry}
\geometry{
    a4paper,
    margin=1in
}

\usepackage{setspace}
\doublespacing  % Double spacing
```

### Advanced Math

```latex
\usepackage{amsmath}    % Advanced math
\usepackage{amssymb}    % Extra symbols
\usepackage{mathtools}  % Math tools
```

### Code Listing

```latex
\usepackage{listings}
\usepackage{xcolor}

\lstset{
    language=Python,
    basicstyle=\ttfamily,
    keywordstyle=\color{blue},
    commentstyle=\color{green},
    stringstyle=\color{red},
    showstringspaces=false
}

\begin{lstlisting}
def hello():
    print("Hello World")
\end{lstlisting}
```

### Tables

```latex
\usepackage{booktabs}  % Professional tables
\usepackage{tabularx}  % Flexible tables
```

### Bibliography

```latex
\usepackage[backend=biber, style=apa]{biblatex}
\addbibresource{references.bib}
```

---

## Tips dan Tricks

### 1. Compile Multiple Kali

Untuk cross-references, TOC, bibliography:
```bash
pdflatex dokumen.tex
pdflatex dokumen.tex  # Compile lagi untuk update references
```

### 2. Non-Breaking Space

Cegah line break di tempat yang tidak diinginkan:
```latex
Dr.~Einstein  % ~ adalah non-breaking space
Gambar~\ref{fig:mesh1}
```

### 3. Quotation Marks

```latex
% SALAH
"Quoted text"

% BENAR
``Quoted text''  % Double backtick di awal, double quote di akhir
```

### 4. Dashes

```latex
Hyphen: kata-kata
En-dash: 1990--2000
Em-dash: This is---important
```

### 5. Special Characters

```latex
\% \$ \& \# \_ \{ \}
```

### 6. Avoid Overfull/Underfull Boxes

```latex
% Jika ada warning tentang overfull hbox
\usepackage{microtype}  % Improve typography
```

### 7. Draft Mode

```latex
\documentclass[draft]{article}
% Gambar di-skip, compile lebih cepat untuk review
```

---

## Referensi

### Dokumentasi & Tutorial
- [Overleaf: Learn LaTeX in 30 Minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) - Tutorial interaktif
- [LaTeX Documentation](https://devdocs.io/latex/) - Dokumentasi lengkap
- [CTAN](https://www.ctan.org/) - Comprehensive TeX Archive Network (repository packages)
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX) - Panduan lengkap

### Online Editors
- [Overleaf](https://www.overleaf.com/) - Online LaTeX editor (paling populer)
- [CoCalc](https://cocalc.com/) - Collaborative calculation
- [Papeeria](https://papeeria.com/) - Online LaTeX editor

### Desktop Editors
- **TeXstudio** (Windows, Mac, Linux) - Full-featured IDE
- **TeXmaker** (Cross-platform) - User friendly
- **VS Code** dengan LaTeX Workshop extension

### Symbol Reference
- [Detexify](http://detexify.kirelabs.org/classify.html) - Draw symbol, find LaTeX command
- [Comprehensive LaTeX Symbol List](http://mirrors.ctan.org/info/symbols/comprehensive/symbols-a4.pdf)

### Templates
- [Overleaf Templates](https://www.overleaf.com/latex/templates) - Ribuan template siap pakai
- [LaTeX Templates](http://www.latextemplates.com/) - Template untuk berbagai keperluan

### Komunitas
- [TeX StackExchange](https://tex.stackexchange.com/) - Q&A tentang LaTeX
- [LaTeX Indonesia](https://www.facebook.com/groups/latexindonesia/) - Grup Facebook

### Panduan Khusus
- **Tesis/Skripsi**: Cari template dari universitasmu
- **Paper/Journal**: Cek template dari journal target
- **Beamer** (Presentasi): [Beamer User Guide](http://mirrors.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf)

---

## Quick Reference Card

### Struktur Dokumen
```latex
\documentclass{article}
\usepackage{packages}
\title{Title}
\author{Author}
\begin{document}
\maketitle
Content...
\end{document}
```

### Text Formatting
- **Bold**: `\textbf{text}`
- **Italic**: `\textit{text}`
- **Underline**: `\underline{text}`

### Sections
- `\section{Title}`
- `\subsection{Title}`
- `\subsubsection{Title}`

### Lists
```latex
\begin{itemize}
  \item Bullet
\end{itemize}

\begin{enumerate}
  \item Numbered
\end{enumerate}
```

### Math
- Inline: `$E=mc^2$`
- Display: `\[E=mc^2\]`
- Numbered: `\begin{equation}...\end{equation}`

### Figures
```latex
\begin{figure}[h]
  \includegraphics{file}
  \caption{Caption}
  \label{fig:label}
\end{figure}
```

### References
- `\label{label}` - Buat label
- `\ref{label}` - Reference number
- `\pageref{label}` - Reference page

---
