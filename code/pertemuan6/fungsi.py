# Fungsi

"""
Fungsi adalah blok kode terorganisir dan dapat digunakan kembali yang digunakan untuk melakukan sebuah tindakan/action. Fungsi memberikan modularitas yang lebih baik untuk aplikasi Anda dan tingkat penggunaan kode yang tinggi.

reference : 
https://belajarpython.com/tutorial/fungsi-python
https://www.w3schools.com/python/python_functions.asp
"""

# Contoh fungsi dengan pertambahan
# def digunakan sebagai definisi atau function
# Petambahan adalah nama fungsi yang akan digunakan
# Didalam tanda kurung terdapat parameter 'a' dan 'b', nantinya ini akan mengambil dari nilai parameter dari pemanggilan fungsi tersebut, jika parameternya kurang maka akan menampilkan pesan error bahwa def pertambahan membutuhkan 2 parameter
# Hasil = a + b, adalah sebuah perintah untuk operator aritmatika perjumlahan
# Lalu nilai akan di kembalikan dengan menggunakan perintah return 
def pertambahan(a,b):
  hasil = a + b
  return hasil

# Contoh fungsi pengurangan
def pengurangan(a,b):
  hasil = a - b
  return hasil

# Contoh Pemanggilan fungsi pengurangan
# hasil adalah contoh deklarasi variable lalu pengurangan adalah memanggil nama fungsi pengurangan dengan 2 parameter didalamnya yaitu angka 8 dan 5, maka angka tersebut akan masuk ke dalam paramater a dan b lalu akan di kurangi nilainya
hasil = pengurangan(8,5)
print(hasil)


# Contoh function string
def sapa(nama,kota):
  print("Nama saya adalah : ", nama)
  print("Asal dari Kota : ", kota)

sapa("Pandu", "Bandung")


# Contoh fungsi menggunakan loop 
def sapa(nama):
  print("Nama saya adalah : ", nama)


nama = ['Pandu', 'Agastya', 'Satriya', 'utama']

for i in nama:
  sapa(i)