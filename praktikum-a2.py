print('praktikum-a2\n\n')

print('Nama  : Abriel Yosua N.L.')
print('NIM   : 231031013')
print('Prodi : Sistem Informasi-A\n')

#Ini Operator Assigment
a = 19
print('Nilai a adalah', a)
a += 3
print('Nilai a+=3 adalah', a)

a = 19
print('Nilai a adalah', a)
a -= 3
print('Nilai a-=3 adalah', a)

a = 19
print('Nilai a adalah', a)
a *= 2
print('Nilai a*= 2 adalah', a)

a = 19
print('Nilai a adalah', a)
a /= 2
print('Nilai a/= 2 adalah', a)

a = 3
print('Nilai a adalah', a)
a **= 2
print('Nilai a**= 2 adalah', a)

a = 35
print('Nilai a adalah', a)
a %= 32
print('Nilai a%= 32 adalah', a)

a = 35
print('Nilai a adalah', a)
a //= 32
print('Nilai a//= 32 adalah', a, '\n')

# Tugas melanjutkan untuk operator selanjutnya dari line 25-59
print('=============TUGAS')
#OR
b = True
print('Nilai b =', b)
b |= False
print('Nilai b|= False akan menjadi', b)
b = False
print('Nilai b =', b)
b |=False
print('Nilai b|= False akan menjadi', b)

#AND
b = True
print('Nilai b =', b)
b &= False
print('Nilai b&= False akan menjadi', b)
b = False
print('Nilai b =', b)
b &=False
print('Nilai b&= False akan menjadi', b)

#XOR
b = True
print('Nilai b =', b)
b ^= False
print('Nilai b^= False akan menjadi', b)
b = False
print('Nilai b =', b)
b ^=False
print('Nilai b^= False akan menjadi', b)

#SHIFTING
c = 0b0100
print('Nilai c =', format(c, '04b'))
c >>= 1
print('Nilai c >>=1 akan menjadi', format(c, '04b'))
c = 0b0100
c <<=1
print('Nilai c <<=1 akan menjadi', format(c, '04b'))


#Operator Perbandingan
a = 9
b = 13 #NIM saya akhirannya 13

print('\n------------ Besar dari 13')
hasil = a > 13
print(a, '> 13 adalah', hasil)
hasil = b > 13
print(b, '> 13 adalah', hasil)

print('\n------------ Kecil dari 13')
hasil = a < 13
print(a, '< 13 adalah', hasil)

hasil = b < 13
print(b, '< 13 adalah', hasil)

#Tugas Lanjutan

print('\n------------ Besar atau sama dari 13 #ujung nim')
hasil = a >= 13
print(a, '>= 13 adalah', hasil)
hasil = b >= 13
print(b, '>= 13 adalah', hasil)

print('\n------------ Kecil atau sama dari 13 #ujung nim')
hasil = a <= 13
print(a, '<= 13 adalah', hasil)
hasil = b <= 13
print(b, '<= 13 adalah', hasil)

print('\n------------ Sama dari 13 #ujung nim')
hasil = a == 13
print(a, '== 13 adalah', hasil)
hasil = b == 13
print(b, '== 13 adalah', hasil)

print('\n------------ Tidak Sama dari 13 #ujung nim')
hasil = a != 13
print(a, '!= 13 adalah', hasil)
hasil = b != 13
print(b, '!= 13 adalah', hasil)

#Operator Logika
a = True
b = False
print('\n==========AND==========')
hasil = a and a
print(a, 'and', a, 'hasilnya =', hasil)

hasil = a and b
print(a, 'and', b, 'hasilnya =', hasil)

hasil = b and a
print(b, 'and', a, 'hasilnya =', hasil)

hasil = b and b
print(b, 'and', b, 'hasilnya =', hasil)

print('\n==========OR==========')
hasil = a or a
print(a, 'or', a, 'hasilnya =', hasil)
hasil = a or b
print(a, 'or', a, 'hasilnya =', hasil)

hasil = b or a
print(a, 'or', a, 'hasilnya =', hasil)

hasil = b or b
print(a, 'or', a, 'hasilnya =', hasil)

print('\n==========XOR==========')
hasil = a ^ a
print(a, 'xor', a, 'hasilnya =', hasil)

hasil = a ^ b
print(a, 'xor', b, 'hasilnya =', hasil)

hasil = b ^ a
print(b, 'xor', a, 'hasilnya =', hasil)

hasil = b ^ b
print(b, 'xor', b, 'hasilnya =', hasil)

print('\n==========NOT==========')
hasil = not a
print('not', a, 'hasilnya =', hasil)

hasil = not b
print('not', b, 'hasilnya =', hasil)


#Operator Membership
print('\n==================IN')
nama = 'Abriel Yosua Nathanael Leskona'
test = 'el'
cek = test in nama
print(test, 'terdapat di', nama, 'adalah', cek)

test = 'ul'
cek = test in nama
print(test, 'terdapat di', nama, 'adalah', cek)
print()

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1, 'terdapat di', nama, 'adalah', cek)
cek = test2 in nama
print(test2, 'terdapat di', nama, 'adalah', cek)
cek = test3 in nama
print(test3, 'terdapat di', nama, 'adalah', cek)
cek = test4 in nama
print(test4, 'terdapat di', nama, 'adalah', cek)
cek = test5 in nama
print(test5, 'terdapat di', nama, 'adalah', cek)

#Lanjutannya
print('\n==================NOT IN')
nama = 'Abriel Yosua Nathanael Leskona'
test = 'el'
cek = test not in nama
print(test, 'tidak terdapat di', nama, 'adalah', cek)

test = 'ul'
cek = test not in nama
print(test, 'tidak terdapat di', nama, 'adalah', cek)
print()

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 not in nama
print(test1, 'tidak terdapat di', nama, 'adalah', cek)
cek = test2 not in nama
print(test2, 'tidak terdapat di', nama, 'adalah', cek)
cek = test3 not in nama
print(test3, 'tidak terdapat di', nama, 'adalah', cek)
cek = test4 not in nama
print(test4, 'tidak terdapat di', nama, 'adalah', cek)
cek = test5 not in nama
print(test5, 'tidak terdapat di', nama, 'adalah', cek)


print()