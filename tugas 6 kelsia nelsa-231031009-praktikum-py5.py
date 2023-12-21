a = True
while a:
    pilih = input('pilihan: ')
    if pilih == 'ya':
        print('selamat datang')
    elif pilih == 'tidak':
        print('sampai jumpa')
    else:
        print('Masukkan pilihan ya atau tidak')

    jawab = input('Apakah Anda ingin melanjutkan? (ya/tidak) ')
    if jawab != 'ya':
        a = False

#Penjelasan:
#Kode di atas menggunakan loop while untuk terus meminta masukan dari pengguna.
#Pengguna diminta untuk memasukkan pilihan 'ya' atau 'tidak'.
#Jika pengguna memasukkan 'ya', maka akan mencetak 'selamat datang'.
#Jika pengguna memasukkan 'tidak', maka akan mencetak 'sampai jumpa'.
#Jika pengguna memasukkan selain 'ya' atau 'tidak', maka akan mencetak pesan untuk memasukkan pilihan yang benar.
#Setelah mencetak pesan berdasarkan pilihan pengguna, program akan menanyakan apakah pengguna ingin melanjutkan. Jika pengguna memilih 'tidak', loop akan berhenti karena variabel a diubah menjadi False.
