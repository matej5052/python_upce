
cislo = input("Zadejte cislo: ")
cislo = int(cislo)
print("Cislo je: " + str(cislo))

if cislo % 6 == 0:
    print("cislo je delitelne 6")
elif cislo % 2 == 0:
    print("cislo je delitelne 2")
elif cislo % 3 == 0:
    print("cislo je delitelne 3")
else:
    print("cislo neni delitelne 2, 3 ani 6")

konec = input("pro vypnuti stiskni libovolnou klavesu...")