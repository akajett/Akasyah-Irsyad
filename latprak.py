print ("<======NILAI MAHASISWA======>")
nama_mhs = input("Nama Mahasiswa :")
kelas = input ("Kelas :")

nilai_a = int(input("Masukkan Nilai Agama:"))
nilai_b = int(input("Masukkan Nilai Algoritma:"))
nilai_c = int(input("Masukkan Nilai Pancasila:"))
nilai_d = int(input("Masukkan Nilai Basis data:"))
nilai_e = int(input("Masukkan Nilai Informatika:"))
nilai_f = int(input("Masukkan Nilai bahasa Indonesia:"))
nilai_g = int(input("Masukkan Nilai Bahasa inggris:"))
rata_rata = (nilai_a +nilai_b+nilai_c+nilai_d+nilai_e+nilai_f+nilai_g) / 7

if rata_rata >=90 and rata_rata <=100:
    print("nilai : A")
elif rata_rata >=80 and rata_rata <=90:
    print ("Nilai : B")    
elif rata_rata >=60 and  rata_rata <=80:
    print ("Nilai : C")
elif rata_rata >=50 and  rata_rata <=60:
    print ("Nilai : D")
else:
    print("Nilai : E")