import os

def judul():
    print('PROGRAM MENGHITUNG LUAS & KELILING'.center(45))
    print('BANGUN DATAR PERSEGI'.center(45))
    print()

def inputan():
    panjang = float(input('Masukkan panjang: '))
    lebar = float(input('Masukkan lebar: '))
    return panjang,lebar

def hitung(panjang, lebar):
    luas = panjang * lebar
    kel = (panjang + lebar)*2
    return luas,kel

def tampil(pesan,nilai):
    print(f'Hasil perhitungan nilai {pesan}: {nilai}')
    
def pilihan():
    pilih = input('Apakah mau lanjut? (y/n): ')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Sampai jumpa.')
    return a


a = True
while a:
    # Judul
    judul()

    # Inputan panjang & lebar
    panjang,lebar = inputan()

    # Hitung luas & keliling
    luas,kel = hitung(panjang,lebar)

    # Cetak atau display
    tampil('Luas',luas)
    tampil('Keliling',kel)

    # Pilihan
    a = pilihan()