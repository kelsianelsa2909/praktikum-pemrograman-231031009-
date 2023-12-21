password = "SI23-A"  # Ganti dengan password yang diinginkan
kesempatan = 3

while kesempatan > 0:
    masukan = input("Masukkan password: ")
    if masukan != password:
        kesempatan -= 1
        if kesempatan > 0:
            print("Password salah!")
            print("Kesempatan Anda tersisa", kesempatan, "kali")
        else:
            print("Anda kehabisan kesempatan")
    else:
        print("Selamat! Anda berhasil login.")
        break
