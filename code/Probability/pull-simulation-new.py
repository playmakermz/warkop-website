# Script Awal pembuatan : 25-08-2025
import time
import statistics
import os
import numpy as np
import pandas as pd
from math import log, ceil
from datetime import datetime

"""
# Teori dibalik ini

1. Memberikan kita jeda waktu untuk melakukan pull. Pull yang akan kita lakukan tidak akan ngawur, melainkan sesuai timing.
2. Memberikan chace kasar yang lebih tinggi untuk mendapatkan jackpot. Karena pull virtual ini, akan memberikan kita chace diluar dari game.
> Perempumaan nomor 2 adalah seperti ini: kita ingin mendapatkan dua dadu dengan angka 6. jika kita hanya melakukan 1 kali percobaan, maka chace kita adalah 1/36. jika kita melakukan 10 kali percobaan, maka chace kita adalah 10/36, lebih baik daripada 1/36.
3. intinya dengan simulasi ini, intinya "Strike when iron is hot".
4. jangan takut gagal di simulasi trial. Ambil yang menurutmu paling tinggi. kalau gagal bisa coba lagi nanti.

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

# ======================================== Catatan Pull ==============================================================

0. Mengubah Persen ke desimal: 0.50% / 100 = 0,0050

Cara penggunaan:
1. modif Probability dan variabel lainnya.
2. lakukan auto pull
3. lakukan manual pull berkali-kali, ikuti note disetiap game. (HSR, untuk setiap 250 pull simulasi == 1 realword)
4. lakukan real world pull

Cara Penggunaan V2:
1. Ubah Probabilitas ke desimal. Contoh: 0.50% jadi 0.50 / 100 = 0,0050
2. Modifikasi Probabilitas dan variabel
3. Auto pull
4. Manual pull pertama. Jika gagal, lakukan insert pull lalu Manual pull ( ulangi 1-4 kali. lalu reset simulasi )
5. Jangan tergoda dengan 10 pull Real World.



*Hati-hati terkadang ampas itu menyertai simulasi. Untuk HSR gunakan simulasi satu hari satu kali

## Informasi Fast Pull

Fast pull ini adalah simulasi pull yang dilakukan dalam satu kali perulangan. Semisal kita melakukan 100 pull dalam satu kali perulangan, maka kita tidak perlu melakukan 100 kali perulangan.

intinya pull dilakukan dalam bentuk batch, bukan satu per satu.
jadi atur batch size sesuai dengan kebutuhan.
semisal untuk AK batch size 100, untuk HSR batch size 600.

jangan terlalu besar ukuran batch size, karena akan membuat simulasi kurang detail. semisal nilai jackpot adalah 5000, dengan setiap batch loop adalah 1000, maka simulasi akan kurang detail.

----------------------------------------------------------- [ PGR  ]


#Game Name
game_name = "PGR"
# Kemungkinan beruntung!
a_probability = 0.0050
# Berapa banyak minimum percobaan
a_percobaan = 2_300
# Batch  size terkecil mau berapa
a_batchSize = 200
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 20



-------------------------------------------------------------------------[Arknight]-----------------------------------------------------------------------
> Laporan pull Ak (2% atau 0.0020):
tertinggi adalah :     10742
lakukan percobaan di : 8000

Jackpot tertinggi: 10742


>>>>>>>>>>>>> Informasi Variabel yang akan digunakan

#Game Name
game_name = "Arknights"
# Kemungkinan beruntung!
a_probability = 0.0020
# Berapa banyak minimum percobaan
a_percobaan = 4_000
# Batch  size terkecil mau berapa
a_batchSize = 300
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 10

>>>>>>>>>>>>>> Informasi jackpot didapatkan

Jackpot Real pull didapatakan saat: 5, 50, 65, 131, 132, 150+

dengan 10 kali Simulasi percobaan gagal
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
> Laporan pull HSR (0.6% atau 0.0006):
Streak tertinggi adalah :    34_487 | gunakan 20_000 - 21_000
Modus Jackpot adalah 3986

Ini adalah Testing Ground untuk HSR. dimana probabilitas milik mereka adalah 0.6%.

0.006 adalah angka desimal.
kita bisa ketahui bentuk persen dengan cara.

Untuk mendapatkan character 5 Star : 0.006 x 100
gunakan 24_300 untuk mengatur jarak jackpot

Untuk mendapatkan character 4 Star : 5.100 / 100 = 0.051
gunakan 18_000 untuk mengatur jarak jackpot



Record Pull HSR 19/08/2025:
Total pull: 233461
Total jackpot: 112

>>>>>>>       Pengalaman Gacha beruntung 03/09/2025 <<<<<<<<

jackpot di HSR tgl 02/09/2025 dan 03/09/2025. Jadi trick simulasi gacha ini hanya gunakan satu kali sehari saja.

disini melakukan satu kali pull setiap ... simulasi pull:

252
252
252
252
252
252
126
357

Nilai pull baru: 13515
Total pull: 343888

>>>>>>>       Pengalaman Gacha beruntung 15/09/2025 <<<<<<<<

pull saber.

disini hanya melakukan 1 kali pull real, tanpa ada pull simulasi tambahan(Manual)

Nilai pull baru: 11490
Total pull: 33052

>>>>>>>>>>>>>>>>>>>>>>>>> Variabel yang digunaka n <<<<<<<<<<<<<<<<<<<<<<<

# Kemungkinan beruntung!
# 0.8 untuk Light Cone
# a_probability = 0.0008
a_probability = 0.0006
# Berapa banyak minimum percobaan
a_percobaan = 20_000
# Batch  size terkecil mau berapa
a_batchSize = 1000
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 10





====================== CAtatan tidak terpakai ==================================================
``
Aturan penggunaan:
0. Pastikan pull rate kamu sesuaikan dengan gamenya. simulasi inin hanya cocok jika pull rate sama dengan yang ada pada game.
1. Cari tau dengan "go 20 jackpot" dua kali. untuk mengetahui Streak tertinggi
2. lakukan pull 10 secara manual dan berjalan ke nilai mendekati yang tertinggi
3. jika sudah dekat, semisal nilai tertinggi adalah 700,
4. lakukan beberapa 10 kali pull simulasi, usahakan jangan terlalu banyak, lalu lakukan 10 pull real world.
"""

