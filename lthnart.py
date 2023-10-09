# latihan konversi satuan temperetur

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUREn\n")

CELCIUS = "CELCIUS".center(10,":")
print("'"+CELCIUS+"'")
celcius = float(input('masukan suhu dalam celcius: '))
print("suhu adalah",celcius, "celcius")

#reamur
REAMUR = "REAMUR".center(10,":")
print("'"+REAMUR+"'")
reamur = (4/5) * celcius 
print("suhu dalam reamur adalah",reamur, "Reamur")

#fahrenheit
FAHRENHEIT = "FAHRENHEIT".center(10,":")
print("'"+FAHRENHEIT+"'")
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "fahrenheit")

# kelvin
KELVIN = "KELVIN".center(10,":")
print("'"+KELVIN+"'")
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin, "kelvin")





