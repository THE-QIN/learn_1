# fungsi
def fungsi():
    "ini adalah fungsi"
    print("halo")
    print("data 1")
fungsi()
fungsi()

# contoh fungsi dengan argument

'''fungsi dengan argument (input)'''

# Template
# def nama_fungsi(argument)
#     badan fungsi

def hello_wolrd(nama):
    '''fungsi hello_word menerima input dengan variabel nama'''
    print(f"selamat datang di dunia tipu-tipu wahai {nama}")
    
hello_wolrd("Manusia")

# contoh program tambah
def tambah(angka1,angka2):
    '''fungsi tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil} ")

tambah(100,900)

# memasukan list
def data_list(stok_item):
    '''ini adalah fungsi item'''
    list_item = stok_item.copy()
    for item in list_item:
        print(f"Ready = {item}")

name_produk = ["singleton","Bacardi","greygoese"]

data_list(name_produk)        

# Template fungsi dengan kembalian
# def nama_fungsi(argument)
#     badan fungsi
#     return output

def kuadrat(input_angka):
    '''Fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat
y = kuadrat(5)
print(y)

z = 10 + kuadrat(7)
print(z)

# fungsi tambah
def fungsi_tambah(angka_1,angka_2):
    '''fungsi return dengan multi input'''
    return angka_1 + angka_2
a = fungsi_tambah(90,10)
print(a)

# fungsi dengan return banyak
def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    
    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)
print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")