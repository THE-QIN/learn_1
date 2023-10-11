# copy dictionary
teman_teman = {
    "Atta":"si paling gym",
    "Brian":"pramuniaga",
    "Obbi":"sedang kuliah",
    "Hudan":"vespa brokk",
    "Edo":"sok keras"
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["Edo"]="penuh inspirasi"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataAtta = friends.pop("Atta")
print(f"data Atta ={dataAtta}\n")
print(f"friend = {friends}\n")

# popitem dictionary (yang trakhir saja)
DataTrakhir = friends.popitem()
print(f"data trakhir = {DataTrakhir}\n")
print(f"friends = {friends}\n")

