# operasi yang dapat dilakukan dengan penyingkatan
# operasi di tambah dengan assignment

a = 5 # adalah assigment
ASSIGMENT = "ASSIGMENT".center(10,":")
print("'"+ASSIGMENT+"'")
print("nilai a =", a)

a += 1 # artinya : a = a + 1 
print("nilai a =+ 1, nilai a menjadi",a)

a -= 2 # artinya : a = a - 2
print("nilai a -= 2, nilai a menjadi",a)

a *= 5 # artinya : a = a * 5 
print("nilai a *= 5, nilai a menjadi",a)

a /= 2  # artinya : a = a /= 5 
print("nilai a /= 2, nilai a menjadi",a)

b = 10 
print("\nnilai b =",b)

# modulus dan floor division 
b %= 3
print("nilai b %= 3, nilai b menjadi",b)

b = 10 
print("\nnilai b =",b)

b //= 3
print("nilai b //= 3, nilai b menjadi",b)

#pangkat atau exsponen
b = 5
print("\nnilai a =",a)
b **= 3
print("nilai a //= 3, nilai a menjadi",b)


# operasi bitwise 
# OR 
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= false, nilai c menjadi",c)
c = False
print("nilai c =",c)
c |= False
print("nilai c |= false, nilai c menjadi",c)

# AND 
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= false, nilai c menjadi",c)
c = True
print("nilai c =",c)
c &= True
print("nilai c &= true, nilai c menjadi",c)

# XOR 
c = True
print("\nnilai c =",c)
c ^= False
print("nilai c ^= false, nilai c menjadi",c)
c = True
print("nilai c =",c)
c ^= True
print("nilai c ^= true, nilai c menjadi",c)
 

# geser geser
d = 0b0100
print("\nnilai d =",format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi",format(d,'04b'))
d <<= 1
print("nilai d <<= 1, nilai d menjadi",format(d,'04b'))