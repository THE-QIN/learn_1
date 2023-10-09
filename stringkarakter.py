 # STRING (KUMPULAN DARI KARAKTER)

data = "this is string"
print(data)
print(type (data))

# 1. cara membuat string

'''
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
'''
data = 'menggunakan single quote'

print(data)
data = "menggunakan double quote"
print(data)

#digabungkan
print('"hallo apa kabar?"') #double
print("'hallo apa kabar'") #single
print("sekarang hari jum'at")

# 2.menggunakan tanda (\) membuat tanda ini menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\it?')

#blacklash (\\)
print("c:\\user\\ucup")

#tab 
print("ball\t\t\tplayers") #jarak semakin jauh

#backspace
print("ball\bplayers") #jarak jadi dekat

#new line
print("baris pertama.\nbaris kedua.") #LF -> line feed
print("baris pertama\rbaris kedua.") # CR -> carriage return -> commodore, acorn,lips   
print("baris pertama\r\nbaris kedua.")# CRLF -> line feed  cariagge return -> di pakai oleh windows

#string literal / raw
print("====WARNING")
print('c:\new folder') # SALAH
print('c:\\new folder') # BENAR

# menggunakan raw string
print(r'c:\new \t\r\b\\folder')
print(r'c:\new folder')

# multiline literal string 
print("""
Nama : yaqin
from : indonesia
      """)

# multiline literal string and raw
print(r"""
Nama : yaqin
from : indonesia\new programer
wibesite : www.yaqin.com/newID
      """)

