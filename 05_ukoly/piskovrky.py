pole = input("vloz pole o dvaceti polickach: ")

def vyhodnot (pole):
    "vyhodnoti, jak dopadly 1-D piskvorky"
    if "xxx" in pole:
        print ("vyhral x ")
    elif "ooo" in pole:
        print ("vyhral o")
    elif "-" in pole:
        print ("hra jeste neskoncila")
    elif "-" not in pole and "ooo" not in pole and "xxx" not in pole:
        print ("remiza")

vyhodnot (pole)
