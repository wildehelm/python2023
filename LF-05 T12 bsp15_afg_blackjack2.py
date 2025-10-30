import random
""" Das Spiel  "Black-Jack"-Kartenspiel (Abwandlung)
dabei spielen Computer und Anwender gegeneinander.
"""

wdh="j"
#SPIEL STARTET
while wdh=="j":
    #Notwendige Variablen
    comsum=0                  #Summe der Karten insgesamt vom Computer
    cnew=True                   #Computer bekommt neue Karte
    spsum=0                     #Summe der Karten insgesamt vom Spieler
    snew=True                   #Spieler bekommt neue Karte
    while cnew==True or snew==True:
        #Karten werden gezogen
        if cnew==True:
            comzz=random.randint(1,14)
        else:
            comzz=0
        if snew==True:
            spzz=random.randint(1,14)
        else:
            spzz=0
        #AUSGABE
        print("Computer: ", comsum, "Neue Karte=",comzz)
        print("Spieler:     ", spsum, "Neue Karte=",spzz)
        #BERECHNUNG Karten werden verrechnet
        comsum=comsum+comzz
        spsum=spsum+spzz
        #AUSGABE
        print("Computer: ", comsum)
        print("Spieler:     ", spsum)
        #SPIELER - Weitere Karte
        if spsum<22 and snew==True:
            antSpieler=input("Möchte Spieler noch eine Karte? (j/n): ")
            if antSpieler=="n":
                snew=False
            else:
                snew=True
        #COMPUTER - Weitere Karte
        if comsum<=16:
            cnew=True
        else:
            cnew=False
            #Prüfe, ob jemand gewonnen hat???
            #Fall 3 comsum=spsum - UNENTSCHIEDEN
            if comsum==spsum:
                print("SPIEL: UNENTSCHIEDEN")
                break
            #Fall 2 comsum>21 und spsum<=21 - SPIELER GEWONNEN
            if (comsum>21 and spsum<=21) or (comsum<spsum and spsum<=21):
                print("SPIEL: SPIELER GEWONNEN.")
                break
            #Fall 1 comsum<=21 und spsum>21 - COMPUTER GEWONNEN
            if spsum<comsum:
                print("SPIEL: COMPUTER GEWONNEN.")
                break
        #print("Das Spiel ist beendet.")
    wdh=input("Das Spiel neu starten? (j/n)")
    if wdh=="j":
        print("Das Spiel startet...")
    else:
        print("Das Programm wird beendet.")
        break
print("Programmende")
    
    
