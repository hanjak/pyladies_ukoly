from random import randint
hrac1 = randint (1,6)
pocet_hodu_hrac1 = 1
while hrac1 !=6:
    print ("hod hrace 1 je", hrac1)
    pocet_hodu_hrac1 = pocet_hodu_hrac1 + 1
    hrac1 = randint (1,6)
print (pocet_hodu_hrac1)

hrac2 = randint (1,6)
pocet_hodu_hrac2 = 1
while hrac2 !=6:
    print ("hod hrace 2 je", hrac2)
    pocet_hodu_hrac2 = pocet_hodu_hrac2 + 1
    hrac2 = randint (1,6)
print (pocet_hodu_hrac2)

hrac3 = randint (1,6)
pocet_hodu_hrac3 = 1
while hrac3 !=6:
    print ("hod hrace 3 je", hrac3)
    pocet_hodu_hrac3 = pocet_hodu_hrac3 + 1
    hrac3 = randint (1,6)
print (pocet_hodu_hrac3)

print (min (pocet_hodu_hrac1,pocet_hodu_hrac2, pocet_hodu_hrac3))
