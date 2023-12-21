print(f'Tugas 2 : buat program')
print()

print(f'1. program penjumlaham waktu')
print()

# Input waktu awal dalam format jam dan menit
waktu_awal = input("Masukkan waktu awal (hh:mm): ")
jam_awal, menit_awal = map(int, waktu_awal.split(':'))

# Input jumlah jam dan menit yang akan ditambahkan
jam_tambahan = int(input("Masukkan jumlah jam yang akan ditambahkan: "))
menit_tambahan = int(input("Masukkan jumlah menit yang akan ditambahkan: "))

# Jumlahkan waktu
jam_total = jam_awal + jam_tambahan
menit_total = menit_awal + menit_tambahan

# Penanganan jika menit lebih dari 60
if menit_total >= 60:
    jam_total += 1
    menit_total -= 60

# Penanganan jika jam lebih dari 24 (untuk menghindari melebihi satu hari)
if jam_total >= 24:
    jam_total -= 24

# Format hasil ke dalam format hh:mm
hasil = f"{jam_total:02d}:{menit_total:02d}"

print(f"Waktu sekarang menunjukkan pukul {hasil}")
print()


print(f'2. program selisih waktu')
print()

from datetime import datetime, timedelta
 
# Input waktu awal dalam format jam.menit
waktu_awal = input("Masukkan waktu awal (hh.mm): ")
jam_awal, menit_awal = map(int, waktu_awal.split('.'))

# Input jumlah jam dan menit yang akan dikurangkan
jam_kurang = int(input("Masukkan jumlah jam yang akan dikurangkan: "))
menit_kurang = int(input("Masukkan jumlah menit yang akan dikurangkan: "))

# Mengonversi input ke objek waktu
waktu_awal = datetime(2023, 1, 1, jam_awal, menit_awal)

# Membentuk objek selisih waktu yang akan dikurangkan
selisih_waktu = timedelta(hours=jam_kurang, minutes=menit_kurang)

# Menghitung waktu sebelumnya
waktu_sebelumnya = waktu_awal - selisih_waktu

# Format hasil dalam format hh:mm
hasil = waktu_sebelumnya.strftime("%H:%M")

print(f"Waktu sekarang menunjukkan pukul {hasil}")






