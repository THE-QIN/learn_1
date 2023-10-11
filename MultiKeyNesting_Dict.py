import datetime

mahasiswa1 = {
    'nama':'Hotman',
    'nim':'1928649817',
    'sks_lulus':125,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,10,10)
    }

mahasiswa2 = {
    'nama':'Andreas',
    'nim':'187819373',
    'sks_lulus':118,
    'beasiswa':True,
    'lahir':datetime.datetime(2000,8,10)
    }

mahasiswa3 = {
    'nama':'Annisa',
    'nim':'17983809',
    'sks_lulus':125,
    'beasiswa':False,
    'lahir':datetime.datetime(2003,2,15)
    }

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}
print(f"{'KEY':<6} {'nama':^17} {'SKS':<3}  {'beasiswa':^9}  {'lahir':<10}")
print("-"*45)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    
    print(f"{KEY:<6} {NAMA:^17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
print("-"*45) 