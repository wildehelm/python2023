import random
""" Das Spiel  "Black-Jack"-Kartenspiel (Abwandlung)
dabei spielen ein Computer (Dealer) und ein Anwender (Spieler) gegeneinander.
LF-05 T10, T11, T12
"""

wdh="j"
#SPIEL STARTET
print("Das Spiel startet...")
while wdh=="j":
    
    #Notwendige Variablen
    comsum=0                    #Summe der Karten insgesamt vom Computer
    cnew=True                   #Computer bekommt neue Karte
    spsum=0                     #Summe der Karten insgesamt vom Spieler
    snew=True                   #Spieler bekommt neue Karte
    wtrmchn=True
    sphateinekarte=False
    comhateinekarte=False

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
        if comzz > 0:
            print("Computer:    ", comsum, "Neue Karte=",comzz)
        else:
            print("Computer:    ", comsum, "hat keine neue Karte gezogen!")
            print("")
        if spzz > 0:
            print("Spieler:     ", spsum, "Neue Karte=",spzz)
        else:
            print("Spieler:     ", spsum, "hat keine neue Karte gezogen!")
            print("")
        
        #BERECHNUNG Kartenwerte werden verrechnet
        comsum=comsum+comzz
        comhateinekearte = True   
        spsum=spsum+spzz
        sphateinekearte = True
        if comsum > 20 or spsum > 20:
            wtrmchn = False
                    
        #AUSGABE
        print("Computer:    ", comsum)
        print("Spieler:     ", spsum)
        
                
        #Fall 3 comsum=spsum - UNENTSCHIEDEN
        if comsum==spsum:
            print("SPIEL: UNENTSCHIEDEN (", spsum,":",comsum,")")
            print("")
        #Fall 2 comsum>21 und spsum<=21 - oder wenn die höchste zahl SPIELER GEWONNEN
        elif spsum<=21 and (spsum>comsum or comsum>21):
            print("SPIEL: SPIELER GEWONNEN (", spsum,":",comsum,")")
            print("")
        #Fall 1 comsum<=21 und spsum>21 - COMPUTER GEWONNEN
        elif spsum < comsum or spsum>21:
            print("SPIEL: COMPUTER GEWONNEN (", comsum,":",spsum,")")
            print("")
            snew=False
        else:
            print("Das Spiel wurde abgebrochen")
            print("Computer:    ", comsum)
            print("Spieler:     ", spsum)
            print("")
            break
        #print("Das Spiel ist beendet.")

        #SPIELER - Weitere Karte
        if spsum<22 and snew==True:
            antSpieler=input("Möchte Spieler noch eine Karte? (j/n): ")
            if antSpieler=="j": # falls jemand andere Buchstaben einträgt
                snew=True       
            else:
                snew=False

        #COMPUTER - Weitere Karte (nur wenn Zahlen < 22)
        if comsum > 21 or spsum > 21:
            wtrmchn = False            # das spiel soll nicht weitergehen
        else:  
            if comsum > 16 or wtrmchn == False:
                cnew=False
            else:
                cnew=True
            
             
    wdh=input("Das Spiel neu starten? (j/n)")
    print("")
    if wdh=="j":
        print("Das Spiel startet...")
    else:
        cnew=False
        snew=False
        print("Das Programm wird beendet.")
        break
print("Programmende")


    
    
