kesempatan = 3
pw_1 = 23
pw_2 = 103
pw_3 = 1013 

while True:
    if kesempatan != 0:
        try:
            inp = int(input('\nMasukkan password pertama: '))
            if inp == pw_1:
                print('Sesi Pertama Berhasil')
                inp = int(input('\nMasukkan password kedua: '))
                if inp == pw_2:
                    print('Sesi Kedua Berhasil')
                    inp = int(input('\nMasukkan password ketiga: '))
                    if inp == pw_3:
                        print('Anda berhasil login.')
                        break
                    elif inp != pw_3:
                        kesempatan -= 1
                        print('Password salah.')
                        print(f'Kesempatan anda tersisa {kesempatan} kali')
                        continue
                elif inp != pw_2:
                    kesempatan -= 1
                    print('Password salah.')
                    print(f'Kesempatan anda tersisa {kesempatan} kali')
                    continue
            elif inp != pw_1:
                kesempatan -= 1
                print('Password salah.')
                print(f'Kesempatan anda tersisa {kesempatan} kali')
                continue
        except ValueError:
            print('Formatnya tidak valid. Diharuskan angka!')
            kesempatan -= 1
            print(f'Kesempatan anda tersisa {kesempatan} kali')
    else:
        print('\nAnda terblokir. Kesempatan anda telah habis')
        break