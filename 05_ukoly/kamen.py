from random import randrange
nahodne_cislo =  randrange (3)
tah_hrac = input ("zadej 'kamen', 'nuzky' nebo 'papir':")
while tah_hrac != "konec":
    while (tah_hrac != "kamen") and (tah_hrac != "nuzky") and (tah_hrac != "papir") and (tah_hrac != "konec"):
        print ("sptane zadane, zkuste znova")
        tah_hrac = input ("zadej 'kamen', 'nuzky' nebo 'papir':")




#prirazeni kamen, nuzky nebo papir promenne tah_pocitac pomoci nahodneho cisla
    if nahodne_cislo == 0:
        tah_pocitac = "kamen"
    elif nahodne_cislo == 1:
        tah_pocitac = "nuzky"
    elif nahodne_cislo == 2:
        tah_pocitac = "papir"
    else:
        print ("chyba v urceni nahodneho cisla")
        print ("pocitac vybral", tah_pocitac)

    if ((tah_pocitac == "kamen" and tah_hrac == "nuzky") or (tah_pocitac == "nuzky"\
        and tah_hrac == "papir") or (tah_pocitac == "papir" and tah_hrac == "kamen")):
        print ("prohrals")
    elif ((tah_pocitac == "kamen" and tah_hrac == "papir") or (tah_pocitac == "nuzky" and tah_hrac == "kamen") or (tah_pocitac == "papir" and tah_hrac == "nuzky")):
        print ("vyhrals")

    elif ((tah_pocitac == "kamen" and tah_hrac == "kamen") or (tah_pocitac == "nuzky" and tah_hrac == "nuzky") or (tah_pocitac == "papir" and tah_hrac == "papir")):
        print ("plichta")

    tah_hrac = input ("zadej 'kamen', 'nuzky' nebo 'papir':")
print ("konec hry")


print ("diky za hru")
