# Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        return 'Tidak ada bilangan bernilai negatif'
    elif n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Program Utama
nilai = 20
hasil = fibonacci(nilai)
print('Fibonacci(%d) = %d' % (nilai,hasil))

print()
# Contoh dengan input (Tugas 6)
bilangan = int(input('Masukkan sebuah bilangan : ')) # Masukkan inputannya
hasil_fibonacci = fibonacci(bilangan) # Hitung fibonaccinya
print(f'Fibonacci({bilangan}) = {hasil_fibonacci}') # Tampilkan hasilnya