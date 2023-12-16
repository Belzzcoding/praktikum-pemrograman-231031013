pendapatan = int(input('Masukkan Pendapatan: '))
if pendapatan <= 1000:
    persentase = 0
elif pendapatan <= 2000:
    persentase = 10
elif pendapatan <= 3000:
    persentase = 20
elif pendapatan <= 4000:
    persentase = 30
elif pendapatan <= 5000:
    persentase = 40
else:
    persentase = 50

bonus = pendapatan * (persentase / 100)
total = pendapatan + bonus

print('Pendapatan:', pendapatan)
print(f'Persentase: {float(persentase)}%' )
print('Bonus:', int(bonus))
print('Total Pendapatan:', int(total))\

