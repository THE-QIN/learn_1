## operasi

#index  0(-3)    1(-2)   2(-1)
data = ["astep","xoan","zeus",]

#menggambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_trakhir = data[-1]
print(f"data terakhir adalah = {data_trakhir}")

data_astep = data[-3]
print(f"data astep = {data_astep}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## manipulasi data list

#menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"playhouse")
print(f"data sesudah di tambah = \n{data}")

# menambah di akhir list\
data.append("THE NINE")
print(f"data ditambah lagi = \n{data}")

#menambah list dengan list 
data_baru = ["Bacardi","gordon","singleton","bombay shapire"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

#merubah data
#kita ubah data 3 menjadi odete
data[2] = "Odete"
print(f"data rubah = \n{data}")

# meremove data 
data.remove("bombay shapire")
print(f"data removce = \n{data}")
# data.remove("bacardi") akan eror karena huruf harus sesuai yaitu "Bacardi"

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")

print(data_akhir)