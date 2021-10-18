Nim = 3220004
Nama = "Melianus_Degei"
Tugas = "P3 Konversi Nilai Mahasiswa"

print("Nim     :", Nim)
print("Nama    :", Nama)
print("Tugas   :", Tugas)

print("*****************************")
# Mengetahui Nilai ketentuan
# >=90 nilai A
# >=70 dan < 90 nilai B
# >=50 dan < 70 nilai C
# >=30 nilai E

nilai_mahasiswa = int(input('Masukan Nilai_Mahasiswa 0, 30, 70, 90, 100 : '))

hasil = None
if nilai_mahasiswa <= 100 and nilai_mahasiswa > 90:
    hasil = 'A'
elif nilai_mahasiswa <= 90 and nilai_mahasiswa > 70:
    hasil = 'B'
elif nilai_mahasiswa <= 70 and nilai_mahasiswa > 30:
    hasil = 'C'
elif nilai_mahasiswa <= 30 and nilai_mahasiswa > 0:
    hasil = 'E'
else:
    print("Inputan Salah")

print('nilai_mahasiswa {} = {}'.format(nilai_mahasiswa, hasil))
