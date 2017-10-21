

"""definice tahu"""
def tah (pole,cislo_policka,symbol):
    "funkce ktera dostane retezec s hernim polem 1d piskoverk, \
    cislo policka a symbol a vrati herni pole s danym symbolem\
     umistenym na danou pozici"
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]


pocet_policek = 20
hra = pocet_policek * "-"
def tah_hrace (pole):
    "funkce ktera se zepta na tah hrace"
    cislo_policka = "chyba"
    while cislo_policka == "chyba":
        cislo_policka =input ("zadej cislo policka od 1 do 20: ")
        try :
            cislo_policka = int (cislo_policka)
            if ((cislo_policka) < 1) or ((cislo_policka) > 20):
                print ("spatne zadane cislo policka, musi byt od 1 do 20!")
                cislo_policka = "chyba"
            elif ((pole[cislo_policka-1]) != "-"):
                print ("policko je jiz obsazene!")
                cislo_policka = "chyba"
        except ValueError:
            print ("to neni cislo!")
            cislo_policka = "chyba"
    hra = tah (pole, cislo_policka-1, "o")
    return hra

print (tah_hrace(hra))
