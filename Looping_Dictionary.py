# looping dictionary

teman_teman = {
    "cup":"cupcupcucucpucp",
    "tong":"tongtongtongtong",
    "dung":"dungdungdungdung",
    "sep":"sepsepsepsepsep",
    "cuy":"cuycuycuycuycucy"
}

# looping first try

for teman in teman_teman:
    print(teman)
    
    
# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))
    
values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)
    
items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)
    
for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")
    
