'''*args'''

# memasukan data / argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi("ucup",175,74)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi(["otong",170,65])

#  *ARGS
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi("rey",176,71)

# studi kasus
def tambah(*data):
    # data tipenya adalah tuple, dia bisa di literasi
    output = 0
    for angka in data:
        output += angka
        
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(10,10,10,5)
print(f"hasil = {hasil}")
