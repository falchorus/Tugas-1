n = int(input("Masukkan bilangan 5 digit: "))

d5 = n % 10
d4 = (n // 10) % 10
d3 = (n // 100) % 10
d2 = (n // 1000) % 10
d1 = (n // 10000) % 10

is_5_digit = n >= 10000 and n <= 99999

jumlah_digit = d1 + d2 + d3 + d4 + d5

genap1 = d1 % 2 == 0
genap2 = d2 % 2 == 0
genap3 = d3 % 2 == 0
genap4 = d4 % 2 == 0
genap5 = d5 % 2 == 0
banyak_genap = genap1 + genap2 + genap3 + genap4 + genap5

terbalik = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1

is_palindrom = n == terbalik

is_harshad = n % jumlah_digit == 0

print("a. Benar 5 digit :", is_5_digit)
print("b. Jumlah digit  :", jumlah_digit)
print("c. Digit genap   :", banyak_genap)
print("d. Terbalik      :", terbalik)
print("e. Palindrom     :", is_palindrom)
print("f. Harshad       :", is_harshad)