import random
import time

a1 = " "
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "
laatikot = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
nappulat = ["x", "o"]
nappula = random.choice(nappulat)
nappulat.remove(nappula)
bottinappula = nappulat[0]

print("\n\nSinä olet: " + nappula)
print("Botti on: " + bottinappula)
print("\n\n")
print("     1   2   3")
print("    ------------")
print(f"a  | {a1} | {a2} | {a3} |")
print("    ------------")
print(f"b  | {b1} | {b2} | {b3} |")
print("    ------------")
print(f"c  | {c1} | {c2} | {c3} |")
print("    ------------\n\n")

# PELI ALKAA #
while True:
    #Pelaajan syöte
    playerSyöte = input("Anna laatikko: ")
    print("\n")

    if playerSyöte == "a1" and playerSyöte in laatikot:
        a1 = nappula
        laatikot.remove("a1")
    elif playerSyöte == "a2" and playerSyöte in laatikot:
        a2 = nappula
        laatikot.remove("a2")
    elif playerSyöte == "a3" and playerSyöte in laatikot:
        a3 = nappula
        laatikot.remove("a3")
    elif playerSyöte == "b1" and playerSyöte in laatikot:
        b1 = nappula
        laatikot.remove("b1")
    elif playerSyöte == "b2" and playerSyöte in laatikot:
        b2 = nappula
        laatikot.remove("b2")
    elif playerSyöte == "b3" and playerSyöte in laatikot:
        b3 = nappula
        laatikot.remove("b3")
    elif playerSyöte == "c1" and playerSyöte in laatikot:
        c1 = nappula
        laatikot.remove("c1")
    elif playerSyöte == "c2" and playerSyöte in laatikot:
        c2 = nappula
        laatikot.remove("c2")
    elif playerSyöte == "c3" and playerSyöte in laatikot:
        c3 = nappula
        laatikot.remove("c3")
    elif playerSyöte not in laatikot:
        print("VIRHE!!!!!\n\n")
        continue

    time.sleep(0.4)
    print("     1   2   3")
    print("    ------------")
    print(f"a  | {a1} | {a2} | {a3} |")
    print("    ------------")
    print(f"b  | {b1} | {b2} | {b3} |" + "     <--- SINÄ LAITOIT")
    print("    ------------")
    print(f"c  | {c1} | {c2} | {c3} |")
    print("    ------------\n\n")

    
    if a1 == nappula and a2 == nappula and a3 == nappula:
        print("VOITIT PELIN!!!!!!!!!!!!!!!!!!!\n\n")
        break
    elif b1 == nappula and b2 == nappula and b3 == nappula:
        print("VOITIT PELIN!!!!!!!!!!!!!!!!!!!\n\n")
        break
    elif c1 == nappula and c2 == nappula and c3 == nappula:
        print("VOITIT PELIN!!!!!!!!!!!!!!!!!!!\n\n")
        break
    elif a1 == nappula and b1 == nappula and c1 == nappula:
        print("VOITIT PELIN!!!!!!!!!!!!!!!!!!!\n\n")
        break
    elif a2 == nappula and b2 == nappula and c2 == nappula:
        print("VOITIT PELIN!!!!!!!!!!!!!!!!!!!\n\n")
        break
    elif a3 == nappula and b3 == nappula and c3 == nappula:
        print("VOITIT PELIN!!!!!!!!!!!!!!!!!!!\n\n")
        break
    elif a1 == nappula and b2 == nappula and c3 == nappula:
        print("VOITIT PELIN!!!!!!!!!!!!!!!!!!!\n\n")
        break
    elif a3 == nappula and b2 == nappula and c1 == nappula:
        print("VOITIT PELIN!!!!!!!!!!!!!!!!!!!\n\n")
        break
    if not laatikot:
        print("TASAPELI...SAATANA...\n\n")
        break


    bottiSyöte = random.choice(laatikot)

    if bottiSyöte == "a1" and bottiSyöte in laatikot:
        a1 = bottinappula
        laatikot.remove("a1")
    elif bottiSyöte == "a2" and bottiSyöte in laatikot:
        a2 = bottinappula
        laatikot.remove("a2")
    elif bottiSyöte == "a3" and bottiSyöte in laatikot:
        a3 = bottinappula
        laatikot.remove("a3")
    elif bottiSyöte == "b1" and bottiSyöte in laatikot:
        b1 = bottinappula
        laatikot.remove("b1")
    elif bottiSyöte == "b2" and bottiSyöte in laatikot:
        b2 = bottinappula
        laatikot.remove("b2")
    elif bottiSyöte == "b3" and bottiSyöte in laatikot:
        b3 = bottinappula
        laatikot.remove("b3")
    elif bottiSyöte == "c1" and bottiSyöte in laatikot:
        c1 = bottinappula
        laatikot.remove("c1")
    elif bottiSyöte == "c2" and bottiSyöte in laatikot:
        c2 = bottinappula
        laatikot.remove("c2")
    elif bottiSyöte == "c3" and bottiSyöte in laatikot:
        c3 = bottinappula
        laatikot.remove("c3")

    time.sleep(0.4)
    print("     1   2   3")
    print("    ------------")
    print(f"a  | {a1} | {a2} | {a3} |")
    print("    ------------")
    print(f"b  | {b1} | {b2} | {b3} |" + "     <--- BOTTI LAITTOI")
    print("    ------------")
    print(f"c  | {c1} | {c2} | {c3} |")
    print("    ------------\n\n")


    if a1 == bottinappula and a2 == bottinappula and a3 == bottinappula:
        print("BOTTI VOITTI.... SÄ HÄVISIT... OOT IHAN PASKA...\n\n")
        break
    elif b1 == bottinappula and b2 == bottinappula and b3 == bottinappula:
        print("BOTTI VOITTI.... SÄ HÄVISIT... OOT IHAN PASKA...\n\n")
        break
    elif c1 == bottinappula and c2 == bottinappula and c3 == bottinappula:
        print("BOTTI VOITTI.... SÄ HÄVISIT... OOT IHAN PASKA...\n\n")
        break
    elif a1 == bottinappula and b1 == bottinappula and c1 == bottinappula:
        print("BOTTI VOITTI.... SÄ HÄVISIT... OOT IHAN PASKA...\n\n")
        break
    elif a2 == bottinappula and b2 == bottinappula and c2 == bottinappula:
        print("BOTTI VOITTI.... SÄ HÄVISIT... OOT IHAN PASKA...\n\n")
        break
    elif a3 == bottinappula and b3 == bottinappula and c3 == bottinappula:
        print("BOTTI VOITTI.... SÄ HÄVISIT... OOT IHAN PASKA...\n\n")
        break
    elif a1 == bottinappula and b2 == bottinappula and c3 == bottinappula:
        print("BOTTI VOITTI.... SÄ HÄVISIT... OOT IHAN PASKA...\n\n")
        break
    elif a3 == bottinappula and b2 == bottinappula and c1 == bottinappula:
        print("BOTTI VOITTI.... SÄ HÄVISIT... OOT IHAN PASKA...\n\n")
        break