# ============================================================= Cukup Modifikasi bagian sini! ===================================================================

#Game Name
game_name = "PGR"
# Kemungkinan beruntung!
a_probability = 0.04
# Berapa banyak minimum percobaan
a_percobaan = 300
# Batch  size terkecil mau berapa
a_batchSize = 5
# alternative batch size
# ini gak boleh lebih dari 10. karena setiap pull disini bernilai 10, beserta laporan mereka juga
a_little_batch_size = 1


# ============================================================= Cukup Modifikasi bagian sini! ===================================================================

# probabilitas jackpot HSR
# karakter probabilitas 5 Star
p = a_probability

# Opsi Auto 03
a_03 = True


# ======================== Variabel penentu =======================================================
# Variabel sampai mendekati jackpot. Ubah Nilai N sesuai dengan Streak tertinggi yang didapatkan sesuai dengan pull game.
nilai_N =  a_percobaan

# Berapa detik sekali melakukan print
log_interval=10

#Ukuran batch size one pull
little_batch_size = 1
#Ukuran batch size automatic pull fast
batch_size = a_batchSize

# ======================== Variabel Modification on process =======================================================
# keseluruhan pull yang dilakukan
total_pulls = 0
# Banyak jackpot yang didapatkan
total_jackpot = 0
# Banyak percobaan yang dilakukan sekarang untuk menuju jackpot
jarak_jackpot = 0
# banyak percobaan untukk jackpot sebelumnya
total_jackpot_terakhir = 0
# list jackpot
jackpot_list = [0]
# nilai total pull baru untuk simulasi selain automatic
new_pull = 0
# loop untuk mendekati 95% jackpot
loop_terakhir = True
# loop bagian dua akan memaksa opsi 3 dilakukan kembali hingga 95% jackpot
loop_bagian_dua = True
# ======================== Variabel Modification on process =======================================================


# untuk automatic pull
loop_test = True

# ================================== Clear screen untuk melakukan refresh screen
def clear_screen():
  # For Windows
  if os.name == 'nt':
      _ = os.system('cls')
  # For macOS and Linux
  else:
      _ = os.system('clear')

