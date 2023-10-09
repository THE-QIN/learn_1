# latihan prulangan membuat lingkaran

# L = Luas lingkaran

# π = 3,14 atau 22/7

# r = jari-jari lingkaran

# segitiga

sisi = 35
# 1.menggunakan for

#dumy variable 
# print("awal for")
# count = 1 
# for i in range(sisi):
#     print("*"*count)
#     count += 1
    
# print("akhir for")
# # 2.menggunakan while

# print('awal while')
# count = 1
# while True:
#     print("*"*count)
#     count += 1
    
#     if count > sisi:
#         break
# print("akhir while")

# # 3.hanya ganjil saja

# print('awal while')
# count = 1
# while True:

#     if (count%2):
#         #print jika ganjil
#         print("*"*count)
#         count += 1
#     else:
#         # akan kembali ke atas jika ganjil
#         count += 1
#         continue

#     #akan break jika count melebihi sisi
#     if count > sisi:
#         break
# print("akhir while")    


# 4.segitiga

print('awal while')
count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        #print jika ganjil
        print(" "*spasi,"O"*count)
        spasi -= 1
        count += 1
    
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    #akan break jika count melebihi sisi
    if count > sisi:
        break
print("akhir while")    

# 5.lingkaran

import turtle 
    
t = turtle.Turtle() 
  
# radius for smallest circle 
r = 10
  
# number of circles 
n = 10
  
# loop for printing tangent circles 
for i in range(1, n + 1, 1): 
    t.circle(r * i) 