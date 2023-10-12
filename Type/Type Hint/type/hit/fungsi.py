'''Type Hint untuk fungsi'''

# bentuk standar fungsi
'''
studi kasus
def fungsi (parameter):
    hasil = parameter**2
    print(hasil)
    
fungsi(1)
fungsi("boy")
fungsi(true)
'''

# penggunaan type hints
import string

def sepuluh_pangkat(argument:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(4)
print(HASIL)

def display(argument:string):
    print(argument)
    
display("Reynand")

