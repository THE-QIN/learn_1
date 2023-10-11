# looping dari list

# for loop
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")
    
peserta = ["reynand","bagus","brian","erik"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dengan range
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka) 
for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")
    
# while
print("\nwhile loop")
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka) 
i = 0

while i < panjang:
    print(f"angka")
    i += 1
    
# list comprehension
print("list comprehension")
data = ["alex",1,2,3,"bruno"]

[print(f"data={i}") for i in data]

angka = [10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nEnumerate")
data_list = ["alex",1,2,3,"bruno"]

for index,data in enumerate(data_list):
    print(f"index = {index},data = {data}")
    