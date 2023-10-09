# Oprasi Aritmatika

a = 10
b = 3
 
 
# operasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi pengurangan
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi pembagian
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi modulus %
hasil = a % b
print(a, '%', b, '=', hasil)


# operasi floor devision //
hasil = a // b
print(a, '//', b, '=', hasil)



# prioritas operasi, operational precedence
'''
    1. ()
    2. expone **
    3. perkalian & friends
    4. pertambahan & pengurangan + - 
'''

x = 3 
y = 2 
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**', y, '*' ,z, '+' ,x, '/' ,y, '-' ,y, '&' ,z, '//' ,x, '=' ,hasil)

hasil = x + y * z
print(x, '+' ,y, '*' ,z, '=' ,hasil)

# kurung akan mengambil langkah paling pertama
hasil = (x + y ) * z
print('(',x,'+',y,') *',z, '=', hasil)
