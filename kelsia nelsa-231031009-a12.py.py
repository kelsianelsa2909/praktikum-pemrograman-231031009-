a = True

#judul
def judul():
    print('PROGRAM MENGHITUNG LUAS DAN KELILING'.center(45))
    print('BANGUN DATAR PERSEGI'.center(45))
    print()

def inputan():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan Lebar: "))
    return panjang,lebar

def hitung(panjang,lebar):
    luas = panjang*lebar
    kel = (panjang,lebar)*2
    return luas,kel

def keliling(panjang,lebar):
    hasil= (panjang+lebar)* 2
    return hasil

def tampil(pesan,nilai):
    print(f"hasil perhitungan nilai {pesan}: {nilai}")

def pilihan():
    pilih = input('Apakah Ingin Melanjutkan? [y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Sampai Jumpah')
    return a

a = True
while a:
    judul()
    #Inputan panjang dan lebar
    panjang,lebar = inputan()
    #hitung luas
    luas,kel= hitung(panjang,lebar)
    #cetak atau display
    tampil('luas',luas)
    tampil("keliling",kel)
    #pilihan
    a = pilihan()

    