tugas = float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))
kehadiran = float(input("Persentase kehadiran: "))
penghasilan = int(input("Penghasilan orang tua per bulan: "))
sertifikat = int(input("Jumlah sertifikat lomba: "))

nilai_akhir = 0.2 * tugas + 0.35 * uts + 0.45 * uas

valid = (0 <= tugas <= 100) and (0 <= uts <= 100) and (0 <= uas <= 100) and (0 <= kehadiran <= 100)
nilai_ok = nilai_akhir >= 80
hadir_ok = kehadiran >= 85
min_nilai = (tugas >= 65) and (uts >= 65) and (uas >= 65)
ekonomi = (penghasilan < 4000000) or (sertifikat >= 2)

layak = valid and nilai_ok and hadir_ok and min_nilai and ekonomi
status = ["TIDAK LAYAK", "LAYAK"][layak]

print(status)