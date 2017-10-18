print ("odpovidej ano/ne!")

stastna = input ("jsi stastna?")
bohata = input ("jsi bohata?")


stastna = (stastna.lstrip ()).lower()
bohata = (bohata.lstrip ()).lower()


# pomoci vnorenych if
if stastna == "ano" or stastna =="a":
    if bohata == "ano" or bohata == "a":
        print ("jsi stastna a bohata")
    elif bohata == "ne" or bohata =="n":
        print ("jsi stastna a chuda")
elif stastna == "ne"  or bohata == "n":
    if bohata == "ano" or bohata == "a":
        print ("jsi nestastna a bohata")
    elif bohata == "ne" or bohata == "n":
        print ("to je teda smula")
else:
    print("nerozumim")
    exit ()

print ("diky za analyzu")
