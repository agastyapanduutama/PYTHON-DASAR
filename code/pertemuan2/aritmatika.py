"""
Dokumentasi Operator Aritmatika

Operator adalah konstruksi yang dapat memanipulasi nilai dari operan.

Operator pada Aritmatika 
Penjumlahan (+) contoh : 1 + 2 = 3
Pengurangan (-) contoh : 1 - 2 = 1
Perkalian (*) contoh : 1 * 2 = 2
Pembagian (/) contoh : 10 / 5 = 2
Sisa Bagi / Modulus (%) contoh : 11 % 2 = 1
Pangkat (**) contoh : 8 ** 2 = 64
Pembagian Bulat (//) contoh : 10 // 3 = 3

Referensi 
https://www.w3schools.com/python/python_operators.asp
https://belajarpython.com/tutorial/operator-python

contoh 
hasil(variable yang nantinya akan di print) = variable1(nilai pertama) +(Operator Aritmatika yang digunakan) variable2(nilai kedua)

contoh secara coding
value = 10 + 11

maka akan menghasilkan angka
21
"""

# Contoh nilai yang digunakan di deklarasi kedalam variable
nilai1 = 10
nilai2 = 4

# Contoh Penggunaan Operator Aritmatika Pertambahan
print("-------Pertambahan-------")
hasil = nilai1+nilai2
print(f"Hasil dari {nilai1} + {nilai2} adalah {hasil}")

# Contoh Penggunaan Operator Aritmatika Pengurangan
print("-------Pengurangan-------")
hasil = nilai1-nilai2
print(f"Hasil dari {nilai1} - {nilai2} adalah {hasil}")

# Contoh Penggunaan Operator Aritmatika Perkalian
print("-------Perkalian-------")
hasil = nilai1*nilai2
print(f"Hasil dari {nilai1} x {nilai2} adalah {hasil}")

# Contoh Penggunaan Operator Aritmatika Pembagian
print("-------Pembagian-------")
hasil = nilai1/nilai2
print(f"Hasil dari {nilai1} / {nilai2} adalah {hasil}")

# Contoh Penggunaan Operator Aritmatika Modulus
print("-------Modulus-------")
hasil = nilai1%nilai2
print(f"Hasil dari {nilai1} ** {nilai2} adalah {hasil}")

# Contoh Penggunaan Operator Aritmatika Pangkat
print("-------Eksponen/Pangkat-------")
hasil = nilai1**nilai2
print(f"Hasil dari {nilai1} % {nilai2} adalah {hasil}")

# Contoh Penggunaan Operator Aritmatika Pembagian Bulat
print("-------Pembagian Bulat -------")
hasil = nilai1//nilai2
print(f"Hasil dari {nilai1} // {nilai2} adalah {hasil}")
