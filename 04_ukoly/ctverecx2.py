pocet_radku = 5
pocet_sloupcu = 6
for radek in range (pocet_radku):
    if radek == 0 or radek == (pocet_radku-1):
        for sloupec in range (pocet_sloupcu):
            print ("X", end = " ")
        print ()
    else:
        print ("X",(pocet_radku-2)*"  ","X")
