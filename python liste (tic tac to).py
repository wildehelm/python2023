#liste übung
#tic tac toe
#2023-01-26, mit Alex Zinner beim GFN

import random
ttt=["1","2","3","4","5","6","7","8","9"]
spieler=[1,2]
zeichen=["X","O"]
sephor = "—"
sepver = "|"
tab = "\t"

#einfache print
print(tab,"1",sepver,"2",sepver,"3")
print(tab, sephor,sepver,sephor,sepver,sephor)
print(tab,"4",sepver,"5",sepver,"6")
print(tab, sephor,sepver,sephor,sepver,sephor)
print(tab,"7",sepver,"8",sepver,"9")

#liste print
def spielfeld_ausgeben():
    print(tab, ttt[0],sepver,ttt[1],sepver,ttt[2])
    print(tab, sephor,sepver,sephor,sepver,sephor)
    print(tab, ttt[3],sepver,ttt[4],sepver,ttt[5])
    print(tab, sephor,sepver,sephor,sepver,sephor)
    print(tab, ttt[6],sepver,ttt[7],sepver,ttt[8])

#HAUPTPROGRAMM
spielfeld_ausgeben
"""das spielfeld ist angezeigt und das spiel darf beginnen"""

#NAMEN DER SPIELER
for x in spieler:
    xname="Spieler"+str(spieler[x-1])
    #print("Wir haben Spieler mit vorläufigen Namen",xname)
    spieler[x-1]=input(xname+". Gib den Spieler den eigenen Namen: ")
    print("Spieler", x, "heisst",spieler[x-1])

if random.randint(1,999)%2==0:
    beginsp = 1
else:
    beginsp = 2
    
try:
    print("Spiel beginnt. Diesmal startet ",spieler[beginsp-1])
except:
    print("Das Spiel konnte nicht beginnen")


# repeat errors: TypeError: unsupported operand type(s) for -: 'str' and 'int'
for n in ttt:
    print(n)   

    #limit output to 1 - 9 with try
    try:
        e=int(input("Wähle die gewünschte Stelle mithilfe der Zahlen, die noch verfügbar sind"))
    except:
        print("Fehler")
    
"""
"""
