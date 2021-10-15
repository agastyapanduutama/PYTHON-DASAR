"""
# Operator Komparasi / Perbandingan
# Lebih besar, lebih kecil, lebih besar sama dengan, lebih kecil sama dengan, sama dengan, tidak sama dengan
# >, <, >=, <=, ==, !=

- Sama dengan (==)	1 == 1	bernilai True Jika masing-masing operan memiliki nilai yang sama, maka kondisi bernilai benar atau True.
- Tidak sama dengan (!=)	2 != 2	bernilai False Akan menghasilkan nilai kebalikan dari kondisi sebenarnya.
- Tidak sama dengan (<>)	2 <> 2	bernilai False Akan menghasilkan nilai kebalikan dari kondisi sebenarnya.
- Lebih besar dari (>)	5 > 3	bernilai True Jika nilai operan kiri lebih besar dari nilai operan kanan, maka kondisi menjadi benar.
- Lebih kecil dari (<)	5 < 3	bernilai True Jika nilai operan kiri lebih kecil dari nilai operan kanan, maka kondisi menjadi benar.
- Lebih besar atau sama dengan (>=)	5 >= 3	bernilai True Jika nilai operan kiri lebih besar dari nilai operan kanan, atau sama, maka kondisi menjadi benar.
- Lebih kecil atau sama dengan (<=)	5 <= 3	bernilai True Jika nilai operan kiri lebih kecil dari nilai operan kanan, atau sama, maka kondisi menjadi benar.

referensi : https://belajarpython.com/tutorial/operator-python
"""

a = 10
b = 20

# Lebih Besar
hasil = a > b
print(f"apakah {a} > {b} = {hasil}")

# Lebih Kecil
hasil = a < b
print(f"apakah {a} < {b} = {hasil}")

# Lebih besar sama dengan
hasil = a >= b
print(f"apakah {a} >= {b} = {hasil}")

# Lebih kecil sama dengan
hasil = a <= b
print(f"apakah {a} <= {b} = {hasil}")

# Sama dengan
hasil = a == b
print(f"apakah {a} == {b} = {hasil}")

# Tidak sama dengan
hasil = a != b
print(f"apakah {a} != {b} = {hasil}")