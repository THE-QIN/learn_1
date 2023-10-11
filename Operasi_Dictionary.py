# Operator dictionary

data_dict = {
    "boy":"boywiliam",
    "j":"ijis",
    "k":"ksksosj"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}") 

# mengecek KEY exist atau tidak 
KEY = "boy"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["boy"])
print(data_dict.get("boy"))
print(data_dict.get("kfc"))
print(data_dict.get("kfc","KEY tidak ditemukan !!!")) # cek key dengan massage tidak di temukan

# mengupdate data 
data_dict["boy"] = "boy THE hack"
print(data_dict)
data_dict["wtf"] = "just kids"
print(data_dict)

data_dict.update({"boy":"handsome"})
print(data_dict)
data_dict.update({"reynand":"goodjob"})
print(data_dict)

# mendelete data pada dictionary
del data_dict["wtf"]
print(data_dict)