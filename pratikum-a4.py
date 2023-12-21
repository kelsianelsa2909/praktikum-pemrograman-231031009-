print()
nim =['2','3','1','0','3','1','0','0','9']
print(nim)
#nim2 ='231031009'
print(nim[1:9])
#print(nim2[2:9])

print()
#akses item
print(f'item indeks 0: {nim[0]}')
print(f'item indeks 4: {nim[4]}')
print(f'item indeks terakhir: {nim[len(nim)-1]}')

print()
#akses indeks negatif
print(f'item indeks terakhir: {nim[-1]}')
print(f'item indeks pertama: {nim[-len(nim)]}')
print(f'item indeks 6[-3]: {nim[-3]}')
print(f'item indeks 4[-5]: {nim[-5]}')
print(f'item indeks 7[-2]: {nim[-2]}')

print()
#akses indeks batas
print(f'item indeks 1,2,....:\n {nim[1:]}')
print(f'item indeks 3,4,....:\n {nim[3:]}')
print(f'item indeks 0,1,2,....:\n {nim[:3]}')
print(f'item indeks 0,1,2,3,....:\n {nim[:4]}')
print(f'item indeks semua:\n {nim[:]}')
print(f'item indeks [:8]:\n {nim[:-1]}')
print(f'item indeks [:6]:\n {nim[:-3]}')

print()
#pengirisan
print(f'item indeks 1,2:\n {nim[1:3]}')
print(f'item indeks 2,3,4:\n {nim[2:5]}')
print(f'item indeks kosong:\n {nim[3:3]}')
print(f'item indeks [0:0]kosong:\n {nim[-1:-1]}')
print(f'item indeks [1:8]kosong:\n {nim[1:-1]}')
print(f'item indeks [1:8]kosong:\n {nim[2:-2]}')

print()
print('latihan list')
data=['kelsia nelsa',2023,'aktif']
nilai= [90,89,93,97]
print(f'{data[0]} status kuliah:{data[2]}')
print(f'Data terbesar nilai adalah: {max(nilai)}')
print(f'Data terkecil nilai adalah: {min(nilai)}')
x_bar= sum(nilai)/len(nilai)
print(f'Rata-rata nilai adalah:{x_bar}')

print()
print('latihan tuple')
data=['kelsia nelsa',2023,'aktif']
nilai= [90,89,93,97]
print(f'Jumlah nilai kelsia nelsa adalah: {len(nilai)}')
print(f'Data terbesar nilai adalah: {max(nilai)}')
print(f'Data terkecil nilai adalah: {min(nilai)}')
x_bar= sum(nilai)/len(nilai)
print(f'Rata-rata nilai adalah:{x_bar}')

print()
print('latihan nested list')

data=[['kelsia nelsa',2023,'aktif'],
      [90,89,93,97],
      [20,22],
      ['S1-Reguler','Ganjil']]

print()
# Nested List
kelas = [('Matkul1',2),
         ('Matkul2',3)]

kelas.append(('Matkul3',3))
kelas.append(('Matkul4',2))
kelas.append(('Matkul5',3))
kelas.append(('Matkul6',2))
kelas.append(('Matkul7',2))
kelas.append(('Matkul8',3))
print(kelas)
# tambahkan matkul 8 dan sksnya

# Mata kuliah 1: matkul1 dengan jumlah 2 sks
print(f'Mata kuliah 1 : {kelas[0][0]} dengan jumlah {kelas[0][1]} sks ')
# Mata kuliah 2: matkul2 dengan jumlah 3 sks
print(f'mata kuliah 2 : {kelas[1][0]} dengan jumlah {kelas[1][1]} sks ')
# Mata kuliah 3: matkul3 dengan jumlah 3 sks
print(f'mata kuliah 3 : {kelas [2][0]} dengan jumlah {kelas[2][1]} sks')
# Mata kuliah 4: matkul4 dengan jumlah 2 sks
print(f'mata kuliah 4 : {kelas [3][0]} dengan jumlah {kelas[3][1]} sks')
# Mata kuliah 5: matkul5 dengan jumlah 3 sks
print(f'mata kuliah 5 : {kelas [4][0]} dengan jumlah {kelas[4][1]} sks')
# Mata kuliah 6: matkul6 dengan jumlah 2 sks
print(f'mata kuliah 6 : {kelas [5][0]} dengan jumlah {kelas[5][1]} sks')
# Mata kuliah 7: matkul7 dengan jumlah 2 sks
print(f'mata kuliah 7 : {kelas [6][0]} dengan jumlah {kelas[6][1]} sks')
# Mata kuliah 8: matkul8 dengan jumlah 3 sks
print(f'mata kuliah 8 : {kelas [7][0]} dengan jumlah {kelas[7][1]} sks')      

# Tambahkan 8 nilai masing-masing
print()
print(data[0][0])
print(data[3][0])
print(data[2][0:])

print(f'Program pendidikan {data[0][0]} :{data[3][0]}')
print(f'Angkatan : {data[0][1]}-{data[3][1]}')
print(f'Jumlah nilai {data[0][0]} adalah:{len(data[1])}')
print(f'Data terbesar nilai {data[0][0]} adalah:{max(data[1])}')
print(f'Data terkecil nilai {data[0][0]} adalah:{min(data[1])}')
x_bar =sum(data[1])/len(data[1])
print(f'Rata-rata nilai {data[0][0]} adalah:{x_bar}')






















