from random import randint

newGame = "y"
gameState = ""
while newGame == "y":
    Player = randint(1, 14)
    Dealer = randint(1, 14)
    print("Du hast: " + str(Player))
    print("Der Dealer hat: " + str(Dealer))
    moreCards = input("Sie haben. Wollen Sie eine weitere Karte? (y/n) ")
    moreDealer = "y"
    while moreCards == "y" or moreDealer == "y":
        if moreCards == "y":
            Player = Player + randint(1, 14)  # Spieler zieht karte
            # moreCards = input("Sie haben. Wollen Sie eine weitere Karte? (y/n) ")
            if Player > 21:
                gameState = "verloren"
                break
            print("Du hast: " + str(Player))
        if Dealer < 17:  # Dealer ziehen nur Karten wenn sie weniger als 17 haben
            Dealer = Dealer + randint(1, 14)  # Dealer zieht Karte
            print("Der Dealer hat: " + str(Dealer))
        else:
            moreDealer = "n"
            print("Der Dealer hat: " + str(Dealer))
        if Dealer > 21:
            gameState = "gewonnen"
            break
        if moreCards == "y":
            moreCards = input("Sie haben. Wollen Sie eine weitere Karte? (y/n) ")
    if gameState == "":
        if Player == Dealer:
            gameState = "ein unentschieden mit dem Dealer"
        elif Player > Dealer:  # sollte unnötig sein "and Dealer < 21" dran zu hängen
            gameState = "gewonnen"
        else:
            gameState = "verloren"

    # print("Du hast: " + str(Player))
    # print("Der Dealer hat: " + str(Dealer))
    print("Du hast " + gameState + ".")
    newGame = input("Wollen Sie ein neues Spiel starten? (y/n) ")

# Dealer und Player While-schleife müssen getrennt werden, da dealer immer noch mehr karten nehmen könnte als der
# Spieler 2 While Schleifen? zu moreCards sollte man moreDealer einbinden
