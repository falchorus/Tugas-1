jam_masuk = int(input("Jam masuk: "))
menit_masuk = int(input("Menit masuk: "))
jam_keluar = int(input("Jam keluar: "))
menit_keluar = int(input("Menit keluar: "))
masuk = jam_masuk * 60 + menit_masuk
keluar = jam_keluar * 60 + menit_keluar
lama_menit = (keluar - masuk) % (24 * 60)
lama_menit = max(lama_menit, 1)
jam = lama_menit // 60
menit = lama_menit % 60
jam_ditagih = (lama_menit + 59) // 60
tarif = 3000 + (jam_ditagih - 1) * 2000
tarif = min(tarif, 20000)
print(f"Lama parkir: {jam} jam {menit} menit")
print(f"Jumlah jam yang ditagih: {jam_ditagih} jam")
print(f"Total tarif: Rp{tarif}")