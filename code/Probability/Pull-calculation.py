import random
import time
import statistics
import os
import numpy as np
import pandas as pd

"""
# Teori dibalik ini 

1. Memberikan kita jeda waktu untuk melakukan pull. Pull yang akan kita lakukan tidak akan ngawur, melainkan sesuai timing.
2. Memberikan chace kasar yang lebih tinggi untuk mendapatkan jackpot. Karena pull virtual ini, akan memberikan kita chace diluar dari game.
> Perempumaan nomor 2 adalah seperti ini: kita ingin mendapatkan dua dadu dengan angka 6. jika kita hanya melakukan 1 kali percobaan, maka chace kita adalah 1/36. jika kita melakukan 10 kali percobaan, maka chace kita adalah 10/36, lebih baik daripada 1/36.
3. intinya dengan simulasi ini, intinya "Strike when iron is hot".

# Teori dalam bentuk matematika

Jawabannya: Tono jauh lebih mungkin dapat “dua angka enam”.

Budi (1 percobaan melempar 2 dadu):
Peluang dua-enam = .

Tono (10 percobaan, masing-masing melempar 2 dadu):
Peluang gagal terus dalam 10 percobaan = .
Jadi peluang minimal sekali dapat dua-enam =


1-\left(\frac{35}{36}\right)^{10}\approx 1-0{,}7545=0{,}2455 \;=\; \mathbf{24{,}55\%}.

Intuisi sederhana: satu percobaan peluangnya kecil (≈2,78%). Dengan 10 percobaan independen, kesempatan “minimal sekali berhasil” naik jadi ≈24,6%. Per percobaan tetap sama sulitnya, tapi banyak percobaan meningkatkan peluang kumulatif.


# Mengenai waktu kapan pull

Pada teori probabilitas, kapan dilakukan pull tidak akan berpengaruh, karena semua total pull yang akan kita lakkukan dihitunga jadi satu.
Semisal kita melempar dua dadu pada hari senin, dan hari selasa, maka total percobaan yang kita lakukan adalah 2 kali.

# Catatan Pull

Cara penggunaan:
1. Lakukan analisa untuk mengetahui kemungkinan jackpot tertinggi.
2. lakukan auto pull untuk mendekati jackpot tertinggi.
3. jika sudah, maka lakukan simulasi beberapa 10 kali pull, berdasarkan informasi "Frekuensi Jarak Jackpot".
4. kalau misalnya disana rata-rata adalah 300, maka lakukan 300 simulasi pull.
5. setelah itu lakukan pull real world.

## Informasi Fast Pull

Fast pull ini adalah simulasi pull yang dilakukan dalam satu kali perulangan. Semisal kita melakukan 100 pull dalam satu kali perulangan, maka kita tidak perlu melakukan 100 kali perulangan.

intinya pull dilakukan dalam bentuk batch, bukan satu per satu.
jadi atur batch size sesuai dengan kebutuhan.
semisal untuk AK batch size 100, untuk HSR batch size 600.

jangan terlalu besar ukuran batch size, karena akan membuat simulasi kurang detail. semisal nilai jackpot adalah 5000, dengan setiap batch loop adalah 1000, maka simulasi akan kurang detail.

-------------------------------------------------------------------------
> Laporan pull Ak (2% atau 0.0020):
tertinggi adalah : 7036


-------------------------------------------------------------------------
> Laporan pull HSR (0.6% atau 0.0006):
Streak tertinggi adalah 22649
Modus Jackpot adalah 3986

Ini adalah Testing Ground untuk HSR. dimana probabilitas milik mereka adalah 0.6%.

0.006 adalah angka desimal.
kita bisa ketahui bentuk persen dengan cara 
0.006 x 100



Record Pull HSR 19/08/2025:
Total pull: 233461
Total jackpot: 112





====================== CAtatan tidak terpakai ==================================================

Aturan penggunaan:
0. Pastikan pull rate kamu sesuaikan dengan gamenya. simulasi inin hanya cocok jika pull rate sama dengan yang ada pada game.
1. Cari tau dengan "go 20 jackpot" dua kali. untuk mengetahui Streak tertinggi
2. lakukan pull 10 secara manual dan berjalan ke nilai mendekati yang tertinggi
3. jika sudah dekat, semisal nilai tertinggi adalah 700, 
4. lakukan beberapa 10 kali pull simulasi, usahakan jangan terlalu banyak, lalu lakukan 10 pull real world.
"""

