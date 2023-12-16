kesempatan = 3
pw = 1013

while True:
    inp = int(input('Masukkan Password: '))
    if inp != pw:
        kesempatan -=1
        print('Password salah')
        print(f'Kesempatan anda tersisa {kesempatan} kali')
        if kesempatan == 0:
            print('Anda kehabisan kesempatan')
            break
    else:
        print('Selamat Anda Login!')
        break

