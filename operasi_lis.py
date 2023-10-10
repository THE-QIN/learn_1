data_angka = [1,2,3,4,5,6,7,8,]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data =  ["astep","xoan","zeus","playhouse"]

print(f"data = {data}")

index_zeus = data.index("zeus")
index_astep = data.index("astep")
print(f"index si zeus = {index_zeus}")
print(f"index si astep = {index_astep}")  

#mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort= \n{data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")