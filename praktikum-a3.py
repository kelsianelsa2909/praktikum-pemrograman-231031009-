

nama  = 'kelsia nelsa'
nim   = '231031009'
meet  = 'praktikum 3'
prodi ='sistem informasi A'
email ='kelsianelsa@gmail.com'
ttl   ='29-09-2005'
alamat='parepare'
asal  ='pinrang'
hobi  ='nonton drakor'
tinggi='153'


sp = 40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.capitalize().rjust(sp))
print(prodi.title().rjust(sp))
print(email.rjust(sp))
print('-'*sp)

print(f'''Halo,nama saya {nama.title()} dengan NIM {nim} dari prodi {prodi.title()},ini adalah file {meet.capitalize()}. Terimah kasih.''')

print(f'''biodata saya,
nama   \t: {nama.title()}
NIM    \t: {nim}
Prodi  \t: {prodi.title()}
TTL    \t: {ttl}
Alamat \t: {alamat}
Asal   \t: {asal}
Hobi   \t: {hobi}
Tinggi \t: {tinggi}cm ''')



stat ='sir issac  frankel issac'
up   = stat.upper()
print(up)
up = up.split() 
print(up)
print(up[-1][0],''.join(up[0:-1]))
print('F SIR ISSAC NEWTON')

print(up[-1],up[0][0],up[1][0])
print('NEWTON S I')

print()

stat2 ='&sir$ @issac# *newton.'
up2   = stat2.upper()
print(up2)
up2   = up2.split()
print(up)
print(up2[0][1:-1],up2[1][1:-1],up2[2][1:-1])
print(up2[0].strip('&$'),up[1].strip('@#'),up2[2].strip('*.'))
print('SIR ISSAC NEWTON')




print()
print('Tugas Pratikum 3'.center(40))
nama = 'kelsia nelsa'
nim = '231031009'
prodi = 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
Prodi\t: {prodi}''')

print()
print('str1')
str1 ='duFort Frankel Von Neumann'
#output: NEUMANN DUFORT FRANKEL VON
up =str1.upper()
up =up.split()
print(up[-1],up[0],up[1],up[2])

print()
print('str2')
str2 ='duFort Frankel Von Neumann'
#output: DFV NEUMANN
up =str2.upper()
up =up.split()
print(up[0][0]+up[0][2]+up[2][0],up[-1])

print()
print('str3')
str3 ='duFort Frankel Von Neumann'
#output: DUFORT FVN
up =str3.upper()
up =up.split()
print(up[0],up[0][2]+up[2][0]+up[-1][0])

print()
print('str4')
str4 ='duFort Frankel Von Neumann'
#output: N duFort FV
up =str4.upper()
up =up.split()
print(up[-1][0],up[0][0].lower()+up[0][1].lower()+up[0][2].upper()+up[0][3].lower()+up[0][4].lower()+up[0][5].lower(),up[0][2]+up[2][0])

print()
print('str5')
str5 ='duFort Frankel Von Neumann'
#output: NEUMANN d f v
up =str5.upper()
up =up.split()
print(up[-1],up[0][0].lower(),up[0][2].lower(),up[2][0].lower())

print()
print('str6')
str6 ='duFort Frankel Von Neumann'
#output: NEUMANN DFV
up =str6.upper()
up =up.split()
print(up[-1],up[0][0]+up[0][2]+up[2][0])

print()
print('str7')
str7 ='@duFort Frankel Von Neumann$'
#output: duFort Frankel Von Neumann
print(str7.strip('@$'),'\n')


str8 ='#duFort4Frankel4Von4Neumann$'
#output: duFort Frankel Von Neumann
print('str8')
str8 = str8.replace('4',' ')
print(str8.strip('#$'),'\n')


str9 ='@duFort@-^Frankel*-(Von(-(Neumann$'
#output: duFort Frankel Von Neumann
print('str9')
str9 = str9.replace('-',' ')
str9 = str9.split()
print(str9[0].strip('@@'),str9[1].strip('^*'),str9[2].strip('(('),str9[-1].strip('($'))

print()
str10 ='@DUFort@1^FraNkel*1(Von(1(NeuMann^'
#output: duFort Frankel Von Neumann
print('str10')
str10 =str10.title()
str10 = str10.replace('1',' ')
str10 = str10.split()
print(str10[0].strip('@@').lower(),str10[1].strip('^*').title(),str10[2].strip('((').title(),str10[-1].strip('(^').title())







