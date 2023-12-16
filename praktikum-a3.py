print('praktikum-a3\n\n')

nama  = 'abriel yosua n.l.'
nim   = '231031013'
meet = 'praktikum 3'
prodi = 'sistem informasi A'
email = 'abrieljhie@gmail.com'
sp = 50
ttl = 'makassar'
alamat = 'Jl. Abd. Dg Sirua'
asal = 'Makassar'
hobi = 'Push Rank'
tinggi = '180'


print('-'*sp)
print(nama.center(sp).upper())
print(nim.center(sp))
print('\n'*2)
print(meet.capitalize().rjust(sp))
print(prodi.title().rjust(sp))
print(email.rjust(sp))
print('-'*sp)

print (f'''Halo nama saya {nama.title()} dengan NIM {nim} dari prodi {prodi.title()}, ini adalah file {meet.capitalize()}. Terima kasih.''')


print(f'''
Biodata saya:
NAMA\t: {nama.title()}
NIM\t: {nim}
Prodi\t: {prodi.title()}
TTL\t: {ttl.title()}
Alamat\t: {alamat}
Asal\t: {asal}
Hobi\t: {hobi}
Tinggi\t: {tinggi}cm
''')

stat = 'Newton Frankel Issac'
up = stat.upper()
print(up)
up = up.split() #up menjadi list 3 item
print(up)
print(up[-1][0],' '.join(up[0:-1])) # N SIR ISSAC
print('F SIR ISSAC NEWTON')
print(up[-1], up[0][0], up[1][0]) # NEWTON S I
print('NEWTON S I\n\n')


stat2 = '&sir$ @issac# *newton.'
up2 = stat2.upper()
print(up2)
up2 = up2.split()
print(up2)
print(up2[0][1:-1], up2[1][1:-1], up2[2][1:-1]) #Menggunakan Slicing
print(up2[0].strip('&$'), up2[1].strip('@#'), up2[2].strip('*.')) #Menggunakan method strip
print('SIR ISSAC NEWTON')










print()
# str1 = '''
# Biodata saya:
# NAMA\t: {}
# NIM\t: {}
# Prodi\t: {}
# TTL\t: {}
# Alamat\t: {}
# Asal\t: {}
# Hobi\t: {}
# Tinggi\t: {}cm
# '''
# print(str1.format(nama.title(), nim, prodi.title(), ttl.title(), alamat.title(), asal.capitalize(), hobi.title(), tinggi))