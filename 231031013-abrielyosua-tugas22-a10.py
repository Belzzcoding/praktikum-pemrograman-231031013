print ('Tugas 2(2)\n')

print('Program Selisih Waktu\n')
# Input waktu awal
waktu_awal = input("Masukkan waktu awal (JJ:MM:DD): ")
jam, menit, detik = map(int, waktu_awal.split(':'))

# Input jam dan menit yang akan dikurangkan
jam_kurang = int(input("Masukkan jumlah jam yang akan dikurangkan: "))
menit_kurang = int(input("Masukkan jumlah menit yang akan dikurangkan: "))
detik_kurang = int(input("Masukkan jumlah detik yang akan dikurangkan: "))

# Hitung waktu akhir
jam_akhir = (jam - jam_kurang - (menit_kurang // 60) - (detik_kurang // 60)) % 24
menit_akhir = (menit - (menit_kurang % 60)) % 60
detik_akhir = (detik - (detik_kurang % 60)) % 60

# Cetak hasil
print(f"Waktu sekarang menunjukkan pukul {jam_akhir:02d}:{menit_akhir:02d}:{detik_akhir:02d}")