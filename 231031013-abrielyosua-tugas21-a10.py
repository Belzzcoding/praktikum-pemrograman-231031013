print ('Tugas 2(1)\n')

print('Program Penjumlahan Waktu\n')
# Input waktu awal dari pengguna
waktu_awal = input("Masukkan waktu awal (JJ:MM:DD): ")
jam_menit = waktu_awal.split(":")
jam_awal = int(jam_menit[0])
menit_awal = int(jam_menit[1])
detik_awal = int(jam_menit[2])

# Input waktu tambahan dalam jam dan menit
jam_tambahan = int(input("Masukkan jam tambahan: "))
menit_tambahan = int(input("Masukkan menit tambahan: "))
detik_tambahan = int(input("Masukkan detik tambahan: "))

# Menghitung waktu akhir
jam_akhir = (jam_awal + jam_tambahan + (menit_awal + menit_tambahan) + (detik_awal + detik_tambahan) // 60) % 24
menit_akhir = (menit_awal + menit_tambahan) % 60
detik_akhir = (detik_awal + detik_tambahan) % 60

# Mencetak hasil
print(f"Waktu sekarang menunjukkan Pukul {jam_akhir:02d}:{menit_akhir:02d}:{detik_akhir:02d}\n\n")