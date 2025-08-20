import random
import time
import statistics
import os
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

Aturan penggunaan:
0. Pastikan pull rate kamu sesuaikan dengan gamenya. simulasi inin hanya cocok jika pull rate sama dengan yang ada pada game.
1. Cari tau dengan "go 20 jackpot" dua kali. untuk mengetahui Streak tertinggi
2. lakukan pull 10 secara manual dan berjalan ke nilai mendekati yang tertinggi
3. jika sudah dekat, semisal nilai tertinggi adalah 700, maka Real world pull harus mendekati 700.

-------------------------------------------------------------------------
> Laporan pull Ak (2% atau 0.0020):
tertinggi adalah : 5065


-------------------------------------------------------------------------
Ini adalah Testing Ground untuk HSR. dimana probabilitas milik mereka adalah 0.6%.

0.006 adalah angka desimal.
kita bisa ketahui bentuk persen dengan cara 
0.006 x 100

> Laporan pull HSR (0.6% atau 0.0006):
Streak tertinggi adalah 15520, 10191
Modus Jackpot adalah 3986

Record Pull HSR 19/08/2025:
Total pull: 233461
Total jackpot: 112



"""

# probabilitas jackpot
p = 0.0006

# Arknight Chane
#p = 0.0020

# variabel statistik global
total_pulls = 0
total_jackpot = 0
jarak_jackpot = 0
total_jackpot_terakhir = 0
jackpot_list = [0]

# Variabel sampai mendekati jackpot
nilai_N =  15520

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
        #time.sleep(0.0001)
        pull_auto()
        print(f"kamu tidak beruntung, Pull sebelum jackpot: {jarak_jackpot}")
        print(f"Jackpot tertinggi adalah: {max(jackpot_list)}")
        print(f"Total pull     : {total_pulls}")
        clear_screen()
        #if max(jackpot_list) >= 2900:
        #    print("2900 tercapai")
        if jarak_jackpot == (nilai_N - 10):  # Ubah angka ini sesuai dengan jarak jackpot tertinggi yang didapatkan
            print("====================> Real Word Pull Now! <=================")
            print(f"Total pull: {total_pulls}")
            print(f"Total jackpot: {total_jackpot}")
            break


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
        print("6. Keluar")
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
            print("Terima kasih sudah mencoba simulasi!")
            break
        else:
            print("Opsi tidak valid, coba lagi.")


if __name__ == "__main__":
    main()
