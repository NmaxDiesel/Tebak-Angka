import random

def play_game():
    number = random.randint(1, 100)  # Memilih angka secara acak antara 1 dan 100
    attempts = 0  # Menghitung jumlah percobaan
    
    print("Selamat datang di game Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 hingga 100.")
    print("Coba tebak angka yang saya pilih!")
    
    while True:
        guess = get_guess()  # Mendapatkan tebakan dari pengguna
        attempts += 1
        
        if guess < number:
            print("Angka terlalu rendah! Coba lagi.")
        elif guess > number:
            print("Angka terlalu tinggi! Coba lagi.")
        else:
            print("Selamat! Anda menebak angka dengan benar dalam {} percobaan.".format(attempts))
            break

def get_guess():
    while True:
        try:
            guess = int(input("Masukkan tebakan Anda: "))
            return guess
        except ValueError:
            print("Input tidak valid. Masukkan angka yang valid.")

play_game()
