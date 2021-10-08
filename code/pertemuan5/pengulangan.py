# Pengulangan

for nilai in range(10):
    print(nilai)

for i in range(5,100,5):
    print(i)

for i in range(10):
    i += 1
    print(i)

for item in range(10):
    print("Pengulangan Ke ", item)
    
for item in range(30):
    if item == 15:
        print("Nilai 15 Ditemukan")
        
    print("Pengulangan Ke : ", item)
    
for item in range(30):
    if item == 15:
        print("Nilai 15 Ditemukan")
        break

    print("Pengulangan Ke : ", item)

for item in range(30):
    if item == 15:
        print("Nilai 15 Ditemukan")

    print("Pengulangan Ke : ", item)

for item in range(30):
    if item == 15:
        print("Nilai 15 Ditemukan")
        continue

    print("Pengulangan Ke : ", item)

for item in range(30):
    if item == 15:
        print("Nilai 15 Ditemukan")
        pass

    print("Pengulangan Ke : ", item)

# While / Pengulangan Tanpa Henti
while True:
    print("Cek Gan")


nilai = 0

while True:
    
    nilai += 1
    print(nilai)

    if nilai == 10:
        break
        
nilai = 0

while True:

    nilai += 1
    print(nilai)

    if nilai == 10:
        print("Nilai 10 ditemukan")
        continue
    elif nilai > 15:
        break


def cekNilai(nilai):
    if nilai < 10:
        nilai += 1
        print(nilai)
        cekNilai(nilai)

cekNilai(1)
