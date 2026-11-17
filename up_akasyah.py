
jumlah_pelanggan = int(input("jumlah pelanggan: "))
i = 1

while i <= jumlah_pelanggan:
    print("\n==PEMESANAN TIKET==")

    nama = input("masukkan nama pelanggan: ")
    jenis = input("Jenis tiket reguler/vip/premium: ")
    jumlah = int(input("Jumlah tiket: "))

    if jenis == "reguler":
        harga = 35000
    elif jenis == "vip":
        harga = 50000
    elif jenis == "premium":
        harga = 75000
    else:
        harga = 0

    total = harga * jumlah

    if jumlah > 3:
        diskon = total * 10 / 100
    else:
        diskon = 0

    bayar = total - diskon

    print("\n==PEMBAYARAN==")
    print("nama:", nama)
    print("jenis tiket:", jenis)
    print("jumlah tiket:", jumlah)
    print("total:", total)
    print("diskon:", diskon)
    print("total pembayaran:", bayar)

    i += 1

print("\nSemua pelanggan selesai!")
