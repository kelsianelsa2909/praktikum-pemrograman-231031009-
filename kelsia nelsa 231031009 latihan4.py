# Menerima input pendapatan dan mengonversinya ke integer
pendapatan = int(input("Masukkan besaran pendapatan: "))

# Mengecek persentase bonus berdasarkan pendapatan
if pendapatan < 1000:
    persentase = 5
elif pendapatan >= 1000 and pendapatan < 5000:
    persentase = 10
else:
    persentase = 15

# Menghitung bonus
bonus = pendapatan * (persentase / 100)

# Menghitung total pendapatan
total = pendapatan + bonus

# Mencetak hasil
print("Pendapatan:", pendapatan)
print("Persentase Bonus:", persentase, "%")
print("Bonus:", bonus)
print("Total Pendapatan:", total)