# ============================== Opsi 01
def satu_pull():
  """Satu kali pull"""
  global jarak_jackpot, total_jackpot, total_jackpot_terakhir, total_pulls,new_pull, loop_test, loop_terakhir, loop_bagian_dua

  # ini adalah berapa banyak batch nilai random yang akan digenerate
  pulls = np.random.random(size=little_batch_size)
  # ini akan mencari tau kalau ada nilai random yang lebih kecil dari p(probabilitas jackpot))
  hits = np.where(pulls < p)[0]  # index jackpot. Informasi array dimana saja jackpot ditemukan.

  # ini adalah mencari tau kalau ada nilai random yang lebih kecil dari p(probabilitas jackpot))
  if len(hits) > 0:
      # Jackpot pertama dalam batch 'hits'
      first_hit = hits[0] + 1
      # Jackpot pertama dalam batch 'hits'
      jarak_jackpot += first_hit
      # Jackpot pertama dalam batch 'hits'
      total_pulls += first_hit
      # Informasi jackpot didapatkan +1
      total_jackpot += 1
      # Informasi jackpot yang sebelumnya didapatkanberapa pull
      total_jackpot_terakhir = jarak_jackpot
      # informasi banyak pull menuju jackpot disimpan ke list jackpot
      jackpot_list.append(jarak_jackpot)
      # informai percobaan di reset ke nol
      jarak_jackpot = 0
      print(f"\n ====>  jackpot jackpot didapatkan {total_pulls}  <====")
      print(f"====>  Informasi New Pull         {new_pull}  <====")
      print(f"\033[31m =================== Jackpot didapatkan. Misi Gagal! ===================== \033[0m")
      # Catatat kegagalan ini
      with open("jackpot.txt", "a") as f:
          f.write(f"\n ------> Kegagalan pada simulasi ke: {new_pull} , pull baru: {new_pull} , Total pull: {total_jackpot_terakhir}")
      # akhiri loop ke 99%
      # New pull di reset ke nol
      new_pull = 0
      loop_terakhir = False

  else:
      # Tidak ada jackpot dalam batch
      jarak_jackpot += little_batch_size
      total_pulls += little_batch_size
      # Tambahkan informasi pull baru (spesial untuk fungsi ini saja   )
      new_pull += little_batch_size
      print(f"kamu tidak beruntung, total pull: {total_pulls}")


# ================================================================== Satu pull alternative ==================================================================
def a_satu_pull(asr):
  """Satu kali pull"""
  global jarak_jackpot, total_jackpot, total_jackpot_terakhir, total_pulls,new_pull, loop_test, loop_terakhir, loop_bagian_dua

  # ini adalah berapa banyak batch nilai random yang akan digenerate
  pulls = np.random.random(size=a_little_batch_size)
  # ini akan mencari tau kalau ada nilai random yang lebih kecil dari p(probabilitas jackpot))
  hits = np.where(pulls < p)[0]  # index jackpot. Informasi array dimana saja jackpot ditemukan.

  # ini adalah mencari tau kalau ada nilai random yang lebih kecil dari p(probabilitas jackpot))
  if len(hits) > 0:
      # Jackpot pertama dalam batch 'hits'
      first_hit = hits[0] + 1
      # Jackpot pertama dalam batch 'hits'
      jarak_jackpot += first_hit
      # Jackpot pertama dalam batch 'hits'
      total_pulls += first_hit
      # Informasi jackpot didapatkan +1
      total_jackpot += 1
      # Informasi jackpot yang sebelumnya didapatkanberapa pull
      total_jackpot_terakhir = jarak_jackpot
      # informasi banyak pull menuju jackpot disimpan ke list jackpot
      jackpot_list.append(jarak_jackpot)
      # informai percobaan di reset ke nol
      jarak_jackpot = 0
      print(f"====>  jackpot jackpot didapatkan {len(jackpot_list)}  <====")
      print(f"====>  Informasi Total pull         {total_pulls}  <====")
      print(f"====>  Informasi New Pull         {new_pull}  <====")
      print(f"====> Menuju p99 {asr} , seharusnya kurang {(asr - new_pull)} percobaan lagi!")
      print(f"\033[31m =================== Jackpot didapatkan. Loop Diulang! ===================== \033[0m")
      # akhiri loop ke 99%
      # New pull di reset ke nol
      new_pull = 0
      loop_terakhir = False

  else:
      # Tidak ada jackpot dalam batch
      jarak_jackpot += a_little_batch_size
      total_pulls += a_little_batch_size
      # Tambahkan informasi pull baru (spesial untuk fungsi ini saja   )
      new_pull += a_little_batch_size

# ====================================================== Opsi 02
def sepuluh_pull():
  """Sepuluh kali pull"""
  # dimulai dari 0 sampai 9(hitungannya adalah 10 kali))
  for i in range(10):
      print(f"Pull ke : {i+1}: ", end="")
      satu_pull()

# =================================================== opsi 04 melakukan input manual =============================================
def manual_pull(asr):
  """ Pull sebanyak input manual """
  for i in range(asr):
    print(f"pull Manual ke : {i+1}. Jarak Jackpot : {jarak_jackpot}", end="")
    satu_pull()

