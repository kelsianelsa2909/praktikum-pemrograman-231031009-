

import hashlib

def hash_password(password, salt):
    # Menggunakan fungsi hash SHA-256 untuk mengenkripsi kata sandi dengan salt
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password

def is_password_strong(password):
    # Memeriksa kompleksitas kata sandi (contoh sederhana)
    return len(password) >= 8 and any(char.isalpha() for char in password) and any(char.isdigit() for char in password)

def main():
    # Input kata sandi dari pengguna
    password = input("Masukkan kata sandi: ")

    # Memeriksa kompleksitas kata sandi
    if not is_password_strong(password):
        print("Kata sandi tidak memenuhi kriteria keamanan.")
        return

    # Menghasilkan salt secara acak (bisa menggunakan modul os atau library khusus)
    salt = "somerandomsalt"

    # Mengenkripsi kata sandi dengan salt
    hashed_password = hash_password(password, salt)

    print("Kata sandi berhasil dienkripsi dengan salt:", hashed_password)

if __name__ == "__main__":
    main()    


#contoh Penguna

username = "kelsia nelsa"
password = "231031009"

from getpass import getpass
uname = input("Enter a user name: ")
uname = uname.strip()
if uname!=username:
    print("Username pengguna salah. Selamat tinggal.") 
else:
    pword=input("Enter your password: ")
    pword = pword.strip()
if pword == password:
    print("welcome to our world of python")
else:
    print("Sandi salah. akses ditolak")




