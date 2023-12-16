# Fungsi Rekursif faktorial dengan perulangan
def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai*faktorial(nilai-1)

# Program Utama
for i in range(11):
    print('%2d ! = %d' % (i,faktorial(i)))

print()
# Contoh dengan input (Tugas 5)
hasil = int(input('Masukkan nilai faktorial = ')) # Masukkan inputannya 
hasil_faktorial = faktorial(hasil) # Hitung faktorialnya
print(f'Nilai Faktorial dari {hasil}! = {hasil_faktorial}') # Tampilkan hasilnya