# ========================================================= Prediksi untuk opsi 03
def predict_next_jackpot_mle(jackpot_distances):
  """
  Prediksi (frekuentis) jarak pull sampai jackpot berikutnya
  berdasarkan data jarak jackpot sebelumnya.
  """
  global data, mean_k, p_hat, mean_pred, median_pred, p90_pred, p95_pred, p99_pred, p98_pred, p100_pred
  data = [int(k) for k in jackpot_distances if isinstance(k, (int, np.integer)) and k > 0]
  if len(data) == 0:
      print("❌ Data jackpot kosong, tidak bisa prediksi.")
      return None

  mean_k = float(np.mean(data))
  p_hat = 1.0 / mean_k

  mean_pred = mean_k
  median_pred = ceil(log(0.5) / log(1 - p_hat))
  p90_pred = ceil(log(1 - 0.90) / log(1 - p_hat))
  p95_pred = ceil(log(1 - 0.95) / log(1 - p_hat))
  p98_pred = ceil(log(1 - 0.95) / log(1 - p_hat))
  p99_pred = ceil(log(1 - 0.99) / log(1 - p_hat))
  p100_pred = ceil(log(1 - 0.999) / log(1 - p_hat))

  print("\n🎯 Prediksi Jackpot Berikutnya (MLE):")
  print(f"- p̂ (peluang jackpot per pull): {p_hat:.6f} ({p_hat*100:.4f}%)")
  print(f"- Rata-rata pulls sampai jackpot berikutnya : {int(round(mean_pred)):,}")
  print(f"- Median pulls (50% kasus)                : {median_pred:,}")
  print(f"- 90% kemungkinan ≤                        : {p90_pred:,}")
  print(f"- 95% kemungkinan ≤                        : {p95_pred:,}")
  print(f"- 98% kemungkinan ≤                        : {p98_pred:,}")
  print(f"- 99% kemungkinan ≤                        : {p99_pred:,}")
  print(f"- 99.09% kemungkinan ≤                       : {p100_pred:,}")

  return {
      "p_hat": p_hat,
      "mean_pred": int(round(mean_pred)),
      "median_pred": int(median_pred),
      "p90_pred": int(p90_pred),
      "p95_pred": int(p95_pred),
      "p98_pred": int(p98_pred),
      "p99_pred": int(p99_pred),
      "p99.09_pred": int(p100_pred),
  }


# ========================================================= Opsi 03
def automatic_pull():
  """
  Tujuan adalah melakukan pull otomatis untuk mendapatkan nilai N.
  dan melakukan pull tambahan sesuai dengan perkiraan 99% menuju jackpot.

  intinya kita akan terus melakukan loop hingga total pull mendekati kemungkinan 99%/95% jackpot.
  """
  global jarak_jackpot, total_jackpot, total_jackpot_terakhir, total_pulls, new_pull, loop_test, loop_terakhir, ii_terakhir, bukti, loop_bagian_dua, a_03

  last_log = time.time()
  while True:
      # Jika sudah mencapai target, hentikan
      if total_jackpot_terakhir >= (nilai_N - 10):
          break

      # Simulasikan beberapa pull sekaligus (batch)
      pulls = np.random.random(size=batch_size)
      hits = np.where(pulls < p)[0]  # index jackpot. Informasi array dimana saja jackpot ditemukan.

      if len(hits) > 0:
          # Jackpot pertama dalam batch
          first_hit = hits[0] + 1
          jarak_jackpot += first_hit
          total_pulls += first_hit
          total_jackpot += 1
          total_jackpot_terakhir = jarak_jackpot
          jackpot_list.append(jarak_jackpot)
          jarak_jackpot = 0
      else:
          # Tidak ada jackpot dalam batch
          jarak_jackpot += batch_size
          total_pulls += batch_size

      # Cek apakah waktunya log progress
      if time.time() - last_log >= log_interval:
          clear_screen()
          print("=====================>  Fast Pull System  <====================\n")
          print(f"kamu tidak beruntung, Pull sebelum jackpot: {total_jackpot_terakhir:,}")
          print(f"Target jarak adalah            : {(nilai_N - 10)}")
          print(f"Jackpot tertinggi adalah       : {max(jackpot_list):,}")
          print(f"Total pull                     : {total_pulls:,}")
          print(f"Total jackpot                  : {total_jackpot:,}")
          last_log = time.time()
          print(f"Array List JackPot       : {sorted(jackpot_list, reverse=True)[:5]}")



  # Setelah selesai, lakukan pull real world
  jarak_jackpot = total_jackpot_terakhir
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
  # Urutkan dari terbesar
  jackpot_list.sort(reverse=True)
  # Buat file untuk list jackpot


  try:
      modus = df["Jarak Jackpot"].mode()[0]
      print(f"\nModus Jackpot: {modus}")
      #file_j = open("jackpot.txt", "w")
      #file_j.write(jackpot_list)
      #file_j.close()
      print('=========> Catatan jackpot telah ditulis ')
  except:
      print("\nModus tidak dapat dihitung (data terlalu unik).")
  predict_next_jackpot_mle(jackpot_list)

  # iteration untuk loop terakhir
  ii_terakhir = 0
  # bukti loop tambahan
  bukti = 0

  while loop_terakhir:
    # tujuan adalah jika off chance pull lebih dari prediksi 95% maka akhiri loop
    if ii_terakhir >= (p100_pred - 10 ): # <============== Atur nilai ini sesuai dengan prediksi 95% jackpot
      a_03 = False
      print(f"\033[34m ===================== Belum Jackpot ======================= \033[0m")
      print("loop berakhir")
      print(f"\033[34m ===================== Semua loop selesai  ======================= \033[0m")
      print("\033[32m ====================> Real World Pull Now! <================= \033[0m")
      # Akhiri loop ini
      loop_terakhir = False
      # akhiri semua loop, ini untuk mastikan bagian kedua berakhir
      loop_bagian_dua = False
      break
    # tujuan jika belum jackpot, lakukan pull normal secara loop ke 95%
    else:
      a_satu_pull(p100_pred)
      bukti += 1
      ii_terakhir += a_little_batch_size





