total_belanja = int(input("Total belanja: "))
uang_bayar = int(input("Uang dibayarkan: "))

uang_cukup = uang_bayar >= total_belanja
uang_kurang = uang_bayar < total_belanja

kekurangan = (total_belanja - uang_bayar) * uang_kurang
kembalian = (uang_bayar - total_belanja) * uang_cukup

sisa = kembalian
p100k = sisa // 100000
sisa = sisa % 100000

p50k = sisa // 50000
sisa = sisa % 50000

p20k = sisa // 20000
sisa = sisa % 20000

p10k = sisa // 10000
sisa = sisa % 10000

p5k = sisa // 5000
sisa = sisa % 5000

p2k = sisa // 2000
sisa = sisa % 2000

p1k = sisa // 1000
sisa = sisa % 1000

p500 = sisa // 500
sisa = sisa % 500

total_lembar = p100k + p50k + p20k + p10k + p5k + p2k + p1k + p500

print("Uang cukup :", uang_cukup)
print("Kekurangan :", kekurangan)
print("Kembalian :", kembalian)
print("Pecahan Rp100.000 :", p100k)
print("Pecahan Rp50.000 :", p50k)
print("Pecahan Rp20.000 :", p20k)
print("Pecahan Rp10.000 :", p10k)
print("Pecahan Rp5.000 :", p5k)
print("Pecahan Rp2.000 :", p2k)
print("Pecahan Rp1.000 :", p1k)
print("Pecahan Rp500 :", p500)
print("Total lembar/keping :", total_lembar)