    
def harga_diskon(PRICE,DISCOUNT):
    jumlah_diskon =(DISCOUNT/100) * PRICE
    harga = PRICE-jumlah_diskon
    return harga
discount = float(input("masukan discount: "))
harga_asli = float(input("Harga : "))
diskon_harga = harga_diskon(harga_asli,discount)
print(f"harga setelah diskon = {diskon_harga} ")
print(f"DISCOUNT = {discount}%") 