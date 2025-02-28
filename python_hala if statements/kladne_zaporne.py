cislo = input("Zadejte cislo: ")
cislo = int(cislo)
print("Cislo je: " + str(cislo))
if cislo > 1:
    print("Cislo je kladne")
elif cislo < 1:
    print("Cislo je zaporne")
else:
    print("cislo je nula")
konec = input("pro vypnuti stiskni libovolnou klavesu...")
