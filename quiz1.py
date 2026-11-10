nama = input ("masukkan nama mahasiswa: ")

if nama == "andi":
    target = 70
elif nama == "budi":
    target = 75
elif nama == "citra":
    target = 80
else:
    print("nama mahasiswa tidak ditemukan!")
    exit()

print("nama mahasiswa : ", nama)
print("Target nilai   :", target)

ulang = 1
lulus = False

while ulang <= 3:
    nilai = int(input("masukkan nilai ujian ke-" + str(ulang) + ": "))

    if nilai >= target:
        lulus = True
        break
    else:
        print("nilai belum mencapai target!")
        ulang += 1

print("\nHASIL AKHIR")

if lulus:
    print(nama, "berhasil lulus!")
    print("ujian ke-", ulang)
else:
    print(nama,"tidak lulus setelah 3 kali ujian.")
