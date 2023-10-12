## Global dan local scope
nama_global = "otong" # <- ini variabel global

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")
    
fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")
    
# percabangan
if True:
    print(f" if menampilkan {nama_global}")
    
## variabel local scope

def fungsi2():
    nama_local = "otong" # <- variable local scope

fungsi2()
# peint(nama_local) #tidak bisa dilakukan

## contoh 1: penggunaan
def say_chel():
    print(f"Hello {nama}")

nama = "Achel"
say_chel()

## contoh 2: merubah variabel global
angka = 0
name = "Achel"
def ubah(nilai_baru,nama_baru):
    global angka # fungsi ini mendapat akses merubah angka
    global name
    angka = nilai_baru
    name = nama_baru
    
print(f"sebelum {angka,name}")
ubah(10,"yola")
print(f"sesudah {angka,name}")

## contoh 3
angka = 0 

for i in range(0,5):
    angka += i
    angka_dummy = 0
    
print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10
    
print(angka)
print(angka_dummy)
