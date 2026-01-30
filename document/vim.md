# Vim Cheatsheet

Vim adalah text editor yang powerful dan tersedia di hampir semua sistem Unix/Linux. Vim memiliki learning curve yang cukup tinggi, tapi setelah mahir, kamu akan bisa mengedit file dengan sangat cepat dan efisien.

## Daftar Isi
1. [Pengenalan Vim](#pengenalan-vim)
2. [Mode dalam Vim](#mode-dalam-vim)
3. [Essentials - Dasar-Dasar](#essentials)
4. [Cursor Movement - Perpindahan Kursor](#cursor-movement-normalvisual-mode)
5. [Editing Text - Mengedit Teks](#editing-text)
6. [Operators - Operator](#operators)
7. [Visual Mode - Mode Visual](#marking-text-visual-mode)
8. [Clipboard - Copy Paste](#clipboard)
9. [Exiting - Keluar dari Vim](#exiting)
10. [Search/Replace - Cari dan Ganti](#searchreplace)
11. [General - Umum](#general)
12. [Advanced - Tingkat Lanjut](#advanced)
13. [Tips dan Trik](#tips-dan-trik)

## Pengenalan Vim

Vim singkatan dari "Vi IMproved". Ini adalah text editor yang sangat populer di kalangan programmer dan system administrator. Yang membuat Vim unik adalah konsep modalnya, di mana keyboard kamu memiliki fungsi berbeda tergantung mode yang sedang aktif.

**Kenapa belajar Vim?**
- Tersedia di hampir semua sistem Unix/Linux
- Sangat cepat dan efisien setelah terbiasa
- Bisa mengedit file tanpa menggunakan mouse
- Customizable dan extensible
- Gratis dan open source

## Mode dalam Vim

Vim memiliki beberapa mode utama:

1. **Normal Mode** (Mode default saat membuka Vim)
   - Untuk navigasi dan perintah
   - Tekan `Esc` untuk kembali ke mode ini

2. **Insert Mode** (Mode untuk mengetik)
   - Untuk memasukkan teks
   - Tekan `i`, `a`, `o` atau `I`, `A`, `O` untuk masuk ke mode ini

3. **Visual Mode** (Mode untuk seleksi)
   - Untuk memilih/menandai teks
   - Tekan `v`, `V`, atau `Ctrl+v` untuk masuk ke mode ini

4. **Command Mode** (Mode perintah)
   - Untuk menjalankan perintah Ex
   - Tekan `:` untuk masuk ke mode ini

## Essentials

### Membuka dan Membuat File

```bash
vim namafile.txt        # Membuka atau membuat file baru
vim +10 namafile.txt    # Membuka file dan langsung ke baris 10
vim -R namafile.txt     # Membuka file dalam mode read-only
```

### Cursor Movement (Normal/Visual Mode)

Perpindahan kursor adalah fondasi dari penggunaan Vim yang efisien.

#### Perpindahan Dasar

- `h` bergerak ke kiri
- `j` bergerak ke bawah
- `k` bergerak ke atas
- `l` bergerak ke kanan

**Tips:** Bayangkan `j` seperti panah ke bawah, dan `k` seperti panah ke atas.

#### Perpindahan Per Kata

- `w` (word) pindah ke awal kata berikutnya
- `b` (back) pindah ke awal kata sebelumnya
- `e` (end) pindah ke akhir kata saat ini/berikutnya
- `ge` pindah ke akhir kata sebelumnya

#### Perpindahan Per Kata (Spasi sebagai Pemisah)

- `W` pindah ke kata berikutnya (hanya spasi sebagai pemisah)
- `B` pindah ke kata sebelumnya (hanya spasi sebagai pemisah)
- `E` pindah ke akhir kata berikutnya (hanya spasi sebagai pemisah)

**Contoh perbedaan `w` vs `W`:**
Untuk teks: `hello-world test`
- `w` akan berhenti di: `hello`, `world`, `test`
- `W` akan berhenti di: `hello-world`, `test`

#### Perpindahan dalam Baris

- `0` (angka nol) pindah ke awal baris
- `$` pindah ke akhir baris
- `^` pindah ke karakter pertama yang bukan spasi di baris

**Contoh:**
Untuk baris: `    hello world`
- `0` akan ke posisi paling kiri (sebelum spasi)
- `^` akan ke huruf 'h' (karakter pertama yang bukan spasi)

## Editing Text

### Masuk ke Insert Mode

- `i` (insert) mulai insert mode di posisi kursor
- `a` (append) mulai insert mode setelah kursor
- `I` mulai insert mode di awal baris
- `A` mulai insert mode di akhir baris
- `o` (open) buat baris baru di bawah dan masuk insert mode
- `O` buat baris baru di atas dan masuk insert mode

**Mnemonic (cara mengingat):**
- `i` = insert (sisipkan di sini)
- `a` = append (tambah setelah ini)
- `o` = open line below (buka baris di bawah)

### Keluar dari Insert Mode

- `Esc` keluar dari insert mode
- `Ctrl+[` alternatif untuk keluar dari insert mode (lebih cepat untuk beberapa orang)

### Operasi Delete dan Change

- `d` (delete) hapus
- `dd` hapus seluruh baris
- `c` (change) hapus lalu masuk insert mode
- `cc` hapus seluruh baris lalu masuk insert mode

## Operators

Operators adalah perintah yang bekerja pada text objects atau motions. Kamu bisa menggabungkan operator dengan movement untuk operasi yang lebih powerful.

### Operator Utama

- `d` (delete) menghapus dari kursor ke lokasi movement
- `c` (change) menghapus dari kursor ke lokasi movement, lalu masuk insert mode
- `y` (yank) menyalin dari kursor ke lokasi movement
- `>` indent satu level
- `<` unindent satu level

### Contoh Kombinasi Operator + Motion

```
dw    # Delete word (hapus kata)
d$    # Delete sampai akhir baris
d0    # Delete sampai awal baris
c2w   # Change 2 words (hapus 2 kata dan masuk insert mode)
y3j   # Yank (copy) 3 baris ke bawah
d3k   # Delete 3 baris ke atas
>3j   # Indent 3 baris ke bawah
```

**Rumus:** `[jumlah] operator motion`

### Text Objects

Text objects membuat editing lebih intuitif. Format: `operator [i/a] object`

- `i` berarti "inner" (di dalam)
- `a` berarti "around" (termasuk pembungkusnya)

**Contoh:**
```
di(   # Delete inner parentheses (hapus isi dalam kurung)
da(   # Delete around parentheses (hapus termasuk kurungnya)
ciw   # Change inner word (ubah kata)
ci"   # Change inner quotes (ubah teks dalam tanda kutip)
dit   # Delete inner tag (untuk HTML)
```

**Text objects yang tersedia:**
- `w` word (kata)
- `s` sentence (kalimat)
- `p` paragraph (paragraf)
- `(` atau `)` atau `b` parentheses
- `[` atau `]` square brackets
- `{` atau `}` atau `B` curly braces
- `<` atau `>` angle brackets
- `"` double quotes
- `'` single quotes
- `` ` `` backticks
- `t` tag (HTML/XML)

## Marking Text (Visual Mode)

Visual mode memungkinkan kamu memilih teks secara visual sebelum melakukan operasi.

### Masuk Visual Mode

- `v` mulai visual mode (karakter per karakter)
- `V` mulai linewise visual mode (baris per baris)
- `Ctrl+v` mulai visual block mode (kolom/blok)

### Keluar dari Visual Mode

- `Esc` atau `Ctrl+[` keluar dari visual mode

### Operasi di Visual Mode

Setelah memilih teks di visual mode, kamu bisa:
- `d` atau `x` hapus teks yang dipilih
- `c` hapus dan masuk insert mode
- `y` copy teks yang dipilih
- `>` atau `>>` indent teks yang dipilih
- `<` atau `<<` unindent teks yang dipilih
- `~` toggle case (besar/kecil huruf)
- `u` ubah ke huruf kecil
- `U` ubah ke huruf besar

## Clipboard

### Copy (Yank)

- `yy` atau `Y` copy seluruh baris
- `yw` copy satu kata
- `y$` copy sampai akhir baris
- `y0` copy sampai awal baris

### Paste

- `p` paste setelah kursor/baris
- `P` paste sebelum kursor/baris

**Tips:** Di Vim, "yank" artinya copy. Jadi `yy` = copy baris.

### Cut (Delete)

- `dd` cut (hapus) seluruh baris
- `x` hapus karakter di bawah kursor (seperti tombol Del)
- `X` hapus karakter sebelum kursor (seperti tombol Backspace)
- `dw` cut satu kata

**Catatan:** Saat kamu delete dengan `d` atau `c`, teks otomatis ter-copy ke clipboard, jadi bisa di-paste dengan `p`.

## Exiting

### Menyimpan dan Keluar

- `:w` write (simpan) file, tapi tidak keluar
- `:wq` atau `:x` write (simpan) dan quit (keluar)
- `ZZ` shortcut untuk save dan quit (tidak perlu titik dua)
- `:w namafile.txt` simpan dengan nama file tertentu

### Keluar Tanpa Menyimpan

- `:q` quit (gagal jika ada perubahan)
- `:q!` quit dan buang semua perubahan
- `ZQ` shortcut untuk quit tanpa save (tidak perlu titik dua)

**Tips untuk pemula:** Jika kamu stuck di Vim dan ingin keluar cepat, tekan `Esc` beberapa kali lalu ketik `:q!` dan Enter.

## Search/Replace

### Search (Mencari)

- `/pattern` cari pattern ke depan
- `?pattern` cari pattern ke belakang
- `n` repeat search ke arah yang sama
- `N` repeat search ke arah berlawanan

**Contoh:**
```
/hello        # Cari kata "hello" ke depan
?world        # Cari kata "world" ke belakang
/\cfoo        # Cari "foo" (case insensitive)
/foo\|bar     # Cari "foo" atau "bar"
```

### Replace (Mengganti)

- `:%s/old/new/g` ganti semua "old" dengan "new" di seluruh file
- `:%s/old/new/gc` ganti semua dengan konfirmasi
- `:s/old/new/g` ganti di baris saat ini saja
- `:%s/old/new/gi` ganti (case insensitive)

**Breakdown perintah `:%s/old/new/g`:**
- `%` berarti seluruh file
- `s` berarti substitute (ganti)
- `/old/new/` pattern lama dan baru
- `g` berarti global (semua di baris tersebut)
- `c` untuk konfirmasi (opsional)

**Options saat konfirmasi:**
- `y` yes (ganti ini)
- `n` no (skip ini)
- `a` all (ganti semua yang tersisa)
- `q` quit (berhenti)
- `l` last (ganti ini dan berhenti)

## General

### Undo dan Redo

- `u` undo (batalkan perubahan terakhir)
- `Ctrl+r` redo (kembalikan perubahan yang dibatalkan)
- `U` undo semua perubahan di baris saat ini

### Repeat Command

- `.` (titik) repeat perintah terakhir

**Contoh:**
```
dd     # Hapus satu baris
.      # Hapus satu baris lagi
.      # Hapus satu baris lagi
```

## Advanced

### Cursor Movement Lanjutan

#### Perpindahan Per Halaman

- `Ctrl+d` geser ke bawah setengah halaman
- `Ctrl+u` geser ke atas setengah halaman
- `Ctrl+f` geser ke bawah satu halaman penuh (forward)
- `Ctrl+b` geser ke atas satu halaman penuh (backward)

#### Perpindahan Per Paragraf

- `}` maju ke paragraf berikutnya (baris kosong berikutnya)
- `{` mundur ke paragraf sebelumnya (baris kosong sebelumnya)

#### Perpindahan ke Baris Tertentu

- `gg` atau `:1` ke baris pertama file
- `G` atau `:$` ke baris terakhir file
- `:10` atau `10G` ke baris 10
- `50%` ke 50% dari file

#### Scroll

- `Ctrl+e` scroll down satu baris (cursor tidak bergerak)
- `Ctrl+y` scroll up satu baris (cursor tidak bergerak)
- `zt` posisikan baris saat ini ke top (atas layar)
- `zz` posisikan baris saat ini ke center (tengah layar)
- `zb` posisikan baris saat ini ke bottom (bawah layar)

### Character Search

Fitur ini memungkinkan kamu melompat ke karakter tertentu dalam satu baris.

- `f[char]` find (cari) karakter ke depan
- `F[char]` find karakter ke belakang
- `t[char]` till (sampai sebelum) karakter ke depan
- `T[char]` till karakter ke belakang
- `;` repeat search ke depan
- `,` repeat search ke belakang

**Contoh:**
Untuk baris: `hello world, this is a test`
- `fw` akan melompat ke huruf 'w' di "world"
- `t,` akan melompat tepat sebelum koma

### Editing Text Lanjutan

- `J` join (gabungkan) baris di bawah ke baris saat ini
- `r[char]` replace karakter di bawah kursor dengan [char]
- `R` masuk replace mode (menimpa teks yang ada)
- `~` toggle case karakter di bawah kursor
- `g~~` toggle case seluruh baris

### Visual Mode Lanjutan

- `O` pindah ke sudut lain dari blok (di visual block mode)
- `o` pindah ke ujung lain dari area yang ditandai
- `gv` reselect (pilih ulang blok terakhir yang dipilih)

## File Tabs

### Mengelola File

- `:e filename` edit file (membuka file)
- `:w filename` write (simpan) dengan nama tertentu
- `:saveas filename` save as (simpan sebagai)

### Tab

- `:tabe` atau `:tabnew` buat tab baru
- `:tabn` atau `gt` ke tab berikutnya
- `:tabp` atau `gT` ke tab sebelumnya
- `:tabc` tutup tab saat ini
- `:tabo` tutup semua tab kecuali yang aktif

### Split Windows (Membagi Layar)

#### Membuat Split

- `:sp` atau `:split` split horizontal (atas/bawah)
- `:vsp` atau `:vsplit` split vertikal (kiri/kanan)
- `Ctrl+w s` split horizontal
- `Ctrl+w v` split vertikal

#### Navigasi Antar Window

- `Ctrl+w w` pindah ke window berikutnya
- `Ctrl+w h` pindah ke window kiri
- `Ctrl+w j` pindah ke window bawah
- `Ctrl+w k` pindah ke window atas
- `Ctrl+w l` pindah ke window kanan

#### Mengatur Ukuran Window

- `Ctrl+w =` samakan ukuran semua window
- `Ctrl+w +` perbesar window vertikal
- `Ctrl+w -` perkecil window vertikal
- `Ctrl+w >` perbesar window horizontal
- `Ctrl+w <` perkecil window horizontal

#### Menutup Window

- `Ctrl+w q` atau `:q` tutup window saat ini
- `Ctrl+w o` atau `:only` tutup semua window kecuali yang aktif

## Marks (Penanda)

Marks memungkinkan kamu menandai posisi tertentu dan melompat kembali ke sana nanti.

### Membuat Mark

- `m[a-z]` buat mark lokal (huruf kecil, untuk file saat ini)
- `m[A-Z]` buat mark global (huruf besar, bekerja antar file)

### Melompat ke Mark

- `'[mark]` melompat ke awal baris di mana mark berada
- `` `[mark] `` melompat ke posisi exact mark (baris dan kolom)
- `''` atau ``` `` ``` kembali ke posisi jump sebelumnya

**Contoh:**
```
ma        # Tandai posisi ini sebagai mark 'a'
(lakukan navigasi ke tempat lain)
'a        # Kembali ke baris mark 'a'
`a        # Kembali ke posisi exact mark 'a'
```

### Mark Otomatis

Vim juga membuat beberapa mark otomatis:
- `'.` posisi perubahan terakhir
- `'"` posisi saat terakhir keluar dari file
- `'[` awal teks yang terakhir diubah/di-yank
- `']` akhir teks yang terakhir diubah/di-yank

## Tips dan Trik

### Numbering dan Relative Number

```vim
:set number           " Tampilkan nomor baris
:set relativenumber   " Tampilkan nomor relatif
:set nonumber         " Sembunyikan nomor baris
```

**Kenapa relative number berguna?**
Dengan relative number, kamu bisa langsung tahu berapa baris yang perlu kamu lompati. Misalnya mau hapus 5 baris ke bawah: `d5j`

### Mencari di Bawah Kursor

- `*` cari kata di bawah kursor (ke depan)
- `#` cari kata di bawah kursor (ke belakang)

### Insert Mode Shortcuts

- `Ctrl+h` hapus karakter sebelumnya (seperti backspace)
- `Ctrl+w` hapus kata sebelumnya
- `Ctrl+u` hapus semua sampai awal baris
- `Ctrl+r 0` paste teks yang terakhir di-yank
- `Ctrl+r "` paste dari default register

### Command Mode Shortcuts

- `Ctrl+r 0` (di command mode) paste teks yang di-yank
- `:!command` jalankan command shell
- `:r !command` baca output command dan masukkan ke file

**Contoh:**
```vim
:!ls              " Jalankan ls di terminal
:r !date          " Masukkan tanggal saat ini ke file
:r !ls -l         " Masukkan hasil ls -l ke file
```

### Macro

Macro memungkinkan kamu merekam serangkaian perintah dan mengulanginya.

```
qa        # Mulai merekam macro di register 'a'
(lakukan serangkaian perintah)
q         # Stop merekam
@a        # Jalankan macro 'a'
@@        # Repeat macro terakhir
10@a      # Jalankan macro 'a' sebanyak 10 kali
```

### Multiple Cursors (Visual Block Mode)

```
Ctrl+v    # Masuk visual block mode
(pilih beberapa baris)
I         # Insert di awal setiap baris
(ketik teks)
Esc       # Terapkan ke semua baris
```

**Contoh use case:** Menambahkan komentar di awal beberapa baris sekaligus.

### Matching Brackets

- `%` melompat ke matching bracket `()`, `[]`, `{}`

**Sangat berguna saat coding!** Letakkan kursor di `(` lalu tekan `%` untuk melompat ke `)`

### Registers

Vim memiliki multiple clipboard yang disebut registers.

- `"ayy` copy baris ke register 'a'
- `"ap` paste dari register 'a'
- `"0` register dengan yank terakhir
- `"1-9` register dengan delete terakhir
- `:reg` lihat semua register

### Auto-Indent

- `==` auto-indent baris saat ini
- `gg=G` auto-indent seluruh file
- `=i{` auto-indent di dalam curly braces

### Folding (Melipat Code)

- `zf` buat fold (di visual mode)
- `zo` buka fold
- `zc` tutup fold
- `za` toggle fold (buka/tutup)
- `zR` buka semua fold
- `zM` tutup semua fold

## Kesalahan Umum Pemula

1. **Lupa mode apa yang sedang aktif**
   - Solusi: Tekan `Esc` beberapa kali untuk memastikan di Normal Mode

2. **Tidak tahu cara keluar**
   - Solusi: `Esc` lalu `:q!` untuk keluar tanpa save

3. **Menggunakan arrow keys**
   - Solusi: Biasakan `hjkl` untuk efisiensi

4. **Tidak memanfaatkan text objects**
   - Solusi: Pelajari `ciw`, `di(`, `da"` dll

5. **Tidak menggunakan `.` (repeat)**
   - Solusi: Setelah melakukan operasi, gunakan `.` untuk repeat

## Konfigurasi Dasar .vimrc

Buat file `~/.vimrc` untuk konfigurasi personal:

```vim
" Tampilan
syntax on                   " Syntax highlighting
set number                  " Tampilkan nomor baris
set relativenumber          " Nomor baris relatif
set cursorline             " Highlight baris saat ini
set showmatch              " Highlight matching brackets

" Indentasi
set autoindent             " Auto indent
set smartindent            " Smart indent
set tabstop=4              " Tab = 4 spasi
set shiftwidth=4           " Indent = 4 spasi
set expandtab              " Gunakan spasi, bukan tab

" Search
set ignorecase             " Case insensitive search
set smartcase              " Case sensitive jika ada huruf besar
set incsearch              " Incremental search
set hlsearch               " Highlight search results

" Lain-lain
set mouse=a                " Enable mouse
set clipboard=unnamedplus  " Gunakan system clipboard
set noswapfile             " Jangan buat swap file
set undofile               " Persistent undo
```

## Resources Belajar Tambahan

### Tutorial Interaktif

1. **vimtutor** (built-in di Vim)
   ```bash
   vimtutor
   ```
   Tutorial interaktif sekitar 30 menit yang sangat recommended untuk pemula.

2. **Vim Adventures** (https://vim-adventures.com/)
   - Game untuk belajar Vim dengan cara fun

3. **OpenVim** (https://www.openvim.com/)
   - Tutorial interaktif di browser

### Cheatsheet Online

- https://vimsheet.com/
- https://vim.rtorr.com/
- https://devhints.io/vim

### Video Tutorial

- "Learning Vim in a Week" di YouTube
- Channel "ThePrimeagen" untuk tips Vim advanced

### Plugin Manager

Setelah mahir Vim dasar, kamu bisa explore plugin:
- **vim-plug** (https://github.com/junegunn/vim-plug)
- **Vundle** (https://github.com/VundleVim/Vundle.vim)

### Neovim

Jika kamu ingin versi modern dari Vim:
- **Neovim** (https://neovim.io/)
- Lebih modular, lebih cepat, dan lebih mudah dikonfigurasi

## Kesimpulan

Vim memiliki learning curve yang cukup curam, tapi investasi waktu untuk belajarnya sangat worth it. Beberapa tips untuk belajar Vim:

1. **Jangan coba belajar semuanya sekaligus** - Fokus pada basic movement dan editing dulu
2. **Gunakan vimtutor** - Tutorial bawaan Vim sangat bagus
3. **Praktik setiap hari** - Gunakan Vim untuk editing sehari-hari
4. **Pelajari satu fitur baru per minggu** - Jangan overwhelm diri sendiri
5. **Disable arrow keys** - Untuk memaksa diri menggunakan `hjkl`
6. **Join komunitas** - Reddit r/vim, Discord servers, dll

Dengan konsisten berlatih, dalam beberapa minggu kamu akan jauh lebih produktif dengan Vim dibanding text editor biasa!

## Reference

Source:
- https://vimsheet.com/
- https://vim.rtorr.com/
- https://www.vim.org/docs.php
- https://github.com/iggredible/Learn-Vim
- https://learnvimscriptthehardway.stevelosh.com/
