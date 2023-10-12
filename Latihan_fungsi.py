'''Latihan fungsi'''

import os

# program menghitung luas dan keliling persegi panjang 

# Membuat header program
# while True:
#     os.system("cls")
#     print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
#     print(f"{'DAN LUAS PERSEGI PANJANG':^40}")
#     print(f"{'-'*40:^40}")

#     # mengambil input use
#     LEBAR = int(input("Masukan nilai lebar :"))
#     PANJANG = int(input("Masukan nilai panjang :")) 

#     # program menghitung luas 
#     LUAS = PANJANG*LEBAR
#     KELILING = 2*(PANJANG*LEBAR)

#     # hasil
#     print(f"Hasil perhitungan luas = {LUAS}")
#     print(f"Hasil perhitungan keliling = {KELILING}")


def header():
    '''fungsi Header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN LUAS PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
        # mengambil input use
    lebar = int(input("Masukan nilai lebar :"))
    panjang = int(input("Masukan nilai panjang :")) 

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)

def display(massage,value):
    '''fungsi display'''
    print(f"Hasil perhitungan {massage} = {value}")
    
    
# program utamanya
while True:
    header()
    opsi = input("pilih satu untuk luas: ")
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)
    
    print(f"luas",LUAS)
    print(f"keliling",KELILING)
    
    
    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print("Program Selesai, Thank you")