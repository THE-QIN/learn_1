# operasi manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Reynand"
nama_kedua = "D"
nama_akhir = "HUGOS"

nama_lengkap = nama_pertama + " " +  nama_kedua + "'" + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))


# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))


D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " Tidak ada di " + nama_lengkap + " = " + str(status))


# mengulang string
print("wk"*10)
print(10*"wk")


# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1): " + nama_lengkap[-1])
print("index ke-(-2): " + nama_lengkap[-2])
print("index ke-[0:2]: " + nama_lengkap[0:4])
print("index ke-[3:7]: " + nama_lengkap[3:3])
print("index ke-[0,2,4,6,8,10]:" + nama_lengkap[0:11:2])


#item kecil
print("paling kecil : " + min(nama_lengkap))
#item besar
print("paling besar : " + max(nama_lengkap))


ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

#operator dalam bentuk method

data ="bola bolu boololo"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))



## Operator dalam bentuk methods
## Merubah case dari string
## Merubah semua ke upper case 

salam = "broo!"    
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# Merubah semua ke lower case
keren = "aku pasti biiiiissssaaaaa"
print("normal =" + keren)
keren = keren.lower()
print("lower =" + keren)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "cuyy"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower =" + str(apakah_lower))
apakah_lower = salam.isupper() # hasilnya bool
print(salam + " is upper =" + str(apakah_lower))

# isalpha() <-- untuk mengecek jika semuanya huruf
# isalnum() <-- untuk mengecek huruh dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab ,newline \n
# istittle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool

print(judul + " is tittle = " + str(cek_judul)) 
    
# mengecek komponen startswith() endswith() <--nice
cek_start = "sangjangnim Oppa". startswith("sangjangnim")
print("start = " + str(cek_start))
cek_end = "sangjangnim Oppa". endswith("sangjangnim")
print("end = " + str(cek_end))  

## penggabungan komponen join() split()
pisah = ['aku','pasti','bisa']
gabungan = ',' .join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm ' .join(pisah)
print(gabungan)

gabungan = "akuehmpastiehmbisa"
print(gabungan.split('ehm'))


#alokasi karakter
print(5*"=" + "data" + "="*5)
# atau
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,":")
print("'"+tengah+"'")

#kebalikannya -> strip()
kanan = kanan.strip(":")
print("'"+kanan+"'")

tengah = tengah.strip(":") #menghilangkan tanda(:)
print("'"+tengah+"'")
