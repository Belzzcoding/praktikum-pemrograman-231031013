# ''' UTS
# 1. Buat variabel jenis list berikut.
    
#     Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
#             'Parepare',
#             'Jurusan Sains',
#             'kartu hasil studi mahasiswa',
#             'Nama Lengkap',
#             'NIM',
#             'S1',
#             'Sistem Informasi A',
#             '2023-2024',
#             'ganjil',
#             'aktif',
#             'Tanggal-Bulan-Tahun Lahir']
# #(NOTED: sesuaikan dengan data anda)


# 2. Buat variabel nested list berikut.

# MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
#         [3,2,3,2,3,3,3,2],
#         ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
#         [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

# #(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

# 3. Buat Kode dengan hasil runing seperti berikut.


#             INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
#                            JURUSAN SAINS
#                     KARTU HASIL STUDI MAHASISWA
#                           GANJIL 2023/2024

                    
# Nama Lengkap    : NAMA LENGKAP
# NIM             : NIM
# Program/Prodi   : S1/Sistem Informasi A
# Tahun Masuk     : 2023-Ganjil
# Status          : Aktif
# |--|--   12   --|--             31            --|-- 7 --|--    13   --|
# -----------------------------------------------------------------------
# No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
# -----------------------------------------------------------------------
# 1   22A1209     | Matkul1                       |   3   |         3.50|
# 2   22A1210     | Matkul2                       |   2   |         3.00|
# 3   22A1211     | Matkul3                       |   3   |         3.75|
# 4   22A1212     | Matkul4                       |   2   |         4.00|
# 5   22A1213     | Matkul5                       |   3   |         3.75|
# 6   22A1214     | Matkul6                       |   3   |         3.50|
# 7   22A1215     | Matkul7                       |   3   |         3.75|
# 8   22A1216     | Matkul8                       |   2   |         3.00|
# -----------------------------------------------------------------------
#                                        TOTAL SKS:   21
# -----------------------------------------------------------------------
# |---------------------------------71-----------------------------------|
# Summary:
# Jumlah Mata Kuliah : 8 Mata Kuliah
# Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
# Nilai Terendah     : 3.00  (22A1211 - Matkul2)
# IP Kumulatif       : 3.00
                                   
#                                                Parepare, 25 Oktober 2023



#                                                      NAMA LENGKAP      
#                                                      ------------
# '''



# Tulis Kode Jawaban di bawah!

# 1. Buat variabel jenis list berikut.
bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Abriel Yosua Nathanael Leskona',
            '231031013',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            '03-12-2004']

# 2. Buat variabel nested list berikut.
mk =   [['Pemrograman','Agama Kristen','Pengantar Teknologi Informasi','Bahasa Indonesia','Kaldas I','CINTA','Sains Terpadu','Pancasila'],
        [3,2,3,2,3,2,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [4.00,3.91,3.85,3.99,3.85,3.92,3.94,3.89]]

# 3. Buat Kode dengan hasil runing seperti berikut.
bio4 = bio[-4].replace('-', '/')
gabung = bio[-3], bio4
gabung = ' '.join(gabung)

sp= 71
print(f'{bio[0].center(sp).upper()}\n{bio[2].center(sp).upper()}\n{bio[3].center(sp).upper()}\n{gabung.center(sp).upper()}')

print(f'''\n
Nama Lengkap\t: {bio[4].upper()}
NIM\t\t: {bio[5]}
Program/Prodi\t: {bio[6]}/{bio[7]}
Tahun Masuk\t: {bio[8][:4]}-{bio[9].upper()}
Status\t\t: {bio[-2].capitalize()}
''')

# Kolom kepala tabel
print('-'*71)
print('No. '+'Kode'.ljust(12)+'|'+'Mata Kuliah'.center(31)+'|'+'SKS'.center(7)+'|'+'Nilai (0-4)'.center(13)+'|')
print('-'*71)

# Isi Tabel baris 1-8
print('1. '+mk[2][0].ljust(12)+' |'+mk[0][0].ljust(31)+'|'+f'{mk[1][0]}'.center(7)+'|'+f'{mk[3][0]:.2f}'.rjust(13)+'|')
print('2. '+mk[2][1].ljust(12)+' |'+mk[0][1].ljust(31)+'|'+f'{mk[1][1]}'.center(7)+'|'+f'{mk[3][1]}'.rjust(13)+'|')
print('3. '+mk[2][2].ljust(12)+' |'+mk[0][2].ljust(31)+'|'+f'{mk[1][2]}'.center(7)+'|'+f'{mk[3][2]}'.rjust(13)+'|')
print('4. '+mk[2][3].ljust(12)+' |'+mk[0][3].ljust(31)+'|'+f'{mk[1][3]}'.center(7)+'|'+f'{mk[3][3]}'.rjust(13)+'|')
print('5. '+mk[2][4].ljust(12)+' |'+mk[0][4].ljust(31)+'|'+f'{mk[1][4]}'.center(7)+'|'+f'{mk[3][4]}'.rjust(13)+'|')
print('6. '+mk[2][5].ljust(12)+' |'+mk[0][5].ljust(31)+'|'+f'{mk[1][5]}'.center(7)+'|'+f'{mk[3][5]}'.rjust(13)+'|')
print('7. '+mk[2][6].ljust(12)+' |'+mk[0][6].ljust(31)+'|'+f'{mk[1][6]}'.center(7)+'|'+f'{mk[3][6]}'.rjust(13)+'|')
print('8. '+mk[2][7].ljust(12)+' |'+mk[0][7].ljust(31)+'|'+f'{mk[1][7]}'.center(7)+'|'+f'{mk[3][7]}'.rjust(13)+'|')
print('-'*71)

# Total SKS
print('TOTAL SKS: '.rjust(51), f'{len(mk[1])}')
print('-'*71)

# Summary
nilai = [mk[1][0] * mk[3][0],
         mk[1][1] * mk[3][1],
         mk[1][2] * mk[3][2],
         mk[1][3] * mk[3][3],
         mk[1][4] * mk[3][4],
         mk[1][5] * mk[3][5],
         mk[1][6] * mk[3][6],
         mk[1][7] * mk[3][7]]
ipk = sum(nilai)/sum(mk[3])

print(f'''Summary:
Jumlah Mata Kuliah : {len(mk[1])} Mata Kuliah
Nilai Tertinggi    : {max(mk[3]):.2f}     ({mk[2][0]} - {mk[0][0]})
Nilai Terendah     : {min(mk[3])}     ({mk[2][5]} - {mk[0][5]})
IP Kumulatif       : {ipk}

''', 
'Parepare, 25 Oktober 2023'.rjust(71),
f'\n\n\n\n{bio[4].upper().rjust(72)}'
)
