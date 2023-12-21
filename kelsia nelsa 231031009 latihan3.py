# Menerima input nama karyawan
nama = input("Masukkan nama karyawan: ")

# Menerima input pendapatan dan mengonversinya ke integer
pendapatan = int(input("Masukkan besaran pendapatan: "))

# Mencetak nama karyawan
print("Nama karyawan:", nama)

# Mencetak pendapatan karyawan
print("Pendapatan karyawan:", pendapatan)

# Mengecek kondisi pendapatan
if pendapatan > 1000:
    print("Status: Berhak")
else:
    print("Status: Tidak Berhak")
