#diskonnya adalah persentase.
#contoh masukan
#harga 1000
#diskon 10
#maka hasilnya adalah 900
#karena 1000*10%
                                  
                                  #contoh soal#

CRAZY_STORE = "THANK YOU ˙ᵕ˙♡ ".center(20," ")
print(" "+CRAZY_STORE +" ")# CRAZY_STORE = "CRAZY STORE".center(20,"-")
print(" "+CRAZY_STORE +" ")

name_item = "BOOK PROGRAMER"
format_str = f" ITEM           = {name_item}"
print(format_str)

price = 1000
format_str = f" PRICE          = {price}.US$"
print(format_str)

discount = 0.10
format_persen = f" DISCOUNT       = {discount:.0%}"
print(format_persen)

price = 1000
discount = 0.10
format_string = f" TOTAL DISCOUNT = {price*discount}.US$"
print(format_string)

price = 900
format_str = f" TOTAL PRICE    = {price}.US$"
print(format_str)
print(
    
)


                                #    contoh
CRAZY_STORE = "CRAZY STORE".center(20,"-")
print(" "+CRAZY_STORE +" ")

def harga_diskon(PRICE,DISCOUNT):
    jumlah_diskon =(DISCOUNT/100) * PRICE
    harga = PRICE-jumlah_diskon
    return harga
discount = float(input("masukan discount: "))
harga_asli = float(input("Harga : "))
diskon_harga = harga_diskon(harga_asli,discount)
print(f"harga setelah diskon = {diskon_harga} ")
print(f"DISCOUNT = {discount}%")


print(

)
CRAZY_STORE = "THANK YOU ˙ᵕ˙♡ ".center(20," ")
print(" "+CRAZY_STORE +" ")




