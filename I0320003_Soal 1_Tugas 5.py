# memasukkan data pengunjung
nama = input("Masukkan nama Anda: ")
gender = input("Masukkan jenis kelamin Anda (L/P): ")
if gender.upper() == 'L':
    print('Selamat Datang, Tuan', nama, '!')
elif gender.upper() == 'P':
    print('Selamat Datang, Nyonya', nama, '!')
else:
    pass
