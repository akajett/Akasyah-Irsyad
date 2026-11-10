nama = input("Masukkan nama: ")

if nama == "andi":
    target = 70
elif nama == "budi":
    target = 75
elif nama == "citra":
    target = 80
else:
    print("Nama tidak terdaftar")

print("\nNama mahasiswa :", nama)
print("Target nilai   :", target)
3
percobaan = 1
lulus = False

while percobaan <= 3:

    print("\nPercobaan ke", percobaan)

    nilai = int(input("Masukkan nilai ujian: "))

    if nilai >= target:
        print("Nilai:", nilai)
        print("Selamat! Kamu berhasil mencapai target.")
        lulus = True
        break
    else:
        print("Nilai:", nilai)
        print("Target belum tercapai. Silakan remedial.")

    percobaan += 1


if lulus:
    print(nama, "berhasil lulus!")
    print("Jumlah percobaan:", percobaan)
else:
    print(nama, "dinyatakan TIDAK LULUS.")
    print("Sudah mengikuti 3 kali percobaan.")
