

def tah (pole,cislo_policka,symbol):
    "funkce ktera dostane retezec s hernim polem 1d piskoverk, cislo policka a symbol a vrati herni pole s danym symbolem umistenym na danou pozici"
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]


hra1 = "x-xxxxxxxxxxxxxxxxxxxxx"



def tah_hrace (pole):
    "funkce ktera se zepta na tah hrace"
    cislo_policka = int (input ("zadej cislo policka od 1 do 20: "))
    symbol = input ("zadej symbol x nebo o: ")
    return (tah (pole, cislo_policka-1, symbol))


symbol_pocitace = "o"
def tah_pocitace (pole):
    from random import randint
    cislo_policka = randint (1,19)
    symbol = symbol_pocitace
    while (pole[cislo_policka-1]) != "-":
        cislo_policka = randint (1,19)
    return (tah (pole, cislo_policka-1,symbol_pocitace))

print (tah_pocitace (hra1))
"""from random import randint
cislo_policka = randint (1,19)
print (hra1[cislo_policka-1])"""
