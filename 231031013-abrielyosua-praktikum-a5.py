a = True # Inisialisasi variable a dengan nilai True
batas = 1 # Inisialisasi variable batas dengan nilai 1

while a: # Menjalankan perulangan while dengan kondisi a (True)
    if batas <= 5: # Memeriksa apakah nilai batas kurang dari atau sama dengan 5
        print(f'Menjalankan Program ke = {batas}') # Jika ya, cetak pesan dengan nilai batas
        batas += 1 # Variable batas akan ditambah 1 setiap kali operasi terpenuhi, dan akan kembali ke perulangan
    else: 
        break # Jika nilai batas lebih dari 5, keluar dari loop while