# break

data_int = int(input("hitung sampai = "))


angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang = {angka}")
    
    if angka == 3:
        print("good")
        break # berhenti 
    
    print("lanjut")
print("sudah!")
    