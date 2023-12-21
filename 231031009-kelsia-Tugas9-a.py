#Buat biodata dictionary

biodata = {
    "Nama\t"          : "kelsia nelsa",
    "Nim\t"           : "231031009",
    "prodi\t"         : "sistem informasi",
    "TTL\t"           : "29 september 2005",
    "Alamat\t"        : "Jl.DRS.H.SYAMSUL ALAM BULU",
    "Hobi\t"          : ["menari","Dengar Musik",],
    "Status\t"        : "Pelajar",
    "asal\t"          : "pinrang",  
}

# Menampilkan biodata
print("Biodata: ")
for key, value in biodata.items():
    print(f"{key}: {value}")
