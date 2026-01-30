# Introduction Python

# Introduction

Salah satu tujuan dari Guido dalam membuat bahasa Python adalah agar bahasa pemrograman ini bisa dengan mudah dibaca oleh siapa saja.

Konsistensi sangatlah penting. Konsistensi di dalam project sangat berpengaruh terhadap kualitas kode yang kamu buat.

## *Code Layout*

### Indentation

Gunakan 4 spasi untuk setiap level indentasi.

```
# Correct:

# Sejajarkan dengan pembatas pembuka
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Tambahkan 4 spasi (level indentasi ekstra) untuk membedakan argumen dari kode lainnya
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents harus menambah satu level
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Atau (opsional)

# Hanging indents bisa diindentasi lebih dari 4 spasi
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)

# Tidak ada indentasi ekstra
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Tambahkan comment untuk memberi pembeda di editor yang mendukung syntax highlighting
if (this_is_one_thing and
    that_is_another_thing):
    # Karena kedua kondisi benar, kita bisa frobnicate
    do_something()

# Tambahkan indentasi ekstra pada baris lanjutan kondisional
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

```

### Tabs atau Spaces?

- Spasi lebih disarankan untuk melakukan indentasi
- Jika sudah memakai tabs, maka selanjutnya juga harus konsisten memakai tabs

Python tidak memperbolehkan untuk menggunakan tabs dan spasi bersamaan. Pilih salah satu dan gunakan secara konsisten.

### Maximum Line Length

Ini adalah aturan dari komunitas Python:

- Untuk penulisan kode maksimal 79 karakter per baris
- Untuk dokumentasi atau comment maksimal 72 karakter per baris

Backslash masih bisa digunakan untuk membuat kelanjutan kode ke baris berikutnya. Jangan lupa untuk menambahkan indentasi pada baris tersebut agar lebih mudah dibaca.

```
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

```

## Penempatan Break Setelah atau Sebelum Operator?

Lebih baik letakkan operator di awal baris baru agar mudah untuk mencocokkan operator dengan operand-nya.

```
# Wrong:
# operator berada jauh dari operand-nya
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

# Correct:
# mudah untuk mencocokkan operator dengan operand
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

```

## Penempatan Blank Line

Beri jarak 2 blank line untuk memisahkan function dan class.

Untuk method yang berada di dalam class, beri jarak 1 blank line.

Ini membantu membuat kode lebih mudah dibaca dan terstruktur dengan baik.

## Source File Encoding

Kode di dalam Python secara default memakai UTF-8. Jangan mengubahnya kecuali untuk keperluan testing atau ada kebutuhan khusus.

### Import Harus Memiliki Baris yang Terpisah

```
## Betul
import os
import sys

## Salah
import os, sys

## Kalau seperti ini boleh, karena mengambil dua object dari satu tempat
from subprocess import Popen, PIPE

```

Import sebaiknya dikelompokkan dalam urutan berikut:

1. Standard library imports (library bawaan Python)
2. Related third party imports (library pihak ketiga)
3. Local application/library specific imports (import dari kode lokal kamu sendiri)

Kamu harus memberi blank line di antara setiap grup import untuk memudahkan pembacaan.

Absolute imports lebih direkomendasikan karena lebih jelas dan mudah dipahami:

```
# Contoh 1: Absolute imports
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

## Contoh 2: Relative imports
from . import sibling
from .sibling import example

```

Saat import class dari module yang memiliki class:

```
from myclass import MyClass
from foo.bar.yourclass import YourClass

```

## Penggunaan Spasi untuk Menata Kode

Berikut adalah aturan penggunaan spasi yang benar:

```
# Correct:
spam(ham[1], {eggs: 2})
# Wrong:
spam( ham[ 1 ], { eggs: 2 } )

# Correct:
foo = (0,)
# Wrong:
bar = (0, )

# Correct:
if x == 4: print(x, y); x, y = y, x
# Wrong:
if x == 4 : print(x , y) ; x , y = y , x

# Correct:
spam(1)
# Wrong:
spam (1)

# Correct:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
# Wrong:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]

# Correct:
dct['key'] = lst[index]
# Wrong:
dct ['key'] = lst [index]

# Correct:
x = 1
y = 2
long_variable = 3
# Wrong:
x             = 1
y             = 2
long_variable = 3

# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
# Wrong:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# Correct:
def munge(input: AnyStr): ...
def munge() -> PosInt: ...
# Wrong:
def munge(input:AnyStr): ...
def munge()->PosInt: ...

# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

# Correct:
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
# Wrong:
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...

# Correct:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
# Rather not:

# Wrong:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()

# Wrong:
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()
# Definitely not:

# Wrong:
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()

```

