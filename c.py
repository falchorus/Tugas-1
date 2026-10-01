tanggal = int(input("Tanggal: "))
bulan = int(input("Bulan: "))
tahun = int(input("Tahun: "))

is_kabisat = (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0)

is_31 = bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12
is_30 = bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11
is_feb = bulan == 2

hari_feb = 28 + (1 * is_kabisat)

jumlah_hari = (31 * is_31) + (30 * is_30) + (hari_feb * is_feb)

is_valid = tanggal >= 1 and tanggal <= jumlah_hari

print("a. Tahun kabisat :", is_kabisat)
print("b. Jumlah hari  :", jumlah_hari)
print("c. Tanggal valid :", is_valid)
