"""hrac = o
pocitac = x"""



"""definice tahu"""
def tah (pole,cislo_policka,symbol):
    "funkce ktera dostane retezec s hernim polem 1d piskoverk, \
    cislo policka a symbol a vrati herni pole s danym symbolem\
     umistenym na danou pozici"
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]


"""definice tahu pocitace s pouzitim strategie
1) utok pri jasnem vitezstvi v prvnim tahu
2) nutna obrana, pokud by k ni nedoslo hrac by jeho prvnim tahu mohl vyhrat
3)utok pri moznem vitezstvi v druhem tahu
4) nutna obrana, pokud by k ni nedoslo hrac by mohl vyhrat v druhem tahu
"""
def tah_pocitace (pole):
    "funkce, ktera dostane retezec s hernim polem 1d piskvorek, a vyhodnoti\
    a provede nejlepsi mozny ah pocitace"
    """utok pri jasnem vitezstvi v prvnim tahu"""
    if "x-x" in pole:
        poloha = pole.index ("x-x")
        hra = tah (pole,poloha + 1, "x")
        return hra
    elif "-xx" in pole:
        poloha = pole.index ("-xx")
        hra = tah (pole, poloha, "x")
        return hra
    elif "xx-" in pole:
        poloha = pole.index ("xx-")
        hra = tah (pole, poloha + 2, "x")
        return hra
        """ nutna obrana, pokud by k ni nedoslo hrac by jeho prvnim tahem mohl vyhrat"""
    elif "oo-" in pole:
        poloha = pole.index ("oo-")
        hra = tah (pole,poloha + 2, "x")
        return hra
    elif "-oo" in pole:
        poloha = pole.index ("-oo")
        hra = tah (pole, poloha, "x")
        return hra
    elif "o-o" in pole:
        poloha = pole.index ("o-o")
        hra = tah (pole, poloha +1,"x")
        return hra
        """utok pri jasnem vitezstvi ve druhem tahu"""
    elif "--x-" in pole:
        poloha = pole.index ("--x-")
        hra = tah (pole, poloha + 1, "x")
        return hra
    elif "-x--" in pole:
        poloha = pole.index ("-x--")
        hra = tah (pole, poloha + 2, "x")
        return hra
        """nutna obrana, pokud by k ni nedoslo hrac by pri jeho druhem tahu mohl vyhrat"""
    elif "--o-" in pole:
        poloha = pole.index ("--o-")
        hra = tah (pole, poloha +1, "x")
        return hra
    elif "-o--" in pole:
        poloha = pole.index ("-o--")
        hra = tah (pole, poloha +2, "x")
        return hra
        "jinak umistit x vedle jineho x, kde je sance dat tri x vedle sebe"
    elif "--x" in pole:
        poloha = pole.index ("--x")
        hra = tah (pole, poloha + 1, "x")
        return hra
    elif "x--" in pole:
        poloha = pole.index ("x--")
        hra = tah (pole, poloha +1, "x")
        "pokud neni ani jedno uvedene, hraje se nahodne"
        return hra
    else:
        from random import randint
        cislo_policka = randint (1,pocet_policek)
        while (pole[cislo_policka-1]) != "-":
            cislo_policka = randint (1,pocet_policek)
        hra = tah (pole, cislo_policka-1,"x")
        return hra


    """definice tahu hrace"""
def tah_hrace (pole):
    "funkce ktera se zepta na tah hrace"
    cislo_policka = int (input ("zadej cislo policka od 1 do 20: "))
    while ((cislo_policka) < 1) or ((cislo_policka) > 20):
        print ("spatne zadane cislo policka, musi byt od 1 do 20!")
        cislo_policka = int (input ("zadej cislo policka od 1 do 20: "))
    while ((pole[cislo_policka-1]) != "-"):
        print ("policko je jiz obsazene!")
        cislo_policka = int (input ("zadej cislo policka od 1 do 20: "))
    hra = tah (pole, cislo_policka-1, "o")
    return hra

""" definice vyhodnoceni"""
def vyhodnot (pole):
    "vyhodnoti, jak dopadly 1-D piskvorky"
    if "xxx" in pole:
        return ("vyhral pocitac ")
    elif "ooo" in pole:
        return ("vyhral hrac")
    elif "-" in pole:
        return ("hra jeste neskoncila")
    elif "-" not in pole and "ooo" not in pole and "xxx" not in pole:
        return ("remiza")

""" hra"""
pocet_policek = 20
hra = "--------------------"
print (hra)
hra = tah_hrace(hra)
print (hra)
hra = tah_pocitace (hra)
print (hra)
print (vyhodnot (hra))
while vyhodnot (hra) == "hra jeste neskoncila":
    hra = tah_hrace(hra)
    print (hra)
    hra = tah_pocitace (hra)
    print (hra)
    print (vyhodnot (hra))
