# Pengulangan
"""
Secara umum, pernyataan pada bahasa pemrograman akan dieksekusi secara berurutan. Pernyataan pertama dalam sebuah fungsi dijalankan pertama, diikuti oleh yang kedua, dan seterusnya.



Reference : https://belajarpython.com/tutorial/loop-python
"""

# Pengulangan For
# Pengulangan akan dilakukan sebanyak 10x, dilihat nilai parameter pada range diisikan angka sepuluh jika parameter diisikan angka lain maka program akan di lakukan pengulangan sebanyak nilai parameter yang diisi, dan program akan dimulai dari angka 0 hingga 9

for nilai in range(10):
    print(nilai)

# Pengulangan yang sama namun dimulai dari angka 5 dan setiap nilainya ditambahkan 5 kita bisa melihatnya dari parameter pertama yaitu angka 5 dimana dimulai dari 5 lalu lanjut 10, 15 dst,
# angka 100 di parameter kedua adalah jumlah pengulangannya, dan
# Angka 5 di parameter ketiga adalah jumlah tambahnya jadi setiap pengulangan angkanya akan ditambah 5   
for i in range(5,100,5):
    print(i)

# Pengulangan dilakukan sebanyak 10 kali namun menggunakan perinta i+=1 jadi program akan dimulai dari angka 1 hingga 10
for i in range(10):
    i += 1
    print(i)

# Pengulangan di gabungkan dengan string
for item in range(10):
    print("Pengulangan Ke ", item)
    
# Mencari nilai 15
for item in range(30):

    # JIka kondisi pengulangan item 15 maka dia akan menampilkan pesan ditemukan
    if item == 15:
        print("Nilai 15 Ditemukan")
        
    print("Pengulangan Ke : ", item)
    

# Memberhentikan Program
for item in range(30):

    # JIka pengulangan item sudah menemukan angka 15 maka program akan diberhentikan dan perintah selanjutnya tidak akan dieksekusi
    if item == 15:
        print("Nilai 15 Ditemukan")
        break

    print("Pengulangan Ke : ", item)

# PEngulangan sebanyak 30x 
for item in range(30):

    # JIka nilai 15 ditemukan maka program akan membaca ke atas lagi dan perintah selanjutnya tidak akan di eksekusi maka output cek tidak akan di tampilkan dan lanjut ke pengulangan selanjutnya
    if item == 15:
        print("Nilai 15 Ditemukan")
        continue
        print("cek")

    print("Pengulangan Ke : ", item)

for item in range(30):

    # JIka nilai 15 ditemukan maka program akan tetap membaca perintah selanjutnya dan perintah selanjutnya tetap akan di eksekusi maka output cek akan di tampilkan dan lanjut ke perintah selanjutnya, sama seperti tidak menggunakan perintah apapun
    if item == 15:
        print("Nilai 15 Ditemukan")
        pass

    print("Pengulangan Ke : ", item)

# Pengulangan dengan data yang sudah ada
# Contoh list variable data adalah data yang sudah diambil dari database 
data = ['a','b','c','d','e']

# Lalu program akan melakukan pengulangan sebanyak jumlah yang ada pada variable data dan akan menghasilkan output satu persatu yang ada pada data
for i in data:
    print(i)



# Pengulangan While
# Hati-hati jika menggunakan while jika tidak diberi kondisi berhenti maka program akan berjalan terus
# Berikut contoh pengulangan tanpa henti
while True:
    print("Cek Gan")


# Untuk mengatasinya kita harus membuat perintah break atau hentikan program contohnya seperti ini

# Buat variable pertama terlebih dahulu
nilai = 0

# Lakukan pengulangan While
while True:
    
    # Variable Nilai, nilainya akan ditambah 1 selama melakukan pengulangan
    nilai += 1
    print(nilai)

    # Jika nilainya sama dengan (==) 10 maka program akan diberhentikan
    if nilai == 10:
        break

      
# Contoh While lainnya menggunakan While continue  
nilai = 0

while True:

    nilai += 1
    print(nilai)

    if nilai == 10:
        print("Nilai 10 ditemukan")
        continue
    elif nilai > 15:
        break

# Pengulangan Menggunakan fungsi yang memanggil fungsinya sendiri - Tidak terlalu digunakan hanya contoh
def cekNilai(nilai):
    if nilai < 10:
        nilai += 1
        print(nilai)
        cekNilai(nilai)

cekNilai(1)