# probabilitas jackpot HSR
p = 0.0006

# Arknight Chane
#p = 0.0020

# variabel statistik global
total_pulls = 0
total_jackpot = 0
jarak_jackpot = 0
total_jackpot_terakhir = 0
jackpot_list = [0]

# Variabel sampai mendekati jackpot. Ubah Nilai N sesuai dengan Streak tertinggi yang didapatkan sesuai dengan pull game.
nilai_N =  20_883

# Berapa detik sekali melakukan print
log_interval=10

# Ukuran batch size 
#sSize = 10_000_000
sSize = 3_000_000
print(sSize)

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


def pull_once():
    """Satu kali pull"""
    global total_pulls, total_jackpot, jarak_jackpot, total_jackpot_terakhir
    total_pulls += 1
    jarak_jackpot += 1
    if random.random() < p:
        total_jackpot += 1
        print(f"====>  jackpot || Total Jackpot: {total_jackpot}  <====")
        total_jackpot_terakhir = jarak_jackpot
        jarak_jackpot = 0

    else:
        print(f"kamu tidak beruntung: {jarak_jackpot}")


def pull_20():
    """Satu kali pull"""
    global total_pulls, total_jackpot, jarak_jackpot, total_jackpot_terakhir, jackpot_list
    total_pulls += 1
    jarak_jackpot += 1
    if random.random() < p:
        total_jackpot += 1
        #print("=====================>  jackpot  <====================\n")
        #print(f"Jarak jackpot ke titik sekarang : {jarak_jackpot}")
        #print(f"Total pull jackkpot terakhir  : {total_jackpot_terakhir}")
        jackpot_list.append(jarak_jackpot)
        total_jackpot_terakhir = jarak_jackpot
        jarak_jackpot = 0


def pull_ten():
    """Sepuluh kali pull"""
    for i in range(10):
        print(f"Pull {i+1}: ", end="")
        pull_once()


def pull_auto():
    """Satu kali pull"""
    global total_pulls, total_jackpot, jarak_jackpot, total_jackpot_terakhir,jackpot_list
    total_pulls += 1
    jarak_jackpot += 1
    if random.random() < p:
        total_jackpot += 1
        print(f"====>  jackpot || Total Jackpot: {total_jackpot}  <====")
        total_jackpot_terakhir = jarak_jackpot
        jackpot_list.append(jarak_jackpot)
        jarak_jackpot = 0
   


def jackpot_20():
    """Dapatkan 15 jackpot"""
    while total_jackpot <= 20:
        pull_20()
    jackpot_list.sort(reverse=True)
    print(jackpot_list)
    modus = statistics.mode(jackpot_list)
    print(f"Modus dari data adalah: {modus}")


def automatic_pull():
    """Lakukkan pull otomatis setiap detik, hingga mendekati jackpot."""
    while jarak_jackpot < nilai_N:  # Ubah angka ini sesuai dengan jarak jackpot tertinggi yang didapatkan
        pull_auto()
        print(f"kamu tidak beruntung, Pull sebelum jackpot: {jarak_jackpot}")
        print(f"Target jarak adalah            : {total_jackpot_terakhir}")
        print(f"Jackpot tertinggi adalah       : {max(jackpot_list)}")
        print(f"Total pull                     : {total_pulls}")
        print(f"Total jackpot                  : {total_jackpot}")
        clear_screen()
        #if max(jackpot_list) >= 2900:
        #    print("2900 tercapai")
        if jarak_jackpot >= (nilai_N - 10):  # Ubah angka ini sesuai dengan jarak jackpot tertinggi yang didapatkan
            print("====================> Real Word Pull Now! <=================")
            print(f"Total pull: {total_pulls}")
            print(f"Total jackpot: {total_jackpot}")
            break



# ======================= Fasst 

