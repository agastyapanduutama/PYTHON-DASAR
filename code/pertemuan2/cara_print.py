# Cara ngeprint 
# Tipe-tipe cara print nilai

# deklarasi contoh variable
nilaiPrint = 10

# Menggunakan koma setelah string
print("Metode 1 print Nilai : ", nilaiPrint)

# Mengkombinasikan string dengan concat + namun nilai harus di konversikan ke string dengan perintah str(nama_variable)
print("Metode 2 print Nilai : " + str(nilaiPrint))

# Menggunakan Format
print("Metode 3 print Nilai : {} ".format(nilaiPrint))

# Metode yang biasa saya gunakan karena mudah di baca namun didepannya harus ditambahkan f 
print(f"Metode 4 print Nilai : {nilaiPrint}")

# 
print("Metodr 5 Print Nilai : %d" % nilaiPrint)