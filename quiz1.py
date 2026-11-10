nama = input("Masukkan nama mahasiswa: ")

if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    print("Nama mahasiswa tidak ditemukan!")
    exit()

print("Nama mahasiswa :", nama)
print("Target nilai   :", target)

ulang = 1
lulus = False

while ulang <= 3:
    nilai = int(input("Masukkan nilai ujian ke-" + str(ulang) + ": "))

    if nilai >= target:
        lulus = True
        break
    else:
        print("Nilai belum mencapai target!")
        ulang += 1

print("\nHASIL AKHIR")

if lulus:
    print(nama, "berhasil lulus!")
    print("Ujian ke-", ulang)
else:
    print(nama, "tidak lulus setelah 3 kali ujian.")