def automatic_pull_fast(batch_size=sSize):
    """
    Optimized automatic pull.
    Tujuan: hentikan simulasi jika jarak_jackpot >= (nilai_N - 10).
    Gunakan numpy untuk percepat simulasi, pandas untuk analisis distribusi.
    """
    global total_pulls, total_jackpot, jarak_jackpot, total_jackpot_terakhir, jackpot_list
    last_log = time.time()
    while True:
        # Jika sudah mencapai target, hentikan
        if jarak_jackpot >= (nilai_N - 10):
            break  

        # Simulasikan beberapa pull sekaligus (batch)
        pulls = np.random.random(size=batch_size)
        hits = np.where(pulls < p)[0]  # index jackpot. Informasi array dimana saja jackpot ditemukan.
        if len(hits) > 0:
           # Jackpot pertama dalam batch
           #clear_screen()
           first_hit = hits[0] + 1
           total_jackpot_terakhir += first_hit
           total_pulls += first_hit
           total_jackpot += 1
           jarak_jackpot = total_jackpot_terakhir
           jackpot_list.append(jarak_jackpot)
           total_jackpot_terakhir = 0

           """
            print("=====================>  Fast Pull System  <====================\n")
           print(f"kamu tidak beruntung, Pull sebelum jackpot: {total_jackpot_terakhir}")
           print(f"Target jarak adalah            : {(nilai_N - 10)}")
           print(f"Jackpot tertinggi adalah       : {max(jackpot_list)}")
           print(f"Total pull                     : {total_pulls}")
           print(f"Total jackpot                  : {total_jackpot}")
           """
           
        else:
           # Tidak ada jackpot dalam batch
           jarak_jackpot += batch_size
           total_pulls += batch_size
           print(f"Tidak ada jackpot setelah {batch_size} pull (jarak sekarang: {jarak_jackpot})")
            
        # Cek apakah waktunya log progress
        if time.time() - last_log >= log_interval:
            clear_screen()
            print("=====================>  Fast Pull System  <====================\n")
            print(f"kamu tidak beruntung, Pull sebelum jackpot: {jarak_jackpot}")
            print(f"Target jarak adalah            : {(nilai_N - 10)}")
            print(f"Jackpot tertinggi adalah       : {max(jackpot_list)}")
            print(f"Total pull                     : {total_pulls}")
            print(f"Total jackpot                  : {total_jackpot}")
            last_log = time.time()
            

    # Setelah selesai, lakukan pull real world
    print("\033[32m ====================> Real World Pull Now! <================= \033[0m")
    print(f"Total pull       : {total_pulls}")
    print(f"Total jackpot    : {total_jackpot}")
    print(f"Jackpot tertinggi: {max(jackpot_list)}")
    print(f"jarak jackpot terakhir: {total_jackpot_terakhir}")

    # Setelah selesai, tampilkan analisis distribusi jackpot
    df = pd.DataFrame(jackpot_list, columns=["Jarak Jackpot"])
    print("\n📊 Distribusi Jackpot:")
    print(df.describe())  # statistik ringkas
    print("\n📊 Frekuensi Jarak Jackpot:")
    print(df["Jarak Jackpot"].value_counts().head(10))  # 10 nilai paling sering muncul
    try:
        modus = df["Jarak Jackpot"].mode()[0]
        print(f"\nModus Jackpot: {modus}")
    except:
        print("\nModus tidak dapat dihitung (data terlalu unik).")

   

# ========================== fast 

def show_stats():
    """Tampilkan statistik"""
    if total_pulls == 0:
        print("Belum ada percobaan dilakukan.")
    else:
        prob_empiris = total_jackpot / total_pulls * 100
        print("\n=== Statistik ===")
        print(f"Total pull     : {total_pulls}")
        print(f"Jarak jackpot  : {jarak_jackpot}")
        print(f"Total jackpot  : {total_jackpot}")
        print(f"Peluang empiris: {prob_empiris:.3f}% (teoritis {p*100:.3f}%)")


def main():
    global total_jackpot
    while True:
        print("\n=== Simulasi Gacha ===")
        print(f"Jarak jackpot ke titik sekarang : {jarak_jackpot}")
        print(f"Total pull jackkpot terakhir  : {total_jackpot_terakhir}")
        print("1. Pull 1 kali")
        print("2. Pull 10 kali")
        print("3. Lihat statistik")
        print("4. Go 20 Jackpot")
        print("5. Automatic pull")
        print("6. Automatic pull fast")
        print("7. Keluar")
        choice = input("Pilih opsi: ")

        if choice == "1":
            pull_once()
        elif choice == "2":
            pull_ten()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            jackpot_20()
            total_jackpot = 0
        elif choice == "5":
            automatic_pull()
        elif choice == "6":
            automatic_pull_fast()
        elif choice == "7":
            print("Terima kasih sudah mencoba simulasi!")
            break
        else:
            print("Opsi tidak valid, coba lagi.")


if __name__ == "__main__":
    main()
