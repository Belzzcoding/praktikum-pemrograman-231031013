
print('praktikum-a4\n')

nim  = ['2','3','1','0','3','1','0','1','3']
# nim2 = '231031013'
print(nim)
# print(nim2[1:3])

#akses item
print(f'item indeks 0: {nim[0]}')
print(f'item indeks 4: {nim[4]}')
print(f'item indeks terakhir: {nim[len(nim)-1]}')

# akses indeks negatif
print(f'item indeks terakhir: {nim[-1]}')
print(f'item indeks pertama: {nim[-len(nim)]}')
print(f'item indeks 6 [-3]: {nim[-3]}')
print(f'item indeks 4 [-5]: {nim[-5]}')
print(f'item indeks 7 [-2]: {nim[-2]}')

# akses indeks batas
print(f'item indeks 1,2,....: \n {nim[1:]}')
print(f'item indeks 3,4,....: \n {nim[3:]}')
print(f'item indeks 0,1,2: \n {nim[:3]}')
print(f'item indeks 0,1,2,3: \n {nim[:4]}')
print(f'item indeks semua: \n {nim[:]}')
print(f'item indeks [:8]: \n {nim[:-1]}')
print(f'item indeks [:6]: \n {nim[:-3]}')

#pengirisan
print(f'item indeks 1,2: \n {nim[1:3]}')
print(f'item indeks 2,3,4: \n {nim[2:5]}')
print(f'item indeks kosong: \n {nim[3:3]}')
print(f'item indeks [8:8] kosong: \n {nim[-1:-1]}')
print(f'item indeks [1:8] kosong: \n {nim[1:-1]}')
print(f'item indeks [2:7] kosong: \n {nim[2:-2]} \n')


#Latihan List
print('='*20+'Latihan List')
data = ['Abel',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])

# Abel status Kuliah: Aktif
print(f'{data[0]} status Kuliah: {data[2]}')
# Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah: {max(nilai)}')
# Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah: {min(nilai)}')
# Rata-rata nilai adalah: 92.25
print(f'Rata-rata nilai adalah: {sum(nilai)/len(nilai)} \n')



#Latihan Tuple
print('='*20+'Latihan Tuple')
data = ('Abel',2023,'Aktif')
nilai= (90,89,93,97)

print(data[1])
print(data[-1])
print(nilai[1:-1])

# Jumlah nilai mahasiswa adalah: 4
print(f'Jumlah nilai mahasiswa adalah: {len(nilai)}')
# Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah: {max(nilai)}')
# Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah: {min(nilai)}')
# Rata-rata nilai adalah: 92.25
print(f'Rata-rata nilai adalah: {sum(nilai)/len(nilai)} \n')


#Latihan Nested List
print('='*20+'Latihan Nested List')
data = [['Abriel Yosua',2023,'Aktif'],
        [90,89,93,97],
        [20,22],
        ['S1-Reguler','Ganjil']]

matkul = ['Agama Kristen', 'Pengantar Pemrograman', 'Pengenalan Teknologi Informasi', 'Bahasa Indonesia']
sks = [2,3,3,2]
#Tugas 1 : Tambahkan matkul dan sks ke dalam data (di akhir)
data.append(matkul)
data.append(sks)

#Tugas 2 :
# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'{data[4][0]} dengam jumlah {data[-1][0]} sks')
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f'{data[4][1]} dengam jumlah {data[-1][1]} sks')
# Mata kuliah 3: Matkul3 dengan jumlah 3 sks
print(f'{data[4][2]} dengam jumlah {data[-1][2]} sks')
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f'{data[4][3]} dengam jumlah {data[-1][3]} sks')

#Menambahkan matkul ke-5
data[4].append('Wawasan Cinta IPTEK dan IMTAQ')
data[5].append(2)
print(f'{data[4][4]} dengam jumlah {data[-1][4]} sks')
#print(data)

#Tambahkan 3 matkul dengan sks nya
#matkul 6 & sks nya
data[4].append('Pancasila')
data[5].append(2)
#matkul 7 & sks nya
data[4].append('Kalkulus Dasar 1')
data[5].append(3)
#matkul 8 & sks nya
data[4].append('Sains Terpadu')
data[5].append(3)

# Mata kuliah 6: Matkul6 dengan jumlah 2 sks
print(f'{data[4][5]} dengam jumlah {data[-1][5]} sks')
# Mata kuliah 7: Matkul7 dengan jumlah 2 sks
print(f'{data[4][6]} dengam jumlah {data[-1][6]} sks')
# Mata kuliah 8: Matkul8 dengan jumlah 2 sks
print(f'{data[4][7]} dengam jumlah {data[-1][7]} sks')

#Tambahkan 8 nilai masing-masing
data[1].append(92)
data[1].append(94)
data[1].append(91)
data[1].append(92)

print(data[0][0])
print(data[3][0])
print(data[2][0:])

# >> Nama Mahasiswa Abel dengan NIM: 231031013 
print(f'Nama Mahasiswa {data[0][0]} dengan NIM:{"".join(nim)}')
# Program pendidikan Abel: S1-Reguler
print(f'Program pendidikan {data[0][0]}: {data[3][0]}')
# Angkatan : 2023-Ganjil
print(f'Angkatan : {data[0][1]}-{data[3][1]}')
# Jumlah nilai Abel adalah: 8
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
# Data terbesar Abel adalah: 97
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
# Data terkecil Abel adalah: 89
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
# Rata-rata nilai Abel adalah: 92.25
print(f'Rata-rata nilai {data[0][0]} adalah: {sum(data[1])/len(data[1])}')