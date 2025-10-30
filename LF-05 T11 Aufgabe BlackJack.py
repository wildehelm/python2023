"""
Aufgabe: Spiel „ Black Jack" Kartenspiel 
Der Computer zieht eine beliebige Zahl aus I bis 14.
Der Spieler wählt auch eine Zahl aus I bis 14. 
Es gilt — der Computer antwortet mit „Zahl ist größer" oder „Zahl ist niedriger" als 21.
Dann darf man eine weitere Zahl eingeben. 
Ziel ist es < 21 näher als der Computer, dann hat der Spieler gewonnen, ansonsten der Computer.

Hinweis: Beim Kartenspiel gibt es Karten mit
1=Ass bzw. 11, Bube 12, Dame 13, König 14, Ziffern von 2 bis 10. 

Am Ende des Spiels, soll gefragt werden, ob man nochmal spielen möchte.  
"""

import random

weitermachen ="j"
weitereKarte ="j"
bGameOver = False
nHumanPlayer =0
sumHumanPlayer = 0
nDealer = 0
sumDealer = 0


while weitermachen == "j":
    weitereKarte = "j"
    while nHumanPlayer < 21 and nDealer < 21 and weitereKarte == "j" and bGameOver == False:
        nHumanPlayer = random.randint(1,14)
        nDealer = random.randint(1,14)
        print(weitereKarte)
        if weitereKarte == "j":
            sumHumanPlayer = sumHumanPlayer + nHumanPlayer
            sumDealer = sumDealer + sumDealer
            print("Player has drawn", nHumanPlayer)
            print("Dealer has drawn", nDealer)
            weitereKarte=input("Beide Parteien haben eine Karte gewählt. Noch hat niemand geplatzt. Wollen Sie eine weitere Karte auswählen?")

            if sumHumanPlayer > 20 or sumDealer > 20:
                print("Game over")
                if sumHumanPlayer > 20 and sumDealer < 21:
                    print("The machine has won")
                elif sumDealer > 20 and sumHumanPlayer < 21:
                    print("The human has won")
                else:
                    print("Nobody has won")
        elif weitereKarte == "n":
            bGameOver = True
            print("Game over. No more cards to draw")
        else:
            bGameOver = True
            print("No success", sumHumanPlayer, sumDealer)
            print(sumHumanPlayer)
            print(sumDealer)
            break


        weitermachen = input("Wollen Sie noch einmal spielen? (j/n)")
        if weitermachen == "j":
            continue
        else:
            print("Programmende")
