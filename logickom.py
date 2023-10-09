# logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3--------10+++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# ++++++3-----------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 =", isKurangDari)

#----------------10+++++++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari 10 =", isLebihDari)

# ++++++3--------10+++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)

#------------3++++++++++10-----------
#  kasus irisan

inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari dari 10\n:"))

#------3++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

#++++++10-----------
IsKurangDari = inputUser < 10
print("KurangDari 10 = ", isKurangDari)

#------3++++++10------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan: ", isCorrect)

#soal
#------0++++++5------8++++++11------
GABUNGAN = "GABUNGAN".center(10,":")
print("'"+GABUNGAN+"'")
InputData = float(input("Masukkan Data : "))

Angka1 = (InputData >= 0 and InputData <= 5)
print(Angka1)

Angka2 = (InputData >= 8 and InputData <= 11)
print(Angka2)

Hasilnya = Angka1 or Angka2
print("Answer :",Hasilnya)

#+++++++0------5++++++8-----11++++++
IRISAN = "IRISAN".center(10,":")
print("'"+IRISAN+"'")
InputData = float(input("Masukkan Data : "))

Angka1 = (InputData <= 0 or InputData >= 5)
print(Angka1)

Angka2 = (InputData <= 8 or InputData >= 11)
print(Angka2)

Hasilnya = Angka1 and Angka2
print("Answer :",Hasilnya)
