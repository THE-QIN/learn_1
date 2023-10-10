## ____LIST_____

# KUMPULAN DATA NUMBERS
data_angka = [1,2,3,4,5]
print(data_angka)

#kumpulan data string
data_string = ["anggur,apel,durian"]
print(data_string)

#kumpulan data boolean
data_boolean = [True,False,True,True]
print(data_boolean)

#kumpulan data campuran
data_campuran =[1,"smartphone",2,"computer","THE_QIN",True,"IBOX",False]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
data_list_pakai_for = [i**3 for i in range(0,10)]
print(data_list_pakai_for)

# membuat list dengan for pakai if
list_pakai_for_if = [i for i in range(0,10) if i != 5]
print(list_pakai_for_if)


list_pakai_for_if = [i for i in range(0,10) if i%2 == 0] #genap
print(list_pakai_for_if)

list_pakai_for_if = [i for i in range(0,10) if i%2 != 0] #ganjil
print(list_pakai_for_if)
