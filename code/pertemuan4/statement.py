# If, Elseif, else statement
"""
Pengambilan keputusan (kondisi if) digunakan untuk mengantisipasi kondisi yang terjadi saat jalanya program dan menentukan tindakan apa yang akan diambil sesuai dengan kondisi.

Pada python ada beberapa statement/kondisi diantaranya adalah if, else dan elif Kondisi if digunakan untuk mengeksekusi kode jika kondisi bernilai benar True.

referensi : 
https://belajarpython.com/tutorial/kondisi-if-else-python
"""

nilai1 = 10
nilai2 = 11

# cek kondisi dari nilai apakah nilai 1 sama dengan nilai 2
if nilai1 == nilai2:
    print("Iya")
else:
    print("Tidak")
    

# Cek kondisi logika AND
a = 19
b = 20
c = 21

if a < b and b < c:
    print("Iya")
else:
    print("tidak")
    

# Cek Kondisi Logika OR
a = 29
b = 30
c = 31

if a > b or b > c:
    print("Iya")
else:
    print("tidak")

    
# Cek nama /string sama dengan
nama = "ucup"
if nama == "ucup":
    print("Hai ucup")
else:
    print("Hai siapa kamu?")


# Cek nama /string tidak sama dengan
nama = input("Masukan Nama kamu : ")
if nama != '':
    print("Hai",nama)
else:
    print("Hai kamu")


# Cek kondisi lebih spesifik
nama = input("Masukan Nama Kamu : ")
if nama=="ucup":
    print("Hai ucup saripudin")
elif nama=="adit":
    print("Hai Dipa Nusantara Adit ")
elif nama=="dwi":
    print("Hai Dwi ki")
else:
    print("Hai siapa kamu?")
    