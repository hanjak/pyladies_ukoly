
hra = "--o-o----------------"
def tah (pole,cislo_policka,symbol):
    "funkce ktera dostane retezec s hernim polem 1d piskoverk, \
    cislo policka a symbol a vrati herni pole s danym symbolem\
     umistenym na danou pozici"
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def tah_hrace (pole):
    "funkce ktera se zepta na tah hrace"
    cislo_policka = int (input ("zadej cislo policka od 1 do 20: "))
        #jeste dodelat kontrolu zda jde o cislo
    while ((cislo_policka) < 1) or ((cislo_policka) > 20):
        print ("spatne zadane cislo policka, musi byt od 1 do 20!")
        cislo_policka = int (input ("zadej cislo policka od 1 do 20: "))
    while ((pole[cislo_policka-1]) != "-"):
        print ("policko je jiz obsazene!")
        cislo_policka = int (input ("zadej cislo policka od 1 do 20: "))
    hra = tah (pole, cislo_policka-1, "o")
    return hra


pocet_policek = 20
hra = "--------------------"
print (hra)
print (tah_hrace (hra))
