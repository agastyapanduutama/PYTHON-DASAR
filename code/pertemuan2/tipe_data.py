
"""
Dokumentasi Tipe Data 

Tipe data adalah suatu media atau memori pada komputer yang digunakan untuk menampung informasi.

Tipe data yang ada pada python yaitu : 
-Boolean : nilainya hanya ada 2 yaitu True atau 1 dan False atau 0
-String : Menyatakan kalimat bisa berupa huruf, angka, simbol dll contohnya saat kita print 
-Integer (int) : Nilai yang menyatakan bilangan bulat contohnya angka 10 maka itu memiliki tipe int
-Float : nilai yang memiliki bilangan koma namun jika di pemrograman menggunakan titik(.) contohnya 10.9
-Hexadecimal : Menyatakan bilangan dalam format heksa (bilangan berbasis 16)
-Complex : Menyatakan pasangan angka real dan imajiner
-List Data : untaian yang menyimpan berbagai tipe data dan isinya bisa diubah-ubah mirip seperti array
-Tuple Data : untaian yang menyimpan berbagai tipe data tapi isinya tidak bisa diubah
-Dictionary : Data untaian yang menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai datanya mirip seperti JSON

Referensi : 
https://www.w3schools.com/python/python_datatypes.asp
https://belajarpython.com/tutorial/tipe-data-python
"""

# Nilai Integer
print("---------INT--------")
nilai_int = 9
print("Nilai int :", nilai_int, " Type datanya :", type(nilai_int))

print("---------STRING--------")
nilai_string = "Udin"
print("Nilai  :", nilai_string, " Type datanya :", type(nilai_string))


print("---------BOOLEAN--------")
nilai_boolean = True
print("Nilai  :", nilai_boolean, " Type datanya :", type(nilai_boolean))


print("---------FLOAT--------")
nilai_float = 9.5
print("Nilai  :", nilai_float, " Type datanya :", type(nilai_float))


# TIdak dibahas namun jika ingin dipelajari silakan 
print("---------COMPLEX--------")
x = complex(1j)
print(type(x))

print("---------LIST--------")
x = list(("apple", "banana", "cherry"))
print(type(x))

print("---------TUPLE--------")
x = tuple(("apple", "banana", "cherry"))
print(type(x)) 

print("---------DICTIONARY--------")
biodata = {"nama":"Andi", 'umur':21} 
print(type(biodata))
