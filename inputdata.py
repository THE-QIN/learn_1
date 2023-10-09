# input data use

#Data yang di masukan pasti string
data = input("Masukan data: ")
print("data = ", data,",type =", type(data))

#jika ingin mengambil data int , maka  
angka_float = float(input("masukan angka: "))
print("data = ", angka_float,",type =", type(angka_float))

angka = int(input("masukan angka: "))
print("data =",angka, ",type =",type(angka))

#bagaimana dengan boolean
biner = bool(int(input("masukan nilai boolean: ")))

print("data = ",biner, ",type =", type(biner))