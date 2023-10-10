## teknik menduplikat list
a = ["mobil","motor","sepeda"]
print(f"item_list = {a}")

b = a
print(f"item_list = {b}")

# merubah member dari a 
# akan merubah kedua list
a[0] = "supercar"
b.sort()
print(f"item_list = {a}")
print(f"item_list = {b}")

# addres dari kedua list a dan b
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")

# menduplikat list dengan copy
print("membuat list c dengan a.copy()")
c = a.copy()
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")
print(f"addres c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "estetic house"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

a[1] = "money"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
