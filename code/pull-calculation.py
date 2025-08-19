import random
import time

"""
# Catatan Pull

Ini adalah Testing Ground untuk HSR. dimana probabilitas milik mereka adalah 0.6%.

0.006 adalah angka desimal.
kita bisa ketahui bentuk persen dengan cara 
0.006 x 100

Laporan:
Streak tertinggi adalah 953 percobaan

Aturan penggunaan:
1. Cari tau dengan "go 20 jackpot" dua kali. untuk mengetahui Streak tertinggi
2. lakukan pull 10 secara manual dan berjalan ke nilai mendekati yang tertinggi
3. jika sudah dekat, semisal nilai tertinggi adalah 700, maka Real world pull harus mendekati 700.


Laporan pull Ak:
tertinggi adalah 264
"""


# probabilitas jackpot
p = 0.020

# variabel statistik global
total_pulls = 0
total_jackpot = 0
jarak_jackpot = 0
total_jackpot_terakhir = 0

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
    global total_pulls, total_jackpot, jarak_jackpot, total_jackpot_terakhir
    total_pulls += 1
    jarak_jackpot += 1
    if random.random() < p:
        total_jackpot += 1
        print("=====================>  jackpot  <====================\n")
        print(f"Jarak jackpot ke titik sekarang : {jarak_jackpot}") 
        print(f"Total pull jackkpot terakhir  : {total_jackpot_terakhir}") 
        total_jackpot_terakhir = jarak_jackpot
        jarak_jackpot = 0


def pull_ten():
    """Sepuluh kali pull"""
    for i in range(10):
        print(f"Pull {i+1}: ", end="")
        pull_once()

def jackpot_20():
    """Dapatkan 15 jackpot"""
    while total_jackpot <= 20:
        pull_20()

def automatic_pull():
    """Lakukkan pull otomatis setiap detik, hingga mendekati jackpot."""
    while jarak_jackpot < 264: # Ubah angka ini sesuai dengan jarak jackpot tertinggi yang didapatkan
        time.sleep(0.1)
        pull_once()
        if jarak_jackpot == 260: # Ubah angka ini sesuai dengan jarak jackpot tertinggi yang didapatkan
            print("====================> Real Word Pull Now <=================")
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
