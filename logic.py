# Operasi logika (boolean) digunakan untuk menggabungkan pernyataan kondisional
# not, or, and, xor,

# NOT
NOT = "NOT".center(10,":")
print("'"+NOT+"'")
a = True
c = not a
print('data a =',a)
print('-------NOT')

# OR (jika salah satu true, maka hasilnya adalah true)
OR = "OR".center(10,":")
print("'"+OR+"'")
a = False
b = False
c = a or b
print(a, 'OR' ,b,'=',c)
a = True
b = False
c = a or b
print(a, ' OR' ,b,'=',c)
a = False
b = True
c = a or b
print(a, 'OR' ,b,' =',c)
a = True
b = True
c = a or b
print(a,  ' OR' ,b,' =',c)

# AND (jika nilai dua buah true, maka hasilnya true)
AND = "AND".center(10,":")
print("'"+AND+"'")
a = False
b = False
c = a and b
print(a, 'AND' ,b,'=',c)
a = True
b = False
c = a and b
print(a, ' AND' ,b,'=',c)
a = False
b = True
c = a and b
print(a, 'AND' ,b,' =',c)
a = True
b = True
c = a and b
print(a,  ' AND' ,b,' =',c)

# XOR (akan true jika salah satu true ,sisanya false)
XOR = "XOR".center(10,":")
print("'"+XOR+"'")
a = False
b = False
c = a ^ b
print(a, 'xor' ,b,'=',c)
a = True
b = False
c = a ^ b
print(a, ' xor' ,b,'=',c)
a = False
b = True
c = a ^ b
print(a, 'xor' ,b,' =',c)
a = True
b = True
c = a ^ b
print(a,  ' xor' ,b,' =',c)
