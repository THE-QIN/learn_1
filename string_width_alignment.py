# width and Multiline

# data
data_nama = "Ainul Yaqin"
data_umur = 21
data_tinggi = 176
data_size_sepatu = 42

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_size_sepatu}"
print(5*"="+"data string"+5*"=")
print(data_string)

# String Multiline (dengan menggunakan enter, new line, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_size_sepatu}"
print("\n"+5*"="+"data string"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_nama = "Yaqin"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_size_sepatu:>5}
"""

print("\n"+5*"="+"data string"+5*"=")
print(data_string)