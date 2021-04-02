# memasukkan data program
nama = input('Masukkan nama Anda: ')
nilai = float(input('Masukkan nilai Anda: '))
if 85<= nilai <=100:
    print('Halo,', nama, '!', 'Nilai Anda setelah dikonversi adalah A')
elif 80<= nilai <=84:
    print('Halo,', nama, '!', 'Nilai Anda setelah dikonversi adalah A-')
elif 75<= nilai <=79:
    print('Halo,', nama, '!', 'Nilai Anda setelah dikonversi adalah B+')
elif 70<= nilai <=74:
    print('Halo,', nama, '!', 'Nilai Anda setelah dikonversi adalah B')
elif 65<= nilai <=69:
    print('Halo,', nama, '!', 'Nilai Anda setelah dikonversi adalah C+')
elif 60<= nilai <=64:
    print('Halo,', nama, '!', 'Nilai Anda setelah dikonversi adalah C')
elif nilai <60:
    print('Halo,', nama, '!', 'Nilai Anda setelah dikonversi adalah E')
else:
    print('Halo,', nama, '!', 'Nilai Anda tidak dapat dikonversikan')