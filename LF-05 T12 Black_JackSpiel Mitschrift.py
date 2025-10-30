import random 
""" Das Spiel "Black-Jack"-Kartenspiel (Abwandlung) 
dabei spielen Computer und Anwender gegeneinander.
"""
#Notwendige Variablen 
comsum=0        #Summe der Karten insgesamt vom Computer
cnew=bool(True)       #Computer bekommt neue Karte 
spsum=0         #Summe der Karten insgesamt vom Spieler
snew=True       #Spieler bekommt neue Karte 
wdh="j"
commzz = 0      #zufallszahl dealer/computer
spzz = 0        #zufallszahl spieler/human

#SPIEL STARTET 
while wdh=="j":
    while cnew == True or snew == True:
        # karten werden gezogen
        if cnew== True:
            comzz = random.randint(1,14)
        else:
            commz=0
        if snew== True:
            spzz = random.randint(1,14)
        else:
            spzz=0
        #AUSGABE 1
        print("Computer:", comsum, "Neue Karte=",commzz)
        print("Spieler:", spsum, "Neue Karte=",spzz)
        #BERECHNUNG
        comsum=comsum+comzz
        spsum=spsum+spzz
        #AUSGABE 2 STAND VOR DER ENTSCHEIDUNG
        print("Computer:", comsum)
        print("Spieler:", spsum)
        if comsum < 22 and spsum < 22:
            antSpieler = input("Möchte Spieler noch eine Karte? (j/n)")
            if antSpieler == "j":
                snew = True
            else:
                snew = False
            #COMPUTER neue Karte
            if comsum < 17:
                cnew=True
            else:
                cnew=False
                #PRÜFE OB JEMAND GEWONNEN HAT
                #fall 3
                if comsum == spsum:
                    print("Spiel unentschieden")
                    break
                #fall 2
                if comsum > 21 and spsum <= 21:
                    print("Spieler hat gewonnen")
                    break
                #fall 1
                if comsum <= 21 and spsum > 21:
                    print("Computer hat gewonnen")
                    break
                
    wdh=input("Das Spiel neu starten? (j/n)") 
    if wdh=="j":
        #Spiel startet...") 
        print("Das Spiel wird gestartet...") 
    else:
        print("Das Programm wird beendet.") 
        break 



