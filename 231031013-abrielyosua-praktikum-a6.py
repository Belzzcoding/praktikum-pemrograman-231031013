a = True # Inisialisasi variabel a sebagai True untuk memulai loop

while a: # Memulai loop while dengan kondisi a (selalu True)
    pilih = input('Pilihan: ') # Mengambil input dari pengguna untuk pilihan
    if pilih == 'ya': # Cek apakah input pengguna adalah 'ya'
        print('Selamat Datang') # Jika ya, cetak pesan Selamat Datang
        break # Hentikan loop
    elif pilih == 'tidak': # Cek apakah input pengguna adalah 'tidak'
        print('Sampai Jumpa') # Jika tidak, cetak pesan Sampai Jumpa
        break # Hentikan loop
    else: # Jika input pengguna bukan 'ya' atau 'tidak'
        print('Pilihan tidak valid, coba lagi.\n') # Cetak pesan kesalahan
        continue # Lanjutkan loop

'''
Penjelasan:
1. Pertama kita membuat terlebih dahulu variable a yang bernilai True.
2. Lalu kita memulai perulangan while dengan kondisi a yang bernilai True.
3. Didalam loop, kita membuat variable input yang isinya adalah inputan dari user.
4. Selanjutnya kita mengecek pengkondisian variable pilih.
5. Jika kondisi variable pilih bernilai/berisi 'ya', maka akan mencetak 'Selamat Datang' lalu program akan berhenti
6. Jika bukan pilihan 'ya', maka mengecek apakah kondisi variable pilih bernilai/berisi 'tidak', jika True maka akan mencetak 'Sampai Jumpa' lalu program akan berhenti
7. Jika if dan elif tidak terpenuhi, maka program akan mencetak 'Pilihan tidak valid, coba lagi.'. Lalu looping akan terus berlanjut.
'''