# opsi 4
def reset_button():
  """Reset semua variabel"""
  global total_pulls, total_jackpot, jarak_jackpot, total_jackpot_terakhir, jackpot_list, new_pull, ii_terakhir, bukti, loop_terakhir
  # ======================== Variabel Modification on process =======================================================
  # keseluruhan pull yang dilakukan
  total_pulls = 0
  # Banyak jackpot yang didapatkan
  total_jackpot = 0
  # Banyak percobaan yang dilakukan sekarang untuk menuju jackpot
  jarak_jackpot = 0
  # banyak percobaan untukk jackpot sebelumnya
  total_jackpot_terakhir = 0
  # list jackpot
  jackpot_list = [0]
  # nilai total pull baru untuk simulasi selain automatic
  new_pull = 0
  # loop untuk mendekati 95% jackpot
  ii_terakhir = 0
  # bukti loop tambahan
  bukti = 0
  # jalankan loop tambahan
  loop_terakhir = True
  # ======================== Variabel Modification on process =======================================================
  clear_screen()
  print("Semua variabel telah direset.")


# ========================= Starter =======================================================

def main():
  global total_jackpot

  # Get the current date and time
  current_datetime = datetime.now()

  # Format the datetime object to a string showing only hour, minute, and second
  formatted_time = current_datetime.strftime("%H:%M:%S")

  # Buat penanda waktu untuk file
  with open("jackpot.txt", "a") as f:
      f.write(f"\n ============  Game Name : (game_name) Time: {formatted_time} =============")
  while True:
      print("\n================= Simulasi Gacha V2 =====================")
      print(f"\n================= Game Name: {game_name} =====================")
      print(f"Nilai Pull baru                : {new_pull}")
      print(f"Banyak percobaan yang dilakukan sekarang untuk menuju jackpot : {jarak_jackpot}")
      print(f"banyak percobaan untukk jackpot sebelumnya  : {total_jackpot_terakhir}")
      print("1. Pull 1 kali")
      print("2. Pull 10 kali")
      if a_03 == True:
        print("3. Automatic pull fast")
      else:
        print('.')
      print("4. Manual pull input")
      choice = input("Pilih opsi: ")

      if choice == "1":
        satu_pull()
      elif choice == "2":
        sepuluh_pull()
      elif choice == "3":
        if a_03 == True:
          while loop_bagian_dua:
            reset_button()
            automatic_pull()
          print("\033[93m =============================== Semua loop selesai ===================================== \033[0m")
          print("\033[93m =============================== Realword Pull      ===================================== \033[0m")
        else:
          print('03 empty')
      elif choice == "4":
        usIN = input("Pilih berapa banyak pull: ")
        with open("jackpot.txt", "a") as f:
          f.write(f"\n Ini nilai percobaan : {usIN} , Nilai pull baru: {new_pull} , Total pull: {jarak_jackpot}")
        manual_pull(int(usIN))
        # Catatan pull terbaru yang lama
        rec_new_pull = new_pull
      else:
          print("Opsi tidak valid, coba lagi.")


if __name__ == "__main__":
  main()
