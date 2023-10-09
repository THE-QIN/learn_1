#x = "Hello World"	#str	
#x = 20	            #int	
#x = 20.5	        #float	
#x = 1j	            #complex	
#x = ["apple", "banana", "cherry"]	#list	
#x = ("apple", "banana", "cherry")	#tuple	
#x = range(6)	range	
#x = {"name" : "John", "age" : 36}	#dict	
#x = {"apple", "banana", "cherry"}	#set	
#x = frozenset({"apple", "banana", "cherry"})	#frozenset	
#x = True	                #bool	
#x = b"Hello"	            #bytes	
#x = bytearray(5)	        #bytearray	
#x = memoryview(bytes(5))	#memoryview	
#x = None	                #NoneType	


# a = 10, a adalah veriable dengan nilai 10

#type data : Angka satuan (integer)
data_integer = 1000000
print("data : ", data_integer)
print("_ bertype : ", type(data_integer))

#tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("_ bertype : ", type(data_float))


#tipe data: kumpulan karakter(string)
data_string = "ucup"
print("data : ", data_string)
print("_ bertype : ", type(data_string))

#tipe data: biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("_ bertype : ", type(data_bool))

##type data khusus

#data kompleks
data_complex = complex(5.6)
print("data : ", data_complex)
print("_ bertype : ", type(data_complex))

#tipe data dari bahasa C

from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data : :", data_c_double)
print("_ bertipe : ", type(data_c_double))