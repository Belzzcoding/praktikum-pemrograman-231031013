nama = input('Masukkan nama karyawan: ')
pendapatan = int(input('Masukkan Pendapatan: '))
print()

print(f'Nama Karyawan: {nama}')
print(f'Pendapatan: {pendapatan}')
if pendapatan > 1000:
    print('Status: Berhak')
else:
    print('Status: Tidak Berhak')