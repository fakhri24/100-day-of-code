from random import randint

from art import logo

EASY = 10
HARD = 6


def mode():
    md = input("Apa mode yang akan kamu pilih? ketik 'mudah' atau 'susah'\n")
    if md == "mudah":
        return EASY
    else:
        return HARD


def game_utama(x, y):
    while x != 0:
        print(f"Kamu punya {x} kesempatan lagi!")
        angka = int(input("Masukkan angka tembakan kamu: "))
        if angka == y:
            return angka
        elif angka < y:
            print("Terlalu rendah!")
            x -= 1
        else:
            print("Terlalu tinggi!")
            x -= 1


def pemenang(x, y):
    if x == y:
        print(f"Benar! Angkanya adalah {y}. Kamu menebak dengan tepat! Selamat! :D")
        return lanjut_main()
    else:
        print("Yah! Kamu gagal menebak dengan benar! :(")
        return lanjut_main()


def lanjut_main():
    lanjut = input("Mau main lagi? ketik 'ayo' atau 'engga'\n")
    if lanjut == "engga":
        print("Senang bermain denganmu! Sampai ketemu lagi! :)")
        return 0


print(logo)

print("Selamat datang di permainan Tebak Angka!")
print("Aku memikirkan suatu angka antara 1 sampai 100.")
print("Kamu akan diberikan beberapa kesempatan untuk menebak angka itu.")
print("Kalau memilih mode 'mudah', kamu akan diberi 10 kesempatan.")
print("Kalau ingin lebih menantang, kamu bisa pilih mode 'susah' yang hanya memberi kamu 5 kesempatan!")

si_angka = randint(1, 100)
a = 0

while a != si_angka:

    kesempatan = mode()

    tebakan = game_utama(kesempatan, si_angka)

    m = pemenang(tebakan, si_angka)
    if m == 0:
        a = si_angka
