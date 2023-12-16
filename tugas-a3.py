print('Tugas Praktikum 3'.center(40))
nama = 'Abriel Yosua Nathanael Leskona'
nim  = '231031013'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi} \n''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''


str1 = 'duFort Frankel Von Neumann'
print(str1, '(ini contoh)\n\n')
up1 = str1.upper()
up1 = up1.split()
print(up1[3], up1[0], up1[1], up1[2], '(1)\n')
#output: NEUMANN DUFORT FRANKEL VON

str2 = 'duFort Frankel Von Neumann'
up2 = str2.upper()
up2 = up2.split()
print(up2[0][0]+up2[1][0]+up2[2][0], up2[3], '(2)\n')
#output: DFV NEUMANN

str3 = 'duFort Frankel Von Neumann'
up3 = str3.upper()
up3 = up3.split()
print(up3[0], up3[1][0]+up3[2][0]+up3[3][0], '(3)\n')
#output: DUFORT FVN

str4 = 'duFort Frankel Von Neumann'
sp4 = str4.split()
print(sp4[3][0], sp4[0], sp4[1][0]+sp4[2][0], '(4)\n')
#output: N duFort FV

str5 = 'duFort Frankel Von Neumann'
sp5 = str5.split()
print(sp5[3].upper(), sp5[0][0], sp5[1][0].lower(), sp5[2][0].lower(), '(5)\n')
#output: NEUMANN d f v

str6 = 'duFort Frankel Von Neumann'
up6 = str6.upper()
up6 = up6.split()
print(up6[3], up6[0][0]+up6[1][0]+up6[2][0], '(6)\n')
#output: NEUMANN DFV

str7 = '@duFort Frankel Von Neumann$'
sp7 = str7.split()
print(sp7[0][1:], sp7[1], sp7[2], sp7[3][0:-1].upper(), '(7)\n')
#output: duFort Frankel Von NEUMANN

str8 = '#duFort4Frankel4Von4Neumann$'
print(str8[1:-1].replace('4', ' '), '(8)\n')
# sr = str8.strip('#$').replace('4', ' ')
# print(sr)
#output: duFort Frankel Von Neumann

str9 = '@duFort@-^Frankel*-(Von(-(Neumann$'
df = str9.replace('-', ' ')
df = df.split()
print(df[0].strip('@'), df[1].strip('^*'), df[2].strip('('), df[3].strip('($'), '(9)\n')
#output: duFort Frankel Von Neumann

str10 = '@DUFort@1^FraNkel*1(VoN(1(NeuMann^'
rp = str10.replace('1', ' ')
rp = rp.split()
print(rp[0][1:3].lower()+rp[0][3:7], rp[1].strip('^*').title(), rp[2].strip('(').title(), rp[3].strip('(^').title(), '(10)')
#output: duFort Frankel Von Neumann