## When to Use Trailing Commas

Trailing commas biasanya opsional, tapi kamu mungkin membutuhkannya jika ingin memudahkan update data di masa depan.

```
# Correct:
FILES = ('setup.cfg',)
# Wrong:
FILES = 'setup.cfg',

# Wrong:
FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)

```

## Comment dalam Kode

Comment inline bisa membantu menjelaskan kode:

`x = x + 1                 # Increment x`

Tapi kadang, comment yang lebih deskriptif lebih berguna:

`x = x + 1                 # Kompensasi untuk border`

## Docstring

[PEP 257](https://peps.python.org/pep-0257) menjelaskan konvensi docstring yang baik. Yang paling penting, `"""` penutup untuk multiline docstring harus berada di baris tersendiri:

```
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""

```

Untuk one liner docstrings, biarkan penutup `"""` di baris yang sama:

```python
"""Return an ex-parrot."""
```

## Penulisan Comment

Comment yang tidak sesuai dengan kode lebih buruk daripada tidak ada comment. Pastikan selalu update comment kamu jika melakukan perubahan kode.

Comment haruslah kalimat lengkap dan dimulai dengan huruf besar. Pastikan comment tersebut bisa dibaca dan dipahami oleh orang lain yang akan membaca kode kamu.

## Penamaan (Naming Convention)

Berikut adalah gaya penamaan yang umum digunakan:

- `b` (single lowercase letter)
- `B` (single uppercase letter)
- `lowercase`
- `lower_case_with_underscores`
- `UPPERCASE`
- `UPPER_CASE_WITH_UNDERSCORES`
- `CapitalizedWords` atau CapWords, atau CamelCase (dinamakan demikian karena bentuk hurufnya yang seperti punuk unta). Ini juga kadang dikenal sebagai StudlyCaps.
    
    Catatan: Saat menggunakan akronim di CapWords, kapitalkan semua huruf dari akronim tersebut. Jadi HTTPServerError lebih baik daripada HttpServerError.
    
- `mixedCase` (berbeda dari CapitalizedWords karena huruf awal lowercase)
- `Capitalized_Words_With_Underscores` (tidak direkomendasikan, kurang bagus)

## Penggunaan is

Gunakan `is not` daripada `not ... is`:

```
# Correct:
if foo is not None:
# Wrong:
if not foo is None:

```

Hindari penggunaan lambda untuk fungsi sederhana, lebih baik gunakan def:

```
# Correct:
def f(x): return 2*x
# Wrong:
f = lambda x: 2*x

```

## Konsisten dalam Melakukan If Statement

Pastikan kamu konsisten dalam menulis if statement. Return value harus konsisten di setiap kondisi:

```
# Correct:

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

# Wrong:

def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)

```

## Note

Beberapa istilah atau kata kunci penting yang perlu dipahami:

- assert statement
- multiline if statement
- multiple with statement

## Reference:

- [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

# Python Code Guide

## Variabel

Variabel adalah tempat untuk menyimpan data dengan tipe data tertentu. 

Beberapa tipe data yang ada di Python:

### Integer

Integer adalah tipe data untuk nilai angka bulat tanpa koma. 

Contoh: -32768, 0, 100, 32768

### Float (Nilai Riil)

Perbedaan antara float dan integer adalah nilai di belakang koma. Float digunakan untuk angka desimal.

Contoh: 3.14, 2.5, -0.001

### Character

Character adalah karakter tunggal. Contohnya "\n" adalah karakter yang digunakan untuk membuat baris baru.

### String

String harus diawali dengan " atau '. String berisi kumpulan karakter atau teks.

Contoh: "Halo dunia", 'Python programming'

### Boolean

Tipe data untuk menyatakan benar atau salah. Hanya ada dua nilai: True atau False.

### Tipe Terstruktur / Function

Function adalah blok kode atau kumpulan kode yang dapat dipakai berulang kali kapan saja dibutuhkan.

# Python Guide

## Perbedaan dari Cache dan Database

Kita harus memahami konsep ini dengan baik. Ingat pattern input, proses, dan output.

Pada **cache**, kamu menyimpan data **output** (hasil pemrosesan). Kalau bisa, jauhi caching karena ini bisa memberikan data yang outdated. Kamu tidak perlu backup data cache karena data ini bisa dibuat lagi kapan saja.

Pada **database**, data yang kamu simpan adalah **input**. Biasanya dimasukkan oleh manusia atau data yang merepresentasikan kondisi di dunia nyata. Sangat penting untuk backup data database karena kamu tidak bisa membuatnya lagi begitu saja. Sedangkan output seperti HTML atau JSON tidak terlalu bernilai karena kita bisa generate ulang dari data mentahnya.

## Relational Database

Pakailah SQL database karena bisa dipakai di berbagai kondisi dan lebih reliable.

Misalkan PostgreSQL sebagai database utama, sedangkan NoSQL bisa dipakai sebagai penyimpanan cache atau untuk kebutuhan spesifik.

PostgreSQL memiliki dokumentasi yang sangat bagus dan lengkap: [https://www.postgresql.org/docs/current/index.html](https://www.postgresql.org/docs/current/index.html)

## Cardinality

Cardinality menjelaskan hubungan antar data dalam database. Ini penting untuk memahami relasi antar tabel.

Reference:

- [https://en.wikipedia.org/wiki/Cardinality_(data_modeling)](https://en.wikipedia.org/wiki/Cardinality_(data_modeling))
- [https://github.com/guettli/programming-guidelines#2-data-structures](https://github.com/guettli/programming-guidelines#2-data-structures)

---

## Basic Python

Panduan ini ditujukan untuk orang yang sudah memahami atau pernah bermain dengan bahasa pemrograman sebelumnya.

## Literal Constant

Literals pada Python terdiri dari: Numeric, String, Boolean, Special (None), dan Literal Collection.

```
var_a = 4  # Integer
var_b = 3.14  # Float
var_c = 'nama orang'  # String

```

Penjelasan:
- "var_a" adalah integer atau numeric literal
- "var_b" adalah nilai desimal dengan tipe float
- "var_c" adalah string

## Kata Kunci yang Tidak Bisa Dipakai sebagai Variabel

Berikut adalah reserved keywords di Python yang tidak boleh digunakan sebagai nama variabel:

```
if, else, for, while, is, as, or, not, and, None, def, class, return, yield, pass, raise, True, False

```

## Operands

Operands juga bisa disebut sebagai variabel. Aturan penting: nama variabel tidak boleh dimulai dari angka dan Python itu case sensitive (huruf besar dan kecil dianggap berbeda).

```
## Dynamically typed:

my_var = 34
my_var = "string"
my_var = [1, 2, 3, 4]
my_var = 3.14

# Variabel bukanlah sebuah tipe yang fix. Python menggunakan garbage collection untuk manajemen memori

```

Beberapa teknik untuk penamaan variabel (naming style):

**Camel Casing Names** (sesuai untuk variabel)
- Contoh: myVar, myString

**Capital Camel Casing Names** (sesuai untuk penamaan class)
- Contoh: MyVar, FileData

**Snake Casing Names** (sesuai untuk variabel atau function names)
- Contoh: my_var, file_data

## Operators

Operator dipakai untuk menjalankan operasi pada operands atau variabel. Ada beberapa jenis operator: arithmetic, assignment, comparison, bitwise, logical, membership, dan identity.

```
# Arithmetic operators
+, -, *, /, %, **, //

# Assignment operators
=, +=, -=, *=, /=, %=, //=, **=, &=, |=, >>=, <<=

# Comparison operators
==, !=, >, <, >=, <=

# Bitwise operators
&, |, ~, <<, >>

# Logical operators
not, and, or

# Membership operators
in, not in

# Identity operators
is, is not

```

## Expressions

Expression adalah evaluasi dari Python interpreter yang menghasilkan nilai atau sequence dengan melakukan operasi (aritmatik, conditional, atau lambda function).

```
# Beberapa contoh expression

"yes" + " this"
x + 6
3 if a==3 else 2
a or b
2 and 3
lambda x: x**2

```

SRC: https://www.petanikode.com/statement-vs-expression/ 

Perbedaan penting:
- **Statement** adalah bagian kode yang mengerjakan sesuatu
- **Expression** adalah bagian kode yang menghasilkan nilai

Contoh statement: loop, if, deklarasi variabel, dan lain-lain.

Contoh kode:
```python
if True:  # ini adalah statement
    nilai = 2 + 3  # "nilai" adalah statement, sedangkan "2 + 3" adalah expression
    print(nilai)  # "print" adalah statement
```

Print bisa menjadi expression jika hasilnya dimasukkan ke dalam variabel.

Ada cara mudah untuk membedakan statement atau expression:
Coba masukkan command tersebut ke dalam variabel. Jika bisa dimasukkan ke variabel maka itu termasuk expression, jika tidak maka itu statement.

Contoh expression:
```python
nilaiA = eval("1 + 1")
nilaiB = 10 + 5
```

```python
value = 10
requirement = 'my apple is 10' if value < 10 else 'my apple not 10'
```

SRC: https://www.petanikode.com/statement-vs-expression/

## Python Syntactic Sugar

Syntactic sugar adalah cara lain untuk menulis expression atau statements dengan cara yang lebih ringkas dan mudah.

```
## Beberapa contoh

a = b = c = 10
# Semua variabel akan bernilai 10

text = "This is text 1. " \
"This is text 2 " \
"And I can also continue here in the next line."

```

## Comments

Comment digunakan untuk memberi penjelasan pada kode agar lebih mudah dipahami.

```
# Ini adalah single line comment

# TODO: Ini adalah todo comment untuk menandai pekerjaan yang harus dilakukan

"""
Ini adalah multiline comment atau docstring
Bisa digunakan untuk menjelaskan fungsi atau class
"""

```

## Indentation

Indentation (indentasi) dipakai untuk Flow Control, Exception Handling, dan Function atau Class definitions pada Python. IndentationError akan muncul jika kamu salah menggunakan indentasi.

```
## Contoh penggunaan indentasi

if 10 > 5:
    print('printed')

```

## Three Types of Namespaces

Python memiliki tiga jenis namespace:

### Built-in Namespace

Berisi fungsi-fungsi bawaan Python yang bisa langsung dipakai.

```
# Contoh fungsi built-in:
# print(), len(), map(), range(), list(), set(), str(), dll.

```

### Global Namespace

Berisi module yang di-import dan variabel atau fungsi yang didefinisikan di level global.

```
import time
my_var = 10

# Semua import module
# Variabel, functions, atau classes yang didefinisikan di level global

```

### Local Namespace

Berisi variabel dan fungsi yang didefinisikan di dalam sebuah fungsi.

```
def name_function():
    my_var = 10

    def name_fun():
        pass

# Variabel "my_var" dan function "name_fun" berada di dalam local namespace

```

## Note Penting

Beberapa topik yang perlu dipelajari lebih lanjut:
- Condition / if statement
- Case / exception handling
- Function
- List, tuple, sets, dictionaries

## List 

```python
[1, 2, 'halo']
```

List sangat berguna untuk menyimpan data secara terurut. Kamu bisa menyimpan berbagai tipe data dalam satu list dan mengaksesnya berdasarkan index.

Keunggulan list:
- Data terurut
- Bisa diubah (mutable)
- Bisa menyimpan berbagai tipe data
- Support indexing dan slicing

## Dictionary 

```python
{
    'name': 'rangga',
    'age': 20,
    'major': 'sains'
}
```

Dictionary tidak terurut seperti list, tetapi berbentuk pasangan `key:value`. Ini sangat berguna untuk menyimpan data yang memiliki label atau identifier.

Keunggulan dictionary:
- Akses data cepat menggunakan key
- Struktur data yang jelas dan deskriptif
- Fleksibel untuk berbagai kebutuhan

## Tuple

```python
('nasi padang', 'nasi goreng', 'nasi rawon')
```

Tuple sama seperti list, tetapi kita tidak bisa mengubah isinya setelah berhasil dibuat (immutable).

Keunggulan tuple:
- Lebih cepat dari list
- Aman dari perubahan data yang tidak disengaja
- Bisa dipakai sebagai key di dictionary

## Set 

```python
{'kucing', 'anjing', 'katak', 'katak'}
```

Kita tidak bisa melakukan indexing pada set karena tidak terurut, dan data pada set bersifat unik (tidak ada duplikasi). Tetapi data bisa ditambahkan dan dikurangi.

Kelebihan utama set adalah menghilangkan duplikasi pada data secara otomatis. Data yang terduplikasi hanya akan ditampilkan satu kali pada set.

Contoh penggunaan:
```python
# Output: {'kucing', 'anjing', 'katak'}
# 'katak' yang duplikat otomatis dihilangkan
```

SRC: https://www.programiz.com/python-programming/list

# Latihan Python

[Latihan Python](./latihan-bahasa/latihan-py.md)

## Source

- [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- https://github.com/huangsam/ultimate-python
- https://github.com/guettli/programming-guidelines
- [https://github.com/Anku5hk/Programmers_guide_to_Python/blob/main/book.md](https://github.com/Anku5hk/Programmers_guide_to_Python/blob/main/book.md)
- https://github.com/Asabeneh/Python-for-Everyone
- [https://roadmap.sh/python](https://roadmap.sh/python)
